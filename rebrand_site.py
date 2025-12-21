#!/usr/bin/env python3
"""
Rebrand Script for Plasma Pay Calculator
Applies new design system across all HTML pages.

Design: Deep Teal + Yellow Gold, Libre Baskerville + Outfit
"""

import os
import re
from pathlib import Path
from typing import Tuple

# Configuration
BASE_DIR = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator')
SKIP_FILES = {
    'new-homepage-design.html',  # Template file
    'advertise.html',  # Already styled
}
SKIP_DIRS = {'node_modules', '.git', 'includes', 'css'}

# New head content to inject
HEAD_INJECT = '''
<!-- Plasma Pay Rebrand 2025 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/theme.css">
'''

# Load partials
def load_partial(name: str) -> str:
    partial_path = BASE_DIR / 'includes' / f'{name}.html'
    with open(partial_path, 'r', encoding='utf-8') as f:
        return f.read()

NAV_HTML = None
FOOTER_HTML = None

def init_partials():
    global NAV_HTML, FOOTER_HTML
    NAV_HTML = load_partial('nav')
    FOOTER_HTML = load_partial('footer')

def find_html_files() -> list:
    """Find all HTML files to process."""
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for file in files:
            if file.endswith('.html') and file not in SKIP_FILES:
                html_files.append(os.path.join(root, file))

    return sorted(html_files)

def inject_head_content(content: str) -> str:
    """Inject new stylesheets into <head>."""
    # Check if already has our theme
    if '/css/theme.css' in content:
        return content

    # Find the closing </head> tag and inject before it
    head_pattern = r'(</head>)'
    if re.search(head_pattern, content, re.IGNORECASE):
        content = re.sub(
            head_pattern,
            HEAD_INJECT + r'\1',
            content,
            count=1,
            flags=re.IGNORECASE
        )

    return content

def replace_nav(content: str) -> str:
    """Replace existing navigation with new nav."""
    # Pattern to match various nav formats
    nav_patterns = [
        # Standard <nav>...</nav>
        r'<nav[^>]*>[\s\S]*?</nav>',
        # Header with nav inside
        r'<header[^>]*class="[^"]*nav[^"]*"[^>]*>[\s\S]*?</header>',
    ]

    for pattern in nav_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            content = re.sub(pattern, NAV_HTML, content, count=1, flags=re.IGNORECASE)
            break

    return content

def replace_footer(content: str) -> str:
    """Replace existing footer with new footer."""
    # Pattern to match footer
    footer_pattern = r'<footer[^>]*>[\s\S]*?</footer>'

    if re.search(footer_pattern, content, re.IGNORECASE):
        content = re.sub(footer_pattern, FOOTER_HTML, content, count=1, flags=re.IGNORECASE)

    return content

def update_body_class(content: str) -> str:
    """Add/update body class for new styles."""
    # If body has no class, add one
    if re.search(r'<body(?:\s+[^>]*)?\s*>', content):
        # Check if body already has class
        if re.search(r'<body[^>]*class=', content):
            # Body has class, don't modify
            pass
        else:
            # Add class to body
            content = re.sub(
                r'<body(\s*[^>]*)?>',
                r'<body class="plasma-rebrand"\1>',
                content,
                count=1
            )
    return content

def remove_old_nav_styles(content: str) -> str:
    """Remove old inline nav/footer styles that conflict."""
    # This is optional - we can let CSS cascade handle it
    # For now, we'll leave inline styles but our theme.css will override
    return content

def process_file(filepath: str, dry_run: bool = False) -> Tuple[bool, str]:
    """Process a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()

        content = original_content

        # Apply transformations
        content = inject_head_content(content)
        content = replace_nav(content)
        content = replace_footer(content)
        content = update_body_class(content)

        # Check if anything changed
        if content == original_content:
            return False, 'No changes needed'

        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

        return True, 'Updated successfully'

    except Exception as e:
        return False, f'Error: {str(e)}'

def main(dry_run: bool = False):
    """Main function to process all files."""
    print("=" * 60)
    print("PLASMA PAY CALCULATOR - FULL REBRAND")
    print("=" * 60)
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print()

    # Initialize partials
    init_partials()

    # Find all HTML files
    html_files = find_html_files()
    print(f"Found {len(html_files)} HTML files to process")
    print()

    stats = {
        'updated': 0,
        'skipped': 0,
        'errors': 0
    }

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, BASE_DIR)
        success, message = process_file(filepath, dry_run)

        if success:
            stats['updated'] += 1
            print(f"  [OK] {rel_path}")
        elif 'Error' in message:
            stats['errors'] += 1
            print(f"  [ERR] {rel_path}: {message}")
        else:
            stats['skipped'] += 1
            # Don't print skipped files to reduce noise

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Updated: {stats['updated']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors:  {stats['errors']}")
    print()

    if dry_run:
        print("This was a DRY RUN. No files were modified.")
        print("Run with --live to apply changes.")
    else:
        print("Rebrand complete!")

if __name__ == '__main__':
    import sys
    dry_run = '--live' not in sys.argv
    main(dry_run=dry_run)
