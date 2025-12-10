#!/usr/bin/env python3
"""
Add hreflang tags to English calculator pages for proper international SEO.
Fixes missing hreflang implementation across ~323 English pages.
"""

import re
from pathlib import Path
import sys

def has_hreflang_tags(content):
    """Check if page already has hreflang tags"""
    return 'hreflang="en"' in content or 'hreflang="es"' in content

def extract_url_path(file_path):
    """Extract URL path from file path"""
    # Convert file path to URL path
    path_str = str(file_path).replace('\\', '/')

    # Handle NYC borough pages
    if 'calculators/new-york/' in path_str:
        # Extract borough name
        match = re.search(r'calculators/new-york/([^/]+)/index\.html', path_str)
        if match:
            borough = match.group(1)
            return f'/calculators/new-york/{borough}/'

    # Handle regular city pages
    match = re.search(r'calculators/([^/]+)/([^/]+)/index\.html', path_str)
    if match:
        state = match.group(1)
        city = match.group(2)
        return f'/calculators/{state}/{city}/'

    return None

def generate_hreflang_tags(url_path):
    """Generate hreflang tags for a given URL path"""
    base_url = "https://plasmapaycalculator.com"

    # Convert English path to Spanish path
    spanish_path = f"/es{url_path}"

    hreflang_html = f'''
    <!-- Hreflang tags -->
    <link rel="alternate" hreflang="en" href="{base_url}{url_path}">
    <link rel="alternate" hreflang="es" href="{base_url}{spanish_path}">
    <link rel="alternate" hreflang="x-default" href="{base_url}{url_path}">
'''

    return hreflang_html

def add_hreflang_to_page(file_path, dry_run=False):
    """Add hreflang tags to a single HTML page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has hreflang
        if has_hreflang_tags(content):
            return False, "Already has hreflang tags"

        # Extract URL path
        url_path = extract_url_path(file_path)
        if not url_path:
            return False, "Could not extract URL path"

        # Generate hreflang tags
        hreflang_tags = generate_hreflang_tags(url_path)

        # Find insertion point (after Open Graph tags, before Twitter Cards or Schema)
        # Look for the last Open Graph tag
        og_pattern = r'(<meta property="og:[^"]+"\s+content="[^"]*">)'
        og_matches = list(re.finditer(og_pattern, content))

        if og_matches:
            # Insert after last OG tag
            last_og_match = og_matches[-1]
            insert_pos = last_og_match.end()

            new_content = content[:insert_pos] + '\n' + hreflang_tags + content[insert_pos:]

            if not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

            return True, None
        else:
            return False, "Could not find Open Graph tags"

    except Exception as e:
        return False, str(e)

def main():
    """Main function to add hreflang tags to English pages"""
    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    print("=== ADDING HREFLANG TAGS TO ENGLISH PAGES ===\n")

    if test_mode:
        print("=== TEST MODE - Testing on 3 sample files ===\n")
        test_files = [
            'calculators/new-york/manhattan/index.html',
            'calculators/california/los-angeles/index.html',
            'calculators/texas/houston/index.html'
        ]
        html_files = [Path(f) for f in test_files if Path(f).exists()]
    else:
        # Find all English calculator pages
        print("Finding all English calculator HTML files...\n")
        html_files = []

        # NYC borough pages
        nyc_boroughs = ['manhattan', 'brooklyn', 'queens', 'bronx', 'staten-island']
        for borough in nyc_boroughs:
            borough_file = Path(f'calculators/new-york/{borough}/index.html')
            if borough_file.exists():
                html_files.append(borough_file)

        # All other calculator pages
        calculators_path = Path('calculators')
        if calculators_path.exists():
            for state_dir in calculators_path.iterdir():
                if state_dir.is_dir():
                    for city_dir in state_dir.iterdir():
                        if city_dir.is_dir():
                            index_file = city_dir / 'index.html'
                            if index_file.exists() and index_file not in html_files:
                                html_files.append(index_file)

        html_files.sort()

    print(f"Found {len(html_files)} English HTML files to process\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0
    errors = []

    for html_file in html_files:
        modified, error = add_hreflang_to_page(html_file, dry_run=dry_run)

        if error:
            if "Already has hreflang" in error:
                skipped_count += 1
            else:
                error_count += 1
                errors.append((html_file, error))
                print(f"❌ Error: {html_file}: {error}")
        elif modified:
            updated_count += 1
            status = "Would update" if dry_run else "✓ Updated"
            print(f"{status}: {html_file}")
        else:
            skipped_count += 1

    print(f"\n=== COMPLETE ===")
    print(f"Updated: {updated_count} files")
    print(f"Skipped: {skipped_count} files (already have hreflang or no changes needed)")
    print(f"Errors: {error_count} files")

    if errors:
        print("\n=== ERRORS ===")
        for file_path, error in errors:
            print(f"{file_path}: {error}")

    if not dry_run and updated_count > 0:
        print(f"\n✅ Added hreflang tags to {updated_count} English pages for international SEO!")

    return 0 if error_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
