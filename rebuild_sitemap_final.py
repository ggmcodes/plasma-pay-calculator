#!/usr/bin/env python3
"""Rebuild sitemap.xml — remove deleted/redirected pages, add new ones, ensure only canonical pages."""
import os, glob
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = 'https://plasmapaycalculator.com'
TODAY = date.today().isoformat()

# Pages that should NOT be in sitemap (deleted or redirected)
EXCLUDED_PATTERNS = [
    '-2025',  # All 2025 pages deleted
]

EXCLUDED_EXACT = {
    # Redirected pages (from .htaccess)
    'blog/which-plasma-center-pays-most-2026.html',
    'blog/first-time-plasma-donor-complete-guide-2026.html',
    'blog/best-plasma-center-for-new-donors-2026.html',
    'blog/first-time-plasma-donation-bonus-calculator.html',
    'blog/best-products-plasma-donors.html',
    'blog/plasma-vs-blood-donation-2026.html',
    'blog/college-student-plasma-income-optimization-2026.html',
    'blog/plasma-donation-denver-co-2026.html',
    'blog/plasma-donation-miami-fl-2026.html',
    'blog/plasma-donation-las-vegas-nv-2026.html',
    'blog/plasma-donation-colorado-springs-co-2026.html',
    'blog/plasma-donation-atlanta-ga-2026.html',
    'blog/plasma-donation-houston-centers-pay-2026.html',
    'blog/best-plasma-center-chicago-illinois.html',
    'blog/best-plasma-center-los-angeles-california.html',
    'blog/plasma-donation-phoenix-centers-pay-2026.html',
    'blog/plasma-donation-dallas-centers-pay-2026.html',
    'blog/plasma-donation-colorado-springs-centers-pay-2026.html',
    'blog/csl-plasma-vs-biolife-comparison.html',
    'blog/csl-plasma-vs-biolife-2026-comparison.html',
    'blog/biolife-vs-csl-plasma-comparison.html',
    'blog/octapharma-vs-biolife-2026-comparison.html',
    'blog/grifols-vs-csl-plasma-2026-comparison.html',
    'blog/octapharma-plasma-pay-chart-2026.html',
    'blog/grifols-plasma-pay-chart-2026.html',
    'blog/kedplasma-pay-chart-2026.html',
    'blog/biolife-plasma-pay-chart-2026.html',
    'blog/biolife-plasma-weight-chart-2026.html',
    'blog/plasma-donation-weight-chart-visual-guide-2026.html',
    'blog/can-i-donate-plasma-with-diabetes-2026.html',
    'blog/can-you-donate-plasma-with-anxiety-2026.html',
    'blog/can-you-donate-plasma-if-anemic-2026.html',
    'blog/plasma-donation-referral-bonus-2026.html',
    'blog/plasma-referral-bonus-guide-2026.html',
    'blog/best-time-to-donate-plasma-2026.html',
    'blog/best-times-donate-plasma.html',
    'blog/how-to-prepare-for-plasma-donation.html',
    'blog/what-to-bring-first-plasma-donation.html',
    'blog/first-time-plasma-donation-what-to-expect.html',
    'blog/first-time-plasma-donation.html',
    'blog/plasma-donation-eligibility-requirements-comprehensive-guide-2026.html',
    'blog/plasma-donation-eligibility-requirements-comprehensive-guide-2025.html',
    'blog/plasma-donation-requirements-2026.html',
    'blog/plasma-donation-requirements-2025.html',
    'blog/plasma-donation-eligibility-requirements-2026.html',
    'blog/plasma-donation-eligibility-quiz-viral.html',
    'es/blog/cuanto-pagan-por-donar-plasma.html',
    # Root redirected
    'csl-plasma-pay-chart-2026.html',
    'csl-plasma-pay-chart-2025.html',
}

def should_exclude(rel_path):
    """Check if a path should be excluded from sitemap."""
    for pattern in EXCLUDED_PATTERNS:
        if pattern in rel_path:
            return True
    if rel_path in EXCLUDED_EXACT:
        return True
    return False

def get_priority(rel_path):
    """Assign priority based on page type."""
    if rel_path in ('index.html', ''):
        return '1.0'
    if rel_path.startswith('calculators/'):
        return '0.9'
    if 'which-plasma-center-pays-most-money' in rel_path:
        return '0.9'
    if any(x in rel_path for x in ['csl-plasma-pay-rates', 'biolife-plasma-pay-rates', 'octapharma-plasma-pay-rates', 'grifols-plasma-pay-rates']):
        return '0.8'
    if rel_path.startswith('blog/'):
        return '0.7'
    if rel_path.startswith('es/blog/'):
        return '0.6'
    if rel_path.startswith(('centers/', 'states/', 'cities/')):
        return '0.6'
    return '0.6'

def get_changefreq(rel_path):
    if rel_path in ('index.html', ''):
        return 'daily'
    if 'pay-rates' in rel_path or 'pay-chart' in rel_path:
        return 'weekly'
    return 'monthly'

def collect_html_files():
    """Collect all HTML files that should be in the sitemap."""
    urls = set()

    # Scan known directories
    scan_dirs = [
        ('', ['*.html']),
        ('blog', ['*.html']),
        ('calculators', ['*.html']),
        ('centers', ['*.html', '**/*.html']),
        ('cities', ['*.html', '**/*.html']),
        ('states', ['*.html', '**/*.html']),
        ('es', ['*.html']),
        ('es/blog', ['*.html']),
        ('es/calculators', ['*.html']),
        ('health', ['*.html']),
        ('tools', ['*.html']),
        ('premium', ['*.html']),
        ('topics', ['*.html']),
        ('seasonal', ['*.html']),
    ]

    for subdir, patterns in scan_dirs:
        full_dir = os.path.join(BASE_DIR, subdir) if subdir else BASE_DIR
        if not os.path.isdir(full_dir):
            continue
        for pattern in patterns:
            for filepath in glob.glob(os.path.join(full_dir, pattern)):
                if os.path.isfile(filepath):
                    rel = os.path.relpath(filepath, BASE_DIR)
                    # Skip utility/script files
                    if rel.startswith('.') or rel.startswith('node_modules'):
                        continue
                    # Skip non-content files
                    skip_names = {'favicon-generator.html', 'create-favicons.html',
                                  'icon-generator.html', 'new-homepage-design.html'}
                    if os.path.basename(rel) in skip_names:
                        continue
                    if not should_exclude(rel):
                        urls.add(rel)

    return sorted(urls)

def build_sitemap(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

    for rel_path in urls:
        # Build URL
        url_path = rel_path
        if url_path == 'index.html':
            url = f'{DOMAIN}/'
        else:
            url = f'{DOMAIN}/{url_path}'

        priority = get_priority(rel_path)
        changefreq = get_changefreq(rel_path)

        lines.append(f'  <url>')
        lines.append(f'    <loc>{url}</loc>')
        lines.append(f'    <lastmod>{TODAY}</lastmod>')
        lines.append(f'    <changefreq>{changefreq}</changefreq>')
        lines.append(f'    <priority>{priority}</priority>')
        lines.append(f'  </url>')

    lines.append('</urlset>')
    return '\n'.join(lines)

if __name__ == '__main__':
    urls = collect_html_files()
    print(f"Found {len(urls)} pages for sitemap")

    # Count by type
    blog_en = sum(1 for u in urls if u.startswith('blog/'))
    blog_es = sum(1 for u in urls if u.startswith('es/blog/'))
    other = len(urls) - blog_en - blog_es
    print(f"  English blog: {blog_en}")
    print(f"  Spanish blog: {blog_es}")
    print(f"  Other pages: {other}")

    sitemap = build_sitemap(urls)
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"\nSitemap written to sitemap.xml ({len(urls)} URLs)")

    # Verify no excluded pages
    excluded_found = []
    for url in urls:
        if '-2025' in url:
            excluded_found.append(url)
        if url in EXCLUDED_EXACT:
            excluded_found.append(url)
    if excluded_found:
        print(f"\nWARNING: {len(excluded_found)} excluded pages still in sitemap!")
        for u in excluded_found:
            print(f"  - {u}")
    else:
        print("\nVerification: No excluded/redirected pages in sitemap")
