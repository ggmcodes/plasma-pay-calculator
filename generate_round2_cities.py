#!/usr/bin/env python3
"""Generate Round 2 City Pages: 25 English + 7 Spanish city pages (32 total)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related
from generate_batch5_spanish_template import make_es_page, make_faq as make_faq_es, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')
ES_BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'es', 'blog')

# ============ 25 ENGLISH CITY PAGES ============
en_cities = [
    ('plasma-donation-syracuse-ny-2026', 'Syracuse', 'NY', 'New York', 'Central New York'),
    ('plasma-donation-fort-wayne-in-2026', 'Fort Wayne', 'IN', 'Indiana', 'Northeast Indiana'),
    ('plasma-donation-fort-collins-co-2026', 'Fort Collins', 'CO', 'Colorado', 'Northern Colorado'),
    ('plasma-donation-nampa-id-2026', 'Nampa', 'ID', 'Idaho', 'Treasure Valley'),
    ('plasma-donation-clarksville-tn-2026', 'Clarksville', 'TN', 'Tennessee', 'North-Central Tennessee near Fort Campbell'),
    ('plasma-donation-little-rock-ar-2026', 'Little Rock', 'AR', 'Arkansas', 'Central Arkansas'),
    ('plasma-donation-savannah-ga-2026', 'Savannah', 'GA', 'Georgia', 'Coastal Georgia'),
    ('plasma-donation-durham-nc-2026', 'Durham', 'NC', 'North Carolina', 'Research Triangle area'),
    ('plasma-donation-broken-arrow-ok-2026', 'Broken Arrow', 'OK', 'Oklahoma', 'Tulsa metro area'),
    ('plasma-donation-billings-mt-2026', 'Billings', 'MT', 'Montana', 'South-Central Montana'),
    ('plasma-donation-amarillo-tx-2026', 'Amarillo', 'TX', 'Texas', 'Texas Panhandle'),
    ('plasma-donation-eugene-or-2026', 'Eugene', 'OR', 'Oregon', 'Willamette Valley'),
    ('plasma-donation-salem-or-2026', 'Salem', 'OR', 'Oregon', 'Mid-Willamette Valley'),
    ('plasma-donation-provo-ut-2026', 'Provo', 'UT', 'Utah', 'Utah Valley'),
    ('plasma-donation-greensboro-nc-2026', 'Greensboro', 'NC', 'North Carolina', 'Piedmont Triad'),
    ('plasma-donation-rapid-city-sd-2026', 'Rapid City', 'SD', 'South Dakota', 'Western South Dakota near the Black Hills'),
    ('plasma-donation-rock-hill-sc-2026', 'Rock Hill', 'SC', 'South Carolina', 'York County, near Charlotte NC'),
    ('plasma-donation-north-little-rock-ar-2026', 'North Little Rock', 'AR', 'Arkansas', 'Central Arkansas metro'),
    ('plasma-donation-las-cruces-nm-2026', 'Las Cruces', 'NM', 'New Mexico', 'Southern New Mexico'),
    ('plasma-donation-charlottesville-va-2026', 'Charlottesville', 'VA', 'Virginia', 'Central Virginia'),
    ('plasma-donation-columbus-ga-2026', 'Columbus', 'GA', 'Georgia', 'West-Central Georgia near Fort Moore'),
    ('plasma-donation-fargo-nd-2026', 'Fargo', 'ND', 'North Dakota', 'Red River Valley (ND/MN border)'),
    ('plasma-donation-auburn-al-2026', 'Auburn', 'AL', 'Alabama', 'East Alabama'),
    ('plasma-donation-biloxi-ms-2026', 'Biloxi', 'MS', 'Mississippi', 'Mississippi Gulf Coast'),
    ('plasma-donation-bozeman-mt-2026', 'Bozeman', 'MT', 'Montana', 'Gallatin Valley'),
]

# ============ 7 SPANISH CITY PAGES ============
es_cities = [
    ('cuanto-pagan-donar-plasma-denver-2026', 'Denver', 'Colorado', 'el area metropolitana de Denver'),
    ('cuanto-pagan-donar-plasma-orlando-2026', 'Orlando', 'Florida', 'el centro de Florida'),
    ('cuanto-pagan-donar-plasma-austin-2026', 'Austin', 'Texas', 'el centro de Texas'),
    ('cuanto-pagan-donar-plasma-san-jose-2026', 'San Jose', 'California', 'el area de la Bahia de San Francisco'),
    ('cuanto-pagan-donar-plasma-tucson-2026', 'Tucson', 'Arizona', 'el sur de Arizona'),
    ('cuanto-pagan-donar-plasma-el-paso-2026', 'El Paso', 'Texas', 'la frontera de Texas con Mexico'),
    ('cuanto-pagan-donar-plasma-sacramento-2026', 'Sacramento', 'California', 'el norte de California'),
]


def gen_en_city(slug, city, state_abbr, state_full, region):
    title = f"Plasma Donation {city}, {state_abbr} 2026: Best Centers & Pay Rates"
    meta = f"Find the best plasma donation centers in {city}, {state_abbr}. Compare pay rates, new donor bonuses up to $1,200, center locations, and hours in the {region} for 2026."
    category = f"{city} {state_abbr} 2026"

    toc = [
        ('quick-answer', 'Quick Answer'),
        ('overview', f'{city} Overview'),
        ('centers', 'Centers Near You'),
        ('pay-rates', 'Pay Rates'),
        ('new-donor', 'New Donor Bonuses'),
        ('tips', 'Local Tips'),
        ('faq', 'FAQ'),
    ]

    content = f'''
<div class="highlight-box" id="quick-answer"><h3>Quick Answer</h3><p>Plasma donors in <strong>{city}, {state_abbr}</strong> can earn <strong>$50-$100 per donation</strong> at local plasma centers, with new donor bonuses of <strong>$700-$1,200</strong> in the first month. Donating twice weekly yields $400-$1,000/month. Major chains in the {region} include CSL Plasma, BioLife, Octapharma, and Grifols — check below for which centers serve {city}.</p></div>

<h2 id="overview">Plasma Donation in {city}, {state_abbr}</h2>
<p>{city} is located in the {region} and offers several options for plasma donation. Whether you\'re a first-time donor looking to earn extra income or a regular donor seeking the best pay rates, this guide covers everything you need to know about donating plasma in {city} and surrounding areas.</p>

<h3>Key Facts for {city} Donors</h3>
<ul>
<li><strong>Average pay:</strong> $50-$100 per donation depending on center, weight, and promotions</li>
<li><strong>New donor bonuses:</strong> $700-$1,200 at most centers for first-month donors</li>
<li><strong>Donation frequency:</strong> Up to 2 times per week (48 hours between visits)</li>
<li><strong>Monthly potential:</strong> $400-$1,000 with consistent twice-weekly visits</li>
<li><strong>First visit:</strong> Allow 2-3 hours for screening and first donation</li>
</ul>

<h2 id="centers">Plasma Centers Near {city}, {state_abbr}</h2>
<p>Here are the major plasma center chains that serve the {city} area. Availability varies — use our <a href="/centers/" style="color: #0d9488; font-weight: 500;">Center Finder</a> to check exact locations near you.</p>

<table><thead><tr><th>Center</th><th>Pay Per Visit</th><th>New Donor Bonus</th><th>Monthly Potential</th></tr></thead><tbody>
<tr><td><a href="/blog/csl-plasma-pay-rates-2026.html">CSL Plasma</a></td><td>$50-$100</td><td>$700-$1,200</td><td>$400-$1,000</td></tr>
<tr><td><a href="/blog/biolife-plasma-pay-rates-2026.html">BioLife</a></td><td>$60-$100</td><td>$900-$1,100</td><td>$400-$900</td></tr>
<tr><td><a href="/blog/octapharma-plasma-pay-rates-2026.html">Octapharma</a></td><td>$50-$85</td><td>$800-$1,000</td><td>$450-$900</td></tr>
<tr><td><a href="/blog/grifols-plasma-pay-rates-2026.html">Grifols/Biomat</a></td><td>$50-$75</td><td>$700-$1,100</td><td>$400-$900</td></tr>
</tbody></table>

<p><strong>Note:</strong> Not all chains have locations in every city. Use the links above or our <a href="/centers/">Center Finder</a> to verify which centers are currently operating in {city}, {state_abbr}.</p>

{AFFILIATE_BLOCK}

<h2 id="pay-rates">Pay Rates in {city} 2026</h2>
<p>Plasma pay rates in {city} follow national pricing from each chain, with some local variation based on market competition and demand.</p>

<h3>Pay by Weight Category</h3>
<table><thead><tr><th>Weight</th><th>Volume</th><th>Per Visit</th><th>Monthly (8 visits)</th></tr></thead><tbody>
<tr><td>110-149 lbs</td><td>690 mL</td><td>$40-$65</td><td>$320-$520</td></tr>
<tr><td>150-174 lbs</td><td>825 mL</td><td>$50-$80</td><td>$400-$640</td></tr>
<tr><td>175-400 lbs</td><td>880 mL</td><td>$60-$100</td><td>$480-$800</td></tr>
</tbody></table>

<h3>Maximizing Pay in {city}</h3>
<ul>
<li><strong>Compare centers:</strong> Visit each center\'s website or call to check current promotions</li>
<li><strong>New donor shop:</strong> Start at whichever center has the highest new donor bonus right now</li>
<li><strong>Watch for local promotions:</strong> Centers in competitive markets often run extra bonuses</li>
<li><strong>Ask about referral bonuses:</strong> Earn $50-$100 per friend you refer</li>
</ul>

{PRO_TOOLKIT}

<h2 id="new-donor">New Donor Bonuses in {city}</h2>
<p>First-time donors in {city} can earn significantly more during their first month:</p>
<ul>
<li><strong>CSL Plasma:</strong> $700-$1,200 over 6-8 first-month donations</li>
<li><strong>BioLife:</strong> $900-$1,100 with app coupons applied</li>
<li><strong>Octapharma:</strong> $800-$1,000 through graduated bonuses</li>
<li><strong>Grifols:</strong> $700-$1,100 depending on location</li>
</ul>

<h3>What to Bring to Your First Donation</h3>
<ol>
<li>Valid government-issued photo ID (driver\'s license or state ID)</li>
<li>Proof of Social Security number (SSN card, tax form, or W-2)</li>
<li>Proof of current address (utility bill, lease, or bank statement within 30 days)</li>
<li>Water bottle for hydration</li>
</ol>

<h2 id="tips">Local Tips for {city} Donors</h2>
<ul>
<li><strong>Best times:</strong> Visit Tuesday-Thursday between 10am-2pm for shortest waits</li>
<li><strong>Preparation:</strong> Drink 64+ oz of water the day before donating</li>
<li><strong>Food:</strong> Eat a protein-rich meal 2-3 hours before your appointment</li>
<li><strong>Clothing:</strong> Wear short sleeves or a shirt that pushes up easily above the elbow</li>
<li><strong>Entertainment:</strong> Bring your phone, tablet, or book — donations take 45-90 minutes</li>
<li><strong>Nearby centers:</strong> If {city} centers have long waits, check surrounding communities in the {region}</li>
</ul>

{related_reading([
    ('/blog/which-plasma-center-pays-most-money.html', 'Which Center Pays the Most Money?'),
    ('/blog/ultimate-first-time-plasma-donor-guide-2026.html', 'First-Time Donor Guide'),
    ('/calculators/', 'Plasma Pay Calculator'),
    ('/blog/best-times-donate-plasma-2026.html', 'Best Times to Donate Plasma'),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Where can I donate plasma in {city}, {state_abbr}?</h3>
<p>Plasma donation centers in the {city} area may include CSL Plasma, BioLife, Octapharma, and Grifols locations. Use our <a href="/centers/">Center Finder</a> to see which chains currently operate in {city} and compare their pay rates.</p>

<h3>How much does plasma donation pay in {city}?</h3>
<p>Plasma donation in {city} pays $50-$100 per visit for repeat donors and $700-$1,200 for new donors in their first month. Monthly earnings range from $400-$1,000 with twice-weekly donations. Pay varies by center, weight, and current promotions.</p>

<h3>What do I need to donate plasma in {city}?</h3>
<p>You need a valid photo ID, proof of Social Security number, proof of local address, and to be 18-69 years old weighing at least 110 lbs. Your first visit takes 2-3 hours including a medical screening.</p>

<h3>Which plasma center pays the most in {city}?</h3>
<p>Pay rates vary by location and current promotions. Generally, CSL Plasma and BioLife offer the highest rates ($50-$100/visit). Check current promotions at each center in {city} — new donor bonuses can make a significant difference in your first month.</p>

{footer_related()}'''

    faqs = [
        make_faq(f"Where can I donate plasma in {city}, {state_abbr}?", f"Centers in the {city} area may include CSL Plasma, BioLife, Octapharma, and Grifols. Use our Center Finder to check current locations."),
        make_faq(f"How much does plasma donation pay in {city}?", f"$50-$100 per visit for repeat donors, $700-$1,200 for new donors in the first month. Monthly potential: $400-$1,000."),
        make_faq(f"What do I need to donate plasma in {city}?", "Valid photo ID, SSN proof, proof of address, age 18-69, weight 110+ lbs."),
        make_faq(f"Which plasma center pays the most in {city}?", "Pay varies by location and promotions. CSL Plasma and BioLife generally offer the highest rates at $50-$100/visit."),
    ]

    return make_en_page(slug, title, meta, category, 8, toc, content, faqs)


def gen_es_city(slug, city, state, region):
    title = f"Donar Plasma en {city} 2026: Cuanto Pagan y Mejores Centros"
    meta = f"Centros de donacion de plasma en {city}, {state}. Pagan $50-$100 por visita, bonos de nuevo donante hasta $1,200. Encuentra los mejores centros y tarifas actuales."
    toc = [('respuesta','Respuesta Rapida'),('centros','Centros Cercanos'),('tarifas','Tarifas'),('bonos','Bonos'),('consejos','Consejos'),('faq','Preguntas Frecuentes')]

    content = f'''
<div class="highlight-box" id="respuesta"><h3>Respuesta Rapida</h3><p>Los centros de plasma en <strong>{city}, {state}</strong> pagan <strong>$50-$100 por donacion</strong>. Los nuevos donantes pueden ganar <strong>$700-$1,200</strong> en su primer mes. Donando dos veces por semana, puedes ganar $400-$1,000 al mes. Los centros principales en {region} incluyen CSL Plasma, BioLife, Octapharma y Grifols.</p></div>

<h2 id="centros">Centros de Plasma Cerca de {city}</h2>
<p>Estos son los principales centros de plasma que sirven el area de {city}. Disponibilidad varia — usa nuestro <a href="/centers/">buscador de centros</a> para verificar ubicaciones exactas.</p>

<table><thead><tr><th>Centro</th><th>Pago por Visita</th><th>Bono Nuevo Donante</th><th>Potencial Mensual</th></tr></thead><tbody>
<tr><td><a href="/es/blog/csl-plasma-cuanto-pagan-tarifas-2026.html">CSL Plasma</a></td><td>$50-$100</td><td>$700-$1,200</td><td>$400-$1,000</td></tr>
<tr><td><a href="/es/blog/biolife-plasma-cuanto-pagan-tarifas-2026.html">BioLife</a></td><td>$60-$100</td><td>$900-$1,100</td><td>$400-$900</td></tr>
<tr><td><a href="/blog/octapharma-plasma-pay-rates-2026.html">Octapharma</a></td><td>$50-$85</td><td>$800-$1,000</td><td>$450-$900</td></tr>
<tr><td><a href="/blog/grifols-plasma-pay-rates-2026.html">Grifols/Biomat</a></td><td>$50-$75</td><td>$700-$1,100</td><td>$400-$900</td></tr>
</tbody></table>

{AFFILIATE_ES}

<h2 id="tarifas">Tarifas en {city} 2026</h2>
<h3>Pago por Peso</h3>
<table><thead><tr><th>Peso</th><th>Volumen</th><th>Por Visita</th><th>Mensual (8 visitas)</th></tr></thead><tbody>
<tr><td>110-149 lbs (50-67 kg)</td><td>690 mL</td><td>$40-$65</td><td>$320-$520</td></tr>
<tr><td>150-174 lbs (68-79 kg)</td><td>825 mL</td><td>$50-$80</td><td>$400-$640</td></tr>
<tr><td>175+ lbs (80+ kg)</td><td>880 mL</td><td>$60-$100</td><td>$480-$800</td></tr>
</tbody></table>

{PRO_TOOLKIT_ES}

<h2 id="bonos">Bonos para Nuevos Donantes en {city}</h2>
<ul>
<li><strong>CSL Plasma:</strong> $700-$1,200 en las primeras 6-8 donaciones</li>
<li><strong>BioLife:</strong> $900-$1,100 con cupones de la aplicacion</li>
<li><strong>Octapharma:</strong> $800-$1,000 con bonos graduales</li>
<li><strong>Grifols:</strong> $700-$1,100 segun ubicacion</li>
</ul>

<h3>Que Necesitas para Tu Primera Donacion</h3>
<ol>
<li>Identificacion con foto vigente (licencia de conducir o ID estatal)</li>
<li>Numero de Seguro Social (tarjeta SSN, W-2, o formulario de impuestos)</li>
<li>Comprobante de domicilio actual (factura de servicios, contrato de renta)</li>
<li>Botella de agua para hidratacion</li>
</ol>

<h2 id="consejos">Consejos para Donantes en {city}</h2>
<ul>
<li><strong>Mejores horarios:</strong> Martes a jueves entre 10am-2pm para esperas mas cortas</li>
<li><strong>Hidratacion:</strong> Toma 64+ oz de agua el dia anterior</li>
<li><strong>Alimentacion:</strong> Come una comida rica en proteina 2-3 horas antes</li>
<li><strong>Ropa:</strong> Usa mangas cortas o camisa que se pueda subir facilmente</li>
<li><strong>Entretenimiento:</strong> Lleva tu telefono o libro — la donacion dura 45-90 minutos</li>
</ul>

{related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar Plasma 2026'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guia Completa de Donacion'),
    ('/es/blog/', 'Blog en Espanol'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Cuanto pagan por donar plasma en {city}?</h3>
<p>Los centros de plasma en {city} pagan $50-$100 por visita para donantes regulares. Los nuevos donantes pueden ganar $700-$1,200 en su primer mes. Con donaciones dos veces por semana, puedes ganar $400-$1,000 mensualmente.</p>

<h3>¿Donde puedo donar plasma en {city}?</h3>
<p>Busca centros de CSL Plasma, BioLife, Octapharma o Grifols en {region}. Usa nuestro <a href="/centers/">buscador de centros</a> para encontrar ubicaciones exactas cerca de ti.</p>

<h3>¿Que necesito para donar plasma por primera vez?</h3>
<p>Necesitas una identificacion con foto, numero de Seguro Social, comprobante de domicilio, tener 18-69 anos de edad y pesar al menos 110 libras (50 kg). Tu primera visita dura 2-3 horas incluyendo examen medico.</p>

<div class="related-articles">
<h3>Guias Relacionadas</h3>
<div class="related-grid">
<a href="/es/blog/guia-completa-donacion-plasma.html" class="related-link">Guia Completa</a>
<a href="/es/blog/requisitos-donacion-plasma.html" class="related-link">Requisitos</a>
<a href="/es/blog/cuanto-pagan-por-donar-plasma-2026.html" class="related-link">Cuanto Pagan 2026</a>
<a href="/es/" class="related-link">Calculadora</a>
</div>
</div>'''

    faqs = [
        make_faq_es(f"¿Cuanto pagan por donar plasma en {city}?", f"$50-$100 por visita para donantes regulares, $700-$1,200 para nuevos donantes en el primer mes."),
        make_faq_es(f"¿Donde puedo donar plasma en {city}?", f"Busca centros de CSL Plasma, BioLife, Octapharma o Grifols en {region}."),
    ]
    return make_es_page(slug, title, meta, f"{city} 2026", 8, toc, content, faqs)


if __name__ == '__main__':
    print("Generating Round 2 City Pages...")

    # English cities
    en_count = 0
    for slug, city, state_abbr, state_full, region in en_cities:
        html = gen_en_city(slug, city, state_abbr, state_full, region)
        path = os.path.join(BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: blog/{slug}.html")
        en_count += 1

    # Spanish cities
    es_count = 0
    for slug, city, state, region in es_cities:
        html = gen_es_city(slug, city, state, region)
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        es_count += 1

    print(f"\nDone! Generated {en_count} English + {es_count} Spanish = {en_count + es_count} city pages.")
