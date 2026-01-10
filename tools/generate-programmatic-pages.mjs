#!/usr/bin/env node

/**
 * Programmatic SEO Page Generator
 *
 * Generates static landing pages for high-intent calculator scenarios.
 *
 * SAFETY FEATURES:
 * - Default max pages: 800 (conservative)
 * - Input validation: skips invalid combinations
 * - Output deduplication: skips near-duplicate pages
 * - Configurable via CLI flags or environment variables
 *
 * Usage:
 *   npm run generate:programmatic              # Generate with defaults
 *   npm run generate:programmatic -- --clean   # Clean output first
 *   npm run generate:programmatic -- --dry-run # Preview without writing
 *   MAX_PAGES=1500 npm run generate:programmatic  # Override max pages
 */

import { writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

import { calculators, DEFAULT_MAX_PAGES, SITE_URL } from './programmatic.config.mjs';
import { renderPage, renderFaq, renderRelatedLinks } from './lib/render.mjs';
import { writeSitemap, createUrlEntry } from './lib/sitemap.mjs';
import {
  cartesianProduct,
  ensureDir,
  cleanDir,
  parseArgs,
  log,
  generateBreadcrumbs,
  getISODate
} from './lib/utils.mjs';

// Get script directory
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = join(__dirname, '..');

// ============================================================================
// CONFIGURATION
// ============================================================================

function getConfig() {
  const args = parseArgs(process.argv.slice(2));

  return {
    maxPages: parseInt(args.values['max-pages'] || process.env.MAX_PAGES || DEFAULT_MAX_PAGES, 10),
    clean: args.flags.clean || false,
    dryRun: args.flags['dry-run'] || args.flags.n || false,
    verbose: args.flags.verbose || args.flags.v || false,
    calculator: args.values.calculator || null, // Run specific calculator only
    outputDir: join(ROOT_DIR, 'p'),
    sitemapPath: join(ROOT_DIR, 'sitemap-programmatic.xml')
  };
}

// ============================================================================
// MAIN GENERATION LOGIC
// ============================================================================

async function generatePages() {
  const config = getConfig();
  const startTime = Date.now();

  log.info(`Programmatic Page Generator`);
  log.info(`Max pages: ${config.maxPages}`);
  log.info(`Output directory: ${config.outputDir}`);
  if (config.dryRun) log.warn('DRY RUN - no files will be written');
  console.log('');

  // Clean output directory if requested
  if (config.clean && !config.dryRun) {
    log.info('Cleaning output directory...');
    cleanDir(config.outputDir);
  }

  // Ensure output directory exists
  if (!config.dryRun && !existsSync(config.outputDir)) {
    mkdirSync(config.outputDir, { recursive: true });
  }

  // Track statistics
  const stats = {
    totalCombinations: 0,
    generated: 0,
    skippedInvalid: 0,
    skippedDedupe: 0,
    skippedLimit: 0
  };

  // Track all generated URLs for sitemap
  const sitemapUrls = [];

  // Track seen canonical keys for deduplication
  const seenKeys = new Set();

  // Filter calculators if specific one requested
  const calcsToRun = config.calculator
    ? calculators.filter(c => c.id === config.calculator)
    : calculators;

  if (calcsToRun.length === 0) {
    log.error(`Calculator "${config.calculator}" not found`);
    process.exit(1);
  }

  // Process each calculator
  for (const calc of calcsToRun) {
    log.info(`Processing: ${calc.id}`);

    // Generate all input combinations
    const combinations = cartesianProduct(calc.inputGrid);
    stats.totalCombinations += combinations.length;

    log.dim(`  ${combinations.length} input combinations`);

    let calcGenerated = 0;
    let calcSkippedInvalid = 0;
    let calcSkippedDedupe = 0;

    for (const inputs of combinations) {
      // Check page limit
      if (stats.generated >= config.maxPages) {
        stats.skippedLimit += combinations.length - calcGenerated - calcSkippedInvalid - calcSkippedDedupe;
        log.warn(`  Reached max pages limit (${config.maxPages})`);
        break;
      }

      // Validate inputs
      if (!calc.validate(inputs)) {
        calcSkippedInvalid++;
        stats.skippedInvalid++;
        continue;
      }

      // Compute outputs
      const outputs = calc.compute(inputs);

      // Check for deduplication
      const canonicalKey = calc.canonicalKey(inputs, outputs);
      if (seenKeys.has(canonicalKey)) {
        calcSkippedDedupe++;
        stats.skippedDedupe++;
        continue;
      }
      seenKeys.add(canonicalKey);

      // Generate slug and paths
      const slug = calc.slug(inputs, outputs);
      const relativePath = `${calc.outBase}/${slug}`;
      const filePath = join(config.outputDir, slug.replace(calc.outBase.split('/').pop() + '/', ''), 'index.html');
      const canonicalUrl = `${SITE_URL}/${relativePath}/`;

      // Build breadcrumbs
      const breadcrumbs = [
        { label: 'Home', url: '/' },
        { label: 'Calculators', url: '/calculators/' },
        { label: calc.pageTitle(inputs, outputs).split(':')[0], url: canonicalUrl }
      ];

      // Generate page content
      const faqItems = calc.faqItems(inputs, outputs);
      const relatedLinks = calc.relatedLinks(inputs, outputs);

      const pageHtml = renderPage({
        title: calc.pageTitle(inputs, outputs),
        metaDescription: calc.metaDescription(inputs, outputs),
        canonicalUrl,
        noindex: false,
        jsonLd: calc.schemaJsonLd(inputs, outputs, canonicalUrl),
        breadcrumbs,
        heroHtml: calc.heroHtml(inputs, outputs),
        summaryHtml: calc.summaryHtml(inputs, outputs),
        tableHtml: calc.tableHtml(inputs, outputs),
        faqHtml: renderFaq(faqItems),
        ctaHtml: calc.ctaHtml(inputs, outputs),
        relatedLinksHtml: renderRelatedLinks(relatedLinks)
      });

      // Write file (unless dry run)
      if (!config.dryRun) {
        const fullPath = join(ROOT_DIR, relativePath, 'index.html');
        ensureDir(fullPath);
        writeFileSync(fullPath, pageHtml, 'utf-8');
      }

      if (config.verbose) {
        log.dim(`  Created: ${relativePath}/`);
      }

      // Add to sitemap
      sitemapUrls.push(createUrlEntry(canonicalUrl, {
        priority: '0.7',
        changefreq: 'monthly'
      }));

      calcGenerated++;
      stats.generated++;
    }

    log.success(`  Generated: ${calcGenerated}, Invalid: ${calcSkippedInvalid}, Deduped: ${calcSkippedDedupe}`);
  }

  // Write sitemap
  if (!config.dryRun && sitemapUrls.length > 0) {
    log.info('Writing sitemap...');
    writeSitemap(config.sitemapPath, sitemapUrls);
    log.success(`  Wrote ${sitemapUrls.length} URLs to sitemap-programmatic.xml`);
  }

  // Print summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log('');
  log.info('========================================');
  log.info('GENERATION COMPLETE');
  log.info('========================================');
  log.info(`Total combinations:  ${stats.totalCombinations}`);
  log.success(`Pages generated:     ${stats.generated}`);
  log.dim(`Skipped (invalid):   ${stats.skippedInvalid}`);
  log.dim(`Skipped (dedupe):    ${stats.skippedDedupe}`);
  if (stats.skippedLimit > 0) {
    log.warn(`Skipped (limit):     ${stats.skippedLimit}`);
  }
  log.info(`Time elapsed:        ${elapsed}s`);
  console.log('');

  if (config.dryRun) {
    log.warn('DRY RUN - no files were written');
    log.info('Run without --dry-run to generate files');
  } else {
    log.success(`Output written to: ${config.outputDir}`);
    log.info(`Sitemap: ${config.sitemapPath}`);
  }

  return stats;
}

// ============================================================================
// RUN
// ============================================================================

generatePages().catch(err => {
  log.error(err.message);
  console.error(err.stack);
  process.exit(1);
});
