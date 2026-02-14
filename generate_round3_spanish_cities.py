#!/usr/bin/env python3
"""Generate Round 3 Spanish blog pages: 15 City pages"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch5_spanish_template import make_es_page, make_faq, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es
ES_BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'es', 'blog')

# ============================================================
# City page definitions
# (slug, city, state, region, en_equivalent, local_details)
# ============================================================

cities = [
    {
        'slug': 'cuanto-pagan-donar-plasma-san-francisco-2026',
        'city': 'San Francisco',
        'state': 'California',
        'region': 'el area de la Bahia de San Francisco',
        'en_equiv': 'plasma-donation-san-francisco-2026.html',
        'centers_note': 'En San Francisco y el area de la Bahia, la mayoria de centros de plasma estan en ciudades circundantes como San Jose, Oakland y Hayward. El alto costo de vida hace que el ingreso por plasma sea especialmente util.',
        'local_tip': 'Considera centros en San Jose o East Bay si no encuentras uno cerca en SF',
        'pay_range': '$55-$100',
        'bonus': '$800-$1,200',
        'monthly': '$450-$1,000',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-seattle-2026',
        'city': 'Seattle',
        'state': 'Washington',
        'region': 'el area metropolitana de Seattle',
        'en_equiv': 'plasma-donation-seattle-2026.html',
        'centers_note': 'Seattle y el area del Puget Sound tienen varios centros de plasma, incluyendo ubicaciones en Tacoma, Renton y Federal Way. El estado de Washington tiene regulaciones favorables para donantes.',
        'local_tip': 'Los centros en suburbios como Renton o Tacoma suelen tener esperas mas cortas',
        'pay_range': '$50-$95',
        'bonus': '$700-$1,100',
        'monthly': '$400-$900',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-portland-2026',
        'city': 'Portland',
        'state': 'Oregon',
        'region': 'el area metropolitana de Portland',
        'en_equiv': 'plasma-donation-portland-or-2026.html',
        'centers_note': 'Portland tiene multiples centros de plasma en el area metro, incluyendo ubicaciones en Beaverton, Gresham y Vancouver (WA). Oregon no tiene impuesto sobre las ventas, lo que maximiza tus ganancias.',
        'local_tip': 'Sin impuesto sobre las ventas en Oregon — tus ganancias de plasma rinden mas',
        'pay_range': '$50-$90',
        'bonus': '$700-$1,100',
        'monthly': '$400-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-tampa-2026',
        'city': 'Tampa',
        'state': 'Florida',
        'region': 'el area de Tampa Bay',
        'en_equiv': 'plasma-donation-tampa-fl-2026.html',
        'centers_note': 'Tampa Bay tiene una concentracion alta de centros de plasma, con ubicaciones en Tampa, St. Petersburg, Brandon y Clearwater. Florida no tiene impuesto estatal sobre la renta, lo que beneficia a los donantes.',
        'local_tip': 'Sin impuesto estatal sobre la renta en Florida — conservas el 100% de tus ganancias',
        'pay_range': '$50-$95',
        'bonus': '$700-$1,200',
        'monthly': '$400-$900',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-detroit-2026',
        'city': 'Detroit',
        'state': 'Michigan',
        'region': 'el area metropolitana de Detroit',
        'en_equiv': 'plasma-donation-detroit-mi-2026.html',
        'centers_note': 'Detroit y el sureste de Michigan tienen varios centros de plasma. Las tarifas suelen ser competitivas debido a la demanda en el area. Centros disponibles en Detroit, Dearborn, Southfield y Warren.',
        'local_tip': 'Los centros en los suburbios del metro Detroit suelen tener bonos mas altos',
        'pay_range': '$50-$90',
        'bonus': '$700-$1,100',
        'monthly': '$400-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-memphis-2026',
        'city': 'Memphis',
        'state': 'Tennessee',
        'region': 'el area de Memphis',
        'en_equiv': 'plasma-donation-memphis-tn-2026.html',
        'centers_note': 'Memphis tiene multiples centros de plasma que sirven la comunidad del medio sur. Tennessee no tiene impuesto estatal sobre la renta, maximizando tus ganancias.',
        'local_tip': 'Sin impuesto estatal sobre la renta en Tennessee — tus ganancias de plasma son 100% tuyas',
        'pay_range': '$45-$85',
        'bonus': '$600-$1,000',
        'monthly': '$350-$800',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-indianapolis-2026',
        'city': 'Indianapolis',
        'state': 'Indiana',
        'region': 'el centro de Indiana',
        'en_equiv': 'plasma-donation-indianapolis-in-2026.html',
        'centers_note': 'Indianapolis tiene una buena seleccion de centros de plasma, con ubicaciones distribuidas por toda el area metro. Las tarifas son competitivas para el Medio Oeste.',
        'local_tip': 'Compara entre varios centros — Indianapolis tiene suficiente competencia para encontrar buenas tarifas',
        'pay_range': '$45-$90',
        'bonus': '$600-$1,100',
        'monthly': '$350-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-nashville-2026',
        'city': 'Nashville',
        'state': 'Tennessee',
        'region': 'el area de Nashville',
        'en_equiv': 'plasma-donation-nashville-tn-2026.html',
        'centers_note': 'Nashville es una ciudad en crecimiento con varios centros de plasma. Tennessee no tiene impuesto estatal sobre la renta, y el costo de vida relativamente bajo hace que el ingreso por plasma sea significativo.',
        'local_tip': 'Sin impuesto estatal sobre la renta y bajo costo de vida — las ganancias de plasma rinden mucho en Nashville',
        'pay_range': '$50-$90',
        'bonus': '$700-$1,100',
        'monthly': '$400-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-albuquerque-2026',
        'city': 'Albuquerque',
        'state': 'Nuevo Mexico',
        'region': 'el centro de Nuevo Mexico',
        'en_equiv': 'plasma-donation-albuquerque-nm-2026.html',
        'centers_note': 'Albuquerque tiene varios centros de plasma que sirven a la comunidad hispanohablante del estado. La cercania con la frontera mexicana crea una demanda alta de servicios en espanol.',
        'local_tip': 'Muchos centros en Albuquerque tienen personal bilingue espanol/ingles',
        'pay_range': '$45-$85',
        'bonus': '$600-$1,000',
        'monthly': '$350-$800',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-raleigh-2026',
        'city': 'Raleigh',
        'state': 'Carolina del Norte',
        'region': 'el area del Triangulo de Carolina del Norte',
        'en_equiv': 'plasma-donation-raleigh-nc-2026.html',
        'centers_note': 'Raleigh y el area del Research Triangle (Durham, Chapel Hill) tienen centros de plasma que sirven a la creciente comunidad latina de la region.',
        'local_tip': 'Busca centros tambien en Durham y Cary para mas opciones',
        'pay_range': '$50-$90',
        'bonus': '$700-$1,100',
        'monthly': '$400-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-charlotte-2026',
        'city': 'Charlotte',
        'state': 'Carolina del Norte',
        'region': 'el area de Charlotte',
        'en_equiv': 'plasma-donation-charlotte-nc-2026.html',
        'centers_note': 'Charlotte es una de las ciudades de mas rapido crecimiento del sureste y tiene multiples centros de plasma. La comunidad hispana de Charlotte esta creciendo rapidamente.',
        'local_tip': 'Los centros en el sur de Charlotte y Gastonia pueden tener esperas mas cortas',
        'pay_range': '$50-$90',
        'bonus': '$700-$1,100',
        'monthly': '$400-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-jacksonville-2026',
        'city': 'Jacksonville',
        'state': 'Florida',
        'region': 'el noreste de Florida',
        'en_equiv': 'plasma-donation-jacksonville-fl-2026.html',
        'centers_note': 'Jacksonville, la ciudad mas grande de Florida por area, tiene varios centros de plasma distribuidos por la ciudad. Florida no tiene impuesto estatal sobre la renta.',
        'local_tip': 'Sin impuesto sobre la renta en Florida — conservas todas tus ganancias de plasma',
        'pay_range': '$50-$90',
        'bonus': '$700-$1,100',
        'monthly': '$400-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-columbus-2026',
        'city': 'Columbus',
        'state': 'Ohio',
        'region': 'el centro de Ohio',
        'en_equiv': 'plasma-donation-columbus-oh-2026.html',
        'centers_note': 'Columbus es la capital de Ohio y tiene una variedad de centros de plasma. Como ciudad universitaria con la Ohio State University, hay buena disponibilidad para estudiantes.',
        'local_tip': 'Estudiantes de OSU: busca centros cerca del campus para conveniencia',
        'pay_range': '$45-$90',
        'bonus': '$600-$1,100',
        'monthly': '$350-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-milwaukee-2026',
        'city': 'Milwaukee',
        'state': 'Wisconsin',
        'region': 'el sureste de Wisconsin',
        'en_equiv': 'plasma-donation-milwaukee-wi-2026.html',
        'centers_note': 'Milwaukee tiene centros de plasma que sirven al area metropolitana. La comunidad hispana de Milwaukee esta concentrada en el sur de la ciudad, cerca de varios centros.',
        'local_tip': 'Los centros en el sur de Milwaukee estan cerca de la comunidad hispana',
        'pay_range': '$45-$90',
        'bonus': '$600-$1,100',
        'monthly': '$350-$850',
    },
    {
        'slug': 'cuanto-pagan-donar-plasma-kansas-city-2026',
        'city': 'Kansas City',
        'state': 'Missouri',
        'region': 'el area metropolitana de Kansas City',
        'en_equiv': 'plasma-donation-kansas-city-mo-2026.html',
        'centers_note': 'Kansas City se extiende entre Missouri y Kansas, ofreciendo centros de plasma en ambos estados. Compara tarifas en ambos lados de la linea estatal para mejores precios.',
        'local_tip': 'Compara centros en el lado de Missouri y Kansas — las tarifas pueden variar',
        'pay_range': '$45-$90',
        'bonus': '$600-$1,100',
        'monthly': '$350-$850',
    },
]


def gen_city_page(c):
    slug = c['slug']
    city = c['city']
    state = c['state']
    region = c['region']
    en_equiv = c['en_equiv']
    pay_range = c['pay_range']
    bonus = c['bonus']
    monthly = c['monthly']
    centers_note = c['centers_note']
    local_tip = c['local_tip']

    title = f"Donar Plasma en {city} 2026: Cuanto Pagan y Mejores Centros"
    meta = f"Centros de donacion de plasma en {city}, {state}. Pagan {pay_range} por visita, bonos de nuevo donante hasta {bonus.split('-')[1]}. Encuentra los mejores centros y tarifas actuales."

    toc = [
        ('respuesta', 'Respuesta Rapida'),
        ('centros', 'Centros Cercanos'),
        ('tarifas', 'Tarifas'),
        ('bonos', 'Bonos'),
        ('consejos', 'Consejos'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = f'''
<div class="highlight-box" id="respuesta">
<h3>Respuesta Rapida</h3>
<p>Los centros de plasma en <strong>{city}, {state}</strong> pagan <strong>{pay_range} por donacion</strong>. Los nuevos donantes pueden ganar <strong>{bonus}</strong> en su primer mes. Donando dos veces por semana, puedes ganar {monthly} al mes. {centers_note}</p>
</div>

<h2 id="centros">Centros de Plasma Cerca de {city}</h2>
<p>Estos son los principales centros de plasma que sirven {region}. Disponibilidad varia — usa nuestro <a href="/centers/">buscador de centros</a> para verificar ubicaciones exactas.</p>

<table><thead><tr><th>Centro</th><th>Pago por Visita</th><th>Bono Nuevo Donante</th><th>Potencial Mensual</th></tr></thead><tbody>
<tr><td><a href="/es/blog/csl-plasma-cuanto-pagan-tarifas-2026.html">CSL Plasma</a></td><td>$50-$100</td><td>$700-$1,200</td><td>$400-$1,000</td></tr>
<tr><td><a href="/es/blog/biolife-plasma-cuanto-pagan-tarifas-2026.html">BioLife</a></td><td>$60-$100</td><td>$900-$1,100</td><td>$400-$900</td></tr>
<tr><td><a href="/es/blog/octapharma-cuanto-pagan-tarifas-2026.html">Octapharma</a></td><td>$50-$85</td><td>$800-$1,000</td><td>$450-$900</td></tr>
<tr><td><a href="/es/blog/grifols-cuanto-pagan-tarifas-2026.html">Grifols/Biomat</a></td><td>$50-$75</td><td>$700-$1,100</td><td>$400-$900</td></tr>
</tbody></table>

{AFFILIATE_ES}

<h2 id="tarifas">Tarifas en {city} 2026</h2>
<h3>Pago por Peso</h3>
<table><thead><tr><th>Peso</th><th>Volumen</th><th>Por Visita</th><th>Mensual (8 visitas)</th></tr></thead><tbody>
<tr><td>110-149 lbs (50-67 kg)</td><td>690 mL</td><td>$40-$65</td><td>$320-$520</td></tr>
<tr><td>150-174 lbs (68-79 kg)</td><td>825 mL</td><td>$50-$80</td><td>$400-$640</td></tr>
<tr><td>175+ lbs (80+ kg)</td><td>880 mL</td><td>$60-$100</td><td>$480-$800</td></tr>
</tbody></table>

<h3>Consejo Local</h3>
<p><strong>{local_tip}</strong></p>

{PRO_TOOLKIT_ES}

<h2 id="bonos">Bonos para Nuevos Donantes en {city}</h2>
<ul>
<li><strong>CSL Plasma:</strong> $700-$1,200 en las primeras 6-8 donaciones</li>
<li><strong>BioLife:</strong> $900-$1,100 con cupones de la aplicacion</li>
<li><strong>Octapharma:</strong> $800-$1,000 con bonos graduales</li>
<li><strong>Grifols:</strong> $700-$1,100 segun ubicacion</li>
</ul>

<h3>Como Maximizar tus Ganancias en {city}</h3>
<ul>
<li><strong>Compara centros:</strong> Visita varios centros en {region} para encontrar las mejores tarifas</li>
<li><strong>Descarga las apps:</strong> BioLife y CSL Plasma tienen aplicaciones con cupones exclusivos</li>
<li><strong>Programa de referencia:</strong> Gana $50-$100 por cada amigo que refieras</li>
<li><strong>Dona consistentemente:</strong> Muchos centros ofrecen bonos por frecuencia mensual</li>
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
<li><strong>Hidratacion:</strong> Toma 64+ oz de agua el dia anterior — crucial para una donacion rapida</li>
<li><strong>Alimentacion:</strong> Come una comida rica en proteina 2-3 horas antes (pollo, huevos, frijoles)</li>
<li><strong>Ropa:</strong> Usa mangas cortas o camisa que se pueda subir facilmente</li>
<li><strong>Entretenimiento:</strong> Lleva tu telefono, auriculares o libro — la donacion dura 45-90 minutos</li>
<li><strong>Estacionamiento:</strong> Verifica si el centro tiene estacionamiento gratuito</li>
</ul>

{related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar Plasma 2026'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos de Donacion'),
    ('/es/blog/cual-centro-plasma-paga-mas-dinero.html', 'Cual Centro Paga Mas?'),
    ('/es/blog/', 'Blog en Espanol'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Cuanto pagan por donar plasma en {city}?</h3>
<p>Los centros de plasma en {city} pagan {pay_range} por visita para donantes regulares. Los nuevos donantes pueden ganar {bonus} en su primer mes. Con donaciones dos veces por semana, puedes ganar {monthly} mensualmente.</p>

<h3>¿Donde puedo donar plasma en {city}?</h3>
<p>Busca centros de CSL Plasma, BioLife, Octapharma o Grifols en {region}. Usa nuestro <a href="/centers/">buscador de centros</a> para encontrar ubicaciones exactas cerca de ti.</p>

<h3>¿Que necesito para donar plasma por primera vez?</h3>
<p>Necesitas una identificacion con foto, numero de Seguro Social, comprobante de domicilio, tener 18-69 anos de edad y pesar al menos 110 libras (50 kg). Tu primera visita dura 2-3 horas incluyendo examen medico.</p>

<h3>¿Cuantas veces puedo donar plasma por semana en {city}?</h3>
<p>Puedes donar plasma hasta 2 veces por semana en todos los centros de {city}, con al menos 48 horas entre donaciones. Esto te permite donar hasta 8 veces al mes.</p>

<div class="related-articles">
<h3>Guias Relacionadas</h3>
<div class="related-grid">
<a href="/es/blog/cuanto-pagan-por-donar-plasma-2026.html" class="related-link">Cuanto Pagan 2026</a>
<a href="/es/blog/requisitos-donacion-plasma.html" class="related-link">Requisitos</a>
<a href="/es/blog/cual-centro-plasma-paga-mas-dinero.html" class="related-link">Cual Paga Mas</a>
<a href="/es/" class="related-link">Calculadora</a>
</div>
</div>'''

    faqs = [
        make_faq(f"¿Cuanto pagan por donar plasma en {city}?",
                 f"Los centros de plasma en {city} pagan {pay_range} por visita para donantes regulares. Nuevos donantes ganan {bonus} en el primer mes."),
        make_faq(f"¿Donde puedo donar plasma en {city}?",
                 f"Busca centros de CSL Plasma, BioLife, Octapharma o Grifols en {region}. Usa nuestro buscador de centros para ubicaciones exactas."),
        make_faq(f"¿Cuantas veces puedo donar plasma por semana en {city}?",
                 f"Puedes donar hasta 2 veces por semana, con al menos 48 horas entre donaciones, para un maximo de 8 donaciones al mes."),
    ]

    return slug, make_es_page(slug, title, meta, f"{city} 2026", 8, toc, content, faqs, en_equiv)


# ============ MAIN ============
if __name__ == '__main__':
    os.makedirs(ES_BLOG_DIR, exist_ok=True)
    print(f"Generating Round 3 Spanish City pages ({len(cities)} pages)...")
    count = 0

    for c in cities:
        slug, html = gen_city_page(c)
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1

    print(f"Done! Generated {count} Spanish city pages.")
