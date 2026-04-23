#!/usr/bin/env python3
"""
Fix footer placement across all HTML files.

Bug: <!-- Affiliate Products Section -->, INLINE_CTA_CONFIG script, and
inline-cta.js loader are placed AFTER </footer>, causing them to render
below the footer. They should render BEFORE the footer.

Fix: cut those blocks and re-insert them immediately before <footer>.

Usage:
  python3 fix_footer_placement.py            # apply fix to all affected files
  python3 fix_footer_placement.py --dry-run  # list affected files, don't edit
  python3 fix_footer_placement.py --verbose  # show skip reasons
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

AFFILIATE_PATTERN = re.compile(
    r'\n?<!-- Affiliate Products Section -->.*?<!-- End Affiliate Products Section -->\n?',
    re.DOTALL,
)

CTA_CONFIG_PATTERN = re.compile(
    r'\n?<script>window\.INLINE_CTA_CONFIG\s*=.*?</script>\n?',
    re.DOTALL,
)

CTA_LOADER_PATTERN = re.compile(
    r'\n?<script src="/assets/js/inline-cta\.js"></script>\n?'
)

FOOTER_PATTERN = re.compile(r'(\s*)(<footer\b[^>]*>)')


def fix_file(path: Path):
    content = path.read_text(encoding='utf-8')
    original = content

    affiliate_match = AFFILIATE_PATTERN.search(content)
    if not affiliate_match:
        return False, 'no affiliate block'

    footer_match = FOOTER_PATTERN.search(content)
    if not footer_match:
        return False, 'no <footer> tag'

    if affiliate_match.start() < footer_match.start():
        return False, 'already before footer'

    cta_config_match = CTA_CONFIG_PATTERN.search(content, pos=footer_match.end())
    cta_loader_match = CTA_LOADER_PATTERN.search(content, pos=footer_match.end())

    affiliate_block = affiliate_match.group(0).strip('\n')
    cta_config_block = cta_config_match.group(0).strip('\n') if cta_config_match else ''
    cta_loader_block = cta_loader_match.group(0).strip('\n') if cta_loader_match else ''

    content = AFFILIATE_PATTERN.sub('\n', content, count=1)
    if cta_config_match:
        content = CTA_CONFIG_PATTERN.sub('\n', content, count=1)
    if cta_loader_match:
        content = CTA_LOADER_PATTERN.sub('\n', content, count=1)

    footer_match = FOOTER_PATTERN.search(content)
    if not footer_match:
        return False, 'footer disappeared after cut'

    parts = [affiliate_block]
    if cta_config_block:
        parts.append(cta_config_block)
    if cta_loader_block:
        parts.append(cta_loader_block)
    insertion = '\n\n' + '\n\n'.join(parts) + '\n\n'

    insert_pos = footer_match.start(2)
    content = content[:insert_pos] + insertion + content[insert_pos:]

    if content == original:
        return False, 'no change'

    path.write_text(content, encoding='utf-8')
    return True, 'fixed'


def main():
    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv

    exclude_dirs = {'node_modules', '.git'}

    html_files = []
    for p in ROOT.rglob('*.html'):
        if any(part in exclude_dirs for part in p.parts):
            continue
        if '.backup' in p.name:
            continue
        html_files.append(p)

    affected = []
    for path in html_files:
        try:
            if '<!-- Affiliate Products Section -->' in path.read_text(encoding='utf-8'):
                affected.append(path)
        except Exception:
            continue

    print(f'Found {len(affected)} files with affiliate section')

    if dry_run:
        for p in affected[:10]:
            print(f'  {p.relative_to(ROOT)}')
        if len(affected) > 10:
            print(f'  ... and {len(affected) - 10} more')
        return

    fixed = 0
    skipped = 0
    errors = 0
    skip_reasons = {}
    for path in affected:
        try:
            changed, reason = fix_file(path)
            if changed:
                fixed += 1
            else:
                skipped += 1
                skip_reasons[reason] = skip_reasons.get(reason, 0) + 1
                if verbose:
                    print(f'  SKIP {path.relative_to(ROOT)}: {reason}')
        except Exception as e:
            errors += 1
            print(f'  ERROR {path.relative_to(ROOT)}: {e}')

    print(f'\nFixed:    {fixed}')
    print(f'Skipped:  {skipped}')
    if skip_reasons:
        for reason, count in skip_reasons.items():
            print(f'            - {reason}: {count}')
    print(f'Errors:   {errors}')


if __name__ == '__main__':
    main()
