# Programmatic SEO Page Generator

This system generates static landing pages for high-intent calculator scenarios, creating crawlable pages that target specific search queries without creating thin or duplicate content.

## Quick Start

```bash
# Generate all programmatic pages (default max: 800 pages)
npm run generate:programmatic

# Preview without writing files
npm run generate:programmatic:dry-run

# Clean output and regenerate
npm run generate:programmatic:clean

# Generate with verbose output
npm run generate:programmatic:verbose

# Generate specific calculator only
npm run generate:plasma-pay
npm run generate:plasma-tax
```

## Safety Features

### 1. Conservative Page Limits
- Default maximum: **800 pages**
- Override via environment variable: `MAX_PAGES=1500 npm run generate:programmatic`
- Override via CLI: `npm run generate:programmatic -- --max-pages=1500`

### 2. Input Validation
Each combination is validated before generation. Invalid combinations are skipped:
- Missing required fields
- Invalid parameter values
- Nonsensical combinations

### 3. Output Deduplication
Pages with effectively identical outputs are deduplicated using `canonicalKey()`:
- Prevents near-duplicate content
- Based on output buckets, not exact values
- Example: Monthly earnings rounded to $50 buckets

### 4. Quality Thresholds
Low-quality pages are either:
- Skipped entirely (preferred)
- Marked with `noindex,follow` (for UX-required pages)

## Directory Structure

```
/tools/
  generate-programmatic-pages.mjs  # Main generator script
  programmatic.config.mjs          # Calculator configurations
  lib/
    render.mjs                     # HTML rendering utilities
    sitemap.mjs                    # Sitemap generation
    utils.mjs                      # Utility functions

/js/engine/
  plasmaPayEngine.mjs              # Pure plasma pay calculator logic
  plasmaTaxEngine.mjs              # Pure tax calculator logic

/p/                                # Generated output directory
  plasma-pay/                      # Plasma pay calculator pages
    csl-plasma-new-donor-175-200-california/
      index.html
    ...
  plasma-tax/                      # Tax calculator pages
    5k-plasma-income-single/
      index.html
    ...

/sitemap-programmatic.xml          # Sitemap for generated pages
```

## Generated Page Structure

Each page includes:

1. **Unique URL slug** - SEO-friendly path with scenario parameters
2. **Hero section** - Scenario-specific title and description
3. **Summary card** - Computed results with key metrics
4. **Comparison table** - Context showing current scenario vs alternatives
5. **CTA** - Link to interactive calculator with prefilled params
6. **FAQ section** - 6-8 questions with scenario-specific answers
7. **Related links** - Internal linking to related calculators
8. **JSON-LD schema** - SoftwareApplication + FAQPage + BreadcrumbList
9. **Self-referential canonical** - Proper canonical URL

## Adding a New Calculator

1. Create pure engine functions in `/js/engine/`:

```javascript
// /js/engine/myCalculatorEngine.mjs
export function calculateMyThing(inputs) {
  // Pure function - no DOM access
  return { result1, result2, ... };
}

export function validateMyInputs(inputs) {
  return { valid: true/false, reason: '...' };
}
```

2. Add calculator config in `/tools/programmatic.config.mjs`:

```javascript
const myCalculatorConfig = {
  id: 'my-calculator',
  interactivePath: '/calculators/my-calculator.html',
  outBase: 'p/my-calculator',

  // Curated input grid - be conservative!
  inputGrid: {
    param1: ['value1', 'value2'],
    param2: [100, 200, 300]
  },

  validate(inputs) { ... },
  compute(inputs) { ... },
  canonicalKey(inputs, outputs) { ... },
  slug(inputs, outputs) { ... },
  pageTitle(inputs, outputs) { ... },
  metaDescription(inputs, outputs) { ... },
  heroHtml(inputs, outputs) { ... },
  summaryHtml(inputs, outputs) { ... },
  tableHtml(inputs, outputs) { ... },
  faqItems(inputs, outputs) { ... },
  ctaHtml(inputs, outputs) { ... },
  relatedLinks(inputs, outputs) { ... },
  schemaJsonLd(inputs, outputs, canonicalUrl) { ... }
};

// Add to exports
export const calculators = [
  plasmaPayConfig,
  plasmaTaxConfig,
  myCalculatorConfig  // Add here
];
```

## Input Grid Design Guidelines

### DO:
- Use curated, high-intent values
- Focus on values people actually search for
- Keep total combinations reasonable (< 500 per calculator)
- Use meaningful buckets (e.g., income levels, weight ranges)

### DON'T:
- Explode all possible combinations
- Include continuous values without bucketing
- Create pages for edge cases with no search intent
- Generate pages with trivial output differences

### Example - Good:
```javascript
inputGrid: {
  center: ['csl', 'biolife', 'octapharma'],  // 3 major centers
  weight: ['110-149', '150-174', '175-200', '200+'],  // 4 ranges
  state: ['CA', 'TX', 'FL', 'NY', 'OH']  // 5 high-volume states
}
// = 60 combinations, all high-intent
```

### Example - Bad:
```javascript
inputGrid: {
  center: ['csl', 'biolife', 'octapharma', 'grifols', 'kedplasma', 'bpl', 'interstate', 'other'],
  weight: [110, 111, 112, ..., 400],  // Every pound
  state: ['AL', 'AK', ..., 'WY']  // All 50 states
}
// = 8 × 290 × 50 = 116,000 combinations, mostly thin content
```

## Verification Checklist

After generation:

- [ ] Sample pages load correctly with CSS
- [ ] Canonical URLs are self-referential and absolute
- [ ] JSON-LD validates (use Google's testing tool)
- [ ] FAQ answers include scenario-specific values
- [ ] Comparison tables highlight current scenario
- [ ] CTA links include correct query params
- [ ] Sitemap contains all generated URLs
- [ ] robots.txt references both sitemaps

## Troubleshooting

### "Too many pages generated"
- Reduce input grid dimensions
- Increase deduplication bucket sizes
- Add stricter validation rules

### "Pages look duplicate"
- Adjust `canonicalKey()` to use broader buckets
- Add more unique content to summaries
- Include more scenario-specific FAQ answers

### "Missing pages for valid combinations"
- Check validation rules aren't too strict
- Verify deduplication isn't too aggressive
- Check max page limit hasn't been reached

## Performance

Typical generation times:
- 100 pages: ~2 seconds
- 500 pages: ~8 seconds
- 800 pages: ~12 seconds

The generator uses synchronous file writes for simplicity. For very large runs, consider batching.
