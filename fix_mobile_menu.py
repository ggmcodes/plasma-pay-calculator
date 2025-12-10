#!/usr/bin/env python3
"""
Add missing toggleMobileMenu JavaScript function to HTML files.
Fixes mobile navigation menu functionality across the site.
"""

import re
from pathlib import Path
import sys

MOBILE_MENU_SCRIPT = """    <script>
        function toggleMobileMenu() {
            const mobileMenu = document.getElementById('mobileMenu');
            mobileMenu.classList.toggle('active');
        }
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const mobileMenu = document.getElementById('mobileMenu');
            const menuBtn = document.querySelector('.mobile-menu-btn');

            if (!mobileMenu.contains(event.target) && !menuBtn.contains(event.target)) {
                mobileMenu.classList.remove('active');
            }
        });
    </script>
"""

def needs_mobile_menu_script(content):
    """Check if file needs the mobile menu script"""
    # Has mobile menu button?
    has_button = 'onclick="toggleMobileMenu()"' in content or "onclick='toggleMobileMenu()'" in content

    # Already has function?
    has_function = 'function toggleMobileMenu' in content

    # Needs script if has button but no function
    return has_button and not has_function

def add_mobile_menu_script(content):
    """Add mobile menu script before </body> tag"""

    # Find </body> tag
    if '</body>' not in content:
        return content, False

    # Insert script before </body>
    content = content.replace('</body>', MOBILE_MENU_SCRIPT + '\n</body>')

    return content, True

def fix_file(file_path, dry_run=False):
    """Fix a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not needs_mobile_menu_script(content):
            return False, None

        new_content, modified = add_mobile_menu_script(content)

        if modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return modified, None

    except Exception as e:
        return False, str(e)

def main():
    """Main function"""
    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    if test_mode:
        print("=== TEST MODE - 3 Sample Files ===\n")
        test_files = [
            'contact.html',
            'calculators/california/los-angeles/index.html',
            'blog/how-much-money-can-you-make-donating-plasma-2025.html'
        ]
        html_files = [Path(f) for f in test_files if Path(f).exists()]
    else:
        print("=== FIXING MOBILE MENU ACROSS ALL FILES ===\n")
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
            html_files.extend(Path('.').glob(pattern))
        html_files = list(set(html_files))

    print(f"Found {len(html_files)} HTML files to check\n")

    fixed_count = 0
    skipped_count = 0
    error_count = 0
    errors = []

    for html_file in html_files:
        modified, error = fix_file(html_file, dry_run=dry_run)

        if error:
            error_count += 1
            errors.append((html_file, error))
            print(f"❌ Error: {html_file}: {error}")
        elif modified:
            fixed_count += 1
            status = "Would fix" if dry_run else "✓ Fixed"
            print(f"{status}: {html_file}")
        else:
            skipped_count += 1

    print(f"\n=== COMPLETE ===")
    print(f"Fixed: {fixed_count} files")
    print(f"Skipped: {skipped_count} files (already have function or no mobile menu)")
    print(f"Errors: {error_count} files")

    if errors:
        print("\n=== ERRORS ===")
        for file_path, error in errors:
            print(f"{file_path}: {error}")

    return 0 if error_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
