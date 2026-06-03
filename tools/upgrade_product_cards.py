#!/usr/bin/env python3
"""Tier 2: turn plain <ul> affiliate lists into visual product-card grids.

Targets the uniform `<ul style="list-style: none; padding: 0;">...</ul>` blocks
that contain real amazon /dp/ links (the "Essential Products for Plasma Donors"
sections). Each <li> becomes a card with emoji + name + benefit + an orange
"Check Price" button, matching the high-converting pattern already used on the
best-products pages. Nothing is invented: href/name/benefit come from the
existing list item; emoji comes from the catalog by ASIN.

Usage: python3 tools/upgrade_product_cards.py [--apply]
"""
import re, sys, glob
sys.path.insert(0, "tools")
from affiliate_catalog import PRODUCTS

APPLY = "--apply" in sys.argv

UL_RE = re.compile(r'<ul style="list-style: none; padding: 0;">(.*?)</ul>', re.S)
LI_RE = re.compile(
    r'<li[^>]*>\s*<a href="(https://www\.amazon\.com/dp/([A-Z0-9]{10})[^"]*)"([^>]*)>([^<]+)</a>\s*'
    r'(?:[-–—]\s*)?([^<]*)</li>',
    re.S)

BTN = ('display:inline-block;background:#ff9900;color:#fff;padding:0.5rem 1rem;'
       'border-radius:6px;text-decoration:none;font-weight:600;font-size:0.85rem;margin-top:auto;')
CARD = ('background:#fff;border-radius:12px;padding:1.25rem;box-shadow:0 2px 8px rgba(0,0,0,0.08);'
        'border:1px solid #eee;display:flex;flex-direction:column;')
GRID = 'display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.25rem;margin:1rem 0;'


def build_cards(inner):
    items = LI_RE.findall(inner)
    if not items:
        return None  # not the uniform pattern; skip
    cards = []
    for href, asin, _attrs, name, desc in items:
        emoji = PRODUCTS.get(asin, ("\U0001F517",))[0]
        name = name.strip()
        desc = desc.strip()
        desc_html = f'<p style="color:#6b7280;font-size:0.85rem;margin:0 0 0.9rem;flex-grow:1;">{desc}</p>' if desc else ''
        cards.append(
            f'<div style="{CARD}">'
            f'<div style="font-size:1.8rem;margin-bottom:0.4rem;">{emoji}</div>'
            f'<h4 style="color:#1f2937;margin:0 0 0.4rem;font-size:1rem;">{name}</h4>'
            f'{desc_html}'
            f'<a href="{href}" target="_blank" rel="nofollow sponsored noopener" style="{BTN}">Check Price →</a>'
            f'</div>')
    return f'<div style="{GRID}">' + ''.join(cards) + '</div>'


def main():
    files = [f for f in glob.glob("**/*.html", recursive=True) if "node_modules" not in f]
    pages = 0
    grids = 0
    for f in files:
        try:
            html = open(f, encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        if 'list-style: none; padding: 0;' not in html or 'amazon.com/dp/' not in html:
            continue
        changed = False

        def repl(m):
            nonlocal changed
            cards = build_cards(m.group(1))
            if cards is None:
                return m.group(0)
            changed = True
            return cards

        new = UL_RE.sub(repl, html)
        if changed and new != html:
            grids += new.count(GRID[:30]) if False else 0
            pages += 1
            if APPLY:
                open(f, "w", encoding="utf-8").write(new)
    print(f"{'APPLIED' if APPLY else 'DRY RUN'}: upgraded product lists -> card grids on {pages} pages")


if __name__ == "__main__":
    main()
