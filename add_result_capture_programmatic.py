#!/usr/bin/env python3
"""Extend result-moment email capture to programmatic calculator pages.

Companion to add_result_capture.py (main calculator pages, commit 63b612bde).
Covers three page shapes:
  1. ES state calculators (es/calculators/<state>/index.html) and the EN
     bay-area page: hidden <div id="results"> revealed by
     classList.remove('hidden') -> insert block after the #results close.
  2. EN state calculators (calculators/<state>/index.html): always-visible
     results panel updated in place by calculateEarnings() -> insert block
     after the calculator grid close; js/result-capture.js reveals it on
     the calculate-button click.
  3. Everything else (city pages, ES content pages): no calculator ->
     skipped.
Adds data-utm-content=<page-slug> so Beehiiv acquisition data shows which
state/city calculators convert.
"""
import glob
import re
import sys

ROOT = '/Users/glengomezmeade/Projects/plasma-pay-calculator'

EN = {
    'headline': 'Get paid more for your plasma.',
    'sub': 'Weekly list of the highest-paying centers and bonuses by email.',
    'placeholder': 'you@email.com',
    'button': 'Send me the list',
    'fine': 'Free. No spam. Unsubscribe anytime.',
    'success': 'Check the new tab to confirm. You will get one weekly email with the highest-paying donation and side hustle offers.',
}
ES = {
    'headline': 'Gana más por tu plasma.',
    'sub': 'Lista semanal de los centros que mejor pagan y los bonos, por email.',
    'placeholder': 'tu@email.com',
    'button': 'Enviarme la lista',
    'fine': 'Gratis. Sin spam. Cancela cuando quieras.',
    'success': 'Revisa la nueva pestaña para confirmar. Recibirás un email semanal con las ofertas de donación y trabajos extra que mejor pagan.',
}

BLOCK = '''
            <!-- Result-moment email capture -->
            <div id="result-capture" data-source="{source}" data-utm-content="{utm_content}" hidden style="background:#ffffff;border:2px solid #0d9488;border-radius:12px;padding:24px 20px;margin:24px auto;max-width:560px;text-align:center;font-family:system-ui,sans-serif;">
                <div class="rc-lead">
                    <p style="color:#111827;font-weight:800;font-size:1.2rem;margin:0 0 6px;">{headline}</p>
                    <p style="color:#6b7280;font-size:0.95rem;margin:0 0 14px;line-height:1.5;">{sub}</p>
                    <form style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0;">
                        <input type="text" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">
                        <input type="email" name="email" required placeholder="{placeholder}" style="flex:1 1 220px;max-width:300px;padding:10px 12px;border:1px solid #d1d5db;border-radius:8px;font-size:1rem;">
                        <button type="submit" style="background:#0d9488;color:#ffffff;border:none;border-radius:8px;padding:10px 18px;font-weight:700;font-size:1rem;cursor:pointer;">{button}</button>
                    </form>
                    <p style="color:#9ca3af;font-size:0.8rem;margin:10px 0 0;">{fine}</p>
                </div>
                <p class="rc-success" hidden style="color:#0d9488;font-weight:600;font-size:1rem;margin:0;line-height:1.5;">{success}</p>
            </div>
            <script src="/js/result-capture.js"></script>
'''

GRID_ANCHOR = '<div class="grid lg:grid-cols-2 gap-8">'
RESULTS_COMMENT = '<!-- Results -->'


def balanced_div_close(html, open_pos):
    """Return index just past the </div> closing the <div at open_pos."""
    depth = 0
    for tok in re.finditer(r'<div\b|</div\s*>', html[open_pos:]):
        if tok.group().startswith('<div'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return open_pos + tok.end()
    return None


def find_results_close(html):
    m = re.search(r'<div\s+id="results"', html)
    if m is None:
        return None
    return balanced_div_close(html, m.start())


def find_grid_close(html):
    """Close of the calculator grid holding the <!-- Results --> panel."""
    cpos = html.find(RESULTS_COMMENT)
    if cpos == -1:
        return None
    gpos = html.rfind(GRID_ANCHOR, 0, cpos)
    if gpos == -1:
        return None
    return balanced_div_close(html, gpos)


def page_slug(rel):
    slug = rel
    for prefix in ('es/calculators/', 'calculators/'):
        if slug.startswith(prefix):
            slug = slug[len(prefix):]
            break
    slug = slug.removesuffix('/index.html').removesuffix('.html')
    slug = slug.replace('/', '-')
    if rel.startswith('es/'):
        slug = 'es-' + slug
    return slug


def main():
    pages = sorted(
        glob.glob(f'{ROOT}/calculators/**/*.html', recursive=True)
        + glob.glob(f'{ROOT}/es/calculators/**/*.html', recursive=True)
    )
    modified, skipped_done, skipped_nocalc = [], [], []

    for path in pages:
        rel = path[len(ROOT) + 1:]
        with open(path, encoding='utf-8') as f:
            html = f.read()

        if 'result-capture' in html:
            skipped_done.append(rel)
            continue

        has_calc = 'onclick="calculateEarnings()' in html
        has_results = re.search(r'<div\s+id="results"', html) is not None

        if has_calc and has_results:
            end = find_results_close(html)
            mode = 'after #results'
        elif has_calc:
            end = find_grid_close(html)
            mode = 'after calc grid'
        else:
            skipped_nocalc.append(rel)
            continue

        if end is None:
            print(f'ERROR: could not locate insertion point in {rel}')
            sys.exit(1)

        slug = page_slug(rel)
        copy = ES if rel.startswith('es/') else EN
        block = BLOCK.format(
            source=f'plasmapaycalculator.com ({slug}-calculator result)',
            utm_content=slug,
            **copy,
        )
        assert '—' not in block and '–' not in block, 'em/en dash found'

        new_html = html[:end] + block + html[end:]

        # Validate: exactly one block, placed after the container close.
        assert new_html.count('id="result-capture"') == 1, rel
        assert new_html.index('id="result-capture"') > end - 10, rel
        bpos = new_html.index('<!-- Result-moment email capture -->')
        assert bpos >= end, f'{rel}: block not after container close'

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        modified.append((rel, mode, slug))
        print(f'OK ({mode}): {rel} [utm_content={slug}]')

    print()
    print(f'MODIFIED: {len(modified)}')
    print(f'SKIPPED (already has block): {len(skipped_done)}')
    for rel in skipped_done:
        print(f'  - {rel}')
    print(f'SKIPPED (no calculator/results container): {len(skipped_nocalc)}')


if __name__ == '__main__':
    main()
