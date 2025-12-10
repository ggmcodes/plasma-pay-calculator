#!/usr/bin/env python3
"""
Reorganize navigation menu to move Centers button to far right.
Updates HTML files to reorder navigation consistently.

Target order: Calculator | Blog | States | Health | FAQ | ES (if present) | Centers
"""

import re
from pathlib import Path
import sys

def reorder_navigation_block(nav_block):
    """Reorder navigation links within a nav block to move Centers to the right"""

    # Extract individual nav items - be flexible with whitespace and line breaks
    nav_items = {
        'calculator': None,
        'blog': None,
        'states': None,
        'centers': None,
        'health': None,
        'faq': None,
        'language': None
    }

    # Pattern to match each nav item (including potential multi-line language switcher)
    # Calculator
    calc_match = re.search(r'<li>\s*<a href="/#calculator"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if calc_match:
        nav_items['calculator'] = calc_match.group(0)

    # Blog
    blog_match = re.search(r'<li>\s*<a href="/blog/"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if blog_match:
        nav_items['blog'] = blog_match.group(0)

    # States
    states_match = re.search(r'<li>\s*<a href="/states\.html"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if states_match:
        nav_items['states'] = states_match.group(0)

    # Centers - may have class="centers-highlight" or other attributes
    centers_match = re.search(r'<li>\s*<a href="/centers/"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if centers_match:
        nav_items['centers'] = centers_match.group(0)

    # Health
    health_match = re.search(r'<li>\s*<a href="/health/"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if health_match:
        nav_items['health'] = health_match.group(0)

    # FAQ
    faq_match = re.search(r'<li>\s*<a href="/faq\.html"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if faq_match:
        nav_items['faq'] = faq_match.group(0)

    # Language switcher - can be /es/ or / (for Spanish pages with EN switcher)
    # Match multi-line language switcher
    lang_match = re.search(r'<li>\s*(?:<a href="(?:/es/|/)"[^>]*class="language-switcher"[^>]*>.*?</a>|<a href="(?:/es/|/)"[^>]*>.*?(?:ES|EN).*?</a>)\s*</li>', nav_block, re.DOTALL)
    if lang_match:
        nav_items['language'] = lang_match.group(0)

    # If Centers wasn't found, don't modify this block
    if not nav_items['centers']:
        return nav_block

    # Build new navigation in desired order
    # Order: Calculator | Blog | States | Health | FAQ | Language | Centers
    new_items = []
    for key in ['calculator', 'blog', 'states', 'health', 'faq', 'language', 'centers']:
        if nav_items[key]:
            new_items.append(nav_items[key])

    # Join items with proper indentation (8 spaces for desktop nav, varies for mobile)
    # Detect indentation from original block
    first_li = re.search(r'\n(\s*)<li>', nav_block)
    indent = first_li.group(1) if first_li else '                '

    # Build new nav block
    new_nav_content = '\n' + indent + ('\n' + indent).join(new_items) + '\n' + indent.replace('    ', '', 1)

    return new_nav_content


def reorder_navigation(content):
    """Reorder navigation links in HTML content"""

    modified = False

    # Pattern for desktop navigation: <ul class="nav-links">...</ul>
    def replace_desktop_nav(match):
        nonlocal modified
        opening = match.group(1)  # <ul class="nav-links">
        nav_content = match.group(2)  # Everything inside <ul>...</ul>
        closing = match.group(3)  # </ul>

        new_nav_content = reorder_navigation_block(nav_content)

        if new_nav_content != nav_content:
            modified = True

        return opening + new_nav_content + closing

    # Update desktop navigation
    desktop_nav_pattern = r'(<ul class="nav-links">)(.*?)(</ul>)'
    content = re.sub(desktop_nav_pattern, replace_desktop_nav, content, flags=re.DOTALL)

    # Pattern for mobile navigation: <div class="mobile-menu" ...><ul>...</ul></div>
    def replace_mobile_nav(match):
        nonlocal modified
        opening = match.group(1)  # <div class="mobile-menu" ...><ul>
        nav_content = match.group(2)  # Everything inside <ul>...</ul>
        closing = match.group(3)  # </ul></div>

        new_nav_content = reorder_navigation_block(nav_content)

        if new_nav_content != nav_content:
            modified = True

        return opening + new_nav_content + closing

    # Update mobile navigation
    mobile_nav_pattern = r'(<div class="mobile-menu"[^>]*>\s*<ul>)(.*?)(</ul>\s*</div>)'
    content = re.sub(mobile_nav_pattern, replace_mobile_nav, content, flags=re.DOTALL)

    return content, modified


def update_navigation_in_file(file_path, dry_run=False):
    """Update navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, modified = reorder_navigation(content)

        if modified:
            if not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            return True, None
        else:
            return False, None

    except Exception as e:
        return False, str(e)


def main():
    """Main function to reorganize navigation across specified files"""

    # Check for dry-run mode
    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    if test_mode:
        print("=== TEST MODE - Testing on 6 sample files ===\n")

        # Test on 6 representative pages
        test_files = [
            'calculators/california/index.html',
            'calculators/california/los-angeles/index.html',
            'blog/index.html',
            'blog/how-much-money-can-you-make-donating-plasma-2025.html',
            'faq.html',
            'contact.html'
        ]

        html_files = [Path(f) for f in test_files if Path(f).exists()]

        if len(html_files) < len(test_files):
            print("⚠️  Warning: Some test files don't exist:")
            for f in test_files:
                if not Path(f).exists():
                    print(f"   - {f}")
            print()
    else:
        print("=== REORGANIZING NAVIGATION MENU ===\n")
        print("Finding all HTML files...\n")

        # Find all HTML files
        html_files = []
        patterns = [
            '*.html',
            'blog/*.html',
            'blog/**/*.html',
            'calculators/**/*.html',
            'topics/**/*.html',
            'seasonal/**/*.html',
            'es/**/*.html'
        ]

        for pattern in patterns:
            found = list(Path('.').glob(pattern))
            html_files.extend(found)

        # Remove duplicates
        html_files = list(set(html_files))
        html_files.sort()

    print(f"Found {len(html_files)} HTML files to process\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0
    errors = []

    for html_file in html_files:
        modified, error = update_navigation_in_file(html_file, dry_run=dry_run)

        if error:
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
    print(f"Skipped: {skipped_count} files (no changes needed)")
    print(f"Errors: {error_count} files")

    if errors:
        print("\n=== ERRORS ===")
        for file_path, error in errors:
            print(f"{file_path}: {error}")

    if not dry_run and updated_count > 0:
        print(f"\n✅ New menu order: Calculator | Blog | States | Health | FAQ | ES | Centers")

    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
