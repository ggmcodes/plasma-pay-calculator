/**
 * HTML rendering utilities for programmatic pages
 * Uses the site's existing styling patterns
 */

import { escapeHtml, getCurrentYear, getSiteUrl } from './utils.mjs';

/**
 * Generate the base HTML template
 * @param {Object} options - Template options
 * @returns {string} Complete HTML document
 */
export function renderPage(options) {
  const {
    title,
    metaDescription,
    canonicalUrl,
    noindex = false,
    jsonLd = [],
    breadcrumbs = [],
    heroHtml = '',
    summaryHtml = '',
    tableHtml = '',
    faqHtml = '',
    ctaHtml = '',
    relatedLinksHtml = '',
    additionalContent = ''
  } = options;

  const siteUrl = getSiteUrl();
  const year = getCurrentYear();
  const robotsMeta = noindex
    ? '<meta name="robots" content="noindex,follow">'
    : '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">';

  const jsonLdScript = jsonLd.length > 0
    ? `<script type="application/ld+json">${JSON.stringify(jsonLd, null, 2)}</script>`
    : '';

  return `<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-053DRWEQLS"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-053DRWEQLS');
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451" crossorigin="anonymous"></script>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="/assets/css/global-fonts.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeHtml(metaDescription)}">
  <link rel="canonical" href="${canonicalUrl}">
  ${robotsMeta}

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="manifest" href="/manifest.json">

  <!-- Open Graph -->
  <meta property="og:title" content="${escapeHtml(title)}">
  <meta property="og:description" content="${escapeHtml(metaDescription)}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="${siteUrl}/screenshot.png">
  <meta property="og:site_name" content="Plasma Pay Calculator">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${escapeHtml(title)}">
  <meta name="twitter:description" content="${escapeHtml(metaDescription)}">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            mint: '#0d9488',
            'mint-light': '#14b8a6',
            coral: '#f97316',
            'coral-dark': '#ea580c',
            charcoal: '#1e293b',
            slate: '#64748b',
            cream: '#fefce8'
          },
          fontFamily: {
            sans: ['DM Sans', 'sans-serif'],
            mono: ['Space Mono', 'monospace']
          }
        }
      }
    }
  </script>

  ${jsonLdScript}

  <style>
    :root {
      --mint: #0d9488;
      --mint-light: #14b8a6;
      --coral: #f97316;
      --coral-dark: #ea580c;
      --charcoal: #1e293b;
      --slate: #64748b;
      --cream: #fefce8;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      color: var(--charcoal);
      background: linear-gradient(180deg, #f0fdfa 0%, #ffffff 50%, #fffbeb 100%);
      min-height: 100vh;
    }

    .font-mono { font-family: 'Space Mono', monospace; }

    nav {
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      padding: 1rem 0;
      position: fixed;
      width: 100%;
      top: 0;
      z-index: 1000;
      border-bottom: 2px solid var(--mint);
    }

    .nav-container {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 1.5rem;
    }

    .logo {
      font-family: 'Space Mono', monospace;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--mint);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .logo-icon {
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, var(--mint) 0%, var(--mint-light) 100%);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: bold;
    }

    .nav-links { display: flex; gap: 1.5rem; align-items: center; }
    .nav-links a { color: var(--charcoal); text-decoration: none; font-weight: 500; transition: color 0.2s; }
    .nav-links a:hover { color: var(--mint); }

    main { padding-top: 80px; }

    .container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }

    .breadcrumbs {
      padding: 1rem 0;
      font-size: 0.875rem;
      color: var(--slate);
    }
    .breadcrumbs a { color: var(--mint); text-decoration: none; }
    .breadcrumbs a:hover { text-decoration: underline; }
    .breadcrumbs span { margin: 0 0.5rem; }

    .hero {
      text-align: center;
      padding: 3rem 0;
    }
    .hero h1 {
      font-size: 2.5rem;
      font-weight: 700;
      color: var(--charcoal);
      margin-bottom: 1rem;
      line-height: 1.2;
    }
    .hero p {
      font-size: 1.25rem;
      color: var(--slate);
      max-width: 700px;
      margin: 0 auto;
    }

    .card {
      background: white;
      border-radius: 16px;
      padding: 2rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      margin-bottom: 2rem;
    }

    .card-title {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--charcoal);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .result-box {
      background: linear-gradient(135deg, var(--mint) 0%, var(--mint-light) 100%);
      border-radius: 12px;
      padding: 2rem;
      text-align: center;
      color: white;
      margin: 1.5rem 0;
    }
    .result-box .amount {
      font-family: 'Space Mono', monospace;
      font-size: 3rem;
      font-weight: 700;
    }
    .result-box .label {
      font-size: 1rem;
      opacity: 0.9;
    }

    .results-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin: 1.5rem 0;
    }
    .result-item {
      background: #f8fafc;
      border-radius: 8px;
      padding: 1rem;
      text-align: center;
    }
    .result-item .value {
      font-family: 'Space Mono', monospace;
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--mint);
    }
    .result-item .label {
      font-size: 0.875rem;
      color: var(--slate);
    }

    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
    }
    .comparison-table th,
    .comparison-table td {
      padding: 0.75rem 1rem;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }
    .comparison-table th {
      background: #f8fafc;
      font-weight: 600;
      color: var(--charcoal);
    }
    .comparison-table tr.current {
      background: #f0fdfa;
      font-weight: 600;
    }
    .comparison-table tr.current td:first-child {
      position: relative;
    }
    .comparison-table tr.current td:first-child::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 4px;
      background: var(--mint);
    }

    .faq-section { margin: 2rem 0; }
    .faq-item {
      border-bottom: 1px solid #e2e8f0;
      padding: 1.5rem 0;
    }
    .faq-item:last-child { border-bottom: none; }
    .faq-question {
      font-weight: 600;
      font-size: 1.125rem;
      color: var(--charcoal);
      margin-bottom: 0.75rem;
    }
    .faq-answer {
      color: var(--slate);
      line-height: 1.7;
    }

    .cta-button {
      display: inline-block;
      background: linear-gradient(135deg, var(--coral) 0%, var(--coral-dark) 100%);
      color: white;
      padding: 1rem 2rem;
      border-radius: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .cta-button:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3);
    }

    .related-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-top: 1rem;
    }
    .related-link {
      display: inline-block;
      padding: 0.5rem 1rem;
      background: #f0fdfa;
      color: var(--mint);
      border-radius: 8px;
      text-decoration: none;
      font-weight: 500;
      transition: background 0.2s;
    }
    .related-link:hover {
      background: #ccfbf1;
    }

    footer {
      background: var(--charcoal);
      color: white;
      padding: 3rem 0;
      margin-top: 4rem;
    }
    .footer-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
    }
    .footer-section h4 {
      font-weight: 600;
      margin-bottom: 1rem;
      color: var(--mint-light);
    }
    .footer-section a {
      display: block;
      color: #94a3b8;
      text-decoration: none;
      margin-bottom: 0.5rem;
      transition: color 0.2s;
    }
    .footer-section a:hover { color: white; }
    .footer-bottom {
      text-align: center;
      padding-top: 2rem;
      margin-top: 2rem;
      border-top: 1px solid #334155;
      color: #64748b;
    }

    @media (max-width: 768px) {
      .hero h1 { font-size: 1.75rem; }
      .hero p { font-size: 1rem; }
      .result-box .amount { font-size: 2rem; }
      .nav-links { display: none; }
    }
  </style>
</head>
<body>
  <nav>
    <div class="nav-container">
      <a href="/" class="logo">
        <div class="logo-icon">P$</div>
        <span>PlasmaPayCalc</span>
      </a>
      <div class="nav-links">
        <a href="/">Calculator</a>
        <a href="/calculators/">All Calculators</a>
        <a href="/states.html">By State</a>
        <a href="/blog/">Blog</a>
        <a href="/faq.html">FAQ</a>
      </div>
    </div>
  </nav>

  <main>
    <div class="container">
      ${renderBreadcrumbs(breadcrumbs)}

      <div class="hero">
        ${heroHtml}
      </div>

      ${summaryHtml ? `<section class="card">${summaryHtml}</section>` : ''}

      ${tableHtml ? `<section class="card">${tableHtml}</section>` : ''}

      ${ctaHtml ? `<section class="card" style="text-align: center;">${ctaHtml}</section>` : ''}

      ${faqHtml ? `<section class="card faq-section">${faqHtml}</section>` : ''}

      ${relatedLinksHtml ? `<section class="card"><h3 class="card-title">Related Calculators</h3>${relatedLinksHtml}</section>` : ''}

      ${additionalContent}
    </div>
  </main>

  <footer>
    <div class="footer-container">
      <div class="footer-section">
        <h4>Calculators</h4>
        <a href="/">Plasma Pay Calculator</a>
        <a href="/csl-plasma-tax-calculator.html">Tax Calculator</a>
        <a href="/tools/eligibility-checker.html">Eligibility Checker</a>
      </div>
      <div class="footer-section">
        <h4>By Center</h4>
        <a href="/csl-plasma-pay-chart-2026.html">CSL Plasma</a>
        <a href="/octapharma-payment-calculator.html">Octapharma</a>
        <a href="/tools/all-plasma-centers-comparison.html">Compare All</a>
      </div>
      <div class="footer-section">
        <h4>Resources</h4>
        <a href="/blog/">Blog</a>
        <a href="/faq.html">FAQ</a>
        <a href="/states.html">By State</a>
      </div>
      <div class="footer-section">
        <h4>Legal</h4>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms of Service</a>
        <a href="/about.html">About</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; ${year} PlasmaPayCalculator.com. For informational purposes only.</p>
    </div>
  </footer>
</body>
</html>`;
}

/**
 * Render breadcrumbs
 * @param {Array} items - Breadcrumb items
 * @returns {string} Breadcrumb HTML
 */
export function renderBreadcrumbs(items) {
  if (!items || items.length === 0) return '';

  const crumbs = items.map((item, i) => {
    const isLast = i === items.length - 1;
    if (isLast) {
      return `<span>${escapeHtml(item.label)}</span>`;
    }
    return `<a href="${item.url}">${escapeHtml(item.label)}</a><span>/</span>`;
  }).join(' ');

  return `<nav class="breadcrumbs">${crumbs}</nav>`;
}

/**
 * Render FAQ items
 * @param {Array} items - FAQ items with q and a properties
 * @returns {string} FAQ HTML
 */
export function renderFaq(items) {
  if (!items || items.length === 0) return '';

  const faqHtml = items.map(item => `
    <div class="faq-item">
      <h3 class="faq-question">${escapeHtml(item.q)}</h3>
      <div class="faq-answer">${item.a}</div>
    </div>
  `).join('');

  return `<h2 class="card-title">Frequently Asked Questions</h2>${faqHtml}`;
}

/**
 * Render related links
 * @param {Array} links - Link items with href and label
 * @returns {string} Related links HTML
 */
export function renderRelatedLinks(links) {
  if (!links || links.length === 0) return '';

  return `<div class="related-links">
    ${links.map(link => `<a href="${link.href}" class="related-link">${escapeHtml(link.label)}</a>`).join('')}
  </div>`;
}

/**
 * Generate JSON-LD for FAQ page
 * @param {Array} items - FAQ items
 * @returns {Object} FAQPage schema
 */
export function generateFaqSchema(items) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map(item => ({
      '@type': 'Question',
      name: item.q,
      acceptedAnswer: {
        '@type': 'Answer',
        text: item.a.replace(/<[^>]*>/g, '') // Strip HTML
      }
    }))
  };
}

/**
 * Generate JSON-LD for SoftwareApplication
 * @param {Object} options - Application details
 * @returns {Object} SoftwareApplication schema
 */
export function generateAppSchema(options) {
  const { name, description, url } = options;
  return {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name,
    description,
    url,
    applicationCategory: 'FinanceApplication',
    operatingSystem: 'Any',
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'USD'
    }
  };
}

/**
 * Generate JSON-LD for BreadcrumbList
 * @param {Array} items - Breadcrumb items
 * @param {string} siteUrl - Base site URL
 * @returns {Object} BreadcrumbList schema
 */
export function generateBreadcrumbSchema(items, siteUrl) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.label,
      item: item.url.startsWith('http') ? item.url : `${siteUrl}${item.url}`
    }))
  };
}
