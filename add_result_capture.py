#!/usr/bin/env python3
"""Insert result-moment email capture block after the #results div."""
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
    'headline': 'Gana mas por tu plasma.',
    'sub': 'Lista semanal de los centros que mejor pagan y los bonos, por email.',
    'placeholder': 'tu@email.com',
    'button': 'Enviarme la lista',
    'fine': 'Gratis. Sin spam. Cancela cuando quieras.',
    'success': 'Revisa la nueva pestana para confirmar. Recibiras un email semanal con las ofertas de donacion y trabajos extra que mejor pagan.',
}
# Proper accented Spanish (files are UTF-8)
ES = {
    'headline': 'Gana más por tu plasma.',
    'sub': 'Lista semanal de los centros que mejor pagan y los bonos, por email.',
    'placeholder': 'tu@email.com',
    'button': 'Enviarme la lista',
    'fine': 'Gratis. Sin spam. Cancela cuando quieras.',
    'success': 'Revisa la nueva pestaña para confirmar. Recibirás un email semanal con las ofertas de donación y trabajos extra que mejor pagan.',
}

PAGES = [
    ('index.html', 'plasmapaycalculator.com (homepage result)', EN),
    ('es/index.html', 'plasmapaycalculator.com (es-homepage result)', ES),
    ('calculators/index.html', 'plasmapaycalculator.com (calculators-index result)', EN),
    ('calculators/california/index.html', 'plasmapaycalculator.com (california-calculator result)', EN),
]

BLOCK = '''
            <!-- Result-moment email capture -->
            <div id="result-capture" data-source="{source}" hidden style="background:#ffffff;border:2px solid #0d9488;border-radius:12px;padding:24px 20px;margin:24px auto;max-width:560px;text-align:center;font-family:system-ui,sans-serif;">
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


def find_results_close(html):
    """Return index just past the </div> that closes <div id="results"...>."""
    m = re.search(r'<div\s+id="results"', html)
    if not m:
        return None
    depth = 0
    pos = m.start()
    for tok in re.finditer(r'<div\b|</div\s*>', html[pos:]):
        if tok.group().startswith('<div'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return pos + tok.end()
    return None


def main():
    for rel, source, copy in PAGES:
        path = f'{ROOT}/{rel}'
        with open(path, encoding='utf-8') as f:
            html = f.read()
        if 'result-capture' in html:
            print(f'SKIP (already has block): {rel}')
            continue
        end = find_results_close(html)
        if end is None:
            print(f'ERROR: could not locate #results close in {rel}')
            sys.exit(1)
        block = BLOCK.format(source=source, **copy)
        assert '—' not in block and '–' not in block, 'em/en dash found'
        html = html[:end] + block + html[end:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'OK: {rel}')


if __name__ == '__main__':
    main()
