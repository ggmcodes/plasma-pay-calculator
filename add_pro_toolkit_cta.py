#!/usr/bin/env python3
"""
Add Pro Toolkit CTA to all blog posts.
Inserts after the 3rd </h2> tag (mid-article) if not already present.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path('/Users/glengomezmeade/plasma-pay-calculator')
BLOG_DIR = BASE_DIR / 'blog'

CTA_HTML = '''
<!-- Pro Toolkit CTA -->
<div style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 100%); border-radius: 12px; padding: 1.5rem 2rem; text-align: center; color: white; margin: 2rem 0;">
    <p style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; margin: 0 0 0.3rem;">Premium Resource</p>
    <p style="font-size: 1.1rem; font-weight: 700; margin: 0 0 0.4rem;">Plasma Donor Pro Toolkit</p>
    <p style="font-size: 0.85rem; opacity: 0.9; margin: 0 0 1rem; max-width: 500px; margin-left: auto; margin-right: auto;">90-day earning playbook, bonus stacking strategy, 2026 tax guide &amp; deduction checklist. Earn $2,000+ in your first 3 months.</p>
    <a href="/premium/" style="display: inline-block; background: white; color: #0d9488; padding: 0.6rem 1.4rem; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.9rem;">Get the Pro Toolkit &mdash; $19</a>
</div>
'''

MARKER = '<!-- Pro Toolkit CTA -->'

stats = {'modified': 0, 'skipped_has_cta': 0, 'skipped_too_short': 0, 'errors': 0}


def add_cta_to_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Skip if already has the CTA
        if MARKER in html:
            stats['skipped_has_cta'] += 1
            return

        # Find all </h2> positions
        h2_closes = [m.end() for m in re.finditer(r'</h2>', html, re.IGNORECASE)]

        # Need at least 3 h2 tags to insert after the 3rd
        if len(h2_closes) < 3:
            # Try after 2nd if we have at least 2
            if len(h2_closes) >= 2:
                insert_pos = h2_closes[1]
            else:
                stats['skipped_too_short'] += 1
                return
        else:
            insert_pos = h2_closes[2]

        # Find the end of the next closing tag after our insert position
        # to avoid breaking mid-section
        next_section = html.find('</section>', insert_pos)
        next_div = html.find('</div>', insert_pos)

        # Insert CTA right after the </h2>
        new_html = html[:insert_pos] + CTA_HTML + html[insert_pos:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)

        stats['modified'] += 1

    except Exception as e:
        print(f'  ERROR: {filepath.name}: {e}')
        stats['errors'] += 1


def main():
    print('Adding Pro Toolkit CTA to blog posts...\n')

    # Process blog/ directory
    blog_files = sorted(BLOG_DIR.glob('*.html'))
    print(f'Found {len(blog_files)} blog files')

    for f in blog_files:
        add_cta_to_file(f)

    # Process root-level guide articles (common patterns)
    root_guides = []
    for pattern in [
        'comprehensive-plasma-*.html',
        'how-much-*.html',
        'make-*.html',
        'best-side-hustle-*.html',
    ]:
        root_guides.extend(BASE_DIR.glob(pattern))

    print(f'Found {len(root_guides)} root-level guide files')

    for f in root_guides:
        add_cta_to_file(f)

    print(f'\nDone!')
    print(f'  Modified:           {stats["modified"]}')
    print(f'  Already had CTA:    {stats["skipped_has_cta"]}')
    print(f'  Too short (< 2 h2): {stats["skipped_too_short"]}')
    print(f'  Errors:             {stats["errors"]}')


if __name__ == '__main__':
    main()
