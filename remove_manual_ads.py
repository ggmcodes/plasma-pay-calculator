#!/usr/bin/env python3
"""Remove manual AdSense ad slots from HTML files.

We use Google Auto Ads only — the <script async src="pagead2..."> tag in
<head> is enough. The manual <ins class="adsbygoogle"> blocks render as
empty grey placeholder rectangles when they fail to fill, which is ugly
and unnecessary. Remove them.

Three wrapper patterns were found across 16 files:
  A. "Ad Break" placeholder in articles
  B. "AdSense Placement" div in tool pages (includes inline push script)
  C. <section class="py-6 bg-gray-100"> wrapper in es/ NY calculators

The async AdSense <script> in <head> and any .push({}) init calls
elsewhere are left alone.

Usage:
  python3 remove_manual_ads.py
  python3 remove_manual_ads.py --dry-run
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

_OPTIONAL_SCRIPT = r'(?:<script>\s*\(adsbygoogle[^<]*?</script>\s*)?'

PATTERN_A = re.compile(
    r'\n?\s*(?:<!--\s*Ad Break\s*-->\s*)?'
    r'<div\s+class="[^"]*\bmy-(?:8|12)\b[^"]*min-h-\[280px\][^"]*"[^>]*>\s*'
    r'<ins\s+class="adsbygoogle"[^>]*>\s*</ins>\s*'
    + _OPTIONAL_SCRIPT +
    r'</div>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)

PATTERN_B = re.compile(
    r'\n?\s*(?:<!--\s*AdSense[^>]*-->\s*)?'
    r'<div\s+style="[^"]*max-width[^"]*"[^>]*>\s*'
    r'<ins\s+class="adsbygoogle"[^>]*></ins>\s*'
    r'<script>\s*\(adsbygoogle\s*=[^<]*?</script>\s*'
    r'</div>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)

PATTERN_C = re.compile(
    r'\n?\s*(?:<!--\s*AdSense[^>]*-->\s*)?'
    r'<section\s+class="py-6\s+bg-(?:gray-100|white)"[^>]*>\s*'
    r'<div\s+class="max-w-4xl[^"]*"[^>]*>\s*'
    r'<ins\s+class="adsbygoogle"[^>]*>\s*</ins>\s*'
    + _OPTIONAL_SCRIPT +
    r'</div>\s*'
    r'</section>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)

PATTERN_D = re.compile(
    r'\n?\s*(?:<!--\s*Ad Space\s*-->\s*)?'
    r'<div\s+class="my-8\s+p-4\s+bg-gray-100[^"]*"[^>]*>\s*'
    r'<ins\s+class="adsbygoogle"[^>]*>\s*</ins>\s*'
    + _OPTIONAL_SCRIPT +
    r'</div>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)

PATTERN_E = re.compile(
    r'\n?\s*(?:<!--\s*Ad Placement\s*-->\s*)?'
    r'<div\s+class="my-8"[^>]*>\s*'
    r'<ins\s+class="adsbygoogle"[^>]*>\s*</ins>\s*'
    + _OPTIONAL_SCRIPT +
    r'</div>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)

PATTERN_F = re.compile(
    r'\n?\s*(?:<!--\s*Ad Container\s*-->\s*)?'
    r'<div\s+class="ad-container"[^>]*>\s*'
    r'(?:<div\s+class="ad-label"[^>]*>[^<]*</div>\s*)?'
    r'<ins\s+class="adsbygoogle"[^>]*>\s*</ins>\s*'
    + _OPTIONAL_SCRIPT +
    r'</div>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)

PATTERN_G = re.compile(
    r'\n?\s*(?:<!--\s*Ad Break\s*-->\s*)?'
    r'<div\s+class="[^"]*\bmin-h-\[280px\][^"]*"[^>]*>\s*'
    r'<span\s+[^>]*>\s*(?:Advertisement|Publicidad|Anuncio)\s*</span>\s*'
    r'</div>\s*\n?',
    re.DOTALL | re.IGNORECASE,
)


def fix_file(path: Path):
    content = path.read_text(encoding='utf-8')
    original = content

    new_content, n_a = PATTERN_A.subn('\n', content)
    new_content, n_b = PATTERN_B.subn('\n', new_content)
    new_content, n_c = PATTERN_C.subn('\n', new_content)
    new_content, n_d = PATTERN_D.subn('\n', new_content)
    new_content, n_e = PATTERN_E.subn('\n', new_content)
    new_content, n_f = PATTERN_F.subn('\n', new_content)
    new_content, n_g = PATTERN_G.subn('\n', new_content)

    remaining = new_content.count('class="adsbygoogle"') + new_content.count('min-h-[280px]')

    if new_content == original:
        return False, 0, remaining

    path.write_text(new_content, encoding='utf-8')
    return True, n_a + n_b + n_c + n_d + n_e + n_f + n_g, remaining


def main():
    dry_run = '--dry-run' in sys.argv

    files = []
    for p in ROOT.rglob('*.html'):
        if 'node_modules' in p.parts or '.git' in p.parts:
            continue
        if '.backup' in p.name:
            continue
        try:
            c = p.read_text(encoding='utf-8')
            if 'class="adsbygoogle"' in c or 'min-h-[280px]' in c:
                files.append(p)
        except Exception:
            continue

    print(f'Found {len(files)} files with <ins class="adsbygoogle">')

    fixed = 0
    total_removed = 0
    still_have = []

    for path in files:
        try:
            if dry_run:
                content = path.read_text(encoding='utf-8')
                n_a = len(PATTERN_A.findall(content))
                n_b = len(PATTERN_B.findall(content))
                n_c = len(PATTERN_C.findall(content))
                n_d = len(PATTERN_D.findall(content))
                n_e = len(PATTERN_E.findall(content))
                n_f = len(PATTERN_F.findall(content))
                n_g = len(PATTERN_G.findall(content))
                would_remove = n_a + n_b + n_c + n_d + n_e + n_f + n_g
                total_in_file = content.count('class="adsbygoogle"')
                if would_remove > 0:
                    fixed += 1
                    total_removed += would_remove
                    print(f'  WOULD REMOVE {would_remove}/{total_in_file} ad block(s) from {path.relative_to(ROOT)}')
                if would_remove < total_in_file:
                    still_have.append(path)
                continue

            changed, removed, remaining = fix_file(path)
            if changed:
                fixed += 1
                total_removed += removed
                print(f'  FIXED {path.relative_to(ROOT)}  (removed {removed}, {remaining} remaining)')
            if remaining > 0:
                still_have.append(path)
        except Exception as e:
            print(f'  ERROR {path.relative_to(ROOT)}: {e}')

    print(f'\nFiles changed: {fixed}')
    print(f'Ad blocks removed: {total_removed}')
    if still_have:
        print(f'\nFiles with remaining <ins class="adsbygoogle"> (patterns not covered):')
        for p in still_have:
            print(f'  {p.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
