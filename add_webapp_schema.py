#!/usr/bin/env python3
"""Add a WebApplication JSON-LD block to calculators/**/*.html pages.

Rules:
- Skip pages that already declare WebApplication or SoftwareApplication in JSON-LD.
- Do NOT modify existing JSON-LD blocks; add one new <script> before </head>.
- name = page h1 text (fallback: <title>), url = canonical href.
- Assert the inserted block json.loads() cleanly.
"""
import glob
import html as htmlmod
import json
import re
import sys

ROOT = '/Users/glengomezmeade/Projects/plasma-pay-calculator'

JSONLD_RE = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE)
CANON_RE = re.compile(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']|'
                      r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']',
                      re.IGNORECASE)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.DOTALL | re.IGNORECASE)
TITLE_RE = re.compile(r'<title\b[^>]*>(.*?)</title>', re.DOTALL | re.IGNORECASE)
TAG_RE = re.compile(r'<[^>]+>')


def declares_webapp(page_html):
    for m in JSONLD_RE.finditer(page_html):
        body = m.group(1)
        if '"WebApplication"' in body or '"SoftwareApplication"' in body:
            return True
    return False


def clean_text(raw):
    text = TAG_RE.sub(' ', raw)
    text = htmlmod.unescape(text)
    # strip emoji/symbols that shouldn't lead a schema name, collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def main():
    files = sorted(glob.glob(f'{ROOT}/calculators/**/*.html', recursive=True))
    modified, skipped_existing, errors = [], [], []

    for path in files:
        with open(path, encoding='utf-8') as f:
            page = f.read()

        if declares_webapp(page):
            skipped_existing.append(path)
            continue

        cm = CANON_RE.search(page)
        canonical = (cm.group(1) or cm.group(2)) if cm else None
        if not canonical:
            errors.append((path, 'no canonical'))
            continue

        name = None
        hm = H1_RE.search(page)
        if hm:
            name = clean_text(hm.group(1))
        if not name:
            tm = TITLE_RE.search(page)
            if tm:
                name = clean_text(tm.group(1))
        if not name:
            errors.append((path, 'no h1/title'))
            continue

        obj = {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": name,
            "url": canonical,
            "applicationCategory": "FinanceApplication",
            "operatingSystem": "Web",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        }
        payload = json.dumps(obj, ensure_ascii=False, indent=2)
        # Validate the exact inserted payload parses.
        parsed = json.loads(payload)
        assert parsed["@type"] == "WebApplication"

        block = f'    <script type="application/ld+json">\n{payload}\n    </script>\n'

        idx = page.lower().rfind('</head>')
        if idx == -1:
            errors.append((path, 'no </head>'))
            continue

        new_page = page[:idx] + block + page[idx:]

        # Re-validate: the new block must parse when re-extracted from the page.
        found = False
        for m in JSONLD_RE.finditer(new_page):
            body = m.group(1)
            if '"WebApplication"' in body:
                json.loads(body)
                found = True
        assert found, path

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_page)
        modified.append(path)

    print(f'total files: {len(files)}')
    print(f'modified: {len(modified)}')
    print(f'skipped (already WebApplication/SoftwareApplication): {len(skipped_existing)}')
    for p in skipped_existing:
        print(f'  skip: {p}')
    if errors:
        print(f'ERRORS: {len(errors)}')
        for p, why in errors:
            print(f'  {p}: {why}')
        sys.exit(1)


if __name__ == '__main__':
    main()
