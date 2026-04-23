#!/usr/bin/env python3
"""Wire up placeholder href="#" affiliate product links to Amazon search URLs.

Pattern across the site:
    <a href="#" target="_blank" rel="noopener" class="...card-ish classes...">
        <span>emoji</span>
        [<div>]
            <h4 class="...">Product Name</h4>
            [<p>tagline</p>]
        [</div>]
    </a>

The <h4> text is the product name. We build:
    https://www.amazon.com/s?k=<url-encoded>&tag=plasma0f-20
and replace the href="#".

Processed link classes:
  - "flex items-center gap-3 bg-white p-4 rounded-lg hover:shadow-md transition-shadow" (and variants)
  - "bg-white p-3 rounded-lg hover:shadow-md transition-shadow text-center"
  - "flex items-center gap-3 bg-white p-3 rounded-lg hover:shadow-md transition-shadow"
  - "flex items-start gap-3 bg-white p-4 rounded-lg hover:shadow-md transition-shadow"
  - "inline-flex items-center gap-2 bg-white px-4 py-2 rounded-lg shadow hover:shadow-md transition-shadow"
  - class="product-link"

Usage:
  python3 wire_affiliate_links.py
  python3 wire_affiliate_links.py --dry-run
"""
import re
import sys
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent
AMAZON_TAG = 'plasma0f-20'

QUALIFYING_CLASSES = {
    'flex items-center gap-3 bg-white p-4 rounded-lg hover:shadow-md transition-shadow',
    'bg-white p-3 rounded-lg hover:shadow-md transition-shadow text-center',
    'flex items-center gap-3 bg-white p-3 rounded-lg hover:shadow-md transition-shadow',
    'flex items-start gap-3 bg-white p-4 rounded-lg hover:shadow-md transition-shadow',
    'inline-flex items-center gap-2 bg-white px-4 py-2 rounded-lg shadow hover:shadow-md transition-shadow',
    'product-link',
    'text-blue-600 hover:text-blue-700 font-medium hover:underline',
}

ANCHOR_RE = re.compile(
    r'<a\b([^>]*?)>(.*?)</a>',
    re.DOTALL | re.IGNORECASE,
)

CLASS_RE = re.compile(r'class="([^"]*)"', re.IGNORECASE)
HREF_HASH_RE = re.compile(r'href="#"', re.IGNORECASE)
HEADING_RE = re.compile(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', re.DOTALL | re.IGNORECASE)
TAG_STRIP_RE = re.compile(r'<[^>]+>')


def clean_text(s: str) -> str:
    s = TAG_STRIP_RE.sub(' ', s)
    s = s.replace('&amp;', '&').replace('&nbsp;', ' ').replace('&#39;', "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def build_amazon_url(product_name: str) -> str:
    q = quote_plus(product_name)
    return f'https://www.amazon.com/s?k={q}&tag={AMAZON_TAG}'


def process_content(content: str):
    replacements = 0

    def maybe_rewrite(m):
        nonlocal replacements
        attrs = m.group(1)
        inner = m.group(2)

        if not HREF_HASH_RE.search(attrs):
            return m.group(0)

        class_m = CLASS_RE.search(attrs)
        cls = class_m.group(1).strip() if class_m else ''
        is_qualifying_class = cls in QUALIFYING_CLASSES
        # For no-class links, require target="_blank" + rel="noopener" as the signal
        # that they were intended to be external/affiliate (and skip id= anchors).
        is_no_class_external = (
            not class_m
            and 'target="_blank"' in attrs
            and 'rel="noopener"' in attrs
            and 'id=' not in attrs
        )
        if not (is_qualifying_class or is_no_class_external):
            return m.group(0)

        h_m = HEADING_RE.search(inner)
        if h_m:
            product = clean_text(h_m.group(1))
        else:
            product = clean_text(inner)
        if not product or len(product) < 2:
            return m.group(0)

        new_href = build_amazon_url(product)
        new_attrs = HREF_HASH_RE.sub(f'href="{new_href}"', attrs, count=1)

        if 'rel=' not in new_attrs:
            new_attrs = new_attrs.rstrip() + ' rel="nofollow noopener sponsored"'
        else:
            if 'nofollow' not in new_attrs or 'sponsored' not in new_attrs:
                new_attrs = re.sub(
                    r'rel="([^"]*)"',
                    lambda rm: f'rel="{" ".join(set(rm.group(1).split()) | {"nofollow", "noopener", "sponsored"})}"',
                    new_attrs, count=1,
                )

        replacements += 1
        return f'<a{new_attrs}>{inner}</a>'

    new_content = ANCHOR_RE.sub(maybe_rewrite, content)
    return new_content, replacements


def main():
    dry_run = '--dry-run' in sys.argv

    html_files = []
    for p in ROOT.rglob('*.html'):
        if any(part in ('node_modules', '.git') for part in p.parts):
            continue
        if '.backup' in p.name:
            continue
        html_files.append(p)

    files_changed = 0
    total_replacements = 0

    for path in html_files:
        try:
            content = path.read_text(encoding='utf-8')
        except Exception:
            continue
        if 'href="#"' not in content:
            continue

        new_content, reps = process_content(content)
        if reps == 0:
            continue

        files_changed += 1
        total_replacements += reps

        if not dry_run:
            path.write_text(new_content, encoding='utf-8')

    print(f'Files with links wired: {files_changed}')
    print(f'Total href="#" replaced: {total_replacements}')
    if dry_run:
        print('(dry-run; no files written)')


if __name__ == '__main__':
    main()
