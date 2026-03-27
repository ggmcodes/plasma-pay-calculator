#!/usr/bin/env node

/**
 * Injects contextual affiliate product sections into pages that don't have them.
 * Targets: calculator pages, center pages, city pages, health pages, topics pages.
 * Skips pages that already contain Amazon affiliate links.
 */

const fs = require('fs');
const path = require('path');

const TAG = 'plasma0f-20';

const donorEssentials = [
  {
    name: 'Iron Supplement (Gentle, 25mg)',
    description: 'Helps maintain hematocrit levels between donations. Gentle formula reduces stomach upset.',
    searchTerm: 'gentle+iron+supplement+25mg',
    price: '$10-15',
    badge: 'Top Pick'
  },
  {
    name: 'Liquid IV Hydration Multiplier',
    description: 'Drink before and after donation to stay hydrated and reduce fatigue. 3x faster hydration.',
    searchTerm: 'liquid+iv+hydration+multiplier',
    price: '$20-25',
    badge: 'Must Have'
  },
  {
    name: 'High-Protein Snack Bars (Variety Pack)',
    description: 'Eat 2-3 hours before donating. Protein helps maintain plasma volume and speeds recovery.',
    searchTerm: 'high+protein+snack+bars+variety+pack',
    price: '$15-25'
  },
  {
    name: 'Insulated Water Bottle (32oz)',
    description: 'Stay hydrated all day. Aim for 64-80oz of water in the 24 hours before donating.',
    searchTerm: 'insulated+water+bottle+32oz',
    price: '$15-30'
  }
];

const healthProducts = [
  {
    name: 'Digital Blood Pressure Monitor',
    description: 'Check your vitals at home before visiting the center. Avoid deferrals from high BP readings.',
    searchTerm: 'omron+blood+pressure+monitor+home',
    price: '$30-60',
    badge: 'Screening Prep'
  },
  {
    name: 'Iron Supplement (Gentle, 25mg)',
    description: 'Maintain healthy iron and hematocrit levels between plasma donations.',
    searchTerm: 'gentle+iron+supplement+25mg',
    price: '$10-15',
    badge: 'Top Pick'
  },
  {
    name: 'Vitamin B-Complex',
    description: 'Supports energy levels and red blood cell production. Important for regular donors.',
    searchTerm: 'vitamin+b+complex+supplement',
    price: '$10-15'
  },
  {
    name: 'Electrolyte Powder Packets',
    description: 'Replenish electrolytes lost during donation. Mix with water before and after visits.',
    searchTerm: 'electrolyte+powder+packets',
    price: '$15-25'
  }
];

function buildProductCard(product) {
  const badgeHtml = product.badge
    ? `<span style="background:#f59e0b;color:#fff;font-size:0.7rem;font-weight:700;padding:2px 8px;border-radius:9999px;margin-left:8px">${product.badge}</span>`
    : '';

  return `
      <div style="background:#fff;border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e5e7eb">
        <div style="display:flex;align-items:center;margin-bottom:6px">
          <h4 style="font-size:0.95rem;font-weight:600;color:#1f2937;margin:0">${product.name}</h4>
          ${badgeHtml}
        </div>
        <p style="font-size:0.85rem;color:#6b7280;margin:0 0 10px 0">${product.description}</p>
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-size:0.85rem;font-weight:600;color:#059669">${product.price}</span>
          <a href="https://www.amazon.com/s?k=${product.searchTerm}&tag=${TAG}" target="_blank" rel="noopener noreferrer nofollow sponsored" style="display:inline-flex;align-items:center;gap:4px;background:#ff9900;color:#fff;padding:6px 14px;border-radius:8px;font-size:0.8rem;font-weight:600;text-decoration:none">View on Amazon &#8599;</a>
        </div>
      </div>`;
}

function buildAffiliateSection(products, title = 'Donor Essentials') {
  const cards = products.map(p => buildProductCard(p)).join('\n');

  return `
<!-- Affiliate Products Section -->
<section style="max-width:800px;margin:2rem auto;padding:24px;background:linear-gradient(135deg,#fffbeb,#fef3c7);border:2px solid #fcd34d;border-radius:16px">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
    <span style="font-size:1.3rem">&#128722;</span>
    <h3 style="font-size:1.15rem;font-weight:700;color:#1f2937;margin:0">${title}</h3>
  </div>
  <p style="font-size:0.75rem;color:#9ca3af;margin:0 0 16px 0">As an Amazon Associate, we earn from qualifying purchases at no extra cost to you.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px">
    ${cards}
  </div>
</section>
<!-- End Affiliate Products Section -->
`;
}

function processFile(filePath, products, title) {
  let html = fs.readFileSync(filePath, 'utf-8');

  // Skip if already has affiliate links
  if (html.includes('amazon.com') || html.includes('amzn.to') || html.includes('Affiliate Products Section')) {
    return false;
  }

  const section = buildAffiliateSection(products, title);

  // Insert before the inline CTA script or before </body>
  if (html.includes('window.INLINE_CTA_CONFIG')) {
    html = html.replace('<script>window.INLINE_CTA_CONFIG', section + '\n<script>window.INLINE_CTA_CONFIG');
  } else if (html.includes('</body>')) {
    html = html.replace('</body>', section + '\n</body>');
  } else {
    return false;
  }

  fs.writeFileSync(filePath, html, 'utf-8');
  return true;
}

function processDirectory(dirPath, products, title) {
  let count = 0;
  const files = [];

  function walk(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(fullPath);
      } else if (entry.name.endsWith('.html')) {
        files.push(fullPath);
      }
    }
  }

  walk(dirPath);

  for (const file of files) {
    if (processFile(file, products, title)) {
      count++;
    }
  }

  return count;
}

// Main
const baseDir = path.resolve(__dirname, '..');

const targets = [
  { dir: 'calculators', products: donorEssentials, title: 'Donor Essentials — Prepare for Your Visit' },
  { dir: 'centers', products: donorEssentials, title: 'Donor Essentials — What to Bring' },
  { dir: 'cities', products: donorEssentials, title: 'Donor Essentials — Prepare for Your Visit' },
  { dir: 'states', products: donorEssentials, title: 'Donor Essentials — Prepare for Your Visit' },
  { dir: 'health', products: healthProducts, title: 'Health Products for Plasma Donors' },
  { dir: 'topics', products: healthProducts, title: 'Recommended Products for Donors' },
  { dir: 'process', products: donorEssentials, title: 'Donor Essentials — What to Bring' },
  { dir: 'tools', products: donorEssentials, title: 'Donor Essentials' },
];

let total = 0;

for (const target of targets) {
  const dirPath = path.join(baseDir, target.dir);
  if (!fs.existsSync(dirPath)) {
    console.log(`Skipping ${target.dir} (not found)`);
    continue;
  }
  const count = processDirectory(dirPath, target.products, target.title);
  console.log(`${target.dir}: ${count} pages updated`);
  total += count;
}

console.log(`\nTotal: ${total} pages updated with affiliate sections`);
