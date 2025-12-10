#!/usr/bin/env python3
"""
Fix canonical URL inconsistencies on Spanish calculator pages.
Changes canonical from /estado/ path to /calculators/ path to match actual URLs.
"""

import re
from pathlib import Path
import sys

def fix_canonical_url(content, actual_path):
    """Fix canonical URL to match actual page path"""

    # Pattern to find canonical link
    canonical_pattern = r'<link rel="canonical" href="([^"]+)">'

    match = re.search(canonical_pattern, content)
    if not match:
        return content, False, "No canonical tag found"

    current_canonical = match.group(1)

    # Check if canonical already correct
    if actual_path in current_canonical:
        return content, False, "Canonical already correct"

    # Check if it's using the old /estado/ path
    if '/estado/' not in current_canonical:
        return content, False, "Not using /estado/ path"

    # Build correct canonical URL
    correct_canonical = f"https://plasmapaycalculator.com{actual_path}"

    # Replace canonical URL
    new_content = content.replace(
        f'<link rel="canonical" href="{current_canonical}">',
        f'<link rel="canonical" href="{correct_canonical}">'
    )

    return new_content, True, None

def extract_url_path(file_path):
    """Extract URL path from file path"""
    path_str = str(file_path).replace('\\', '/')

    # Handle NYC borough pages
    if 'es/calculators/new-york/' in path_str:
        match = re.search(r'es/calculators/new-york/([^/]+)/index\.html', path_str)
        if match:
            borough = match.group(1)
            return f'/es/calculators/new-york/{borough}/'

    # Handle regular city pages
    match = re.search(r'es/calculators/([^/]+)/([^/]+)/index\.html', path_str)
    if match:
        state = match.group(1)
        city = match.group(2)
        return f'/es/calculators/{state}/{city}/'

    return None

def fix_spanish_canonical(file_path, dry_run=False):
    """Fix canonical URL in a single Spanish HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract actual URL path
        url_path = extract_url_path(file_path)
        if not url_path:
            return False, "Could not extract URL path"

        # Fix canonical URL
        new_content, modified, error = fix_canonical_url(content, url_path)

        if error:
            return False, error

        if modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return modified, None

    except Exception as e:
        return False, str(e)

def main():
    """Main function to fix Spanish canonical URLs"""
    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    print("=== FIXING SPANISH CANONICAL URLs ===\n")

    if test_mode:
        print("=== TEST MODE - Testing on 3 sample Spanish files ===\n")
        test_files = [
            'es/calculators/new-york/manhattan/index.html',
            'es/calculators/california/los-angeles/index.html',
            'es/calculators/texas/houston/index.html'
        ]
        html_files = [Path(f) for f in test_files if Path(f).exists()]
    else:
        # Find all Spanish calculator pages
        print("Finding all Spanish calculator HTML files...\n")
        html_files = []

        es_calculators_path = Path('es/calculators')
        if es_calculators_path.exists():
            html_files = list(es_calculators_path.glob('**/*.html'))

        html_files.sort()

    print(f"Found {len(html_files)} Spanish HTML files to process\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0
    errors = []

    for html_file in html_files:
        modified, error = fix_spanish_canonical(html_file, dry_run=dry_run)

        if error:
            if "already correct" in error.lower() or "not using /estado/" in error.lower():
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
    print(f"Skipped: {skipped_count} files (already correct or no changes needed)")
    print(f"Errors: {error_count} files")

    if errors:
        print("\n=== ERRORS ===")
        for file_path, error in errors:
            print(f"{file_path}: {error}")

    if not dry_run and updated_count > 0:
        print(f"\n✅ Fixed canonical URLs on {updated_count} Spanish pages!")

    return 0 if error_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
