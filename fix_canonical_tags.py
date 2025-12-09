#!/usr/bin/env python3
"""
Fix canonical tag issues across all HTML files.
Addresses Google Search Console "Alternate page with proper canonical tag" warnings.
"""

import re
from pathlib import Path

# California blog posts that should canonicalize to main blog posts
CALIFORNIA_TO_MAIN = {
    'can-you-make-1000-month-donating-plasma.html': 'can-you-make-1000-month-donating-plasma',
    'do-plasma-centers-report-social-security.html': 'do-plasma-centers-report-social-security',
    'do-you-get-1099-plasma-donation.html': 'do-you-get-1099-plasma-donation',
    'does-irs-track-plasma-donations.html': 'does-irs-track-plasma-donations',
    'first-time-plasma-donation.html': 'first-time-plasma-donation',
    'maximize-plasma-earnings.html': 'maximize-plasma-earnings',
    'plasma-center-comparison.html': 'plasma-center-comparison',
    'plasma-donation-requirements.html': 'plasma-donation-requirements',
    'plasma-donation-schedule.html': 'plasma-donation-schedule',
    'plasma-donation-taxes.html': 'plasma-donation-taxes',
    'california-plasma-donation-maximize-earnings.html': 'maximize-plasma-earnings',
}

def fix_canonical_tags(file_path):
    """Fix canonical tag issues in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    original_content = content

    # Fix 1: Remove www from canonical URLs (force non-www)
    content = re.sub(
        r'<link rel="canonical" href="https://www\.plasmapaycalculator\.com',
        '<link rel="canonical" href="https://plasmapaycalculator.com',
        content,
        flags=re.IGNORECASE
    )

    # Also fix href= format
    content = re.sub(
        r'<link href="https://www\.plasmapaycalculator\.com([^"]+)" rel="canonical"',
        r'<link rel="canonical" href="https://plasmapaycalculator.com\1"',
        content,
        flags=re.IGNORECASE
    )

    # Fix 2: Handle California blog posts -> main blog canonicals
    if '/blog/california/' in str(file_path):
        filename = file_path.name
        if filename in CALIFORNIA_TO_MAIN:
            main_slug = CALIFORNIA_TO_MAIN[filename]
            # Replace California canonical with main blog canonical
            # Match any California blog canonical and replace with main blog version
            pattern = r'<link rel="canonical" href="https://plasmapaycalculator\.com/blog/california/[^"]+">'
            replacement = f'<link rel="canonical" href="https://plasmapaycalculator.com/blog/{main_slug}">'
            content = re.sub(pattern, replacement, content)

            # Also check href= format
            pattern2 = r'<link href="https://plasmapaycalculator\.com/blog/california/[^"]+" rel="canonical"'
            replacement2 = f'<link rel="canonical" href="https://plasmapaycalculator.com/blog/{main_slug}"'
            content = re.sub(pattern2, replacement2, content)

    # Fix 3: Fix broken # canonical (california-tech-irs-plasma-tracking.html)
    content = re.sub(
        r'<link rel="canonical" href="#">',
        '<link rel="canonical" href="https://plasmapaycalculator.com/blog/does-irs-track-plasma-donations">',
        content,
        flags=re.IGNORECASE
    )

    # Fix 4: Fix best-side-hustle-2025.html canonical (missing .html extension)
    if file_path.name == 'best-side-hustle-2025.html':
        content = re.sub(
            r'<link rel="canonical" href="https://plasmapaycalculator\.com/best-side-hustle-2025">',
            '<link rel="canonical" href="https://plasmapaycalculator.com/best-side-hustle-2025.html">',
            content,
            flags=re.IGNORECASE
        )

    # Fix 5: Fix /es/states.html to point to itself (not English version)
    if file_path.name == 'states.html' and '/es' in str(file_path):
        # Fix canonical - try multiple patterns
        content = re.sub(
            r'<link rel="canonical" href="https://plasmapaycalculator\.com/states\.html">',
            '<link rel="canonical" href="https://plasmapaycalculator.com/es/states.html">',
            content
        )
        content = re.sub(
            r'<link href="https://plasmapaycalculator\.com/states\.html" rel="canonical"',
            '<link rel="canonical" href="https://plasmapaycalculator.com/es/states.html"',
            content
        )
        # Fix lang attribute
        content = re.sub(
            r'<html lang="en">',
            '<html lang="es">',
            content
        )

    # Only write if content changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False

    return False

def main():
    print("=== FIXING CANONICAL TAG ISSUES ===\n")

    # Directories to scan
    directories = [
        Path('blog'),
        Path('blog/california'),
        Path('es/blog'),
        Path('es'),
        Path('.'),  # Root directory
    ]

    updated_files = []
    skipped = 0

    for directory in directories:
        if not directory.exists():
            print(f"Skipping {directory} (doesn't exist)")
            continue

        print(f"Scanning {directory}/...")

        for html_file in directory.glob('*.html'):
            # Skip subdirectories when scanning root
            if directory == Path('.') and html_file.is_dir():
                continue

            if fix_canonical_tags(html_file):
                updated_files.append(str(html_file))
                print(f"  ✓ Updated: {html_file}")
            else:
                skipped += 1

    print(f"\n=== COMPLETE ===")
    print(f"Files updated: {len(updated_files)}")
    print(f"Files skipped (no changes needed): {skipped}")

    if updated_files:
        print(f"\nUpdated files:")
        for file in updated_files[:20]:  # Show first 20
            print(f"  - {file}")
        if len(updated_files) > 20:
            print(f"  ... and {len(updated_files) - 20} more")

    print(f"\nChanges made:")
    print(f"  • Standardized to non-www (plasmapaycalculator.com)")
    print(f"  • Fixed California blog duplicates → main blog canonicals")
    print(f"  • Fixed broken # canonical")
    print(f"  • Fixed /es/states.html canonical and lang attribute")
    print(f"  • Fixed file extension inconsistencies")

if __name__ == '__main__':
    main()
