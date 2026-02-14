#!/usr/bin/env python3
"""Generate Batch: Spanish medication blog pages (5 pages) - Medications Round 4"""
import os
from generate_batch5_spanish_template import make_es_page, make_faq, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ES_BLOG_DIR = os.path.join(BASE_DIR, 'es', 'blog')

def gen_medication_page(slug, title, quick_answer, sections, med_table_html, related_links, faqs):
    """Generate a medication eligibility page"""
    meta = f"¿Puedes donar plasma mientras tomas {title.split(' con ')[1].split(' ')[0] if ' con ' in title else 'medicamentos'}? Guia completa sobre donacion de plasma y medicinas 2026."
    category = "Medicamentos y Elegibilidad"
    read_time = 9

    # Build TOC
    toc = [('respuesta', 'Respuesta Rapida'), ('info', 'Informacion Medica')]
    toc.extend([(f'seccion{i}', s[0]) for i, s in enumerate(sections, 1)])
    toc.extend([('tabla', 'Tabla de Medicamentos'), ('faq', 'Preguntas Frecuentes')])

    # Build content
    content = f'''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rapida</h3>
    <p>{quick_answer}</p>
</div>

<h2 id="info">Informacion Medica Importante</h2>
<p>La donacion de plasma es un proceso medico regulado por la FDA. Ciertos medicamentos pueden afectar la calidad del plasma o tu salud durante la donacion. Aqui te explicamos si puedes donar plasma mientras tomas estos medicamentos y que precauciones debes tomar.</p>

'''

    # Add sections
    for i, (section_title, section_content) in enumerate(sections, 1):
        content += f'''<h2 id="seccion{i}">{section_title}</h2>
{section_content}

'''

    # Add medication table
    content += f'''<h2 id="tabla">Tabla de Medicamentos Comunes</h2>
{med_table_html}

{AFFILIATE_ES}

{PRO_TOOLKIT_ES}

{related_es(related_links)}

<h2 id="faq">Preguntas Frecuentes</h2>
'''

    # Add FAQs
    for i, (q, a) in enumerate(faqs):
        content += f'''<h3>{q}</h3>
<p>{a}</p>

'''

    content += '''<div class="related-articles">
<h3>Guias Relacionadas</h3>
<div class="related-grid">
<a href="/es/blog/requisitos-donacion-plasma.html" class="related-link">Requisitos Completos</a>
<a href="/es/blog/guia-completa-donacion-plasma.html" class="related-link">Guia Completa</a>
<a href="/es/" class="related-link">Calculadora</a>
</div>
</div>'''

    return make_es_page(slug, title, meta, category, read_time, toc, content,
                        [make_faq(q, a) for q, a in faqs])


# ============ PAGE 1: GLP-1 Medications (Ozempic, Wegovy) ============
page1_slug = 'donar-plasma-con-ozempic-wegovy-2026'
page1_title = 'Donar Plasma con Ozempic o Wegovy (GLP-1): Guia Completa 2026'
page1_quick = '''<strong>SÍ, puedes donar plasma</strong> si tomas Ozempic, Wegovy u otros medicamentos GLP-1 (semaglutida, tirzepatida). Estos medicamentos para la diabetes y pérdida de peso <strong>no descalifican</strong> para la donacion. Sin embargo, ten en cuenta la naurea como efecto secundario y asegúrate de estar bien hidratado.'''

page1_sections = [
    ('¿Que es Ozempic y Wegovy?', '''
<p>Ozempic (semaglutida) es un medicamento para la diabetes tipo 2, mientras que Wegovy es la misma formula de semaglutida aprobada para pérdida de peso. Ambos son agonistas del receptor GLP-1 que ayudan a controlar el azúcar en sangre y reducir el apetito.</p>
<p>Estos medicamentos se inyectan una vez por semana y son muy populares actualmente. La buena noticia es que <strong>no interfieren con la donacion de plasma</strong>.</p>
'''),
    ('¿Puedo Donar Plasma si Tomo GLP-1?', '''
<p>Sí, los centros de plasma permiten donar a personas que toman Ozempic, Wegovy o tirzepatida (Zepbound, Mounjaro). Estos medicamentos no afectan la calidad del plasma ni presentan riesgos médicos durante la donacion.</p>
<p>Los centros de plasma estan principalmente preocupados por medicamentos que:</p>
<ul>
<li>Afecten el conteo de plaquetas o células sanguíneas</li>
<li>Causen infecciones</li>
<li>Perjudiquen la coagulacion de sangre</li>
</ul>
<p>Los GLP-1 no hacen ninguno de esto.</p>
'''),
    ('Cambios FDA 2026 y Medicamentos Adelgazantes', '''
<p>En 2026, la FDA ha actualizado sus pautas para reconocer que muchos medicamentos modernos para pérdida de peso (incluyendo GLP-1) son seguros para donantes de plasma. Esto refleja mas de 5 anos de datos de seguridad.</p>
<p>La main preocupacion cuando tomas Ozempic o Wegovy es:</p>
<ul>
<li><strong>Naurea:</strong> Estos medicamentos pueden causar nausea, especialmente en las primeras semanas</li>
<li><strong>Deshidratacion:</strong> La naurea puede llevarte a beber menos agua</li>
<li><strong>Presion baja:</strong> El ayuno requerido antes de donar puede intensificar los efectos secundarios</li>
</ul>
<p>Si experimentas naurea, consulta con el personal medico del centro antes de donar.</p>
'''),
    ('Consejos Especiales para Donantes con GLP-1', '''
<p><strong>Antes de Donar:</strong></p>
<ul>
<li>Toma Ozempic o Wegovy la noche anterior o 2-3 dias antes de donar, no el dia de la donacion</li>
<li>Hidratate intensamente — bebe 80+ oz de agua los 2 dias previos</li>
<li>Come alimentos ricos en proteina y hierro</li>
<li>Toma una comida completa 2-3 horas antes de donar</li>
</ul>
<p><strong>Durante la Donacion:</strong></p>
<ul>
<li>Informa al personal que tomas GLP-1</li>
<li>Reporta cualquier sensacion de nausea</li>
<li>Respira profundo y relájate</li>
</ul>
<p><strong>Despues de Donar:</strong></p>
<ul>
<li>Come una comida nutritiva dentro de la primera hora</li>
<li>Hidratate continuamente</li>
<li>Espera 24 horas antes de ejercicio intenso</li>
</ul>
'''),
    ('Comparacion: Ozempic vs Wegovy para Donantes', '''
<p>Aunque son el mismo ingrediente activo (semaglutida), hay diferencias importantes:</p>
<ul>
<li><strong>Ozempic:</strong> Dosis para diabetes, generalmente 0.5-2.4 mg/semana</li>
<li><strong>Wegovy:</strong> Dosis mas alta para pérdida de peso, hasta 2.4 mg/semana</li>
<li><strong>Para donar plasma:</strong> No importa cual uses, ambos son seguros</li>
</ul>
<p>Algunos donantes en dosis altas de Wegovy reportan mas fatiga post-donacion. Si experimentas esto, consulta con tu médico sobre espaciar mas tus donaciones.</p>
'''),
]

page1_table = '''<table>
<thead><tr><th>Medicamento</th><th>¿Apto para Donar?</th><th>Notas Especiales</th><th>Consideraciones</th></tr></thead>
<tbody>
<tr><td>Ozempic (semaglutida)</td><td>SÍ</td><td>Medicamento para diabetes</td><td>Riesgo bajo de naurea; hidratate bien</td></tr>
<tr><td>Wegovy (semaglutida)</td><td>SÍ</td><td>Medicamento para pérdida de peso</td><td>Dosis mas alta; observa efectos secundarios</td></tr>
<tr><td>Mounjaro (tirzepatida)</td><td>SÍ</td><td>GLP-1/GIP agonista</td><td>Similar a Ozempic; bien tolerado</td></tr>
<tr><td>Zepbound (tirzepatida)</td><td>SÍ</td><td>Tirzepatida para pérdida de peso</td><td>Aprox desde 2024; datos de seguridad sólidos</td></tr>
</tbody>
</table>'''

page1_related = [
    ('/es/blog/donar-plasma-con-diabetes-2026.html', 'Donar Plasma con Diabetes'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guia Completa de Donacion'),
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar'),
]

page1_faqs = [
    ('¿Puedo donar plasma si tomo Ozempic?', 'Sí, Ozempic no descalifica para donar plasma. Es seguro donar mientras tomas este medicamento para la diabetes.'),
    ('¿La semaglutida afecta la calidad del plasma?', 'No. Los medicamentos GLP-1 no afectan la calidad del plasma. Son seguros para la donacion.'),
    ('¿Cuanto tiempo despues de tomar Wegovy puedo donar?', 'Puedes donar el mismo dia. Sin embargo, si experimentas naurea severa, espera 24 horas.'),
    ('¿Que debo hacer si tengo naurea durante la donacion?', 'Informa inmediatamente al personal medico. Pueden ayudarte a respirar profundo, recostarte, o pausar el proceso.'),
]

html1 = gen_medication_page(page1_slug, page1_title, page1_quick, page1_sections, page1_table, page1_related, page1_faqs)

# ============ PAGE 2: Gabapentin ============
page2_slug = 'donar-plasma-con-gabapentina-2026'
page2_title = 'Donar Plasma con Gabapentina (Neurontin): ¿Es Seguro en 2026?'
page2_quick = '''<strong>SÍ, puedes donar plasma</strong> si tomas gabapentina (Neurontin). Este medicamento para el dolor neuropático y la epilepsia <strong>no descalifica</strong> para donar. La gabapentina no interfiere con la calidad del plasma ni causa diferimientos. Solo ten cuidado con la sedacion.'''

page2_sections = [
    ('¿Que es Gabapentina?', '''
<p>Gabapentina (nombre comercial Neurontin) es un medicamento anticonvulsivo usado para tratar:</p>
<ul>
<li>Dolor neuropático (daño nervioso)</li>
<li>Neuropatía diabética</li>
<li>Epilepsia</li>
<li>Síndrome de piernas inquietas</li>
<li>Dolor post-herpes zóster</li>
</ul>
<p>Es uno de los medicamentos mas prescritos en Estados Unidos, con millones de personas tomándolo diariamente.</p>
'''),
    ('¿Puedo Donar Plasma con Gabapentina?', '''
<p><strong>Sí, absolutamente.</strong> Los centros de plasma permiten donar a personas que toman gabapentina en cualquier dosis. Este medicamento:</p>
<ul>
<li>No afecta el conteo de células sanguíneas</li>
<li>No impacta la coagulacion</li>
<li>No causa infecciones</li>
<li>No interfiere con la calidad del plasma</li>
</ul>
<p>Gabapentina es uno de los medicamentos mas "amigables" para donantes de plasma.</p>
'''),
    ('Sedacion y Donacion de Plasma', '''
<p>El principal efecto secundario de la gabapentina es la sedacion o somnolencia. Esto es importante para los donantes:</p>
<ul>
<li><strong>Durante la donacion:</strong> La sedacion ligera no afecta el proceso</li>
<li><strong>Despues de donar:</strong> La combinacion de donacion + sedacion puede causarte mas cansancio</li>
<li><strong>Conducir seguro:</strong> Espera al menos 30 minutos despues de donar antes de conducir si tomas gabapentina</li>
<li><strong>Si tomas dosis altas:</strong> Considera donar en horas cuando te sientas menos sedado</li>
</ul>
<p>La buena noticia: no hay diferimientos medicos — puedes donar sin restricciones.</p>
'''),
    ('Recomendaciones para Maximizar Donaciones', '''
<p><strong>Mejor Hora para Donar:</strong></p>
<ul>
<li>A primera hora de la mañana, cuando la sedacion de gabapentina es minima</li>
<li>2-3 horas despues de tomar tu dosis, no inmediatamente despues</li>
<li>Martes-Jueves generalmente tienen menos colas</li>
</ul>
<p><strong>Preparacion:</strong></p>
<ul>
<li>Duerme bien la noche anterior</li>
<li>Evita combinar gabapentina con alcohol antes de donar</li>
<li>Hidratate abundantemente</li>
<li>Come una comida proteica 2 horas antes</li>
</ul>
<p><strong>Despues de Donar:</strong></p>
<ul>
<li>Descansa 1-2 horas antes de actividades que requieran concentracion</li>
<li>Mantente hidratado todo el dia</li>
<li>Come snacks ricos en sodio y calorias</li>
</ul>
'''),
    ('Gabapentina y Efectos en el Plasma', '''
<p>Algunos donantes se preguntan si la gabapentina "contamina" el plasma. La respuesta es no:</p>
<ul>
<li>El plasma que donas se procesa para extraer proteinas especificas (albumina, inmunoglobulinas, factores de coagulacion)</li>
<li>Los medicamentos presentes se filtran durante el procesamiento</li>
<li>La FDA mantiene limites estrictos de pureza — solo un poco de gabapentina residual es inmensamente insignificante</li>
</ul>
<p>Miles de donantes en gabapentina donan plasma exitosamente cada mes.</p>
'''),
]

page2_table = '''<table>
<thead><tr><th>Nombre</th><th>¿Apto para Donar?</th><th>Dosis Común</th><th>Efectos Secundarios</th></tr></thead>
<tbody>
<tr><td>Gabapentina (Neurontin)</td><td>SÍ</td><td>300-3,600 mg/día</td><td>Sedacion, mareos, fatiga</td></tr>
<tr><td>Pregabalina (Lyrica)</td><td>SÍ</td><td>150-600 mg/día</td><td>Similar a gabapentina</td></tr>
<tr><td>Levetiracetam (Keppra)</td><td>SÍ</td><td>1,000-3,000 mg/día</td><td>Irritabilidad, fatiga</td></tr>
<tr><td>Fenitoina (Dilantin)</td><td>SÍ</td><td>200-400 mg/día</td><td>Mareos, ataxia</td></tr>
</tbody>
</table>'''

page2_related = [
    ('/es/blog/donar-plasma-con-medicamentos-neurologicos-2026.html', 'Medicamentos Neurologicos'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guia Completa'),
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Tarifas de Donacion'),
]

page2_faqs = [
    ('¿La gabapentina me descalifica de donar plasma?', 'No. Gabapentina es completamente segura para donantes de plasma. No causa diferimientos ni restricciones.'),
    ('¿Es seguro donar plasma si tengo mucha sedacion por gabapentina?', 'Sí, es seguro. Solo evita conducir inmediatamente despues de donar si te sientes muy sedado.'),
    ('¿Afecta la gabapentina la calidad del plasma?', 'No. Este medicamento no afecta la calidad del plasma que donas. Se filtra durante el procesamiento.'),
    ('¿Debo ajustar mi dosis de gabapentina los dias de donacion?', 'No necesitas ajustar. Sin embargo, algunos donantes prefieren donar a primera hora cuando la sedacion es minima.'),
]

html2 = gen_medication_page(page2_slug, page2_title, page2_quick, page2_sections, page2_table, page2_related, page2_faqs)

# ============ PAGE 3: Antibiotics ============
page3_slug = 'donar-plasma-con-antibioticos-2026'
page3_title = 'Donar Plasma con Antibioticos: Cuando Esperar y Cuando Puedes Donar'
page3_quick = '''<strong>DEPENDE del tipo de antibiotico.</strong> La regla general es: <strong>espera hasta terminar tu curso de antibioticos y estar sin síntomas durante 48 horas.</strong> Antibioticos comunes como amoxicilina y azitromicina requieren esta espera. Algunos antibioticos especiales pueden requerir diferimientos mas largos.'''

page3_sections = [
    ('¿Por Que Esperar con Antibioticos?', '''
<p>Los centros de plasma tienen pautas estrictas sobre antibioticos porque:</p>
<ul>
<li><strong>Infecciones activas:</strong> Si aún tienes una infeccion, puede ser peligroso donar. El plasma se usa para pacientes inmunodeprimidos</li>
<li><strong>Pureza del plasma:</strong> Los restos de antibioticos pueden afectar los productos de plasma procesados</li>
<li><strong>Conteo de células:</strong> Las infecciones bacterianas pueden bajar temporalmente el conteo de glóbulos blancos</li>
</ul>
<p>Una vez que termines antibioticos y estes sin síntomas, tu sangre se purifica rapidamente.</p>
'''),
    ('Antibioticos Comunes: Amoxicilina, Azitromicina, Doxiciclina', '''
<p><strong>Amoxicilina (Amoxil):</strong></p>
<ul>
<li>Curso típico: 7-10 días</li>
<li>Espera: 48 horas despues de terminar</li>
<li>¿Apto para donar?: SÍ despues de esperar</li>
</ul>
<p><strong>Azitromicina (Z-pack, Zithromax):</strong></p>
<ul>
<li>Curso típico: 3-5 días</li>
<li>Espera: 48 horas despues de terminar (importante: es de acción prolongada)</li>
<li>¿Apto para donar?: SÍ despues de esperar</li>
</ul>
<p><strong>Doxiciclina:</strong></p>
<ul>
<li>Curso típico: 7-14 días</li>
<li>Espera: 48 horas despues de terminar</li>
<li>¿Apto para donar?: SÍ despues de esperar</li>
</ul>
<p><strong>Norma General:</strong> Termina el curso completo, siente que ya no tienes síntomas de infeccion, espera 2 días más.</p>
'''),
    ('Antibioticos que Requieren Diferimientos Mas Largos', '''
<p>Algunos antibioticos necesitan esperas mas largas debido a efectos secundarios o residuos prolongados:</p>
<ul>
<li><strong>Isotretinoina (Accutane):</strong> NO puedes donar durante el tratamiento ni 1 mes despues (riesgo de defectos de nacimiento si va a bancos de sangre reproductiiva)</li>
<li><strong>Fluoroquinolonas (levofloxacina, ciprofloxacina):</strong> Espera 72 horas despues de terminar</li>
<li><strong>Medicamentos tuberculosos:</strong> Diferimiento tipicamente por 12 meses despues de terminar tratamiento</li>
</ul>
<p>Siempre pregunta al personal del centro si tienes dudas sobre tu antibiotico específico.</p>
'''),
    ('Como Saber si tu Infeccion se Ha Resuelto', '''
<p>Antes de donar despues de antibioticos, asegurate de que:</p>
<ul>
<li><strong>Fiebre:</strong> Tu temperatura es normal (98.6°F / 37°C)</li>
<li><strong>Síntomas:</strong> Tos, sarpullido, secreción, o dolor han desaparecido</li>
<li><strong>Energia:</strong> Te sientes con energia normal, no agotado</li>
<li><strong>Tiempo:</strong> Han pasado al menos 48 horas desde tu última dosis de antibiotico</li>
</ul>
<p>Si aún tienes síntomas despues de terminar antibioticos, habla con tu médico. Podría haber una infeccion que requiere un curso diferente de medicamento.</p>
'''),
    ('Otros Antibioticos Comunes y Sus Diferimientos', '''
<p><strong>Penicilinas:</strong> Amoxicilina, ampicilina — 48 horas despues de terminar</p>
<p><strong>Cefalosporinas:</strong> Cephalexin, ceftriaxona — 48 horas despues de terminar</p>
<p><strong>Macrólidos:</strong> Azitromicina, eritromicina — 48 horas despues de terminar (azitromicina: 72 horas es mas seguro debido a acción prolongada)</p>
<p><strong>Sulfamidas:</strong> Septra, bactrim — 48 horas despues de terminar</p>
<p><strong>Nitrofurantoina:</strong> Para infecciones urinarias — 48 horas despues de terminar</p>
<p><strong>Lincosamidas:</strong> Clindamicina — 48 horas despues de terminar</p>
<p>Si tu antibiotico no está en esta lista, llamá a tu centro de plasma para preguntar sobre el diferimiento específico.</p>
'''),
]

page3_table = '''<table>
<thead><tr><th>Antibiotico</th><th>¿Apto para Donar?</th><th>Espera Despues de Terminar</th><th>Notas</th></tr></thead>
<tbody>
<tr><td>Amoxicilina</td><td>SÍ*</td><td>48 horas</td><td>Común para infecciones bacterianas</td></tr>
<tr><td>Azitromicina (Z-pack)</td><td>SÍ*</td><td>48-72 horas</td><td>Accion prolongada; espera mas para seguridad</td></tr>
<tr><td>Doxiciclina</td><td>SÍ*</td><td>48 horas</td><td>Comun para infecciones respiratorias</td></tr>
<tr><td>Cephalexin</td><td>SÍ*</td><td>48 horas</td><td>Cefalosporina segura</td></tr>
<tr><td>Fluoroquinolonas</td><td>SÍ*</td><td>72 horas</td><td>Levofloxacina, ciprofloxacina — espera mas</td></tr>
</tbody>
</table>
<p><strong>*SÍ solo despues de:</strong> Terminar curso completo + 48-72 horas sin el medicamento + sin síntomas de infeccion</p>'''

page3_related = [
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guia de Donacion'),
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Tarifas 2026'),
]

page3_faqs = [
    ('¿Cuanto tiempo debo esperar despues de terminar antibioticos?', 'Generalmente 48 horas despues de terminar tu última dosis. Para algunos antibioticos como azitromicina, espera 72 horas para mayor seguridad.'),
    ('¿Puedo donar plasma si aún estoy tomando antibioticos?', 'No. Debes terminar el curso completo y esperar el diferimiento antes de donar.'),
    ('¿Que pasa si doné plasma sin darme cuenta que aún tenía una infeccion activa?', 'Llamá a tu centro de plasma inmediatamente. El plasma se puede descartar si hay riesgo de contaminacion.'),
    ('¿Necesito un examen medico despues de terminar antibioticos?', 'No necesariamente para donar plasma. Solo asegurate de que tu infeccion se ha resuelto (sin fiebre, sin síntomas).'),
]

html3 = gen_medication_page(page3_slug, page3_title, page3_quick, page3_sections, page3_table, page3_related, page3_faqs)

# ============ PAGE 4: Corticosteroids ============
page4_slug = 'donar-plasma-con-esteroides-prednisona-2026'
page4_title = 'Donar Plasma con Esteroides (Prednisona): Guia de Eligibilidad 2026'
page4_quick = '''<strong>DEPENDE del tipo de esteroide.</strong> Los esteroides tópicos (cremas, ungüentos) son seguros — puedes donar sin restricciones. Los esteroides sistémicos (prednisona, dexametasona, metilprednisolona) requieren diferimientos mientras los tomes y a veces despues. Para condiciones autoinmunes graves, es mejor consultar con tu centro.'''

page4_sections = [
    ('Esteroides Topicos vs Sistemicos: Diferencia Crucial', '''
<p><strong>Esteroides Topicos:</strong></p>
<ul>
<li>Aplicaciones locales: cremas, ungüentos, sprays, inhaladores</li>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Ejemplos: Hidrocortisona, triamcinolona (aplicación cutánea)</li>
<li>Razon: Minima absorcion sistémica</li>
</ul>
<p><strong>Esteroides Sistemicos:</strong></p>
<ul>
<li>Medicamentos orales o inyectables que afectan todo el cuerpo</li>
<li>¿Apto para donar?: NO mientras tomes — diferimiento requerido</li>
<li>Ejemplos: Prednisona, dexametasona, metilprednisolona</li>
<li>Razon: Suprimen el sistema inmunologico, afectan células sanguíneas</li>
</ul>
<p>La diferencia es enorme. Asegurate de saber cual tipo tomas.</p>
'''),
    ('Prednisona: El Esteroide Sistemico Mas Comun', '''
<p>Prednisona es el esteroide sistémico más prescrito para:</p>
<ul>
<li>Artritis reumatoide y lupus</li>
<li>Asma grave</li>
<li>Reacciones alergicas severas</li>
<li>Inflamacion post-quirurgica</li>
<li>Enfermedad de Crohn y colitis ulcerosa</li>
</ul>
<p><strong>¿Puedo donar plasma si tomo prednisona?</strong></p>
<p>Mientras tomes prednisona, NO puedes donar. Los centros de plasma deben diferir a donantes en esteroides sistémicos porque:</p>
<ul>
<li>Suprimen los glóbulos blancos y linfocitos</li>
<li>Aumentan riesgo de infecciones secundarias</li>
<li>Afectan el conteo de plaquetas</li>
<li>Comprometen la integridad del plasma</li>
</ul>
<p><strong>Despues de terminar prednisona:</strong> Espera 2-4 semanas para que tu sistema inmunologico se recupere completamente.</p>
'''),
    ('Diferimiento para Esteroides Sistemicos', '''
<p><strong>Mientras tomas esteroides:</strong> Diferimiento completo — no puedes donar</p>
<p><strong>Despues de terminar esteroides:</strong></p>
<ul>
<li>Dosis bajas (5-20 mg): Espera 2 semanas</li>
<li>Dosis moderadas (20-50 mg): Espera 3-4 semanas</li>
<li>Dosis altas (50+ mg): Espera 4-6 semanas</li>
<li>Inyecciones intramusculares de esteroides: Espera 2-4 semanas segun dosis</li>
</ul>
<p>Esto permite que tu sistema inmunologico se recupere. El personal del centro puede ajustar estos tiempos.</p>
'''),
    ('Condiciones Autoinmunes y Donacion de Plasma', '''
<p>Si tienes una condicion autoinmune (lupus, artritis reumatoide, esclerosis multiple, etc.), la donacion de plasma puede ser complicada:</p>
<ul>
<li><strong>Mientras tomas esteroides:</strong> No puedes donar</li>
<li><strong>Si tu enfermedad es activa:</strong> Tu conteo de células puede estar bajo — te descalificaran</li>
<li><strong>Si ests en remision:</strong> Posiblemente puedas donar despues de esperar despues de esteroides</li>
<li><strong>Con terapias biologicas (TNF inhibidores):</strong> Diferentes reglas — consulta tu centro</li>
</ul>
<p>Es muy importante tener una conversacion completa con el personal medico del centro si tienes una condicion autoinmune.</p>
'''),
    ('Inhaladores de Esteroides para Asma: ¿Puedo Donar?', '''
<p><strong>Inhaladores de esteroides (beclometasona, fluticasona):</strong></p>
<ul>
<li>Aunque inyectados por inhalacion, absorben principalmente en los pulmones</li>
<li>Exposicion sistémica minima</li>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
</ul>
<p><strong>Inyecciones de esteroides para asma (triamcinolona):</strong></p>
<ul>
<li>Estas son inyecciones intramuscular es o IV, no inhaladas</li>
<li>Absorcion sistémica significativa</li>
<li>¿Apto para donar?: Espera 2-4 semanas despues de la inyeccion</li>
</ul>
<p>Pregunta a tu medico si tu "inyeccion de esteroides" es una inhalacion (segura) o una inyeccion intramuscular (diferimiento requerido).</p>
'''),
]

page4_table = '''<table>
<thead><tr><th>Tipo de Esteroide</th><th>¿Apto para Donar?</th><th>Diferimiento</th><th>Ejemplos</th></tr></thead>
<tbody>
<tr><td>Esteroides Topicos</td><td>SÍ</td><td>Ninguno</td><td>Crema de hidrocortisona, triamcinolona ungüento</td></tr>
<tr><td>Inhaladores de Esteroides</td><td>SÍ</td><td>Ninguno</td><td>Fluticasona, beclometasona (inhalada)</td></tr>
<tr><td>Prednisona Oral</td><td>NO *</td><td>2-6 semanas despues de terminar</td><td>Dosis: 5-80+ mg/día</td></tr>
<tr><td>Dexametasona</td><td>NO *</td><td>2-6 semanas despues de terminar</td><td>Potente; usado para inflamacion</td></tr>
<tr><td>Inyecciones IM de Esteroides</td><td>NO *</td><td>2-4 semanas despues de la inyeccion</td><td>Triamcinolona inyectada, metilprednisolona inyectada</td></tr>
</tbody>
</table>
<p><strong>* NO mientras tomes. Diferimiento requerido despues de terminar.</strong></p>'''

page4_related = [
    ('/es/blog/donar-plasma-con-autoinmunidad-2026.html', 'Condiciones Autoinmunes'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guia Completa'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos'),
]

page4_faqs = [
    ('¿Puedo donar plasma si tomo prednisona?', 'No, mientras tomes prednisona no puedes donar. Debes esperar 2-6 semanas despues de terminar, dependiendo de la dosis.'),
    ('¿Son seguros los inhaladores de esteroides para donar plasma?', 'Sí, los inhaladores de esteroides (para asma) son completamente seguros. Puedes donar sin restricciones.'),
    ('¿Que diferencia hay entre esteroides topicos y esteroides sistemicos?', 'Topicos (cremas) absorben localmente — seguro para donar. Sistemicos (pastillas, inyecciones) afectan todo el cuerpo — diferimiento requerido.'),
    ('¿Cuanto tiempo espero despues de una inyeccion de esteroides?', 'Generalmente 2-4 semanas despues de una inyeccion intramuscular de esteroides, dependiendo del tipo y dosis.'),
]

html4 = gen_medication_page(page4_slug, page4_title, page4_quick, page4_sections, page4_table, page4_related, page4_faqs)

# ============ PAGE 5: Oral Contraceptives ============
page5_slug = 'donar-plasma-con-anticonceptivos-pastillas-2026'
page5_title = 'Donar Plasma Tomando Anticonceptivos: Pastillas, DIU, Implantes 2026'
page5_quick = '''<strong>SÍ, puedes donar plasma</strong> si tomas anticonceptivos orales (pastillas anticonceptivas) o usas cualquier forma de anticoncepcion: DIU, implante, inyeccion, parches. Los anticonceptivos hormonales <strong>no descalifican</strong> para donar plasma y no requieren diferimientos.'''

page5_sections = [
    ('Tipos de Anticonceptivos y Donacion de Plasma', '''
<p><strong>Pastillas Anticonceptivas (Anticonceptivos Orales):</strong></p>
<ul>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Incluye: combinadas (estrógeno + progestina) y solo progestina (minipílulas)</li>
<li>Diferimiento: Ninguno requerido</li>
</ul>
<p><strong>DIU (Dispositivo Intrauterino):</strong></p>
<ul>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Incluye: Mirena, Kyleena, Skyla (hormonales), Paragard (cobre)</li>
<li>Diferimiento: Ninguno requerido</li>
</ul>
<p><strong>Implante (Nexplanon):</strong></p>
<ul>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Pequeño dispositivo en el brazo liberando progestina</li>
<li>Diferimiento: Ninguno requerido</li>
</ul>
<p><strong>Inyeccion (Depo-Provera):</strong></p>
<ul>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Inyeccion cada 3 meses</li>
<li>Diferimiento: Ninguno requerido</li>
</ul>
<p><strong>Parche (Ortho Evra):</strong></p>
<ul>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Parche semanal que libera hormona</li>
<li>Diferimiento: Ninguno requerido</li>
</ul>
<p>La conclusión: todos los metodos anticonceptivos hormonales y no-hormonales son seguros para donantes de plasma.</p>
'''),
    ('¿Por Que los Anticonceptivos No Afectan la Donacion de Plasma?', '''
<p>A diferencia de otros medicamentos, los anticonceptivos hormonales:</p>
<ul>
<li><strong>No afectan la produccion de plasma:</strong> El plasma es principalmente agua, proteinas, electrolitos — no es afectado por hormonas</li>
<li><strong>No suprimen el sistema inmunologico:</strong> Las dosis de hormonas en anticonceptivos son muy bajas</li>
<li><strong>No causan infecciones:</strong> No hay riesgo de patógenos transmitidos por sangre</li>
<li><strong>No afectan el conteo de células:</strong> Los glóbulos blancos y rojos permanecen en niveles normales</li>
<li><strong>No hay riesgo tromboembolico relevante:</strong> Aunque los anticonceptivos aumentan ligeramente el riesgo de coagulos, este riesgo es individual y no es una razon para diferir donantes de plasma</li>
</ul>
<p>La FDA ha revisado extensamente estos datos y declara que anticonceptivos son completamente seguros para donantes.</p>
'''),
    ('Mitos Sobre Anticonceptivos y Donacion de Sangre', '''
<p><strong>Mito 1: "Los anticonceptivos hacen que mi sangre sea mas gruesa"</strong></p>
<p>Verdad: Los anticonceptivos no aumentan significativamente la viscosidad del plasma. La donacion de plasma es generalmente segura.</p>
<p><strong>Mito 2: "El DIU me descalifica de donar"</strong></p>
<p>Verdad: Los DIU — sean hormonales o de cobre — no descalifican. Muchas donantes tienen DIU.</p>
<p><strong>Mito 3: "Necesito esperar despues de una inyeccion anticonceptiva"</strong></p>
<p>Verdad: Depo-Provera y otros anticonceptivos inyectados no requieren diferimientos. Puedes donar el mismo dia.</p>
<p><strong>Mito 4: "Los anticonceptivos hacen que el plasma sea de mala calidad"</strong></p>
<p>Verdad: Los anticonceptivos no afectan las proteinas vitales en el plasma. La calidad es normal.</p>
<p><strong>Mito 5: "Las mujeres fértiles no deben donar plasma"</strong></p>
<p>Verdad: Las mujeres en edad fértil, tomando anticonceptivos o no, son donantes excelentes. No hay diferencia en la calidad del plasma.</p>
'''),
    ('Anticonceptivos Especiales: Consideraciones Unicas', '''
<p><strong>Pastillas de Dosis Baja (microdosis):</strong></p>
<ul>
<li>Incluyen: Lo Loestrin, Yaz, Beyaz (dosis muy bajas de estrógeno)</li>
<li>¿Apto para donar?: SÍ, completamente seguro</li>
<li>Nota: Son aún mas seguras que pastillas convencionales debido a dosis mas baja</li>
</ul>
<p><strong>Anticonceptivos de Ciclo Extendido (Seasonale, Seasonique):</strong></p>
<ul>
<li>Tomas pastillas activas 12 semanas en lugar de 3 semanas</li>
<li>¿Apto para donar?: SÍ, sin restricciones</li>
<li>Nota: No hay diferencia en la seguridad de donacion</li>
</ul>
<p><strong>Anticonceptivos de Emergencia (Plan B, ella):</strong></p>
<ul>
<li>¿Apto para donar?: SÍ, despues de 48 horas</li>
<li>Diferimiento: Espera 2 días despues de tomar Plan B o ella</li>
<li>Razon: Es una dosis alta de hormona; dejar que se estabilice</li>
</ul>
<p><strong>Mifeprex (Medicamento para Aborto):</strong></p>
<ul>
<li>¿Apto para donar?: Diferimiento de 3-6 meses despues</li>
<li>Razon: Es importante permitir que el útero se recupere completamente</li>
</ul>
'''),
    ('Beneficios de Donar Plasma si Tomas Anticonceptivos', '''
<p>Si eres mujer tomando anticonceptivos y donante regular, tienes algunas ventajas únicas:</p>
<ul>
<li><strong>Ciclo de donacion predecible:</strong> Si tomas anticonceptivos, tu ciclo es regular — puedes planificar donaciones</li>
<li><strong>Menos efecto de períodos:</strong> Los anticonceptivos reducen cambios hormonales drasticos, lo que significa mejor consistencia de plasma</li>
<li><strong>Sin diferimientos por gravidez:</strong> Si estas en un anticonceptivo efectivo, no necesitas preocuparte por diferimientos por embarazo</li>
<li><strong>Mayor estabilidad:</strong> Tu hemoglobina y hematocrito tienden a ser mas estables con anticonceptivos regulares</li>
</ul>
<p>Los centros de plasma actualmente valoran altamente a donantes consistentes — y los anticonceptivos pueden ayudar a mantener esa consistencia.</p>
'''),
]

page5_table = '''<table>
<thead><tr><th>Tipo de Anticoncepcion</th><th>¿Apto para Donar?</th><th>Diferimiento</th><th>Notas</th></tr></thead>
<tbody>
<tr><td>Pastillas Anticonceptivas</td><td>SÍ</td><td>Ninguno</td><td>Combinadas o solo progestina — ambas seguras</td></tr>
<tr><td>DIU Hormonal (Mirena, Kyleena)</td><td>SÍ</td><td>Ninguno</td><td>Completamente seguro; bajo nivel hormonal</td></tr>
<tr><td>DIU de Cobre (Paragard)</td><td>SÍ</td><td>Ninguno</td><td>No hormonal; seguro para donar</td></tr>
<tr><td>Implante (Nexplanon)</td><td>SÍ</td><td>Ninguno</td><td>Libera progestina; completamente seguro</td></tr>
<tr><td>Inyeccion (Depo-Provera)</td><td>SÍ</td><td>Ninguno</td><td>Cada 3 meses; segura para donantes</td></tr>
<tr><td>Parche (Ortho Evra)</td><td>SÍ</td><td>Ninguno</td><td>Semanal; seguro para donar</td></tr>
<tr><td>Anillo Vaginal (NuvaRing)</td><td>SÍ</td><td>Ninguno</td><td>Mensual; completamente seguro</td></tr>
</tbody>
</table>'''

page5_related = [
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Tarifas de Donacion 2026'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guia Completa'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos'),
]

page5_faqs = [
    ('¿Puedo donar plasma si estoy tomando pastillas anticonceptivas?', 'Sí, completamente. Las pastillas anticonceptivas no descalifican para donar plasma.'),
    ('¿El DIU me impide donar plasma?', 'No. Tanto los DIU hormonales como los de cobre son seguros para donantes de plasma.'),
    ('¿Debo esperar despues de una inyeccion de Depo-Provera para donar?', 'No. Puedes donar el mismo dia o cualquier dia despues de tu inyeccion de Depo-Provera.'),
    ('¿Los anticonceptivos afectan la calidad del plasma que doné?', 'No. Los anticonceptivos no afectan la calidad del plasma. Tu plasma es tan valido como el de cualquier otro donante.'),
]

html5 = gen_medication_page(page5_slug, page5_title, page5_quick, page5_sections, page5_table, page5_related, page5_faqs)


# ============ WRITE ALL FILES ============
if __name__ == '__main__':
    print("Generating Batch: Spanish medication blog pages (5 pages)...")
    count = 0

    # Ensure directory exists
    os.makedirs(ES_BLOG_DIR, exist_ok=True)

    # Write all 5 pages
    pages = [
        (page1_slug, html1),
        (page2_slug, html2),
        (page3_slug, html3),
        (page4_slug, html4),
        (page5_slug, html5),
    ]

    for slug, html in pages:
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1

    print(f"\nDone! Generated {count} Spanish medication blog pages.")
    print(f"Location: {ES_BLOG_DIR}/")
