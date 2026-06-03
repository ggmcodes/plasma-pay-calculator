#!/usr/bin/env python3
"""Replace dead Amazon /s?k= search links with real /dp/ASIN product links.

Tier 1 (this script): in-place URL swap. Every search link whose query maps to a
real donor product (see affiliate_catalog) becomes a direct product link that
sets the affiliate cookie and is creditable. Anchor text is preserved. Off-topic
queries (tax/finance/etc.) are left untouched.

Usage:
  python3 tools/fix_affiliate_links.py            # dry run, report only
  python3 tools/fix_affiliate_links.py --apply    # write changes
"""
import re, sys, glob, collections
sys.path.insert(0, "tools")
from affiliate_catalog import map_query_to_asin, TAG

APPLY = "--apply" in sys.argv

# matches href="https://www.amazon.com/s?k=QUERY&tag=..."  or without &tag
LINK_RE = re.compile(r'https://www\.amazon\.com/s\?k=([^"&\']+)(?:&[^"\']*)?')

files = sorted(glob.glob("**/*.html", recursive=True))
files = [f for f in files if "node_modules" not in f]

swapped = collections.Counter()
left = collections.Counter()
pages_changed = 0
total_swaps = 0

for f in files:
    try:
        html = open(f, encoding="utf-8", errors="ignore").read()
    except Exception:
        continue
    if "amazon.com/s?k=" not in html:
        continue
    orig = html

    def repl(m):
        global total_swaps
        query = m.group(1)
        hit = map_query_to_asin(query)
        if not hit:
            left[query] += 1
            return m.group(0)
        asin, name, emoji, desc = hit
        swapped[asin] += 1
        total_swaps += 1
        return f"https://www.amazon.com/dp/{asin}?tag={TAG}"

    html = LINK_RE.sub(repl, html)
    if html != orig:
        pages_changed += 1
        if APPLY:
            open(f, "w", encoding="utf-8").write(html)

print(f"{'APPLIED' if APPLY else 'DRY RUN'}")
print(f"Pages changed: {pages_changed}")
print(f"Total links swapped to real /dp/: {total_swaps}")
print(f"\nSwaps by product ASIN:")
from affiliate_catalog import PRODUCTS
for a, c in swapped.most_common():
    print(f"  {c:5}  {a}  {PRODUCTS[a][1]}")
print(f"\nLeft as search link (no confident product), top 25 distinct queries:")
for q, c in left.most_common(25):
    print(f"  {c:5}  {q}")
print(f"\nDistinct unmapped queries: {len(left)} | total unmapped links: {sum(left.values())}")
