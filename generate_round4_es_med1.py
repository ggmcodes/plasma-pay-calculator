#!/usr/bin/env python3
"""Generate 5 Spanish medication blog pages for plasma donation eligibility"""
import os
from generate_batch5_spanish_template import make_es_page, make_faq, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ES_BLOG_DIR = os.path.join(BASE_DIR, 'es', 'blog')

def gen_medication_page_1():
    """Donar plasma con insulina (diabetes)"""
    slug = 'donar-plasma-con-insulina-diabetes-2026'
    title = 'Donar Plasma con Insulina (Diabetes Tipo 1 y 2) 2026'
    meta_desc = 'Puedes donar plasma con insulina? Guia completa sobre diabetes, A1C, glucosa, bombas de insulina y CGM. Requisitos y recomendaciones para donantes diabeticos 2026.'
    category = 'Medicamentos y Elegibilidad'
    read_time = 9
    toc_items = [
        ('respuesta', 'Respuesta Rapida'),
        ('insulina', 'Tipos de Insulina'),
        ('requisitos', 'Requisitos de A1C y Glucosa'),
        ('bombas', 'Bombas y CGM'),
        ('consejos', 'Consejos para Donantes'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content_html = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rapida: SÍ con Condiciones</h3>
    <p><strong>¿Puedo donar plasma con insulina?</strong> SÍ, pero con restricciones basadas en control de diabetes. Tu A1C debe ser menor de 9%, glucosa en ayunas 100-250 mg/dL, y debes estar estable en insulina por al menos 3 meses. Centros como CSL Plasma, BioLife y Octapharma permiten donantes diabeticos controlados.</p>
</div>

<h2 id="insulina">Tipos de Insulina y Donacion</h2>
<p>Los diferentes tipos de insulina no descalifican la donacion, pero requieren mayor control:</p>

<table>
<thead>
<tr>
<th>Tipo de Insulina</th>
<th>Velocidad</th>
<th>Donacion Permitida</th>
<th>Notas</th>
</tr>
</thead>
<tbody>
<tr>
<td>Insulina Rapida (Humalog, Novolog)</td>
<td>15-30 minutos</td>
<td>SÍ con A1C &lt;9%</td>
<td>Requiere monitoreo frecuente antes de donar</td>
</tr>
<tr>
<td>Insulina de Accion Intermedia (NPH)</td>
<td>2-4 horas</td>
<td>SÍ con A1C &lt;9%</td>
<td>Estable, buen candidato para donacion</td>
</tr>
<tr>
<td>Insulina de Accion Prolongada (Lantus, Tresiba)</td>
<td>12-24 horas</td>
<td>SÍ con A1C &lt;9%</td>
<td>Mejor opcion para donantes regulares</td>
</tr>
<tr>
<td>Insulina Inhalada (Afrezza)</td>
<td>12-15 minutos</td>
<td>SÍ con A1C &lt;9%</td>
<td>Menos comun, mismos requisitos</td>
</tr>
</tbody>
</table>

{AFFILIATE_ES}

<h2 id="requisitos">Requisitos de A1C y Glucosa Sanguinea</h2>
<p>Los centros de plasma tienen criterios especificos para donantes diabeticos:</p>

<h3>Hemoglobina A1C (HbA1c)</h3>
<ul>
<li><strong>Menor de 7%:</strong> Excelente control, donacion sin restricciones</li>
<li><strong>7% a 9%:</strong> Buen control, donacion permitida</li>
<li><strong>Mayor de 9%:</strong> Control insuficiente, puede ser rechazado</li>
</ul>

<h3>Glucosa en Ayunas</h3>
<ul>
<li><strong>70-100 mg/dL:</strong> Normal, ideal para donacion</li>
<li><strong>100-150 mg/dL:</strong> Aceptable el dia de la donacion</li>
<li><strong>150-250 mg/dL:</strong> Permitido con aprobacion medica</li>
<li><strong>Mayor de 250 mg/dL:</strong> Rechazado, riesgo de complicaciones</li>
</ul>

<h3>Glucosa al Azar</h3>
<table>
<thead>
<tr>
<th>Rango</th>
<th>Estado</th>
<th>Donacion Permitida</th>
</tr>
</thead>
<tbody>
<tr>
<td>&lt;140 mg/dL</td>
<td>Normal</td>
<td>SÍ</td>
</tr>
<tr>
<td>140-250 mg/dL</td>
<td>Elevada pero estable</td>
<td>SÍ con aprobacion</td>
</tr>
<tr>
<td>&gt;250 mg/dL</td>
<td>Muy elevada</td>
<td>NO</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT_ES}

<h2 id="bombas">Bombas de Insulina y Sistemas CGM</h2>
<p>Muchos donantes usan tecnologia avanzada para controlar su diabetes:</p>

<h3>Bombas de Insulina (Insulin Pumps)</h3>
<ul>
<li><strong>Medtronic, Tandem, Omnipod:</strong> Permitidas en centros de plasma</li>
<li><strong>Consideracion:</strong> El personal medico debe revisar la bomba antes de la flebotomia</li>
<li><strong>Ventaja:</strong> Mejor control de glucosa = mas probabilidades de aprobacion</li>
<li><strong>Riesgo:</strong> La bomba no debe interferir con acceso venoso en el brazo</li>
</ul>

<h3>Monitores Continuos de Glucosa (CGM)</h3>
<ul>
<li><strong>Freestyle Libre, Dexcom, Medtronic Guardian:</strong> Recomendados para donantes</li>
<li><strong>Beneficio:</strong> Datos en tiempo real para monitoreo pre-donacion</li>
<li><strong>Ventaja para centros:</strong> Menos riesgo de hipoglucemia durante/despues</li>
<li><strong>Requisito:</strong> Algunos centros piden datos de CGM de ultimas 2 semanas</li>
</ul>

<h2 id="consejos">Consejos para Donantes Diabeticos</h2>
<h3>Antes de la Donacion</h3>
<ol>
<li><strong>Verifica tu glucosa:</strong> 2 horas antes, debe estar 100-200 mg/dL</li>
<li><strong>Come bien:</strong> Comida rica en proteina y carbohidratos complejos 2-3 horas antes</li>
<li><strong>Hidratate:</strong> 64+ oz de agua el dia anterior y manana de donacion</li>
<li><strong>Lleva glucometro:</strong> Por si necesitas verificar durante espera</li>
<li><strong>Informa al personal:</strong> Sobre tu diabetes, tipo de insulina y ultimos valores de A1C</li>
</ol>

<h3>Durante la Donacion</h3>
<ul>
<li>Comunica cualquier sensacion de mareo, sudoracion o debilidad inmediatamente</li>
<li>Si usas bomba, coordina con personal para colocacion segura</li>
<li>Mantente hidratado durante el proceso (45-90 minutos)</li>
<li>Toma descansos si sientes sintomas de hipoglucemia</li>
</ul>

<h3>Despues de la Donacion</h3>
<ol>
<li>Come y bebe inmediatamente despues (jugo + snack de carbohidratos)</li>
<li>Monitorea glucosa cada 30 minutos durante 2 horas</li>
<li>Revisa tu insulina (puede necesitar ajuste tras perdida de plasma)</li>
<li>Descansa lo suficiente - evita ejercicio intenso por 24 horas</li>
<li>Reporta cualquier hipoglucemia al centro medico</li>
</ol>

{related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar Plasma 2026'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos de Donacion'),
    ('/es/blog/medicamentos-prohibidos-donacion-plasma.html', 'Medicamentos Prohibidos'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Mi diabetes descalifica mi donacion de plasma?</h3>
<p>No necesariamente. Si tu diabetes esta bien controlada (A1C &lt;9%, glucosa 100-250 mg/dL), puedes donar. Centros como CSL Plasma y BioLife aceptan donantes diabeticos. Lo importante es control consistente.</p>

<h3>¿Que A1C necesito para donar plasma?</h3>
<p>Necesitas A1C menor de 9% para la mayoria de centros. Si es menor de 7%, tienes mejor probabilidad de aprobacion inmediata. Valores entre 7-9% requieren aprobacion del medico del centro.</p>

<h3>¿Puedo donar con bomba de insulina?</h3>
<p>Sí, muchos donantes usan bombas Medtronic, Tandem u Omnipod. El personal medico reviara la bomba para asegurar no interfiera con acceso venoso. La bomba debe ser removida o reposicionada segun protocolo del centro.</p>

<h3>¿Que pasa si tengo hipoglucemia durante la donacion?</h3>
<p>Notifica inmediatamente al personal. El proceso se detiene, te dan jugo o carbohidratos rapidos, y monitorizan tu recuperacion. Muchos centros tienen dextrosa IV disponible. Es raro pero importante comunicar tus sintomas.</p>
'''

    faq_schema = [
        make_faq("¿Puedo donar plasma si tengo diabetes?", "Sí, si tu diabetes está bien controlada con A1C menor de 9% y glucosa 100-250 mg/dL. Centros como CSL Plasma aceptan donantes diabeticos."),
        make_faq("¿Qué A1C necesito para donar plasma?", "Necesitas A1C menor de 9%. Menor de 7% es ideal. Valores entre 7-9% requieren aprobación médica."),
        make_faq("¿Puedo donar con insulina?", "Sí, todos los tipos de insulina (rápida, intermedia, prolongada) son permitidos si tu diabetes está controlada."),
        make_faq("¿Puedo donar con bomba de insulina?", "Sí, las bombas (Medtronic, Tandem, Omnipod) son permitidas. El personal médico las revisará antes de la flebotomía."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema)


def gen_medication_page_2():
    """Donar plasma con metformina"""
    slug = 'donar-plasma-con-metformina-2026'
    title = 'Donar Plasma con Metformina 2026: Guia Completa'
    meta_desc = 'Puedes donar plasma si tomas metformina para diabetes tipo 2? Sí, sin diferimiento. Información sobre efectos gastrointestinales y recomendaciones 2026.'
    category = 'Medicamentos y Elegibilidad'
    read_time = 9
    toc_items = [
        ('respuesta', 'Respuesta Rapida'),
        ('metformina', 'Que es Metformina'),
        ('donacion', 'Donacion y Metformina'),
        ('efectos', 'Efectos Gastrointestinales'),
        ('consejos', 'Consejos Practicos'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content_html = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rapida: SÍ</h3>
    <p><strong>¿Puedo donar plasma si tomo metformina?</strong> SÍ. La metformina no descalifica donantes. No hay periodo de diferimiento. Los centros de plasma (CSL Plasma, BioLife, Octapharma, Grifols) aceptan donantes que toman metformina siempre que controlen bien su diabetes tipo 2.</p>
</div>

<h2 id="metformina">Que es Metformina y Como Funciona</h2>
<p>La metformina es el medicamento mas comun para diabetes tipo 2:</p>

<h3>Informacion Basica</h3>
<ul>
<li><strong>Tipo:</strong> Medicamento antidiabetico oral (biguanida)</li>
<li><strong>Nombres Comerciales:</strong> Glucophage, Glumetza, Fortamet, Riomet</li>
<li><strong>Funcion:</strong> Reduce produccion de glucosa en higado y mejora sensibilidad a insulina</li>
<li><strong>Dosis Tipica:</strong> 500-2,550 mg diarios dividido en 2-3 dosis</li>
<li><strong>Presentaciones:</strong> Tabletas, tabletas extendidas, liquido</li>
</ul>

<h3>Marcas Genericas vs Marcas</h3>
<table>
<thead>
<tr>
<th>Marca</th>
<th>Tipo</th>
<th>Donacion Permitida</th>
</tr>
</thead>
<tbody>
<tr>
<td>Glucophage (Merck)</td>
<td>Marca original</td>
<td>SÍ</td>
</tr>
<tr>
<td>Glumetza (Noven)</td>
<td>Liberacion extendida</td>
<td>SÍ</td>
</tr>
<tr>
<td>Metformina Generica</td>
<td>Clorhidrato de metformina</td>
<td>SÍ</td>
</tr>
<tr>
<td>Fortamet</td>
<td>Liberacion extendida</td>
<td>SÍ</td>
</tr>
</tbody>
</table>

{AFFILIATE_ES}

<h2 id="donacion">Donacion de Plasma y Metformina</h2>
<p>La metformina se considera completamente compatible con donacion de plasma:</p>

<h3>Razones por las que es Permitida</h3>
<ul>
<li><strong>No interfiere con donacion:</strong> La metformina se metaboliza en el higado, no afecta plasma</li>
<li><strong>Sin diferimiento:</strong> Puedes donar mismo dia que tomas metformina</li>
<li><strong>Sin restricciones:</strong> Frecuencia de donacion es la misma (2 veces/semana)</li>
<li><strong>Seguridad:</strong> No aumenta riesgo de complicaciones durante/despues donacion</li>
</ul>

<h3>Requisitos Previos a Donacion</h3>
<ul>
<li>A1C menor de 9% (mismo que otros donantes diabeticos)</li>
<li>Glucosa en ayunas 100-250 mg/dL el dia de donacion</li>
<li>Presion arterial normal (&lt;180/120)</li>
<li>Hematocrito adecuado (tipicamente &gt;38%)</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="efectos">Efectos Gastrointestinales y Donacion</h2>
<p>Un efecto secundario comun de metformina es molestia gastrointestinal:</p>

<h3>Efectos Secundarios Comunes</h3>
<ul>
<li><strong>Nausea:</strong> 26% de usuarios (usualmente temporal)</li>
<li><strong>Diarrea:</strong> 17% de usuarios (mejora con liberacion extendida)</li>
<li><strong>Dolor abdominal:</strong> 12% de usuarios</li>
<li><strong>Sabor metalico:</strong> Comun pero no peligroso para donacion</li>
</ul>

<h3>Estrategias para Minimizar Problemas en Donacion</h3>
<ol>
<li><strong>Toma metformina con comidas:</strong> Reduce efectos GI significativamente</li>
<li><strong>Come ligero antes de donar:</strong> Evita comidas grasosas 4 horas antes</li>
<li><strong>Hidratacion:</strong> 64+ oz de agua el dia anterior ayuda con digestion</li>
<li><strong>Si tienes diarrea:</strong> Puedes seguir donando - no es contraindicacion</li>
<li><strong>Informa al personal:</strong> Diles si tienes efectos GI para mejor monitoreo</li>
</ol>

<h3>Cuando Posponer Donacion</h3>
<ul>
<li>Nausea severa o vomito el dia de donacion</li>
<li>Diarrea severa con deshidratacion evidente</li>
<li>Dolor abdominal intenso que afecte concentracion</li>
<li>Estos casos son raros con uso prolongado de metformina</li>
</ul>

<h2 id="consejos">Consejos Practicos para Donantes con Metformina</h2>

<h3>Antes de tu Primer Donacion</h3>
<ol>
<li>Informa al personal que tomas metformina - es comun y bien conocido</li>
<li>Lleva lista completa de medicamentos (incluyendo dosis de metformina)</li>
<li>Trae prueba de diagnos tico de diabetes (receta o carta medica)</li>
<li>Verifica tu A1C con tu doctor antes de ir (debes tener registros)</li>
</ol>

<h3>Dia de Donacion</h3>
<ul>
<li>Toma tu metformina normal a la hora habitual</li>
<li>Come desayuno con proteina 2-3 horas antes de donacion</li>
<li>Toma mucha agua pero no demasiado liquido azucarado</li>
<li>Lleva snacks de proteina para despues (nueces, queso, barras proteina)</li>
<li>Si tienes efectos GI, no te alarmes - sigue proceso normal</li>
</ul>

<h3>Despues de Donacion</h3>
<ul>
<li>Come algo ligero y proteico inmediatamente</li>
<li>Si sientes nausea post-donacion, pide a personal asistencia</li>
<li>No cambies tu dosis de metformina por la donacion</li>
<li>Si tienes diarrea post-donacion, aumenta hidratacion</li>
<li>Descansa bien - combinacion de metformina + donacion requiere recuperacion</li>
</ul>

{related_es([
    ('/es/blog/medicamentos-permitidos-donacion-plasma.html', 'Medicamentos Permitidos para Donar'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos de Donacion'),
    ('/es/blog/donar-plasma-con-insulina-diabetes-2026.html', 'Donar con Insulina'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Puedo donar plasma si tomo metformina?</h3>
<p>Sí, absolutamente. La metformina no es razón para diferimiento. Puedes donar el mismo día que tomas metformina. Los centros como CSL Plasma, BioLife y Octapharma aceptan donantes que toman metformina.</p>

<h3>¿La metformina afecta la calidad de plasma?</h3>
<p>No. La metformina se metaboliza en el hígado y no afecta la composición o calidad del plasma. Tus donaciones serán aceptadas sin problemas.</p>

<h3>¿Tengo que parar metformina para donar?</h3>
<p>No. Continúa tu dosis normal. No hay necesidad de cambiar tu medicamento. De hecho, mantener tu metformina es importante para control de glucosa durante/después donación.</p>

<h3>¿Qué hago si tengo diarrea por metformina?</h3>
<p>Puedes seguir donando a menos que sea severa con deshidratación. Bebe más agua. Si es grave el día de donación, puedes posponer. Muchos donantes usan metformina de liberación extendida que causa menos diarrea.</p>
'''

    faq_schema = [
        make_faq("¿Puedo donar plasma si tomo metformina?", "Sí, sin restricciones. La metformina no descalifica donantes. Puedes donar el mismo día que tomas metformina."),
        make_faq("¿La metformina afecta la calidad del plasma?", "No. La metformina se metaboliza en el hígado y no afecta el plasma. Tus donaciones serán aceptadas normalmente."),
        make_faq("¿Tengo que dejar de tomar metformina?", "No. Continúa tu dosis normal. No hay necesidad de cambiar tu medicamento."),
        make_faq("¿Qué tipo de metformina es mejor para donantes?", "Metformina de liberación extendida (Glumetza, Fortamet) causa menos efectos GI que la versión inmediata."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema)


def gen_medication_page_3():
    """Donar plasma con ibuprofeno y antiinflamatorios"""
    slug = 'donar-plasma-con-ibuprofeno-antiinflamatorios-2026'
    title = 'Donar Plasma con Ibuprofeno y Antiinflamatorios 2026'
    meta_desc = 'Puedes donar plasma si tomas ibuprofeno, aspirina o naproxeno? Sí, con restricciones. Guia sobre tiempos de espera y medicamentos antiinflamatorios 2026.'
    category = 'Medicamentos y Elegibilidad'
    read_time = 9
    toc_items = [
        ('respuesta', 'Respuesta Rapida'),
        ('ibuprofeno', 'Ibuprofeno y Donacion'),
        ('aspirina', 'Aspirina - 48h Espera'),
        ('naproxeno', 'Naproxeno y Otros AINE'),
        ('recomendaciones', 'Recomendaciones'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content_html = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rapida: SÍ (Con Restricciones)</h3>
    <p><strong>¿Puedo donar plasma si tomo ibuprofeno?</strong> SÍ - Ibuprofeno (Advil, Motrin) es permitido sin espera. <strong>Aspirina?</strong> SÍ pero espera 48 horas desde ultima dosis. <strong>Naproxeno (Aleve)?</strong> SÍ sin espera. Los centros aceptan donantes que toman AINE comunes.</p>
</div>

<h2 id="ibuprofeno">Ibuprofeno y Donacion de Plasma</h2>
<p>El ibuprofeno es el AINE mas comun y completamente compatible con donacion:</p>

<h3>Informacion del Ibuprofeno</h3>
<ul>
<li><strong>Nombres Comerciales:</strong> Advil, Motrin, Ibuprofen generico</li>
<li><strong>Tipo:</strong> AINE (Antiinflamatorio no esteroideo)</li>
<li><strong>Dosis Tipica:</strong> 200-800 mg cada 4-6 horas</li>
<li><strong>Donacion:</strong> SÍ, sin periodo de espera</li>
<li><strong>Vida Media:</strong> 1.8-2 horas - sale del cuerpo rapidamente</li>
</ul>

<h3>Tabla de Compatibilidad</h3>
<table>
<thead>
<tr>
<th>AINE</th>
<th>Donacion Permitida</th>
<th>Espera Requerida</th>
<th>Notas</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ibuprofeno (Advil, Motrin)</td>
<td>SÍ</td>
<td>Ninguna</td>
<td>Puedes donar mismo dia que tomas dosis</td>
</tr>
<tr>
<td>Naproxeno (Aleve, Naprosyn)</td>
<td>SÍ</td>
<td>Ninguna</td>
<td>Vida media 12-17 horas, pero permitido</td>
</tr>
<tr>
<td>Acetaminofen (Tylenol)</td>
<td>SÍ</td>
<td>Ninguna</td>
<td>No es AINE pero permitido</td>
</tr>
<tr>
<td>Indometacina (Indocin)</td>
<td>SÍ</td>
<td>Ninguna</td>
<td>AINE mas fuerte, permitido</td>
</tr>
<tr>
<td>Ketoprofeno (Orudis)</td>
<td>SÍ</td>
<td>Ninguna</td>
<td>Raro pero permitido</td>
</tr>
</tbody>
</table>

{AFFILIATE_ES}

<h2 id="aspirina">Aspirina - Regla de 48 Horas</h2>
<p>La aspirina tiene restriccion especial por su efecto anticoagulante:</p>

<h3>Por Que Aspirina Requiere Espera</h3>
<ul>
<li><strong>Mecanismo:</strong> La aspirina inhibe agregacion plaquetaria (delgadiza sangre)</li>
<li><strong>Riesgo:</strong> Mayor sangrado durante puncion venosa y despues</li>
<li><strong>Duracion:</strong> El efecto persiste 48-72 horas despues de ultima dosis</li>
<li><strong>Requisito:</strong> La mayoria de centros piden espera de 48 horas minimo</li>
</ul>

<h3>Directrices de Aspirina</h3>
<ul>
<li><strong>Aspirina de dosis baja (81 mg):</strong> Espera 48 horas</li>
<li><strong>Aspirina regular (325-500 mg):</strong> Espera 48 horas</li>
<li><strong>Dosis unica de aspirina:</strong> Espera 48 horas desde toma</li>
<li><strong>Aspirina diaria cronica:</strong> Algunos centros permiten, otros piden 48h entre donacion y ultima dosis</li>
</ul>

<h3>Ejemplo Timeline</h3>
<ul>
<li>Lunes 10am: Tomas aspirina</li>
<li>Martes 10am: Aun dentro de 48 horas - NO DONAR</li>
<li>Martes 10:01pm: Pasadas 48 horas - PUEDES DONAR</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="naproxeno">Naproxeno y Otros AINE</h2>
<p>El naproxeno es permitido sin periodo de espera a diferencia de aspirina:</p>

<h3>Naproxeno (Aleve)</h3>
<ul>
<li><strong>Presentacion:</strong> Naproxen de liberacion inmediata o extendida</li>
<li><strong>Dosis Tipica:</strong> 220-500 mg cada 8-12 horas</li>
<li><strong>Donacion:</strong> SÍ, sin espera</li>
<li><strong>Ventaja:</strong> Vida media mas larga (12-17 hrs) pero no requiere espera como aspirina</li>
<li><strong>Nota:</strong> Verifica siempre con centro local - algunos tienen politicas estrictas</li>
</ul>

<h3>Otros AINE Permitidos</h3>
<table>
<thead>
<tr>
<th>Medicamento</th>
<th>Marca</th>
<th>Donacion</th>
<th>Espera</th>
</tr>
</thead>
<tbody>
<tr>
<td>Diclofenac</td>
<td>Voltaren, Cataflam</td>
<td>SÍ</td>
<td>Ninguna</td>
</tr>
<tr>
<td>Meloxicam</td>
<td>Mobic</td>
<td>SÍ</td>
<td>Ninguna</td>
</tr>
<tr>
<td>Piroxicam</td>
<td>Feldene</td>
<td>SÍ</td>
<td>Ninguna</td>
</tr>
<tr>
<td>Indomethacin</td>
<td>Indocin</td>
<td>SÍ</td>
<td>Ninguna</td>
</tr>
</tbody>
</table>

<h2 id="recomendaciones">Recomendaciones Practicas</h2>

<h3>Si Tomas Ibuprofeno Regularmente</h3>
<ol>
<li>Puedes donar sin cambiar tu medicamento</li>
<li>Informa al personal que tomas ibuprofeno</li>
<li>No hay periodo de espera requerido</li>
<li>Puedes donar 2 veces por semana normalmente</li>
</ol>

<h3>Si Tomas Aspirina</h3>
<ol>
<li>Espera minimo 48 horas desde ultima dosis</li>
<li>Planifica donaciones considerando este tiempo de espera</li>
<li>Si tomas aspirina diaria por corazon, consulta tu doctor y el centro</li>
<li>Algunos centros permiten con documentacion medica</li>
</ol>

<h3>Si Tomas Naproxeno (Aleve)</h3>
<ol>
<li>Puedes donar sin espera</li>
<li>Informa al personal sobre uso de Aleve</li>
<li>Similar a ibuprofeno - sin restriccion temporal</li>
</ol>

<h3>Alternativas a AINE Antes de Donar</h3>
<ul>
<li><strong>En lugar de aspirina:</strong> Usa acetaminofen (Tylenol) o ibuprofeno 48h antes</li>
<li><strong>Para dolor:</strong> Acetaminofen es buena alternativa sin restriccion</li>
<li><strong>Para inflamacion:</strong> Ibuprofeno sin periodo de espera</li>
</ul>

{related_es([
    ('/es/blog/medicamentos-prohibidos-donacion-plasma.html', 'Medicamentos Prohibidos'),
    ('/es/blog/medicamentos-permitidos-donacion-plasma.html', 'Medicamentos Permitidos'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos de Donacion'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Puedo donar plasma si tomo ibuprofeno?</h3>
<p>Sí, puedes donar. No hay periodo de espera. El ibuprofeno (Advil, Motrin) es permitido y no afecta la donación.</p>

<h3>¿Necesito esperar después de tomar aspirina?</h3>
<p>Sí, necesitas esperar 48 horas desde la última dosis de aspirina antes de donar. La aspirina afecta la coagulación por eso requiere este tiempo de espera.</p>

<h3>¿Puedo donar si tomo Aleve (naproxeno)?</h3>
<p>Sí, sin periodo de espera. El naproxeno es permitido sin restricción temporal, a diferencia de la aspirina.</p>

<h3>¿Qué medicamento puedo tomar para dolor si dono regularmente?</h3>
<p>Ibuprofeno (Advil, Motrin) o acetaminofen (Tylenol) son las mejores opciones. Ibuprofeno es especialmente bueno porque no requiere espera.</p>
'''

    faq_schema = [
        make_faq("¿Puedo donar plasma si tomo ibuprofeno?", "Sí, sin espera. El ibuprofeno es permitido el mismo día de donación."),
        make_faq("¿Necesito esperar después de aspirina?", "Sí, necesitas esperar 48 horas mínimo desde la última dosis de aspirina."),
        make_faq("¿Puedo donar si tomo Aleve (naproxeno)?", "Sí, sin espera. El naproxeno es permitido sin restricción temporal."),
        make_faq("¿Qué medicamento es mejor para donantes?", "Ibuprofeno es la mejor opción para donantes frecuentes - no requiere espera."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema)


def gen_medication_page_4():
    """Donar plasma con antihipertensivos"""
    slug = 'donar-plasma-con-antihipertensivos-2026'
    title = 'Donar Plasma con Antihipertensivos 2026: Lisinopril, Losartan, Amlodipino'
    meta_desc = 'Puedes donar plasma si tomas presión arterial medicamentos? Sí. Información sobre lisinopril, losartan, amlodipino, metoprolol y requisitos de presión 2026.'
    category = 'Medicamentos y Elegibilidad'
    read_time = 9
    toc_items = [
        ('respuesta', 'Respuesta Rapida'),
        ('antihipertensivos', 'Medicamentos Antihipertensivos'),
        ('tipos', 'Tipos Permitidos'),
        ('presion', 'Requisitos de Presion Arterial'),
        ('consejos', 'Consejos para Donantes'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content_html = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rapida: SÍ</h3>
    <p><strong>¿Puedo donar plasma si tomo medicamentos para la presion?</strong> SÍ. Medicamentos como lisinopril, losartan, amlodipino y metoprolol son completamente permitidos. Centros como CSL Plasma, BioLife y Octapharma aceptan donantes en tratamiento de hipertension controlada. No hay periodo de espera.</p>
</div>

<h2 id="antihipertensivos">Medicamentos Antihipertensivos y Donacion</h2>
<p>Los medicamentos para la presion arterial son seguros y recomendados para donantes:</p>

<h3>Por Que Son Permitidos</h3>
<ul>
<li><strong>No afectan plasma:</strong> Los antihipertensivos no cambian composicion del plasma</li>
<li><strong>Sin interferencia:</strong> No interfieren con proceso de donacion</li>
<li><strong>Mejora seguridad:</strong> Presion controlada es mas segura durante donacion</li>
<li><strong>Sin diferimiento:</strong> Puedes donar el mismo dia que tomas medicamento</li>
</ul>

<h3>Medicamentos Comunes Permitidos</h3>
<table>
<thead>
<tr>
<th>Tipo</th>
<th>Medicamento</th>
<th>Marca</th>
<th>Donacion</th>
</tr>
</thead>
<tbody>
<tr>
<td>ACE Inhibitor</td>
<td>Lisinopril</td>
<td>Prinivil, Zestril</td>
<td>SÍ</td>
</tr>
<tr>
<td>ACE Inhibitor</td>
<td>Enalapril</td>
<td>Vasotec</td>
<td>SÍ</td>
</tr>
<tr>
<td>ARB</td>
<td>Losartan</td>
<td>Cozaar</td>
<td>SÍ</td>
</tr>
<tr>
<td>ARB</td>
<td>Valsartan</td>
<td>Diovan</td>
<td>SÍ</td>
</tr>
<tr>
<td>Bloqueador de Canal de Calcio</td>
<td>Amlodipino</td>
<td>Norvasc</td>
<td>SÍ</td>
</tr>
<tr>
<td>Beta Bloqueador</td>
<td>Metoprolol</td>
<td>Lopressor, Toprol-XL</td>
<td>SÍ</td>
</tr>
<tr>
<td>Diuretico</td>
<td>Hidrocloro tiazida</td>
<td>HCTZ, Microzide</td>
<td>SÍ</td>
</tr>
</tbody>
</table>

{AFFILIATE_ES}

<h2 id="tipos">Tipos de Antihipertensivos Permitidos</h2>

<h3>Inhibidores ACE (ACE Inhibitors)</h3>
<p><strong>Ejemplos:</strong> Lisinopril (Prinivil), Enalapril (Vasotec), Ramipril (Altace)</p>
<ul>
<li>Completamente permitidos para donacion</li>
<li>Entre los antihipertensivos mas comunes</li>
<li>Sin restriccion de tiempo entre dosis y donacion</li>
<li>Donantes pueden ser muy activos</li>
</ul>

<h3>Antagonistas del Receptor de Angiotensina (ARBs)</h3>
<p><strong>Ejemplos:</strong> Losartan (Cozaar), Valsartan (Diovan), Irbesartan (Avapro)</p>
<ul>
<li>Permitidos sin restricciones</li>
<li>Alternativa a ACE inhibitors</li>
<li>Generalmente mejor tolerados (menos tos)</li>
<li>Seguros para donacion frecuente</li>
</ul>

<h3>Bloqueadores de Canal de Calcio</h3>
<p><strong>Ejemplos:</strong> Amlodipino (Norvasc), Diltiazem, Verapamilo</p>
<ul>
<li>Totalmente permitidos</li>
<li>Buen perfil de efectos secundarios</li>
<li>Seguros con donacion regular</li>
<li>No afectan composicion sanguinea</li>
</ul>

<h3>Beta Bloqueadores</h3>
<p><strong>Ejemplos:</strong> Metoprolol (Lopressor), Atenolol (Tenormin), Propranolol</p>
<ul>
<li>Permitidos para donacion</li>
<li>Pueden causar fatiga - toma en cuenta para recuperacion</li>
<li>Sin periodo de espera</li>
<li>Importante mantenerse hidratado durante donacion</li>
</ul>

<h3>Diureticos</h3>
<p><strong>Ejemplos:</strong> Hidroclorotiazida (HCTZ), Furosemida (Lasix), Torsemida</p>
<ul>
<li>Permitidos con extra hidratacion</li>
<li>Aumenta importancia de beber agua antes/despues</li>
<li>Puede causar desequilibrio de electrolitos - informa al personal</li>
<li>Come alimentos ricos en potasio (platano, espinaca)</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="presion">Requisitos de Presion Arterial</h2>
<p>Los centros tienen limites de presion para donacion segura:</p>

<h3>Presion Arterial Ideal para Donacion</h3>
<table>
<thead>
<tr>
<th>Sistolica</th>
<th>Diastolica</th>
<th>Estado</th>
<th>Puedo Donar</th>
</tr>
</thead>
<tbody>
<tr>
<td>&lt;120</td>
<td>&lt;80</td>
<td>Optima</td>
<td>SÍ</td>
</tr>
<tr>
<td>120-129</td>
<td>&lt;80</td>
<td>Elevada</td>
<td>SÍ</td>
</tr>
<tr>
<td>130-139</td>
<td>80-89</td>
<td>Hipertension Etapa 1</td>
<td>SÍ si controlada</td>
</tr>
<tr>
<td>140-179</td>
<td>90-119</td>
<td>Hipertension Etapa 2</td>
<td>SÍ si controlada</td>
</tr>
<tr>
<td>&gt;180</td>
<td>&gt;120</td>
<td>Crisis Hipertensiva</td>
<td>NO</td>
</tr>
</tbody>
</table>

<h3>Limites de Centros de Plasma</h3>
<ul>
<li><strong>CSL Plasma:</strong> Tipicamente menos de 180/120 mmHg</li>
<li><strong>BioLife:</strong> Menos de 180/120 mmHg</li>
<li><strong>Octapharma:</strong> Menos de 180/120 mmHg</li>
<li><strong>Grifols:</strong> Menos de 180/120 mmHg</li>
<li><strong>KedPlasma:</strong> Menos de 180/120 mmHg</li>
</ul>

<h2 id="consejos">Consejos para Donantes con Antihipertensivos</h2>

<h3>Antes de Donacion</h3>
<ol>
<li><strong>Toma tu medicamento normal:</strong> No omitas tu antihipertensivo el dia de donacion</li>
<li><strong>Come ligero:</strong> Comida balanceada 2-3 horas antes</li>
<li><strong>Hidratate:</strong> 64+ oz de agua el dia anterior y manana</li>
<li><strong>Descansa bien:</strong> Especialmente si tomas beta bloqueador (pueden causar fatiga)</li>
<li><strong>Llega tranquilo:</strong> Ansiedad eleva presion - llega con tiempo</li>
<li><strong>Verifica presion en casa:</strong> Si es posible, toma presion antes de ir</li>
</ol>

<h3>Durante Donacion</h3>
<ul>
<li>Informa al personal que tomas antihipertensivo</li>
<li>Comunica si sientes mareo, vision borrosa o palpitaciones</li>
<li>Mantente tranquilo y respira profundamente</li>
<li>Bebe agua si se te permite durante procedimiento</li>
</ul>

<h3>Despues de Donacion</h3>
<ol>
<li>Come algo con carbohidratos y proteina inmediatamente</li>
<li>Bebe mas liquidos de lo normal (especialmente si tomas diuretico)</li>
<li>Descansa al menos 2 horas antes de ejercicio</li>
<li>Si tomas beta bloqueador, ten cuidado con actividades intensas</li>
<li>Reporta cualquier efecto inusual</li>
</ol>

<h3>Consideraciones por Tipo</h3>
<ul>
<li><strong>Beta Bloqueadores:</strong> Descansa mas, come bien despues</li>
<li><strong>Diureticos:</strong> Extra hidratacion, consume potasio</li>
<li><strong>ACE Inhibitors/ARBs:</strong> Proceso normal sin ajustes</li>
<li><strong>Bloqueadores Calcio:</strong> Proceso normal, sin cambios</li>
</ul>

{related_es([
    ('/es/blog/medicamentos-permitidos-donacion-plasma.html', 'Medicamentos Permitidos'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos de Donacion'),
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuanto Pagan por Donar'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Puedo donar plasma si tomo lisinopril o losartan?</h3>
<p>Sí, completamente permitido. Lisinopril y losartan (ambos antihipertensivos) no descalifican donantes. Centros como CSL Plasma aceptan donantes en tratamiento de hipertensión.</p>

<h3>¿Mi presión arterial tiene que ser baja para donar?</h3>
<p>Tu presión debe ser menor de 180/120 mmHg. El control con medicamentos es importante. Si tomas antihipertensivos regularmente, deberías estar dentro de límites. Verifica tu presión antes de ir.</p>

<h3>¿Tengo que cambiar mi medicamento para la presión?</h3>
<p>No. Continúa tu medicamento normal. De hecho, mantener tu antihipertensivo es más seguro para donación. Es importante tener presión controlada.</p>

<h3>¿Qué pasa si mi presión está un poco alta el día de donación?</h3>
<p>El centro verificará tu presión. Si está arriba de 180/120, pueden rechazar esa donación. Toma tu medicamento, come bien, descansa y llega temprano para no estar ansioso.</p>
'''

    faq_schema = [
        make_faq("¿Puedo donar plasma si tomo antihipertensivos?", "Sí, medicamentos como lisinopril, losartan y amlodipino son completamente permitidos."),
        make_faq("¿Mi presión arterial tiene que ser baja para donar?", "Debe ser menor de 180/120 mmHg. El control con medicamentos es importante."),
        make_faq("¿Tengo que parar mi medicamento para la presión?", "No, continúa tu medicamento normal. Es más seguro mantener presión controlada."),
        make_faq("¿Qué medicamentos para la presión son mejores para donantes?", "Lisinopril, losartan, amlodipino y hidroclorotiazida son todos seguros para donantes."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema)


def gen_medication_page_5():
    """Donar plasma con anticoagulantes"""
    slug = 'donar-plasma-con-anticoagulantes-2026'
    title = 'Donar Plasma con Anticoagulantes 2026: Warfarina, Eliquis, Xarelto'
    meta_desc = 'Puedes donar plasma si tomas anticoagulantes? Warfarina y Eliquis NO permitidos. Aspirina baja SÍ. Información completa sobre anticoagulantes 2026.'
    category = 'Medicamentos y Elegibilidad'
    read_time = 9
    toc_items = [
        ('respuesta', 'Respuesta Rapida'),
        ('prohibidos', 'Anticoagulantes Prohibidos'),
        ('permitidos', 'Anticoagulantes Permitidos'),
        ('riesgos', 'Por Que No Se Permiten'),
        ('alternativas', 'Alternativas y Opciones'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content_html = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rapida: MAYORIA NO PERMITIDA</h3>
    <p><strong>¿Puedo donar plasma si tomo anticoagulantes?</strong> NO para la mayoria. Warfarina, Eliquis, Xarelto, Dabigatran, Apixaban estan PROHIBIDOS. Aspirina en dosis baja (81 mg) SÍ es permitida (espera 48h). Si tomas anticoagulante, consulta con tu centro de plasma.</p>
</div>

<h2 id="prohibidos">Anticoagulantes PROHIBIDOS para Donacion</h2>
<p>Los siguientes medicamentos descalifican la donacion de plasma:</p>

<h3>Anticoagulantes Orales Directo (DOACs)</h3>
<table>
<thead>
<tr>
<th>Medicamento</th>
<th>Marca</th>
<th>Tipo</th>
<th>Donacion Permitida</th>
</tr>
</thead>
<tbody>
<tr>
<td>Apixaban</td>
<td>Eliquis</td>
<td>Factor Xa Inhibitor</td>
<td>NO</td>
</tr>
<tr>
<td>Rivaroxaban</td>
<td>Xarelto</td>
<td>Factor Xa Inhibitor</td>
<td>NO</td>
</tr>
<tr>
<td>Edoxaban</td>
<td>Savaysa</td>
<td>Factor Xa Inhibitor</td>
<td>NO</td>
</tr>
<tr>
<td>Dabigatran</td>
<td>Pradaxa</td>
<td>Trombina Inhibitor</td>
<td>NO</td>
</tr>
</tbody>
</table>

<h3>Anticoagulantes Tradicionales</h3>
<ul>
<li><strong>Warfarina (Coumadin):</strong> NO permitida</li>
<li><strong>Heparina Inyectable:</strong> NO permitida (incluyendo inyecciones subcutaneas)</li>
<li><strong>Acenocumarol:</strong> NO permitida</li>
</ul>

<h3>Anticoagulantes Inyectable</h3>
<ul>
<li><strong>Enoxaparina (Lovenox):</strong> NO permitida</li>
<li><strong>Dalteparina (Fragmin):</strong> NO permitida</li>
<li><strong>Fondaparinux (Arixtra):</strong> NO permitida</li>
</ul>

{AFFILIATE_ES}

<h2 id="permitidos">Anticoagulantes PERMITIDOS (Limitados)</h2>
<p>Solo aspirina en dosis baja tiene permiso limitado:</p>

<h3>Aspirina en Dosis Baja (81 mg)</h3>
<ul>
<li><strong>Nombres:</strong> Aspirin, Aspirin Low-Dose, Buffered Aspirin</li>
<li><strong>Razon permitida:</strong> Dosis muy baja, efecto anticoagulante minimo</li>
<li><strong>Requisito:</strong> Espera 48 horas desde ultima dosis</li>
<li><strong>Frecuencia:</strong> Muchos donantes toman aspirina diaria cardio protectora</li>
<li><strong>Verificacion:</strong> Confirma con tu centro - algunas ubicaciones piden documentacion</li>
</ul>

<h3>Que NO es Anticoagulante</h3>
<p>Estos medicamentos antiinflamatorios son permitidos (no anticoagulantes):</p>
<ul>
<li><strong>Ibuprofeno (Advil):</strong> Permitido sin espera</li>
<li><strong>Naproxeno (Aleve):</strong> Permitido sin espera</li>
<li><strong>Acetaminofen (Tylenol):</strong> Permitido sin espera</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="riesgos">Por Que Anticoagulantes No Se Permiten</h2>

<h3>Riesgos de Sangrado</h3>
<ul>
<li><strong>Flebotomia (pinchazo):</strong> Riesgo aumentado de hematoma grande o sangrado prolongado</li>
<li><strong>Moretones:</strong> Mucho mas probable con anticoagulantes</li>
<li><strong>Hemorragia:</strong> En casos raros, sangrado no controlable en brazo</li>
<li><strong>Paro del procedimiento:</strong> Si sangra demasiado, no pueden completar donacion</li>
</ul>

<h3>Calidad de Plasma Afectada</h3>
<ul>
<li><strong>Factores de coagulacion:</strong> Disminuidos en donantes anticoagulados</li>
<li><strong>Factores V, VII, X:</strong> Plasma puede estar deficiente en estos</li>
<li><strong>INR elevado:</strong> Si tomas warfarina, INR afecta calidad</li>
<li><strong>Rechazo potencial:</strong> Plasma puede ser descartado por baja actividad</li>
</ul>

<h3>Riesgos Medicos para Donante</h3>
<ul>
<li><strong>Hipotension:</strong> Perdida de sangre (aunque minima) puede bajar presion peligrosamente</li>
<li><strong>Trombocitopenia:</strong> Bajo platelet count puede causar sangrado anormal</li>
<li><strong>Infeccion:</strong> Hematomas grandes pueden infectarse</li>
<li><strong>Complicaciones cardiacas:</strong> Si tomas warfarina por fibrilacion atrial, riesgo aumentado</li>
</ul>

<h2 id="alternativas">Opciones y Alternativas</h2>

<h3>Si Tomas Warfarina o DOAC</h3>
<p>Lamentablemente, no hay alternativa para donar plasma mientras tomas estos medicamentos. Opciones limitadas:</p>
<ul>
<li><strong>Esperar a cambio de medicamento:</strong> Si tu doctor considera cambiar terapia anticoagulante</li>
<li><strong>Parar temporalmente:</strong> SOLO con aprobacion medica - nunca hagas esto sin consultar doctor</li>
<li><strong>Donacion diferida:</strong> Algunos donantes posponen hasta cambio de medicamento (a largo plazo)</li>
<li><strong>Donar diferente producto:</strong> Plasma no, pero consulta sobre otras donaciones (sangre entera, plaquetas)</li>
</ul>

<h3>Si Tomas Aspirina Diaria</h3>
<p>Si tomas 81 mg diaria para proteccion cardiaca:</p>
<ul>
<li><strong>Opcion 1:</strong> Donar cumpliendo requisito 48h entre ultima dosis y donacion</li>
<li><strong>Opcion 2:</strong> Consultar con cardiologo si es seguro espaciar dosis alrededor de donacion</li>
<li><strong>Opcion 3:</strong> Algunos centros aceptan aspirina diaria con documentacion medica</li>
<li><strong>Nota:</strong> Verifica politica especifica de tu centro</li>
</ul>

<h3>Medicamentos Alternativos para Condiciones Comunes</h3>
<table>
<thead>
<tr>
<th>Condicion</th>
<th>Anticoagulante (NO)</th>
<th>Alternativa (Consulta Doctor)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fibrilacion Atrial</td>
<td>Warfarina, Eliquis, Xarelto</td>
<td>Consultar cardiologo sobre opciones</td>
</tr>
<tr>
<td>TVP / Embolia</td>
<td>Heparina, Enoxaparina</td>
<td>Consultar hematolog sobre opciones</td>
</tr>
<tr>
<td>Riesgo Cardiaco</td>
<td>Warfarina</td>
<td>Aspirina 81 mg (con espera 48h)</td>
</tr>
</tbody>
</table>

{related_es([
    ('/es/blog/medicamentos-prohibidos-donacion-plasma.html', 'Medicamentos Prohibidos'),
    ('/es/blog/donar-plasma-con-ibuprofeno-antiinflamatorios-2026.html', 'Ibuprofeno y AINE'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos de Donacion'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>¿Puedo donar plasma si tomo Eliquis o Xarelto?</h3>
<p>No. Eliquis (apixaban) y Xarelto (rivaroxaban) son anticoagulantes directos que descalifican donantes. El riesgo de sangrado es muy alto. No se permiten en ningún centro de plasma.</p>

<h3>¿Puedo donar si tomo warfarina?</h3>
<p>No. La warfarina está prohibida para donación de plasma. El alto riesgo de sangrado y el efecto en factores de coagulación la hace ineligible. Consulta con tu médico cardiaco.</p>

<h3>¿Qué pasa si tomo aspirina diaria?</h3>
<p>Aspirina en dosis baja (81 mg) puede estar permitida. Requiere esperar 48 horas desde la última dosis. Verifica con tu centro específico si aceptan aspirina diaria.</p>

<h3>¿Hay excepciones para anticoagulantes?</h3>
<p>En general no. Los anticoagulantes (excepto aspirina baja) descalifican permanentemente. Si tu medicamento es vital para tu salud, la donación de plasma no es opción. Tu salud es lo primero.</p>
'''

    faq_schema = [
        make_faq("¿Puedo donar plasma si tomo anticoagulantes?", "No para la mayoría. Warfarina, Eliquis y Xarelto están prohibidos. Aspirina baja (81 mg) está permitida con espera de 48h."),
        make_faq("¿Por qué no se permiten anticoagulantes?", "Riesgo muy alto de sangrado durante punción venosa y complicaciones post-donación."),
        make_faq("¿Qué hago si tomo warfarina pero quiero donar?", "Consulta con tu cardiólogo. No hagas cambios sin aprobación médica. Tu salud es lo primero."),
        make_faq("¿Es seguro parar anticoagulantes para donar?", "Nunca hagas esto sin supervisión médica. Los anticoagulantes son críticos para condiciones como fibrilación atrial."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema)


if __name__ == '__main__':
    print("Generating 5 Spanish medication blog pages...")

    # Ensure directory exists
    os.makedirs(ES_BLOG_DIR, exist_ok=True)

    pages = [
        ('donar-plasma-con-insulina-diabetes-2026', gen_medication_page_1()),
        ('donar-plasma-con-metformina-2026', gen_medication_page_2()),
        ('donar-plasma-con-ibuprofeno-antiinflamatorios-2026', gen_medication_page_3()),
        ('donar-plasma-con-antihipertensivos-2026', gen_medication_page_4()),
        ('donar-plasma-con-anticoagulantes-2026', gen_medication_page_5()),
    ]

    for slug, html in pages:
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")

    print(f"\nDone! Generated {len(pages)} Spanish medication blog pages.")
