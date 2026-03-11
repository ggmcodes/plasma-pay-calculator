#!/usr/bin/env python3
"""Generate Batch 5: Spanish template pages (city + center + comparisons) - 16 pages"""
import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ES_BLOG_DIR = os.path.join(BASE_DIR, 'es', 'blog')

def make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema, en_equivalent=None):
    canonical = f"https://plasmapaycalculator.com/es/blog/{slug}"
    faq_json = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq_schema}, ensure_ascii=False)
    article_json = json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":meta_desc,"datePublished":"2026-02-13","dateModified":"2026-02-13","author":{"@type":"Organization","name":"PlasmaPayCalculator.com"}}, ensure_ascii=False)
    toc_html = ''.join(f'<li><a href="#{tid}">{tname}</a></li>' for tid, tname in toc_items)

    hreflang = ''
    if en_equivalent:
        hreflang = f'''<link rel="alternate" hreflang="en" href="https://plasmapaycalculator.com/blog/{en_equivalent}">
<link rel="alternate" hreflang="es" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="https://plasmapaycalculator.com/blog/{en_equivalent}">'''

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-053DRWEQLS"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-053DRWEQLS');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451" crossorigin="anonymous"></script>
<meta charset="UTF-8">
<link rel="stylesheet" href="/assets/css/global-fonts.css"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://plasmapaycalculator.com/es/"}},
    {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://plasmapaycalculator.com/es/blog/"}},
    {{"@type": "ListItem", "position": 3, "name": "{title}"}}
  ]
}}
</script>
<meta name="description" content="{meta_desc}">
<meta name="theme-color" content="#0D4F4F">
<link rel="canonical" href="{canonical}">
{hreflang}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/theme.css"><link rel="stylesheet" href="../../css/blog.css">
<script type="application/ld+json">
{faq_json}
</script>
<script type="application/ld+json">
{article_json}
</script>
<meta property="og:image" content="https://plasmapaycalculator.com/images/plasma-donation-guide.jpg">
</head>
<body class="plasma-rebrand">
<div class="reading-progress" id="readingProgress"></div>
<nav class="nav" id="mainNav"><div class="nav-inner"><a href="../../es/" class="logo"><span class="logo-mark">$</span> Plasma Pay</a><ul class="nav-links"><li><a href="../../es/">Calculadora</a></li><li><a href="../../es/blog/">Blog</a></li><li><a href="../../centers/">Centros</a></li><li><a href="../../centers/" class="nav-cta">Encontrar Centros</a></li></ul><button class="mobile-toggle" onclick="toggleMobileMenu()"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg></button></div></nav>
<header class="blog-header"><div class="blog-header-inner"><span class="blog-category">{category}</span><h1>{title}</h1>
<div style="display: inline-block; background: #dcfce7; color: #166534; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500; margin: 0.5rem 0;">
Actualizado: Febrero 2026
</div><div class="blog-meta"><div class="blog-meta-item"><span>Guia de Pago</span></div><div class="blog-meta-item reading-time">{read_time} min lectura</div></div></div></header>
<div class="blog-layout">
<aside class="toc-sidebar"><div class="toc-container"><h4 class="toc-title">Contenido</h4><ul class="toc-list">{toc_html}</ul></div></aside>
<article class="blog-content">

{content_html}

</article></div>
<footer class="footer"><div class="footer-bottom"><p>&copy; 2026 PlasmaPayCalculator.com</p></div></footer>
<script>window.addEventListener('scroll', () => {{document.getElementById('readingProgress').style.width = Math.min((window.scrollY / (document.querySelector('.blog-content').offsetHeight - window.innerHeight)) * 100, 100) + '%';document.getElementById('mainNav').classList.toggle('scrolled', window.scrollY > 50);}});function toggleMobileMenu() {{ document.querySelector('.nav-links').classList.toggle('active'); }}</script>
</body></html>'''

def make_faq(q, a):
    return {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}

AFFILIATE_ES = '''
<section style="margin: 2rem 0; padding: 1.5rem; background: linear-gradient(135deg, #f0fdf4 0%, #fff 100%); border-radius: 12px; border: 1px solid #bbf7d0;">
    <p style="font-size: 0.85rem; color: #666; margin-bottom: 1rem;"><em>Como asociado de Amazon, ganamos con las compras que califican.</em></p>
    <h3 style="margin-top: 0; color: #166534;">Productos Esenciales para Donantes</h3>
    <ul style="list-style: none; padding: 0;">
        <li style="margin: 0.75rem 0;"><a href="https://www.amazon.com/s?k=Liquid+IV+Hydration+Multiplier&tag=plasma0f-20" target="_blank" rel="nofollow noopener" style="color: #166534; font-weight: 500;">Liquid I.V. Hidratacion</a> - Optimiza hidratacion antes de donar</li>
        <li style="margin: 0.75rem 0;"><a href="https://www.amazon.com/s?k=Premier+Protein+Shakes+30g&tag=plasma0f-20" target="_blank" rel="nofollow noopener" style="color: #166534; font-weight: 500;">Premier Protein Batidos 30g</a> - Proteina para mejor calidad de plasma</li>
        <li style="margin: 0.75rem 0;"><a href="https://www.amazon.com/s?k=Anker+Portable+Charger+10000mAh&tag=plasma0f-20" target="_blank" rel="nofollow noopener" style="color: #166534; font-weight: 500;">Anker Cargador Portatil</a> - Mantén tu telefono cargado durante la donacion</li>
        <li style="margin: 0.75rem 0;"><a href="https://www.amazon.com/s?k=Insulated+Water+Bottle+32oz&tag=plasma0f-20" target="_blank" rel="nofollow noopener" style="color: #166534; font-weight: 500;">Botella de Agua 32oz</a> - Mantente hidratado todo el dia</li>
    </ul>
</section>'''

PRO_TOOLKIT_ES = '''
<div style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 100%); border-radius: 12px; padding: 1.5rem 2rem; text-align: center; color: white; margin: 2rem 0;">
    <p style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; margin: 0 0 0.3rem;">Recurso Premium</p>
    <p style="font-size: 1.1rem; font-weight: 700; margin: 0 0 0.4rem;">Kit Pro para Donantes de Plasma</p>
    <p style="font-size: 0.85rem; opacity: 0.9; margin: 0 0 1rem;">Plan de ganancias de 90 dias, estrategia de bonos, guia de impuestos 2026. Gana $2,000+ en tus primeros 3 meses.</p>
    <a href="/premium/" style="display: inline-block; background: white; color: #0d9488; padding: 0.6rem 1.4rem; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.9rem;">Obtener Kit Pro &mdash; $19</a>
</div>'''

def related_es(links):
    items = ''.join(f'<li><a href="{u}" style="color: #0369a1; text-decoration: none; font-weight: 500;">{t} &rarr;</a></li>' for u,t in links)
    return f'''<div class="related-articles" style="margin: 2rem 0; padding: 1.5rem; background: #f0f9ff; border-radius: 12px; border-left: 4px solid #0ea5e9;">
    <h3 style="margin: 0 0 1rem 0; color: #0c4a6e; font-size: 1.1rem;">Guias Relacionadas</h3>
    <ul style="list-style: none; padding: 0; margin: 0;">{items}</ul></div>'''

# ============ SPANISH CITY PAGES ============
es_cities = [
    ('cuanto-pagan-donar-plasma-san-diego-2026', 'San Diego', 'California', 'el sur de California'),
    ('cuanto-pagan-donar-plasma-miami-2026', 'Miami', 'Florida', 'el sur de Florida'),
    ('cuanto-pagan-donar-plasma-houston-2026', 'Houston', 'Texas', 'el area metropolitana de Houston'),
    ('cuanto-pagan-donar-plasma-los-angeles-2026', 'Los Angeles', 'California', 'el area de Los Angeles'),
    ('cuanto-pagan-donar-plasma-dallas-2026', 'Dallas', 'Texas', 'el area metropolitana de Dallas-Fort Worth'),
    ('cuanto-pagan-donar-plasma-chicago-2026', 'Chicago', 'Illinois', 'el area de Chicago'),
    ('cuanto-pagan-donar-plasma-phoenix-2026', 'Phoenix', 'Arizona', 'el Valle del Sol'),
    ('cuanto-pagan-donar-plasma-san-antonio-2026', 'San Antonio', 'Texas', 'el centro-sur de Texas'),
    ('cuanto-pagan-donar-plasma-nueva-york-2026', 'Nueva York', 'New York', 'el area metropolitana de Nueva York'),
    ('cuanto-pagan-donar-plasma-yuma-arizona-2026', 'Yuma', 'Arizona', 'el suroeste de Arizona'),
    ('cuanto-pagan-donar-plasma-san-ysidro-california-2026', 'San Ysidro', 'California', 'la frontera sur de California'),
    ('cuanto-pagan-donar-plasma-atlanta-2026', 'Atlanta', 'Georgia', 'el area metropolitana de Atlanta'),
    ('cuanto-pagan-donar-plasma-las-vegas-2026', 'Las Vegas', 'Nevada', 'el area de Las Vegas'),
]

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
        make_faq(f"¿Cuanto pagan por donar plasma en {city}?", f"$50-$100 por visita para donantes regulares, $700-$1,200 para nuevos donantes en el primer mes."),
        make_faq(f"¿Donde puedo donar plasma en {city}?", f"Busca centros de CSL Plasma, BioLife, Octapharma o Grifols en {region}."),
    ]
    return make_es_page(slug, title, meta, f"{city} 2026", 8, toc, content, faqs)

# ============ SPANISH CENTER PAGES ============
es_centers = [
    ('octapharma-cuanto-pagan-tarifas-2026', 'Octapharma', '$50-$85', '$800-$1,000', '$450-$900', 'octapharma-plasma-pay-rates-2026'),
    ('grifols-cuanto-pagan-tarifas-2026', 'Grifols', '$50-$75', '$700-$1,100', '$400-$900', 'grifols-plasma-pay-rates-2026'),
    ('kedplasma-cuanto-pagan-tarifas-2026', 'KedPlasma', '$50-$75', '$600-$1,000', '$400-$800', 'kedplasma-pay-rates-2026'),
]

def gen_es_center(slug, name, pay_range, bonus_range, monthly, en_slug):
    title = f"{name}: ¿Cuanto Pagan por Donar Plasma en 2026? Tarifas Completas"
    meta = f"{name} paga {pay_range} por donacion. Nuevos donantes ganan {bonus_range} el primer mes. Consulta tarifas, bonos y comparaciones 2026."
    toc = [('respuesta','Respuesta Rapida'),('tarifas','Tarifas'),('bonos','Bonos Nuevos'),('peso','Por Peso'),('comparacion','Comparacion'),('faq','Preguntas Frecuentes')]

    content = f'''
<div class="highlight-box" id="respuesta"><h3>Respuesta Rapida</h3><p>{name} paga <strong>{pay_range} por donacion</strong> para donantes regulares, con ganancias mensuales de <strong>{monthly}</strong> donando dos veces por semana. Los nuevos donantes pueden ganar <strong>{bonus_range}</strong> en su primer mes con bonos promocionales.</p></div>

<h2 id="tarifas">Tarifas de {name} 2026</h2>
<table><thead><tr><th>Tipo de Donante</th><th>Primera Donacion/Semana</th><th>Segunda Donacion/Semana</th><th>Potencial Mensual</th></tr></thead><tbody>
<tr><td>Nuevo Donante (Mes 1)</td><td>$100-$150</td><td>$100-$150</td><td>{bonus_range}</td></tr>
<tr><td>Donante Regular</td><td>{pay_range.split("-")[0]}</td><td>{pay_range.split("-")[1] if "-" in pay_range else pay_range}</td><td>{monthly}</td></tr>
<tr><td>Peso Alto (175+ lbs)</td><td>${int(pay_range.split("$")[1].split("-")[0])+10}</td><td>${int(pay_range.split("-$")[1])+10}</td><td>${int(monthly.split("$")[1].split("-")[0])+80}-${int(monthly.split("-$")[1])}</td></tr>
</tbody></table>

{AFFILIATE_ES}

<h2 id="bonos">Bonos para Nuevos Donantes</h2>
<p>{name} ofrece bonos generosos para nuevos donantes que completan multiples donaciones en su primer mes:</p>
<ul>
<li><strong>Periodo:</strong> Primeros 30-45 dias</li>
<li><strong>Requisito:</strong> Completar 6-8 donaciones</li>
<li><strong>Potencial:</strong> {bonus_range} en el primer mes</li>
<li><strong>Estructura:</strong> Bonos graduales que aumentan con cada donacion</li>
</ul>

<h2 id="peso">Pago por Peso</h2>
<table><thead><tr><th>Peso</th><th>Volumen</th><th>Pago por Visita</th></tr></thead><tbody>
<tr><td>110-149 lbs (50-67 kg)</td><td>690 mL</td><td>{pay_range.split("-")[0]}</td></tr>
<tr><td>150-174 lbs (68-79 kg)</td><td>825 mL</td><td>{pay_range}</td></tr>
<tr><td>175+ lbs (80+ kg)</td><td>880 mL</td><td>${int(pay_range.split("-$")[1])+10}</td></tr>
</tbody></table>

{PRO_TOOLKIT_ES}

<h2 id="comparacion">Comparacion con Otros Centros</h2>
<table><thead><tr><th>Centro</th><th>Pago por Visita</th><th>Bono Nuevo</th><th>Mensual</th></tr></thead><tbody>
<tr><td><strong>{name}</strong></td><td>{pay_range}</td><td>{bonus_range}</td><td>{monthly}</td></tr>
<tr><td>CSL Plasma</td><td>$50-$100</td><td>$700-$1,200</td><td>$400-$1,000</td></tr>
<tr><td>BioLife</td><td>$60-$100</td><td>$900-$1,100</td><td>$400-$900</td></tr>
</tbody></table>

{related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar Plasma'),
    ('/es/blog/cual-centro-plasma-paga-mas-dinero.html', 'Cual Centro Paga Mas?'),
    ('/es/blog/', 'Blog en Espanol'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Cuanto paga {name} por donar plasma?</h3>
<p>{name} paga {pay_range} por donacion para donantes regulares. Los nuevos donantes ganan {bonus_range} en el primer mes con bonos especiales.</p>

<h3>¿Cuanto ganan los nuevos donantes en {name}?</h3>
<p>Los nuevos donantes pueden ganar {bonus_range} completando 6-8 donaciones en sus primeros 30-45 dias.</p>

<div class="related-articles">
<h3>Guias Relacionadas</h3>
<div class="related-grid">
<a href="/es/blog/guia-completa-donacion-plasma.html" class="related-link">Guia Completa</a>
<a href="/es/blog/requisitos-donacion-plasma.html" class="related-link">Requisitos</a>
<a href="/es/" class="related-link">Calculadora</a>
</div>
</div>'''

    faqs = [
        make_faq(f"¿Cuanto paga {name} por donar plasma?", f"{name} paga {pay_range} por donacion. Nuevos donantes ganan {bonus_range} en el primer mes."),
        make_faq(f"¿Cuanto ganan los nuevos donantes en {name}?", f"Nuevos donantes pueden ganar {bonus_range} completando 6-8 donaciones en 30-45 dias."),
    ]
    return make_es_page(slug, title, meta, f"{name} 2026", 10, toc, content, faqs, en_slug)

# ============ SPANISH COMPARISON PAGES ============
def gen_es_comparison(slug, center1, center2, en_slug=None):
    title = f"{center1} vs {center2}: Comparacion Completa 2026"
    meta = f"{center1} vs {center2} comparados: tarifas, bonos, ubicaciones y cual paga mas en 2026. Guia completa para elegir el mejor centro de plasma."
    toc = [('respuesta','Respuesta'),('tarifas','Tarifas'),('bonos','Bonos'),('veredicto','Veredicto'),('faq','Preguntas')]

    content = f'''
<div class="highlight-box" id="respuesta"><h3>Respuesta Rapida</h3><p>Ambos {center1} y {center2} ofrecen tarifas competitivas para donacion de plasma en 2026. Las tarifas exactas varian por ubicacion. En general, la mejor opcion depende de que centro esta mas cerca de ti y cuales promociones estan activas en tu area.</p></div>

<h2 id="tarifas">Comparacion de Tarifas</h2>
<table><thead><tr><th>Categoria</th><th>{center1}</th><th>{center2}</th></tr></thead><tbody>
<tr><td>Pago por visita</td><td>$50-$100</td><td>$50-$100</td></tr>
<tr><td>Bono nuevo donante</td><td>$700-$1,200</td><td>$700-$1,100</td></tr>
<tr><td>Potencial mensual</td><td>$400-$1,000</td><td>$400-$900</td></tr>
<tr><td>Bono de referencia</td><td>$50-$100</td><td>$50-$100</td></tr>
</tbody></table>

{AFFILIATE_ES}

<h2 id="bonos">Bonos y Promociones</h2>
<h3>{center1}</h3>
<ul>
<li>Bonos de nuevo donante competitivos</li>
<li>Programa de lealtad con puntos</li>
<li>Promociones estacionales frecuentes</li>
</ul>

<h3>{center2}</h3>
<ul>
<li>Bonos graduales para nuevos donantes</li>
<li>Bonos por frecuencia mensual</li>
<li>Promociones de temporada</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="veredicto">¿Cual Elegir?</h2>
<ul>
<li><strong>Elige {center1} si:</strong> Tiene mejor bono de nuevo donante en tu area, o esta mas cerca</li>
<li><strong>Elige {center2} si:</strong> Ofrece mejores tarifas para donantes regulares en tu ubicacion</li>
<li><strong>Consejo pro:</strong> Empieza en el centro con mejor bono de nuevo donante, luego evalua cual paga mas a largo plazo</li>
</ul>

{related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar Plasma'),
    ('/es/blog/cual-centro-plasma-paga-mas-dinero.html', 'Cual Centro Paga Mas?'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿{center1} o {center2} paga mas?</h3>
<p>Varia por ubicacion. Ambos pagan $50-$100 por visita. Compara las tarifas actuales en los centros de tu area para determinar cual ofrece mejor compensacion.</p>

<div class="related-articles">
<h3>Guias Relacionadas</h3>
<div class="related-grid">
<a href="/es/blog/cuanto-pagan-por-donar-plasma-2026.html" class="related-link">Cuanto Pagan 2026</a>
<a href="/es/blog/cual-centro-plasma-paga-mas-dinero.html" class="related-link">Cual Paga Mas</a>
<a href="/es/" class="related-link">Calculadora</a>
</div>
</div>'''

    faqs = [make_faq(f"¿{center1} o {center2} paga mas?", "Varia por ubicacion. Ambos pagan $50-$100 por visita. Compara tarifas locales.")]
    return make_es_page(slug, title, meta, "Comparacion 2026", 8, toc, content, faqs, en_slug)


if __name__ == '__main__':
    print("Generating Batch 5: Spanish template pages (16 pages)...")
    count = 0

    # City pages
    for slug, city, state, region in es_cities:
        html = gen_es_city(slug, city, state, region)
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1

    # Center pages
    for slug, name, pay, bonus, monthly, en_slug in es_centers:
        html = gen_es_center(slug, name, pay, bonus, monthly, en_slug)
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1

    print(f"Done! Generated {count} Spanish template pages.")
