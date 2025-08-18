#!/usr/bin/env python3
import os
import glob
import re

# Complete Spanish footer HTML
footer_html = '''<!-- Footer -->
<footer>
<div class="footer-content">
<div class="footer-section">
<h4>Calculadora de Pago de Plasma</h4>
<p>Obtén estimaciones precisas de ingresos por donación de plasma con las tarifas actuales de 2025. Ve exactamente cuánto ganarás antes de donar.</p>
</div>
<div class="footer-section">
<h4>Recursos de Ganancias</h4>
<ul>
<li><a href="/es/">Calculadora de Ganancias</a></li>
<li><a href="/es/blog/">Consejos para Maximizar Ingresos</a></li>
<li><a href="/es/faq.html">Preguntas Frecuentes sobre Pagos</a></li>
<li><a href="/es/centers/">Encontrar Centros</a></li>
</ul>
</div>
<div class="footer-section">
<h4>🔥 Calculadoras Virales</h4>
<ul>
<li><a href="/es/blog/calculadora-bono-primera-donacion-plasma.html" style="color: #f39c12; font-weight: 600;">🚨 Calculadora de Bono Primera Vez</a></li>
<li><a href="/es/blog/maximizador-horario-donacion-plasma.html" style="color: #f39c12; font-weight: 600;">📅 Secreto de $8,000+</a></li>
<li><a href="/es/blog/detector-estafas-donacion-plasma.html" style="color: #f39c12; font-weight: 600;">⚠️ Detector de Estafas</a></li>
<li><a href="/es/blog/calculadora-beneficios-salud-donacion-plasma.html" style="color: #f39c12; font-weight: 600;">🔬 Calculadora de Beneficios de Salud</a></li>
</ul>
</div>
<div class="footer-section">
<h4>Legal y Soporte</h4>
<ul>
<li><a href="/es/about.html">Acerca de</a></li>
<li><a href="/es/privacy.html">Política de Privacidad</a></li>
<li><a href="/es/terms.html">Términos de Servicio</a></li>
<li><a href="/es/contact.html">Contacto</a></li>
<li><a href="/es/faq.html">Preguntas Frecuentes</a></li>
<li><a href="/es/states.html">Todos los Estados</a></li>
</ul>
</div>
</div>
<p>© 2025 Calculadora de Pago de Plasma. Estimaciones basadas en tarifas actuales. Las ganancias reales pueden variar. Información con fines educativos.</p>
</footer>'''

def fix_footer_in_file(filepath):
    """Fix or add footer to a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Check if proper footer structure exists
        if re.search(r'<footer>\s*<div class="footer-content">', content):
            return False, "Proper footer already exists"
        
        # Remove any existing malformed footer-like structures
        # Remove </div></footer></main> type issues
        content = re.sub(r'</div>\s*</footer>\s*</main>', '</div>\n</main>', content)
        
        # Remove standalone closing footer tags
        content = re.sub(r'</footer>(?!.*<footer)', '', content)
        
        # Remove any existing incomplete footer
        content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
        
        # Remove any copyright line that might be outside proper footer
        content = re.sub(r'<div class="border-t[^>]*>.*?© 2025.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<p>© 2025 Calculadora de Pago de Plasma.*?</p>(?!</footer>)', '', content, flags=re.DOTALL)
        
        # Find the right place to insert footer
        if '</main>' in content:
            # Insert after main tag
            content = content.replace('</main>', '</main>\n\n' + footer_html)
        elif '</body>' in content:
            # Insert before closing body tag
            content = content.replace('</body>', '\n' + footer_html + '\n</body>')
        else:
            return False, "No suitable insertion point found"
        
        # Clean up any duplicate closing tags
        content = re.sub(r'</body>\s*</body>', '</body>', content)
        content = re.sub(r'</html>\s*</html>', '</html>', content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Footer fixed successfully"
        else:
            return False, "No changes needed"
    
    except Exception as e:
        return False, str(e)

def main():
    # Find all HTML files in es directory
    es_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator/es'
    html_files = glob.glob(os.path.join(es_dir, '**/*.html'), recursive=True)
    
    print(f"Found {len(html_files)} HTML files in Spanish directory")
    
    fixed = 0
    skipped = 0
    errors = 0
    
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, es_dir)
        success, message = fix_footer_in_file(filepath)
        
        if success:
            fixed += 1
            print(f"✓ Fixed footer in: {rel_path}")
        elif "already exists" in message or "No changes" in message:
            skipped += 1
            # Uncomment to see skipped files
            # print(f"- Skipped: {rel_path} ({message})")
        else:
            errors += 1
            print(f"✗ Error with {rel_path}: {message}")
    
    print(f"\n=== Summary ===")
    print(f"Total files: {len(html_files)}")
    print(f"Footers fixed: {fixed}")
    print(f"Skipped (already correct): {skipped}")
    print(f"Errors: {errors}")
    
    # Final verification
    print("\n=== Verification ===")
    proper_footers = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            if '<footer>' in f.read():
                proper_footers += 1
    
    print(f"Files with footer tag: {proper_footers}/{len(html_files)}")

if __name__ == "__main__":
    main()