#!/usr/bin/env python3
"""Wire the new gap pages into the internal-link graph and strengthen linking on
top money pages. Injects a 'Related Plasma Guides' block immediately before the
<footer> on a curated set of high-traffic pages. Idempotent via a marker.

Run: python3 tools/wire_internal_links.py [--apply]
"""
import sys, re

APPLY = "--apply" in sys.argv
MARKER = "<!-- RELATED_GUIDES_2026_06 -->"

NEW = {
    "paysign": ("/blog/paysign-plasma-card-guide-2026", "PaySign Plasma Card: Balance, Fees &amp; Cash Out"),
    "proscons": ("/blog/pros-and-cons-of-donating-plasma-2026", "Pros and Cons of Donating Plasma"),
    "green": ("/blog/why-is-my-plasma-green-color-guide-2026", "Why Is My Plasma Green? Color Guide"),
    "universal": ("/blog/universal-plasma-donor-blood-type-guide-2026", "Universal Plasma Donor: Best Blood Type"),
}
MONEY = {
    "calc": ("/", "Plasma Pay Calculator"),
    "centers": ("/centers/", "Find Plasma Centers Near You"),
    "which": ("/blog/which-plasma-center-pays-most-money", "Which Plasma Center Pays the Most?"),
    "biolife": ("/blog/biolife-plasma-pay-chart-2026", "BioLife Plasma Pay Chart 2026"),
    "grifols": ("/blog/grifols-plasma-pay-chart-2026", "Grifols Plasma Pay Chart 2026"),
    "cslrates": ("/blog/csl-plasma-pay-rates-2026", "CSL Plasma Pay Rates 2026"),
    "cslweight": ("/blog/csl-plasma-weight-chart-2026", "CSL Plasma Weight Chart 2026"),
    "kedplasma": ("/blog/kedplasma-pay-chart-2026", "KEDPLASMA Pay Chart 2026"),
}

# curated high-traffic targets -> the 6 most contextually-relevant links to add
TARGETS = {
    "blog/biolife-plasma-pay-chart-2026.html": ["paysign", "proscons", "universal", "which", "grifols", "cslrates"],
    "blog/grifols-plasma-pay-chart-2026.html": ["paysign", "proscons", "universal", "which", "biolife", "cslrates"],
    "blog/csl-plasma-pay-rates-2026.html": ["paysign", "proscons", "green", "which", "cslweight", "biolife"],
    "blog/csl-plasma-weight-chart-2026.html": ["universal", "green", "paysign", "which", "cslrates", "biolife"],
    "blog/kedplasma-pay-chart-2026.html": ["paysign", "proscons", "universal", "which", "biolife", "grifols"],
    "blog/which-plasma-center-pays-most-money.html": ["paysign", "proscons", "universal", "biolife", "grifols", "cslrates"],
    "blog/octapharma-plasma-pay-chart-2026.html": ["paysign", "proscons", "universal", "which", "biolife", "grifols"],
    "plasma-donation-pay-chart-by-state.html": ["which", "paysign", "proscons", "biolife", "grifols", "cslrates"],
    "blog/grifols-plasma-bonus-promotions-2026.html": ["paysign", "proscons", "which", "grifols", "biolife", "cslrates"],
    "blog/biolife-busy-times-best-hours-2026.html": ["proscons", "green", "paysign", "biolife", "which", "cslrates"],
    "blog/csl-biolife-octapharma-comparison-guide.html": ["which", "paysign", "universal", "biolife", "grifols", "cslrates"],
    "blog/does-donating-plasma-hurt-pain-guide-2026.html": ["proscons", "green", "universal", "which", "biolife", "calc"],
    "blog/what-disqualifies-you-from-donating-plasma-2026.html": ["proscons", "universal", "green", "paysign", "which", "calc"],
    "blog/how-often-can-you-donate-plasma-2026.html": ["proscons", "paysign", "which", "biolife", "cslrates", "calc"],
    "blog/plasma-donation-what-to-eat-before-2026.html": ["green", "proscons", "universal", "which", "biolife", "calc"],
}

ALL = {**NEW, **MONEY}


def block(keys, root_rel):
    # root_rel: prefix for "/" links if page is at root vs blog (both use absolute "/...", so fine)
    items = "".join(f'<li><a href="{ALL[k][0]}">{ALL[k][1]}</a></li>' for k in keys)
    return (MARKER +
            '<section style="margin:2.5rem 0;padding:1.5rem;background:#f8fafc;border-radius:12px;'
            'border:1px solid #e5e7eb;"><h3 style="margin-top:0;">Related Plasma Guides</h3>'
            f'<ul style="line-height:1.9;">{items}</ul></section>')


def main():
    changed = 0
    for path, keys in TARGETS.items():
        try:
            html = open(path, encoding="utf-8", errors="ignore").read()
        except FileNotFoundError:
            print(f"SKIP (missing): {path}")
            continue
        if MARKER in html:
            print(f"SKIP (already wired): {path}")
            continue
        # filter out links that already appear prominently to avoid pure dupes is optional;
        # we keep all 6 since a curated related block is standard practice.
        m = re.search(r'<footer\b', html)
        if not m:
            print(f"SKIP (no footer): {path}")
            continue
        inject = block(keys, "")
        new = html[:m.start()] + inject + "\n" + html[m.start():]
        if APPLY:
            open(path, "w", encoding="utf-8").write(new)
        changed += 1
        print(f"{'WIRED' if APPLY else 'WOULD WIRE'}: {path}  (+{len(keys)} links)")
    print(f"\n{'Applied' if APPLY else 'Dry run'}: {changed} pages")


if __name__ == "__main__":
    main()
