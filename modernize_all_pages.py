#!/usr/bin/env python3
"""
Comprehensive Site Modernization Script
Removes old inline styles, applies new theme consistently across all pages
"""

import os
import re
from pathlib import Path

# Configuration
BASE_DIR = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator')
SKIP_DIRS = {'node_modules', '.git', 'includes'}
SKIP_FILES = {'new-homepage-design.html', 'home.html'}

# Files that are already modernized or should be skipped
ALREADY_MODERN = set()

# Stats
stats = {
    'processed': 0,
    'modified': 0,
    'errors': 0,
    'skipped': 0
}

def get_depth_prefix(file_path):
    """Calculate relative path prefix for CSS/includes"""
    rel_path = file_path.relative_to(BASE_DIR)
    depth = len(rel_path.parts) - 1
    if depth == 0:
        return ''
    return '../' * depth

def is_spanish_page(file_path):
    """Check if file is in Spanish section"""
    return '/es/' in str(file_path)

def remove_inline_styles(html):
    """Remove all inline <style> blocks"""
    # Remove style tags and their contents (including multiline)
    pattern = r'<style[^>]*>[\s\S]*?</style>'
    cleaned = re.sub(pattern, '', html, flags=re.IGNORECASE)
    return cleaned

def remove_tailwind_cdn(html):
    """Remove Tailwind CDN script and config"""
    # Remove tailwind script tag
    html = re.sub(r'<script[^>]*src="[^"]*tailwindcss[^"]*"[^>]*></script>', '', html)
    # Remove tailwind config block
    html = re.sub(r'<script>\s*tailwind\.config\s*=\s*\{[\s\S]*?\}\s*</script>', '', html)
    return html

def ensure_fonts_and_theme(html, depth_prefix):
    """Ensure Google Fonts and theme.css are in head"""

    # Check if already has our theme
    if 'Plasma Pay Rebrand 2025' in html:
        # Already has rebrand, but may need style cleanup
        return html

    # Font and CSS injection
    injection = f'''
<!-- Plasma Pay Rebrand 2025 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth_prefix}css/theme.css">
'''

    # Insert before </head>
    if '</head>' in html:
        html = html.replace('</head>', injection + '</head>')

    return html

def get_nav_html(is_spanish=False, depth_prefix=''):
    """Get navigation HTML"""
    if is_spanish:
        return f'''<!-- Navigation -->
<nav class="nav" id="mainNav">
    <div class="nav-inner">
        <a href="{depth_prefix}index.html" class="logo">
            <span class="logo-mark">$</span>
            Plasma Pay
        </a>
        <ul class="nav-links">
            <li><a href="{depth_prefix}index.html">Calculadora</a></li>
            <li><a href="{depth_prefix}centers/">Encontrar Centros</a></li>
            <li><a href="{depth_prefix}blog/">Blog</a></li>
            <li><a href="{depth_prefix}faq.html">Preguntas</a></li>
            <li><a href="{depth_prefix}centers/" class="nav-cta">Centros Cerca de Mi</a></li>
        </ul>
        <button class="mobile-toggle" onclick="toggleMobileMenu()" aria-label="Toggle menu">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 12h18M3 6h18M3 18h18"/>
            </svg>
        </button>
    </div>
</nav>

<script>
// Nav scroll effect
window.addEventListener('scroll', () => {{
    const nav = document.getElementById('mainNav');
    if (window.scrollY > 50) {{
        nav.classList.add('scrolled');
    }} else {{
        nav.classList.remove('scrolled');
    }}
}});

// Mobile menu toggle
function toggleMobileMenu() {{
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}}
</script>
'''
    else:
        return f'''<!-- Navigation -->
<nav class="nav" id="mainNav">
    <div class="nav-inner">
        <a href="{depth_prefix}/" class="logo">
            <span class="logo-mark">$</span>
            Plasma Pay
        </a>
        <ul class="nav-links">
            <li><a href="{depth_prefix}/">Calculator</a></li>
            <li><a href="{depth_prefix}centers/">Find Centers</a></li>
            <li><a href="{depth_prefix}blog/">Blog</a></li>
            <li><a href="{depth_prefix}faq.html">FAQ</a></li>
            <li><a href="{depth_prefix}centers/" class="nav-cta">Find Centers Near Me</a></li>
        </ul>
        <button class="mobile-toggle" onclick="toggleMobileMenu()" aria-label="Toggle menu">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 12h18M3 6h18M3 18h18"/>
            </svg>
        </button>
    </div>
</nav>

<script>
// Nav scroll effect
window.addEventListener('scroll', () => {{
    const nav = document.getElementById('mainNav');
    if (window.scrollY > 50) {{
        nav.classList.add('scrolled');
    }} else {{
        nav.classList.remove('scrolled');
    }}
}});

// Mobile menu toggle
function toggleMobileMenu() {{
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}}
</script>
'''

def get_footer_html(is_spanish=False, depth_prefix=''):
    """Get footer HTML"""
    if is_spanish:
        return f'''<!-- Footer -->
<footer class="footer">
    <div class="footer-grid">
        <div class="footer-brand">
            <a href="{depth_prefix}index.html" class="logo">
                <span class="logo-mark">$</span>
                Plasma Pay
            </a>
            <p>Ayudando a miles de donantes a maximizar sus ganancias por donacion de plasma desde 2023.</p>
        </div>

        <div class="footer-section">
            <h4>Calculadoras</h4>
            <ul>
                <li><a href="{depth_prefix}index.html">Calculadora de Plasma</a></li>
                <li><a href="{depth_prefix}cuanto-pagan-por-donar-plasma-2025.html">Cuanto Pagan 2025</a></li>
            </ul>
        </div>

        <div class="footer-section">
            <h4>Recursos</h4>
            <ul>
                <li><a href="{depth_prefix}centers/">Encontrar Centros</a></li>
                <li><a href="{depth_prefix}blog/">Blog</a></li>
                <li><a href="{depth_prefix}faq.html">Preguntas Frecuentes</a></li>
            </ul>
        </div>

        <div class="footer-section">
            <h4>Compania</h4>
            <ul>
                <li><a href="{depth_prefix}about.html">Acerca de</a></li>
                <li><a href="{depth_prefix}contact.html">Contacto</a></li>
                <li><a href="{depth_prefix}privacy.html">Privacidad</a></li>
                <li><a href="{depth_prefix}terms.html">Terminos</a></li>
            </ul>
        </div>
    </div>

    <div class="advertise-banner">
        <p>Eres un centro de plasma buscando alcanzar nuevos donantes? Anunciate con nosotros!</p>
        <a href="{depth_prefix}advertise.html">Mas Informacion</a>
    </div>

    <div class="footer-bottom">
        <p>&copy; 2024 PlasmaPayCalculator.com. Todos los derechos reservados.</p>
        <div class="footer-legal">
            <a href="{depth_prefix}privacy.html">Privacidad</a>
            <a href="{depth_prefix}terms.html">Terminos</a>
        </div>
    </div>
</footer>
'''
    else:
        return f'''<!-- Footer -->
<footer class="footer">
    <div class="footer-grid">
        <div class="footer-brand">
            <a href="{depth_prefix}/" class="logo">
                <span class="logo-mark">$</span>
                Plasma Pay
            </a>
            <p>Helping thousands of donors maximize their plasma donation earnings since 2023. Find the best-paying centers, calculate your earnings, and start earning today.</p>
        </div>

        <div class="footer-section">
            <h4>Calculators</h4>
            <ul>
                <li><a href="{depth_prefix}/">Plasma Pay Calculator</a></li>
                <li><a href="{depth_prefix}biolife-plasma-pay-chart.html">BioLife Pay Chart</a></li>
                <li><a href="{depth_prefix}csl-plasma-pay-chart.html">CSL Pay Chart</a></li>
                <li><a href="{depth_prefix}grifols-biomat-pay-chart.html">Grifols Pay Chart</a></li>
                <li><a href="{depth_prefix}octapharma-plasma-pay-chart.html">Octapharma Pay Chart</a></li>
            </ul>
        </div>

        <div class="footer-section">
            <h4>Resources</h4>
            <ul>
                <li><a href="{depth_prefix}centers/">Find Centers</a></li>
                <li><a href="{depth_prefix}blog/">Blog</a></li>
                <li><a href="{depth_prefix}faq.html">FAQ</a></li>
                <li><a href="{depth_prefix}plasma-donation-requirements.html">Requirements</a></li>
                <li><a href="{depth_prefix}first-time-donor-guide.html">First Time Guide</a></li>
            </ul>
        </div>

        <div class="footer-section">
            <h4>Company</h4>
            <ul>
                <li><a href="{depth_prefix}about.html">About Us</a></li>
                <li><a href="{depth_prefix}contact.html">Contact</a></li>
                <li><a href="{depth_prefix}advertise.html">Advertise</a></li>
                <li><a href="{depth_prefix}privacy.html">Privacy Policy</a></li>
                <li><a href="{depth_prefix}terms.html">Terms of Service</a></li>
            </ul>
        </div>
    </div>

    <div class="advertise-banner">
        <p>Are you a plasma center looking to reach new donors? Advertise with us!</p>
        <a href="{depth_prefix}advertise.html">Learn More</a>
    </div>

    <div class="footer-bottom">
        <p>&copy; 2024 PlasmaPayCalculator.com. All rights reserved. Not affiliated with any plasma donation center.</p>
        <div class="footer-legal">
            <a href="{depth_prefix}privacy.html">Privacy</a>
            <a href="{depth_prefix}terms.html">Terms</a>
            <a href="{depth_prefix}disclaimer.html">Disclaimer</a>
        </div>
    </div>
</footer>
'''

def update_nav_and_footer(html, is_spanish, depth_prefix):
    """Replace old nav and footer with new ones"""

    new_nav = get_nav_html(is_spanish, depth_prefix)
    new_footer = get_footer_html(is_spanish, depth_prefix)

    # Replace nav - match various nav patterns
    nav_patterns = [
        r'<!-- Navigation -->[\s\S]*?</script>\s*(?=<!-- Navigation|<main|<section|<div class="hero|<header)',
        r'<nav[^>]*class="nav[^"]*"[^>]*>[\s\S]*?</nav>\s*<script>[\s\S]*?</script>',
        r'<nav[^>]*>[\s\S]*?</nav>',
    ]

    nav_replaced = False
    for pattern in nav_patterns:
        if re.search(pattern, html):
            html = re.sub(pattern, new_nav, html, count=1)
            nav_replaced = True
            break

    if not nav_replaced:
        # Insert after <body>
        if '<body' in html:
            html = re.sub(r'(<body[^>]*>)', r'\1\n' + new_nav, html)

    # Replace footer
    footer_pattern = r'<footer[^>]*>[\s\S]*?</footer>'
    if re.search(footer_pattern, html):
        html = re.sub(footer_pattern, new_footer, html)
    else:
        # Insert before </body>
        if '</body>' in html:
            html = html.replace('</body>', new_footer + '\n</body>')

    return html

def add_body_class(html):
    """Add plasma-rebrand class to body"""
    if 'class="plasma-rebrand"' in html:
        return html

    # Add class to existing body tag
    html = re.sub(r'<body([^>]*)>', r'<body\1 class="plasma-rebrand">', html)
    # Fix double class attributes
    html = re.sub(r'class="([^"]*)" class="plasma-rebrand"', r'class="\1 plasma-rebrand"', html)

    return html

def clean_duplicate_elements(html):
    """Remove duplicate nav/footer elements"""
    # Count navs and keep only the new one
    nav_count = html.count('<nav class="nav"')
    if nav_count > 1:
        # Keep only the first new nav
        parts = html.split('<nav class="nav"')
        if len(parts) > 2:
            html = parts[0] + '<nav class="nav"' + parts[1]
            for i in range(2, len(parts)):
                # Remove extra navs but keep content after
                remaining = re.sub(r'^[^>]*>[\s\S]*?</nav>\s*<script>[\s\S]*?</script>', '', parts[i])
                html += remaining

    return html

def update_theme_color(html):
    """Update meta theme-color to new teal"""
    html = re.sub(r'<meta name="theme-color" content="#[0-9a-fA-F]+">',
                  '<meta name="theme-color" content="#0D4F4F">', html)
    return html

def fix_inline_color_styles(html):
    """Replace old green colors with new theme colors in inline styles"""
    # Replace old green with teal in any remaining inline styles
    html = html.replace('#27ae60', 'var(--deep-teal)')
    html = html.replace('#2ecc71', 'var(--teal-light)')
    html = html.replace('#e74c3c', 'var(--gold)')
    html = html.replace('#c0392b', 'var(--gold)')
    html = html.replace('rgb(39, 174, 96)', 'var(--deep-teal)')
    html = html.replace('rgba(39, 174, 96', 'rgba(13, 79, 79')
    return html

def modernize_page(file_path):
    """Main function to modernize a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_html = f.read()

        html = original_html
        depth_prefix = get_depth_prefix(file_path)
        is_spanish = is_spanish_page(file_path)

        # Step 1: Remove all inline styles
        html = remove_inline_styles(html)

        # Step 2: Remove Tailwind CDN
        html = remove_tailwind_cdn(html)

        # Step 3: Ensure fonts and theme CSS are included
        html = ensure_fonts_and_theme(html, depth_prefix)

        # Step 4: Update nav and footer
        html = update_nav_and_footer(html, is_spanish, depth_prefix)

        # Step 5: Add body class
        html = add_body_class(html)

        # Step 6: Update theme color meta
        html = update_theme_color(html)

        # Step 7: Fix any inline color references
        html = fix_inline_color_styles(html)

        # Step 8: Clean up duplicate elements
        html = clean_duplicate_elements(html)

        # Step 9: Clean up extra whitespace
        html = re.sub(r'\n{3,}', '\n\n', html)

        # Check if anything changed
        if html != original_html:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            stats['modified'] += 1
            return True
        else:
            stats['skipped'] += 1
            return False

    except Exception as e:
        print(f"  ERROR: {file_path.name}: {e}")
        stats['errors'] += 1
        return False

def process_directory(directory, pattern='**/*.html'):
    """Process all HTML files in directory"""
    dir_path = BASE_DIR / directory if directory else BASE_DIR
    files = list(dir_path.glob(pattern))

    print(f"\nProcessing {len(files)} files in {directory or 'root'}...")

    for file_path in files:
        # Skip directories and special files
        if any(skip in str(file_path) for skip in SKIP_DIRS):
            continue
        if file_path.name in SKIP_FILES:
            continue
        if file_path.name in ALREADY_MODERN:
            continue

        stats['processed'] += 1
        result = modernize_page(file_path)
        if result:
            print(f"  Updated: {file_path.relative_to(BASE_DIR)}")

def main():
    print("=" * 60)
    print("COMPREHENSIVE SITE MODERNIZATION")
    print("=" * 60)

    # Process different sections
    sections = [
        ('', '*.html'),           # Root pages
        ('calculators', '**/*.html'),  # Calculator pages
        ('es', '**/*.html'),      # Spanish pages
    ]

    for directory, pattern in sections:
        process_directory(directory, pattern)

    print("\n" + "=" * 60)
    print("MODERNIZATION COMPLETE")
    print("=" * 60)
    print(f"Total processed: {stats['processed']}")
    print(f"Files modified:  {stats['modified']}")
    print(f"Files skipped:   {stats['skipped']}")
    print(f"Errors:          {stats['errors']}")
    print("=" * 60)

if __name__ == '__main__':
    main()
