#!/usr/bin/env python3
import os
import glob

# Spanish footer HTML
footer_html = '''
<!-- Footer -->
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
</footer>
'''

def add_footer_to_file(filepath):
    """Add footer to a single HTML file if it doesn't have one."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if footer already exists
        if '<footer>' in content or '<footer' in content:
            return False, "Footer already exists"
        
        # Find the closing body tag
        if '</body>' not in content:
            return False, "No closing body tag found"
        
        # Insert footer before closing body tag
        new_content = content.replace('</body>', footer_html + '\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Footer added successfully"
    
    except Exception as e:
        return False, str(e)

def main():
    # Find all HTML files in es directory
    es_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator/es'
    html_files = glob.glob(os.path.join(es_dir, '**/*.html'), recursive=True)
    
    print(f"Found {len(html_files)} HTML files in Spanish directory")
    
    added = 0
    skipped = 0
    errors = 0
    
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, es_dir)
        success, message = add_footer_to_file(filepath)
        
        if success:
            added += 1
            print(f"✓ Added footer to: {rel_path}")
        elif "already exists" in message:
            skipped += 1
            # print(f"- Skipped (has footer): {rel_path}")
        else:
            errors += 1
            print(f"✗ Error with {rel_path}: {message}")
    
    print(f"\n=== Summary ===")
    print(f"Total files: {len(html_files)}")
    print(f"Footers added: {added}")
    print(f"Skipped (already had footer): {skipped}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    main()