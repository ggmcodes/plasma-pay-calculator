#!/usr/bin/env python3
"""
Add internal links from plasma center brand names to /centers/ page
- CSL Plasma → /centers/
- BioLife Plasma → /centers/
- Grifols Plasma → /centers/
- Octapharma Plasma → /centers/
- KEDPLASMA → /centers/

Only link brand names in center cards/sections, not in general text.
"""

import re
from pathlib import Path

# Brand names and their variations
BRANDS = {
    'CSL Plasma': '/centers/',
    'BioLife Plasma': '/centers/',
    'BioLife': '/centers/',
    'Grifols Plasma': '/centers/',
    'Grifols': '/centers/',
    'Octapharma Plasma': '/centers/',
    'Octapharma': '/centers/',
    'KEDPLASMA': '/centers/',
}

def add_brand_links(file_path):
    """Add links to brand names in plasma center sections"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Only link brand names in center cards (h3 tags within center sections)
        # Pattern: <h3 class="text-xl font-bold text-gray-900 mb-3">CSL Plasma</h3>
        # Replace with: <h3 class="text-xl font-bold text-gray-900 mb-3"><a href="/centers/" class="text-gray-900 hover:text-blue-600 transition-colors">CSL Plasma</a></h3>

        for brand_name, url in BRANDS.items():
            # Pattern for h3 tags with brand names (in center cards)
            pattern = rf'(<h3 class="text-xl font-bold text-gray-900 mb-3">)({re.escape(brand_name)})(</h3>)'
            replacement = rf'\1<a href="{url}" class="text-gray-900 hover:text-blue-600 transition-colors">\2</a>\3'
            content = re.sub(pattern, replacement, content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    print("=== ADDING BRAND NAME INTERNAL LINKS ===\n")
    print("Linking plasma center brands to /centers/ page...\n")

    # Find all city pages
    calculators_dir = Path('calculators')
    city_pages = []

    for state_dir in calculators_dir.iterdir():
        if state_dir.is_dir():
            for city_dir in state_dir.iterdir():
                if city_dir.is_dir():
                    index_file = city_dir / 'index.html'
                    if index_file.exists():
                        city_pages.append(index_file)

    print(f"Found {len(city_pages)} city pages to process\n")

    updated_count = 0
    links_added = 0

    for city_page in city_pages:
        if add_brand_links(city_page):
            updated_count += 1
            # Estimate 3-6 brand mentions per page
            links_added += 4  # Average
            if updated_count % 50 == 0:
                print(f"Progress: {updated_count}/{len(city_pages)} pages updated")

    print(f"\n=== COMPLETE ===")
    print(f"Updated: {updated_count} city pages")
    print(f"Estimated links added: ~{links_added} internal links")
    print(f"\nBrand names now link to /centers/:")
    print("  • CSL Plasma → /centers/")
    print("  • BioLife Plasma → /centers/")
    print("  • Grifols Plasma → /centers/")
    print("  • Octapharma Plasma → /centers/")
    print("  • KEDPLASMA → /centers/")
    print(f"\nBenefits:")
    print("  ✓ Better navigation to center finder")
    print("  ✓ Stronger internal linking structure")
    print("  ✓ Improved SEO with contextual links")
    print("  ✓ Enhanced user experience")

if __name__ == '__main__':
    main()
