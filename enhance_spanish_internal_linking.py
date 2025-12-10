#!/usr/bin/env python3
"""
Phase 1: Enhance Spanish internal linking for better SEO and user experience.
- Add cross-links between related blog posts
- Add calculator links to blog posts
- Add blog links to calculator footers
- Add deep links to FAQ
"""

import re
from pathlib import Path
import sys

# Blog post relationship mapping
BLOG_CROSS_LINKS = {
    'cuanto-pagan-por-donar-plasma.html': [
        ('¿Cuánto Dinero Puedes Ganar Donando Plasma?', '/es/blog/cuanto-dinero-puedes-ganar-donando-plasma.html'),
        ('Bonos y Promociones de Donación de Plasma', '/es/blog/bonos-promociones-donacion-plasma.html'),
        ('¿Qué Centro de Plasma Paga Más Dinero?', '/es/blog/cual-centro-plasma-paga-mas-dinero.html'),
    ],
    'cuanto-dinero-puedes-ganar-donando-plasma.html': [
        ('¿Cuánto Pagan Por Donar Plasma en 2025?', '/es/blog/cuanto-pagan-por-donar-plasma.html'),
        ('¿Puedes Ganar $1000 al Mes Donando Plasma?', '/es/blog/ganar-1000-donando-plasma.html'),
        ('Mejores Horarios para Donar Plasma', '/es/blog/mejores-horarios-donar-plasma.html'),
    ],
    'ganar-1000-donando-plasma.html': [
        ('Bonos y Promociones de Donación de Plasma', '/es/blog/bonos-promociones-donacion-plasma.html'),
        ('Mejores Horarios para Donar Plasma', '/es/blog/mejores-horarios-donar-plasma.html'),
        ('Guía Completa de Donación de Plasma', '/es/blog/guia-completa-donacion-plasma.html'),
    ],
    'requisitos-donacion-plasma.html': [
        ('Guía Completa de Donación de Plasma', '/es/blog/guia-completa-donacion-plasma.html'),
        ('Consejos para Principiantes', '/es/blog/consejos-donacion-plasma-principiantes.html'),
        ('¿Cuánto Pagan Por Donar Plasma?', '/es/blog/cuanto-pagan-por-donar-plasma.html'),
    ],
    'consejos-donacion-plasma-principiantes.html': [
        ('Requisitos para Donación de Plasma', '/es/blog/requisitos-donacion-plasma.html'),
        ('Guía Completa de Donación de Plasma', '/es/blog/guia-completa-donacion-plasma.html'),
        ('¿Cuánto Pagan Por Donar Plasma?', '/es/blog/cuanto-pagan-por-donar-plasma.html'),
    ],
    'guia-completa-donacion-plasma.html': [
        ('Requisitos para Donación de Plasma', '/es/blog/requisitos-donacion-plasma.html'),
        ('Consejos para Principiantes', '/es/blog/consejos-donacion-plasma-principiantes.html'),
        ('Bonos y Promociones', '/es/blog/bonos-promociones-donacion-plasma.html'),
    ],
    'cual-centro-plasma-paga-mas-dinero.html': [
        ('BioLife vs CSL Plasma: Comparación', '/es/blog/biolife-vs-csl-plasma-comparacion.html'),
        ('Los Mejores Centros de Plasma en California', '/es/blog/mejores-centros-plasma-california.html'),
        ('¿Cuánto Pagan Por Donar Plasma?', '/es/blog/cuanto-pagan-por-donar-plasma.html'),
    ],
    'mejores-centros-plasma-california.html': [
        ('¿Qué Centro de Plasma Paga Más?', '/es/blog/cual-centro-plasma-paga-mas-dinero.html'),
        ('BioLife vs CSL Plasma', '/es/blog/biolife-vs-csl-plasma-comparacion.html'),
        ('Calculadora de California', '/es/calculators/california/'),
    ],
    'biolife-vs-csl-plasma-comparacion.html': [
        ('¿Qué Centro Paga Más Dinero?', '/es/blog/cual-centro-plasma-paga-mas-dinero.html'),
        ('Bonos y Promociones', '/es/blog/bonos-promociones-donacion-plasma.html'),
        ('Los Mejores Centros en California', '/es/blog/mejores-centros-plasma-california.html'),
    ],
    'mejores-horarios-donar-plasma.html': [
        ('Bonos y Promociones de Donación', '/es/blog/bonos-promociones-donacion-plasma.html'),
        ('¿Cuánto Dinero Puedes Ganar?', '/es/blog/cuanto-dinero-puedes-ganar-donando-plasma.html'),
        ('Guía Completa de Donación de Plasma', '/es/blog/guia-completa-donacion-plasma.html'),
    ],
    'bonos-promociones-donacion-plasma.html': [
        ('¿Cuánto Pagan Por Donar Plasma?', '/es/blog/cuanto-pagan-por-donar-plasma.html'),
        ('¿Puedes Ganar $1000 al Mes?', '/es/blog/ganar-1000-donando-plasma.html'),
        ('¿Qué Centro Paga Más?', '/es/blog/cual-centro-plasma-paga-mas-dinero.html'),
    ],
}

# Calculator links to add to specific blog posts
BLOG_TO_CALCULATOR_LINKS = {
    'cuanto-dinero-puedes-ganar-donando-plasma.html': [
        ('California', '/es/calculators/california/'),
        ('Nueva York', '/es/calculators/new-york/'),
        ('Texas', '/es/calculators/texas/'),
        ('Florida', '/es/calculators/florida/'),
    ],
    'ganar-1000-donando-plasma.html': [
        ('Los Ángeles', '/es/calculators/california/los-angeles/'),
        ('Manhattan, Nueva York', '/es/calculators/new-york/manhattan/'),
        ('Houston', '/es/calculators/texas/houston/'),
        ('Miami', '/es/calculators/florida/miami/'),
    ],
    'mejores-centros-plasma-california.html': [
        ('Los Ángeles', '/es/calculators/california/los-angeles/'),
        ('San Francisco', '/es/calculators/california/san-francisco/'),
        ('San Diego', '/es/calculators/california/san-diego/'),
        ('Sacramento', '/es/calculators/california/sacramento/'),
    ],
}

def add_related_posts_section(content, blog_filename):
    """Add related posts section to a blog post"""

    if blog_filename not in BLOG_CROSS_LINKS:
        return content, False

    # Check if already has related posts section
    if 'Artículos Relacionados' in content or 'artículos relacionados' in content.lower():
        return content, False

    related_links = BLOG_CROSS_LINKS[blog_filename]

    # Build related posts HTML
    related_html = '''
        <!-- Related Posts Section -->
        <section class="py-12 bg-gray-50">
            <div class="max-w-4xl mx-auto px-4">
                <h2 class="text-2xl font-bold text-gray-900 mb-6">📚 Artículos Relacionados</h2>
                <div class="grid md:grid-cols-3 gap-4">
'''

    for title, url in related_links:
        related_html += f'''                    <a href="{url}" class="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200">
                        <h3 class="font-semibold text-gray-900 mb-2">{title}</h3>
                        <span class="text-green-600 text-sm font-medium">Leer más →</span>
                    </a>
'''

    related_html += '''                </div>
            </div>
        </section>
'''

    # Insert before footer
    footer_match = re.search(r'<footer', content)
    if footer_match:
        insert_pos = footer_match.start()
        new_content = content[:insert_pos] + related_html + '\n' + content[insert_pos:]
        return new_content, True

    return content, False

def add_calculator_links_to_blog(content, blog_filename):
    """Add calculator links within blog post content"""

    if blog_filename not in BLOG_TO_CALCULATOR_LINKS:
        return content, False

    calculator_links = BLOG_TO_CALCULATOR_LINKS[blog_filename]

    # Build calculator links HTML
    calc_html = f'''
        <div class="bg-green-50 border-l-4 border-green-500 p-6 my-8">
            <h3 class="font-bold text-gray-900 mb-3">🧮 Calcula Tus Ganancias:</h3>
            <div class="grid md:grid-cols-2 gap-3">
'''

    for location, url in calculator_links:
        calc_html += f'''                <a href="{url}" class="bg-white px-4 py-2 rounded-lg font-semibold text-green-600 hover:bg-green-100 transition-colors block text-center">
                    Calculadora de {location}
                </a>
'''

    calc_html += '''            </div>
        </div>
'''

    # Insert after first major section (after first </p> following an <h2>)
    h2_pattern = r'(<h2[^>]*>.*?</h2>.*?</p>)'
    match = re.search(h2_pattern, content, re.DOTALL)

    if match:
        insert_pos = match.end()
        new_content = content[:insert_pos] + calc_html + content[insert_pos:]
        return new_content, True

    return content, False

def add_blog_links_to_calculator_footer(content, state_or_city):
    """Add blog post links to calculator page footer"""

    # Check if already has blog links section
    if 'Guías Útiles' in content or 'Artículos del Blog' in content:
        return content, False  # Already has it

    # Default blog links for any calculator
    blog_links = [
        ('Cuánto Pagan en 2025', '/es/blog/cuanto-pagan-por-donar-plasma.html'),
        ('Bonos y Promociones', '/es/blog/bonos-promociones-donacion-plasma.html'),
        ('Consejos para Principiantes', '/es/blog/consejos-donacion-plasma-principiantes.html'),
    ]

    # Add state-specific links
    if 'california' in state_or_city.lower():
        blog_links.insert(1, ('Mejores Centros en California', '/es/blog/mejores-centros-plasma-california.html'))

    # Build blog links HTML
    blog_html = '''
        <!-- Blog Links Section -->
        <section class="py-12 bg-gray-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <h2 class="text-2xl font-bold text-center text-gray-900 mb-8">
                    📚 Artículos Útiles del Blog
                </h2>
                <div class="grid md:grid-cols-3 gap-4 max-w-4xl mx-auto">
'''

    for title, url in blog_links:
        blog_html += f'''                    <a href="{url}" class="bg-white p-5 rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200">
                        <h3 class="font-semibold text-gray-900 mb-2">{title}</h3>
                        <span class="text-green-600 text-sm font-medium">Leer más →</span>
                    </a>
'''

    blog_html += '''                </div>
            </div>
        </section>
'''

    # Insert before footer
    footer_match = re.search(r'<footer', content)
    if footer_match:
        insert_pos = footer_match.start()
        new_content = content[:insert_pos] + blog_html + '\n' + content[insert_pos:]
        return new_content, True

    return content, False

def process_blog_post(file_path, dry_run=False):
    """Process a single blog post"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        blog_filename = file_path.name
        modified = False

        # Add related posts section
        new_content, related_added = add_related_posts_section(content, blog_filename)
        if related_added:
            content = new_content
            modified = True

        # Add calculator links
        new_content, calc_added = add_calculator_links_to_blog(content, blog_filename)
        if calc_added:
            content = new_content
            modified = True

        if modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

        return modified, None

    except Exception as e:
        return False, str(e)

def process_calculator_page(file_path, dry_run=False):
    """Process a single calculator page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract state/city from path
        path_str = str(file_path)

        # Add blog links to footer
        new_content, modified = add_blog_links_to_calculator_footer(content, path_str)

        if modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return modified, None

    except Exception as e:
        return False, str(e)

def main():
    """Main function"""
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    print("=== ENHANCING SPANISH INTERNAL LINKING (PHASE 1) ===\n")

    # Process blog posts
    print("Processing Spanish blog posts...\n")
    blog_path = Path('es/blog')
    blog_files = [f for f in blog_path.glob('*.html') if f.name != 'index.html']

    blog_updated = 0
    blog_skipped = 0

    for blog_file in blog_files:
        modified, error = process_blog_post(blog_file, dry_run)
        if error:
            print(f"❌ Error: {blog_file.name}: {error}")
        elif modified:
            blog_updated += 1
            status = "Would update" if dry_run else "✓ Updated"
            print(f"{status}: {blog_file.name}")
        else:
            blog_skipped += 1

    # Process calculator pages (sample - major states and cities)
    print("\nProcessing Spanish calculator pages...\n")

    calculator_files = []
    # State pages
    for state_dir in Path('es/calculators').iterdir():
        if state_dir.is_dir():
            index_file = state_dir / 'index.html'
            if index_file.exists():
                calculator_files.append(index_file)

            # Major cities only (to avoid processing 300+ files)
            major_cities = ['los-angeles', 'san-francisco', 'manhattan', 'brooklyn',
                          'houston', 'miami', 'chicago', 'phoenix']
            for city_dir in state_dir.iterdir():
                if city_dir.is_dir() and city_dir.name in major_cities:
                    city_index = city_dir / 'index.html'
                    if city_index.exists():
                        calculator_files.append(city_index)

    calc_updated = 0
    calc_skipped = 0

    for calc_file in calculator_files:
        modified, error = process_calculator_page(calc_file, dry_run)
        if error:
            print(f"❌ Error: {calc_file}: {error}")
        elif modified:
            calc_updated += 1
            status = "Would update" if dry_run else "✓ Updated"
            print(f"{status}: {calc_file}")
        else:
            calc_skipped += 1

    print(f"\n=== COMPLETE ===")
    print(f"Blog posts updated: {blog_updated}")
    print(f"Blog posts skipped: {blog_skipped}")
    print(f"Calculator pages updated: {calc_updated}")
    print(f"Calculator pages skipped: {calc_skipped}")

    if not dry_run and (blog_updated > 0 or calc_updated > 0):
        print(f"\n✅ Enhanced Spanish internal linking!")
        print(f"   - Added related posts sections to {blog_updated} blog posts")
        print(f"   - Added calculator links to blog posts")
        print(f"   - Added blog links to {calc_updated} calculator pages")

    return 0

if __name__ == '__main__':
    sys.exit(main())
