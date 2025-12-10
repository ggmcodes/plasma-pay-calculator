#!/usr/bin/env python3
"""
Phase 5: Fix sitemap.xml hreflang references
- Fix incorrect hreflang hrefs (both en and es pointing to same URL)
- Add x-default hreflang tags
- Add Spanish NYC borough URLs to sitemap
- Ensure proper en ↔ es bidirectional linking
"""

import re
from datetime import datetime
import sys

def fix_url_block(url_block):
    """Fix hreflang in a single URL block"""

    # Extract the loc URL
    loc_match = re.search(r'<loc>(https://plasmapaycalculator\.com[^<]+)</loc>', url_block)
    if not loc_match:
        return url_block, False

    english_url = loc_match.group(1)

    # Only process calculator URLs
    if '/calculators/' not in english_url:
        return url_block, False

    # Determine Spanish URL
    spanish_url = english_url.replace(
        'plasmapaycalculator.com/calculators/',
        'plasmapaycalculator.com/es/calculators/'
    )

    # Check if already correct
    if f'hreflang="es" href="{spanish_url}"' in url_block and 'hreflang="x-default"' in url_block:
        return url_block, False

    # Remove existing hreflang lines
    url_block = re.sub(r'\s*<html:link rel="alternate"[^>]+/>\n?', '', url_block)

    # Build new hreflang tags
    hreflang_tags = f'''    <html:link rel="alternate" hreflang="en" href="{english_url}" />
    <html:link rel="alternate" hreflang="es" href="{spanish_url}" />
    <html:link rel="alternate" hreflang="x-default" href="{english_url}" />
'''

    # Insert hreflang tags before closing </url>
    url_block = url_block.replace('</url>', hreflang_tags + '  </url>')

    return url_block, True

def get_spanish_url_blocks():
    """Generate URL blocks for Spanish NYC borough pages"""

    nyc_boroughs = [
        ('manhattan', 'Manhattan'),
        ('brooklyn', 'Brooklyn'),
        ('queens', 'Queens'),
        ('bronx', 'Bronx'),
        ('staten-island', 'Staten Island')
    ]

    today = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')

    spanish_blocks = []

    for slug, name in nyc_boroughs:
        english_url = f"https://plasmapaycalculator.com/calculators/new-york/{slug}/"
        spanish_url = f"https://plasmapaycalculator.com/es/calculators/new-york/{slug}/"

        spanish_block = f'''<url>
    <loc>{spanish_url}</loc>
    <lastmod>{today}</lastmod>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
    <html:link rel="alternate" hreflang="en" href="{english_url}" />
    <html:link rel="alternate" hreflang="es" href="{spanish_url}" />
    <html:link rel="alternate" hreflang="x-default" href="{english_url}" />
  </url>'''

        spanish_blocks.append(spanish_block)

    return spanish_blocks

def fix_sitemap(sitemap_path, dry_run=False):
    """Fix entire sitemap file"""

    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into URL blocks
    url_pattern = r'(<url>.*?</url>)'
    url_blocks = re.findall(url_pattern, content, re.DOTALL)

    fixed_count = 0
    new_blocks = []

    for url_block in url_blocks:
        fixed_block, was_fixed = fix_url_block(url_block)
        new_blocks.append(fixed_block)
        if was_fixed:
            fixed_count += 1

    # Check if Spanish NYC borough URLs already exist
    spanish_boroughs_exist = any(
        '/es/calculators/new-york/manhattan/' in block or
        '/es/calculators/new-york/brooklyn/' in block or
        '/es/calculators/new-york/queens/' in block or
        '/es/calculators/new-york/bronx/' in block or
        '/es/calculators/new-york/staten-island/' in block
        for block in new_blocks
    )

    added_spanish_boroughs = False
    if not spanish_boroughs_exist:
        # Add Spanish NYC borough URLs
        spanish_blocks = get_spanish_url_blocks()
        new_blocks.extend(spanish_blocks)
        added_spanish_boroughs = True
        print(f"✓ Added 5 Spanish NYC borough URLs to sitemap")

    # Reconstruct sitemap
    new_content = content[:content.find('<url>')]  # Header
    new_content += '\n'.join(new_blocks)
    new_content += '\n</urlset>'

    if not dry_run:
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return fixed_count, added_spanish_boroughs

def main():
    """Main function"""

    dry_run = '--dry-run' in sys.argv
    sitemap_path = 'sitemap.xml'

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    print("=== FIXING SITEMAP HREFLANG REFERENCES ===\n")

    try:
        fixed_count, added_spanish = fix_sitemap(sitemap_path, dry_run=dry_run)

        print(f"\n=== COMPLETE ===")
        print(f"Fixed hreflang: {fixed_count} calculator URLs")
        print(f"Added Spanish NYC boroughs: {'Yes (5 URLs)' if added_spanish else 'No (already exist)'}")

        if not dry_run:
            print(f"\n✅ Sitemap.xml updated with correct hreflang references!")
            print(f"   - Fixed {fixed_count} English calculator URLs")
            print(f"   - Added proper en ↔ es bidirectional linking")
            print(f"   - Added x-default hreflang tags")
            if added_spanish:
                print(f"   - Added 5 Spanish NYC borough URLs")

        return 0

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
