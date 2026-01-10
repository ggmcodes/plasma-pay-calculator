/**
 * Sitemap generation utilities for programmatic pages
 */

import { writeFileSync } from 'fs';
import { getISODate } from './utils.mjs';

/**
 * Generate sitemap XML content
 * @param {Array} urls - Array of URL objects with loc, priority, changefreq
 * @returns {string} Sitemap XML content
 */
export function generateSitemapXml(urls) {
  const date = getISODate();

  const urlEntries = urls.map(url => `  <url>
    <loc>${url.loc}</loc>
    <lastmod>${url.lastmod || date}</lastmod>
    <priority>${url.priority || '0.7'}</priority>
    <changefreq>${url.changefreq || 'monthly'}</changefreq>
  </url>`).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urlEntries}
</urlset>`;
}

/**
 * Generate sitemap index XML for multiple sitemaps
 * @param {Array} sitemaps - Array of sitemap URLs
 * @param {string} siteUrl - Base site URL
 * @returns {string} Sitemap index XML content
 */
export function generateSitemapIndex(sitemaps, siteUrl) {
  const date = getISODate();

  const sitemapEntries = sitemaps.map(sitemap => `  <sitemap>
    <loc>${siteUrl}/${sitemap}</loc>
    <lastmod>${date}</lastmod>
  </sitemap>`).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapEntries}
</sitemapindex>`;
}

/**
 * Write sitemap to file
 * @param {string} filePath - Output file path
 * @param {Array} urls - URL entries
 * @returns {number} Number of URLs written
 */
export function writeSitemap(filePath, urls) {
  const xml = generateSitemapXml(urls);
  writeFileSync(filePath, xml, 'utf-8');
  return urls.length;
}

/**
 * Split URLs into multiple sitemaps if needed (max 50,000 URLs per sitemap)
 * @param {Array} urls - All URL entries
 * @param {string} basePath - Base file path (without extension)
 * @param {number} maxPerFile - Maximum URLs per sitemap file
 * @returns {Array} Array of generated sitemap filenames
 */
export function writeSitemaps(urls, basePath, maxPerFile = 50000) {
  if (urls.length <= maxPerFile) {
    const filename = `${basePath}.xml`;
    writeSitemap(filename, urls);
    return [filename];
  }

  const sitemaps = [];
  const chunks = Math.ceil(urls.length / maxPerFile);

  for (let i = 0; i < chunks; i++) {
    const start = i * maxPerFile;
    const end = Math.min(start + maxPerFile, urls.length);
    const chunk = urls.slice(start, end);
    const filename = `${basePath}-${i + 1}.xml`;
    writeSitemap(filename, chunk);
    sitemaps.push(filename);
  }

  return sitemaps;
}

/**
 * Create URL entry object
 * @param {string} loc - Full URL
 * @param {Object} options - Optional priority, changefreq, lastmod
 * @returns {Object} URL entry object
 */
export function createUrlEntry(loc, options = {}) {
  return {
    loc,
    priority: options.priority || '0.7',
    changefreq: options.changefreq || 'monthly',
    lastmod: options.lastmod || getISODate()
  };
}
