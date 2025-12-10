#!/usr/bin/env python3
"""
Fix Spanish navigation menu:
1. Move Centers button to far right
2. Add English language switcher (EN)
3. Ensure consistent navigation order

Target order: Calculadora | Blog | Estados | Salud | FAQ | EN | Centros
"""

import re
from pathlib import Path
import sys

def reorder_spanish_navigation_block(nav_block):
    """Reorder Spanish navigation links to move Centers to the right and add EN switcher"""

    # Extract individual nav items - Spanish specific patterns
    nav_items = {
        'calculadora': None,
        'blog': None,
        'estados': None,
        'centros': None,
        'salud': None,
        'faq': None,
        'language': None
    }

    # Calculadora
    calc_match = re.search(r'<li>\s*<a href="/es/#calculator"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if calc_match:
        nav_items['calculadora'] = calc_match.group(0)

    # Blog
    blog_match = re.search(r'<li>\s*<a href="/es/blog/"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if blog_match:
        nav_items['blog'] = blog_match.group(0)

    # Estados (States)
    estados_match = re.search(r'<li>\s*<a href="/es/states\.html"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if estados_match:
        nav_items['estados'] = estados_match.group(0)

    # Centros (Centers) - may have class="centers-highlight"
    centros_match = re.search(r'<li>\s*<a href="/es/centers/"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if centros_match:
        nav_items['centros'] = centros_match.group(0)

    # Salud (Health)
    salud_match = re.search(r'<li>\s*<a href="/es/health/"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if salud_match:
        nav_items['salud'] = salud_match.group(0)

    # FAQ
    faq_match = re.search(r'<li>\s*<a href="/es/faq\.html"[^>]*>.*?</a>\s*</li>', nav_block, re.DOTALL)
    if faq_match:
        nav_items['faq'] = faq_match.group(0)

    # Language switcher (EN) - check if already exists
    lang_match = re.search(r'<li>\s*<a href="/"[^>]*>.*?EN.*?</a>\s*</li>', nav_block, re.DOTALL)
    if lang_match:
        nav_items['language'] = lang_match.group(0)
    else:
        # Create EN language switcher
        nav_items['language'] = '<li><a href="/" class="language-switcher" title="English">🇺🇸 EN</a></li>'

    # If Centros wasn't found, don't modify this block
    if not nav_items['centros']:
        return nav_block

    # Build new navigation in desired order
    # Order: Calculadora | Blog | Estados | Salud | FAQ | EN | Centros
    new_items = []
    for key in ['calculadora', 'blog', 'estados', 'salud', 'faq', 'language', 'centros']:
        if nav_items[key]:
            new_items.append(nav_items[key])

    # Detect indentation from original block
    first_li = re.search(r'\n(\s*)<li>', nav_block)
    indent = first_li.group(1) if first_li else '                '

    # Build new nav block
    new_nav_content = '\n' + indent + ('\n' + indent).join(new_items) + '\n' + indent.replace('    ', '', 1)

    return new_nav_content


def reorder_spanish_navigation(content):
    """Reorder navigation links in Spanish HTML content"""

    modified = False

    # Pattern for desktop navigation: <ul class="nav-links">...</ul>
    def replace_desktop_nav(match):
        nonlocal modified
        opening = match.group(1)
        nav_content = match.group(2)
        closing = match.group(3)

        new_nav_content = reorder_spanish_navigation_block(nav_content)

        if new_nav_content != nav_content:
            modified = True

        return opening + new_nav_content + closing

    # Update desktop navigation
    desktop_nav_pattern = r'(<ul class="nav-links">)(.*?)(</ul>)'
    content = re.sub(desktop_nav_pattern, replace_desktop_nav, content, flags=re.DOTALL)

    # Pattern for mobile navigation
    def replace_mobile_nav(match):
        nonlocal modified
        opening = match.group(1)
        nav_content = match.group(2)
        closing = match.group(3)

        new_nav_content = reorder_spanish_navigation_block(nav_content)

        if new_nav_content != nav_content:
            modified = True

        return opening + new_nav_content + closing

    # Update mobile navigation
    mobile_nav_pattern = r'(<div class="mobile-menu"[^>]*>\s*<ul>)(.*?)(</ul>\s*</div>)'
    content = re.sub(mobile_nav_pattern, replace_mobile_nav, content, flags=re.DOTALL)

    return content, modified


def update_navigation_in_file(file_path, dry_run=False):
    """Update navigation in a single Spanish HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, modified = reorder_spanish_navigation(content)

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
    """Main function to reorganize Spanish navigation"""

    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    if test_mode:
        print("=== TEST MODE - Testing on 3 sample Spanish files ===\n")

        test_files = [
            'es/index.html',
            'es/blog/index.html',
            'es/calculators/california/index.html'
        ]

        html_files = [Path(f) for f in test_files if Path(f).exists()]

        if len(html_files) < len(test_files):
            print("⚠️  Warning: Some test files don't exist:")
            for f in test_files:
                if not Path(f).exists():
                    print(f"   - {f}")
            print()
    else:
        print("=== FIXING SPANISH NAVIGATION MENU ===\n")
        print("Finding all Spanish HTML files...\n")

        # Find all Spanish HTML files
        html_files = list(Path('es').glob('**/*.html'))
        html_files.sort()

    print(f"Found {len(html_files)} Spanish HTML files to process\n")

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
        print(f"\n✅ New Spanish menu order: Calculadora | Blog | Estados | Salud | FAQ | EN | Centros")

    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
