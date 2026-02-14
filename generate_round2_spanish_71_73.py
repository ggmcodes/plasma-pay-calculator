#!/usr/bin/env python3
"""Generate 3 Spanish medical condition pages (pages 71-73): anxiety/depression, vaccines, thyroid."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch5_spanish_template import make_es_page, make_faq, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es
ES_BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'es', 'blog')


def gen_ansiedad_depresion():
    slug = "donar-plasma-con-ansiedad-depresion-2026"
    title = "Donar Plasma con Ansiedad o Depresion 2026: Medicamentos y Consejos"
    meta_desc = "Puedes donar plasma si tienes ansiedad o depresion? Si, en la mayoria de los casos. Guia sobre SSRIs, SNRIs, benzodiacepinas y como manejar la ansiedad durante la donacion."
    category = "Condiciones Medicas"
    read_time = 9
    toc_items = [
        ("respuesta", "Respuesta Rapida"),
        ("medicamentos", "Medicamentos Permitidos"),
        ("screening", "Que Decir en el Screening"),
        ("manejar-ansiedad", "Manejar la Ansiedad Durante la Donacion"),
        ("medicamentos-prohibidos", "Medicamentos que Pueden Descalificarte"),
        ("consejos", "Consejos para Donantes con Ansiedad"),
        ("faq", "Preguntas Frecuentes"),
    ]

    content_html = f'''
<div class="highlight-box" id="respuesta">
<h3>Respuesta Rapida</h3>
<p><strong>Si, puedes donar plasma si tienes ansiedad o depresion</strong> en la mayoria de los casos. La clave esta en tus medicamentos y la estabilidad de tu condicion. Los antidepresivos comunes como <strong>SSRIs (sertralina, fluoxetina, escitalopram)</strong> y <strong>SNRIs (venlafaxina, duloxetina)</strong> generalmente son aceptados. Lo importante es que tu condicion este estable y controlada con medicamentos durante al menos 30 dias.</p>
</div>

<h2 id="medicamentos">Medicamentos Permitidos para Donar Plasma</h2>
<p>La mayoria de los medicamentos para ansiedad y depresion <strong>no te descalifican</strong> para donar plasma. Los centros de plasma evaluan caso por caso, pero estas son las categorias principales:</p>

<h3>SSRIs (Inhibidores Selectivos de Recaptacion de Serotonina)</h3>
<p>Los SSRIs son los antidepresivos mas comunes y generalmente son <strong>100% aceptados</strong> en todos los centros de plasma:</p>
<ul>
<li><strong>Sertralina (Zoloft)</strong> — Aceptado en todos los centros principales</li>
<li><strong>Fluoxetina (Prozac)</strong> — Aceptado sin restricciones</li>
<li><strong>Escitalopram (Lexapro)</strong> — Aceptado en CSL, BioLife, Octapharma, Grifols</li>
<li><strong>Paroxetina (Paxil)</strong> — Aceptado con dosis estable</li>
<li><strong>Citalopram (Celexa)</strong> — Aceptado sin problemas</li>
</ul>

<h3>SNRIs (Inhibidores de Recaptacion de Serotonina-Norepinefrina)</h3>
<ul>
<li><strong>Venlafaxina (Effexor)</strong> — Generalmente aceptado</li>
<li><strong>Duloxetina (Cymbalta)</strong> — Aceptado en la mayoria de centros</li>
<li><strong>Desvenlafaxina (Pristiq)</strong> — Aceptado con dosis estable</li>
</ul>

<h3>Benzodiacepinas</h3>
<p>Las benzodiacepinas requieren mas cuidado. Algunos centros las aceptan, otros no:</p>
<ul>
<li><strong>Alprazolam (Xanax)</strong> — Varia por centro; algunos requieren que no lo tomes el dia de la donacion</li>
<li><strong>Lorazepam (Ativan)</strong> — Similar al alprazolam, consulta tu centro especifico</li>
<li><strong>Clonazepam (Klonopin)</strong> — Generalmente aceptado si la dosis es baja y estable</li>
</ul>
<p><strong>Nota importante:</strong> Si tomas benzodiacepinas, pregunta directamente a tu centro antes de tu primera visita. Las politicas varian significativamente.</p>

{AFFILIATE_ES}

<h2 id="screening">Que Decir en el Screening Medico</h2>
<p>El proceso de screening puede causar ansiedad adicional. Aqui tienes una guia para manejarlo:</p>

<h3>Se Honesto Pero Conciso</h3>
<p>Los tecnicos de screening necesitan saber sobre tus medicamentos, pero no necesitan detalles extensos sobre tu historial de salud mental. Enfocate en:</p>
<ul>
<li><strong>Nombre del medicamento y dosis:</strong> "Tomo sertralina 50mg diariamente"</li>
<li><strong>Duracion:</strong> "Lo he tomado por 6 meses, dosis estable"</li>
<li><strong>Estabilidad:</strong> "Mi condicion esta bien controlada"</li>
</ul>

<h3>Lo Que Buscan los Centros</h3>
<p>Los centros de plasma no buscan descalificarte — buscan asegurar que donar sea <strong>seguro para ti</strong>. Las condiciones que SI causan descalificacion son:</p>
<ul>
<li>Hospitalizacion psiquiatrica reciente (ultimos 6-12 meses)</li>
<li>Cambio de medicamento en los ultimos 30 dias</li>
<li>Ideacion suicida activa o inestabilidad severa</li>
<li>Medicamentos antipsicoticos especificos (varia por centro)</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="manejar-ansiedad">Como Manejar la Ansiedad Durante la Donacion</h2>
<p>Muchos donantes con ansiedad reportan que las primeras visitas son las mas dificiles. Estas estrategias ayudan:</p>

<h3>Antes de la Donacion</h3>
<ul>
<li><strong>Visita el centro primero:</strong> Familiarizarte con el lugar reduce la ansiedad anticipatoria</li>
<li><strong>Hidratate bien:</strong> La deshidratacion empeora la ansiedad y hace las venas mas dificiles de encontrar</li>
<li><strong>Come proteina:</strong> Una comida solida 2-3 horas antes estabiliza el azucar en sangre</li>
<li><strong>Practica respiracion:</strong> 4-7-8 (inhala 4 seg, sostiene 7, exhala 8) funciona bien</li>
</ul>

<h3>Durante la Donacion</h3>
<ul>
<li><strong>Distraccion:</strong> Lleva audifonos con musica, podcast o serie descargada</li>
<li><strong>No mires la aguja:</strong> Mira hacia otro lado durante la insercion</li>
<li><strong>Comunica:</strong> Dile al tecnico si sientes ansiedad — estan entrenados para ayudar</li>
<li><strong>Respira profundo:</strong> Si sientes panico, enfocate en la respiracion abdominal</li>
</ul>

<h2 id="medicamentos-prohibidos">Medicamentos que Pueden Descalificarte</h2>
<p>Aunque la mayoria de medicamentos para ansiedad y depresion son aceptados, algunos tratamientos SI pueden causar descalificacion temporal o permanente:</p>
<table>
<thead><tr><th>Medicamento</th><th>Estado</th><th>Motivo</th></tr></thead>
<tbody>
<tr><td>Litio</td><td>Generalmente descalificado</td><td>Rango terapeutico estrecho, riesgo de toxicidad</td></tr>
<tr><td>Antipsicoticos atipicos</td><td>Varia por centro</td><td>Depende del medicamento especifico y la condicion</td></tr>
<tr><td>MAOIs</td><td>Generalmente descalificado</td><td>Interacciones potenciales serias</td></tr>
<tr><td>Bupropion (Wellbutrin)</td><td>Generalmente aceptado</td><td>Aceptado en la mayoria de centros</td></tr>
</tbody>
</table>

<h2 id="consejos">Consejos para Donantes con Ansiedad o Depresion</h2>
<ol>
<li><strong>Programa citas temprano:</strong> Menos personas = menos espera = menos ansiedad</li>
<li><strong>Establece una rutina:</strong> Donar los mismos dias y horas crea familiaridad</li>
<li><strong>Celebra pequenas victorias:</strong> Cada donacion completada es un logro</li>
<li><strong>Usa el ingreso como motivacion positiva:</strong> El dinero extra puede reducir estres financiero, mejorando tu salud mental</li>
<li><strong>Descansa despues:</strong> No te apures a volver a tus actividades, tomate 15-20 minutos</li>
</ol>

{related_es([
    ('/es/blog/medicamentos-donar-plasma-lista-2026.html', 'Lista de Medicamentos Aceptados para Donar Plasma'),
    ('/es/blog/efectos-secundarios-donar-plasma-2026.html', 'Efectos Secundarios de Donar Plasma'),
    ('/es/blog/que-descalifica-donar-plasma-2026.html', 'Que Te Descalifica para Donar Plasma'),
    ('/es/blog/como-prepararse-primera-donacion-plasma-2026.html', 'Como Prepararse para Tu Primera Donacion'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>Puedo donar plasma si tomo antidepresivos?</h3>
<p>Si, la gran mayoria de antidepresivos (SSRIs como sertralina, fluoxetina, escitalopram y SNRIs como venlafaxina, duloxetina) son aceptados en todos los centros de plasma. Tu dosis debe ser estable por al menos 30 dias.</p>

<h3>Las benzodiacepinas me descalifican para donar plasma?</h3>
<p>No necesariamente. Algunos centros aceptan benzodiacepinas con dosis estable, mientras otros pueden pedir que no las tomes el dia de la donacion. Consulta directamente con tu centro antes de tu primera visita.</p>

<h3>Tengo que decir que tengo ansiedad en el screening?</h3>
<p>Debes ser honesto sobre tus medicamentos, pero no necesitas dar detalles extensos sobre tu diagnostico. Simplemente menciona el nombre y dosis de tu medicamento y que tu condicion esta estable.</p>

<h3>Que pasa si tengo un ataque de ansiedad durante la donacion?</h3>
<p>Informa al tecnico inmediatamente. Pueden pausar o detener el procedimiento si es necesario. La donacion se puede completar otro dia sin penalizacion. Tu seguridad es la prioridad.</p>

<h3>Donar plasma puede empeorar mi ansiedad o depresion?</h3>
<p>Para la mayoria de las personas, no. De hecho, muchos donantes reportan que la rutina y el ingreso extra reducen su estres. Sin embargo, si notas que tus sintomas empeoran, consulta a tu medico y considera reducir la frecuencia de donacion.</p>
'''

    faqs = [
        make_faq("Puedo donar plasma si tomo antidepresivos?", "Si, la mayoria de antidepresivos como SSRIs (sertralina, fluoxetina, escitalopram) y SNRIs (venlafaxina, duloxetina) son aceptados. Tu dosis debe ser estable por al menos 30 dias."),
        make_faq("Las benzodiacepinas me descalifican para donar plasma?", "No necesariamente. Algunos centros aceptan benzodiacepinas con dosis estable. Consulta directamente con tu centro antes de tu primera visita."),
        make_faq("Tengo que decir que tengo ansiedad en el screening?", "Debes ser honesto sobre tus medicamentos. Menciona el nombre y dosis de tu medicamento y que tu condicion esta estable. No necesitas dar detalles extensos."),
        make_faq("Que pasa si tengo un ataque de ansiedad durante la donacion?", "Informa al tecnico inmediatamente. Pueden pausar o detener el procedimiento. La donacion se puede completar otro dia sin penalizacion."),
        make_faq("Donar plasma puede empeorar mi ansiedad o depresion?", "Para la mayoria de las personas, no. Muchos donantes reportan que la rutina y el ingreso extra reducen su estres. Si tus sintomas empeoran, consulta a tu medico."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faqs, en_equivalent="can-you-donate-plasma-with-anxiety-depression-2026.html")


def gen_despues_vacuna():
    slug = "donar-plasma-despues-vacuna-2026"
    title = "Donar Plasma Despues de Vacunarte 2026: Tiempos de Espera por Vacuna"
    meta_desc = "Cuanto tiempo esperar para donar plasma despues de una vacuna? COVID 14 dias, gripe 48 horas, y mas. Guia completa de tiempos de espera por tipo de vacuna segun la FDA."
    category = "Condiciones Medicas"
    read_time = 8
    toc_items = [
        ("respuesta", "Respuesta Rapida"),
        ("tiempos", "Tiempos de Espera por Vacuna"),
        ("covid", "Vacunas COVID-19"),
        ("comunes", "Vacunas Comunes"),
        ("viaje", "Vacunas de Viaje"),
        ("fda", "Regulaciones de la FDA"),
        ("faq", "Preguntas Frecuentes"),
    ]

    content_html = f'''
<div class="highlight-box" id="respuesta">
<h3>Respuesta Rapida</h3>
<p>Si, puedes donar plasma despues de vacunarte, pero debes esperar un <strong>periodo de diferimiento</strong> que varia segun el tipo de vacuna. Los tiempos mas comunes: <strong>vacuna COVID-19: 14 dias</strong>, <strong>vacuna de la gripe: 48 horas</strong>, <strong>vacunas con virus vivos atenuados: 4 semanas</strong>. Si no tienes sintomas y el periodo de espera ha pasado, puedes donar normalmente.</p>
</div>

<h2 id="tiempos">Tiempos de Espera por Tipo de Vacuna</h2>
<p>Cada vacuna tiene un tiempo de diferimiento diferente. Esta tabla resume las politicas actuales de los principales centros de plasma en 2026:</p>

<table>
<thead><tr><th>Vacuna</th><th>Tiempo de Espera</th><th>Tipo</th><th>Notas</th></tr></thead>
<tbody>
<tr><td><strong>COVID-19 (mRNA)</strong></td><td>14 dias</td><td>mRNA</td><td>Pfizer, Moderna — sin sintomas</td></tr>
<tr><td><strong>COVID-19 (J&J)</strong></td><td>14 dias</td><td>Vector viral</td><td>Johnson & Johnson</td></tr>
<tr><td><strong>Gripe (inyectable)</strong></td><td>48 horas</td><td>Inactivada</td><td>Si no hay fiebre ni sintomas</td></tr>
<tr><td><strong>Gripe (nasal/FluMist)</strong></td><td>4 semanas</td><td>Virus vivo atenuado</td><td>Diferimiento mas largo por virus vivo</td></tr>
<tr><td><strong>Tetanos/Tdap</strong></td><td>48 horas</td><td>Inactivada</td><td>Si no hay fiebre</td></tr>
<tr><td><strong>Hepatitis A</strong></td><td>48 horas</td><td>Inactivada</td><td>Aceptado rapidamente</td></tr>
<tr><td><strong>Hepatitis B</strong></td><td>48 horas</td><td>Recombinante</td><td>Sin restriccion larga</td></tr>
<tr><td><strong>HPV (Gardasil)</strong></td><td>48 horas</td><td>Recombinante</td><td>Si no hay sintomas</td></tr>
<tr><td><strong>Varicela</strong></td><td>4 semanas</td><td>Virus vivo atenuado</td><td>Diferimiento estandar para virus vivo</td></tr>
<tr><td><strong>MMR (sarampion)</strong></td><td>4 semanas</td><td>Virus vivo atenuado</td><td>Diferimiento estandar</td></tr>
<tr><td><strong>Fiebre amarilla</strong></td><td>4 semanas</td><td>Virus vivo atenuado</td><td>Vacuna de viaje comun</td></tr>
<tr><td><strong>Rabia (profilactica)</strong></td><td>48 horas</td><td>Inactivada</td><td>Solo profilactica, no post-exposicion</td></tr>
<tr><td><strong>Rabia (post-exposicion)</strong></td><td>12 meses</td><td>Post-exposicion</td><td>Diferimiento largo por exposicion potencial</td></tr>
<tr><td><strong>Viruela/Mpox</strong></td><td>8 semanas</td><td>Virus vivo modificado</td><td>JYNNEOS requiere espera adicional</td></tr>
</tbody>
</table>

{AFFILIATE_ES}

<h2 id="covid">Vacunas COVID-19: Guia Detallada</h2>
<p>Las vacunas contra COVID-19 son las que mas preguntas generan entre donantes de plasma. Aqui estan los detalles:</p>

<h3>Vacunas mRNA (Pfizer, Moderna)</h3>
<ul>
<li><strong>Tiempo de espera:</strong> 14 dias despues de cada dosis</li>
<li><strong>Requisito:</strong> No tener fiebre, dolor de cuerpo, ni sintomas activos</li>
<li><strong>Refuerzos:</strong> El mismo periodo de 14 dias aplica para cada refuerzo</li>
<li><strong>Documentacion:</strong> Algunos centros pueden pedir tu tarjeta de vacunacion</li>
</ul>

<h3>Vacuna Johnson & Johnson (vector viral)</h3>
<ul>
<li><strong>Tiempo de espera:</strong> 14 dias</li>
<li><strong>Nota:</strong> Aunque esta vacuna se usa menos en 2026, el diferimiento es el mismo</li>
</ul>

<h3>Nuevos Refuerzos 2025-2026</h3>
<p>Los refuerzos actualizados para las variantes mas recientes siguen las mismas reglas: <strong>14 dias de espera</strong> sin importar el fabricante. Verifica con tu centro si tienes dudas sobre una vacuna especifica.</p>

<h2 id="comunes">Vacunas Comunes y Sus Diferimientos</h2>

<h3>Regla General Rapida</h3>
<p>Puedes recordar facilmente los tiempos con estas categorias:</p>
<ul>
<li><strong>Vacunas inactivadas/recombinantes:</strong> 48 horas (gripe inyectable, tetanos, hepatitis, HPV)</li>
<li><strong>Vacunas de virus vivo atenuado:</strong> 4 semanas (MMR, varicela, gripe nasal, fiebre amarilla)</li>
<li><strong>Vacunas COVID-19:</strong> 14 dias (todas las marcas)</li>
<li><strong>Post-exposicion (rabia):</strong> 12 meses</li>
</ul>

{PRO_TOOLKIT_ES}

<h2 id="viaje">Vacunas de Viaje</h2>
<p>Si planeas viajar y necesitas vacunas especiales, programa tu donacion de plasma antes de vacunarte o planea el diferimiento:</p>
<ul>
<li><strong>Fiebre amarilla:</strong> 4 semanas — planifica con anticipacion si viajas a Sudamerica o Africa</li>
<li><strong>Fiebre tifoidea (oral):</strong> 4 semanas — es virus vivo atenuado</li>
<li><strong>Fiebre tifoidea (inyectable):</strong> 48 horas — version inactivada</li>
<li><strong>Colera:</strong> 48 horas — generalmente sin restriccion larga</li>
<li><strong>Encefalitis japonesa:</strong> 48 horas — vacuna inactivada</li>
</ul>
<p><strong>Consejo:</strong> Si tienes viajes planeados, dona lo mas posible antes de vacunarte para no perder ingreso durante el diferimiento.</p>

<h2 id="fda">Regulaciones de la FDA sobre Vacunas y Donacion</h2>
<p>La FDA establece las pautas que todos los centros de plasma deben seguir. Los puntos clave son:</p>
<ul>
<li>Los diferimientos existen para proteger tanto al donante como a los receptores del plasma</li>
<li>Las vacunas de virus vivo requieren periodos mas largos porque el virus atenuado puede estar presente en el plasma</li>
<li>Las vacunas inactivadas no contienen virus vivo, por lo que el diferimiento es mas corto</li>
<li>Si desarrollas fiebre o sintomas despues de vacunarte, debes esperar hasta que los sintomas se resuelvan completamente, ademas del periodo de diferimiento</li>
<li>Los centros individuales pueden tener politicas mas conservadoras que las de la FDA</li>
</ul>

{related_es([
    ('/es/blog/que-descalifica-donar-plasma-2026.html', 'Que Te Descalifica para Donar Plasma'),
    ('/es/blog/medicamentos-donar-plasma-lista-2026.html', 'Lista de Medicamentos y Donacion de Plasma'),
    ('/es/blog/cuantas-veces-donar-plasma-frecuencia-2026.html', 'Con Que Frecuencia Puedes Donar Plasma'),
    ('/es/blog/como-prepararse-primera-donacion-plasma-2026.html', 'Como Prepararse para Tu Primera Donacion'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>Cuanto tiempo espero para donar plasma despues de la vacuna COVID?</h3>
<p>Debes esperar 14 dias despues de cualquier vacuna COVID-19 (Pfizer, Moderna o J&J), incluyendo refuerzos. Ademas, no debes tener fiebre ni sintomas activos al momento de donar.</p>

<h3>Puedo donar plasma despues de la vacuna de la gripe?</h3>
<p>Si, puedes donar despues de solo 48 horas si recibiste la vacuna inyectable y no tienes fiebre. La vacuna nasal (FluMist) requiere 4 semanas porque contiene virus vivo atenuado.</p>

<h3>Que pasa si no digo que me vacune?</h3>
<p>Debes ser honesto en el cuestionario de salud. Las vacunas recientes pueden afectar la calidad del plasma. Mentir en el screening puede resultar en descalificacion permanente si se descubre.</p>

<h3>Me vacune ayer, puedo donar hoy?</h3>
<p>Depende de la vacuna. Para vacunas inactivadas como la gripe inyectable o tetanos, necesitas esperar al menos 48 horas. Para COVID-19, son 14 dias. Para virus vivo atenuado, 4 semanas.</p>

<h3>Las vacunas de viaje afectan mi capacidad de donar?</h3>
<p>Si. Las vacunas de viaje con virus vivo (fiebre amarilla, tifoidea oral) requieren 4 semanas de espera. Las vacunas inactivadas de viaje generalmente solo necesitan 48 horas. Planifica tus donaciones antes del viaje.</p>
'''

    faqs = [
        make_faq("Cuanto tiempo espero para donar plasma despues de la vacuna COVID?", "Debes esperar 14 dias despues de cualquier vacuna COVID-19 (Pfizer, Moderna o J&J), incluyendo refuerzos. No debes tener fiebre ni sintomas activos."),
        make_faq("Puedo donar plasma despues de la vacuna de la gripe?", "Si, puedes donar despues de 48 horas si recibiste la vacuna inyectable y no tienes fiebre. La vacuna nasal FluMist requiere 4 semanas."),
        make_faq("Que pasa si no digo que me vacune?", "Debes ser honesto en el cuestionario de salud. Mentir en el screening puede resultar en descalificacion permanente."),
        make_faq("Me vacune ayer, puedo donar hoy?", "Depende de la vacuna. Gripe inyectable o tetanos: 48 horas. COVID-19: 14 dias. Virus vivo atenuado: 4 semanas."),
        make_faq("Las vacunas de viaje afectan mi capacidad de donar?", "Si. Vacunas de virus vivo como fiebre amarilla requieren 4 semanas. Vacunas inactivadas de viaje generalmente necesitan 48 horas."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faqs, en_equivalent="can-you-donate-plasma-after-vaccine-2026.html")


def gen_enfermedad_tiroidea():
    slug = "donar-plasma-con-enfermedad-tiroidea-2026"
    title = "Donar Plasma con Enfermedad Tiroidea 2026: Hipotiroidismo, Hipertiroidismo y Hashimoto"
    meta_desc = "Puedes donar plasma con enfermedad tiroidea? Si, en la mayoria de los casos. Guia sobre hipotiroidismo, hipertiroidismo, Hashimoto, Graves y medicamentos como levotiroxina."
    category = "Condiciones Medicas"
    read_time = 8
    toc_items = [
        ("respuesta", "Respuesta Rapida"),
        ("condiciones", "Condiciones Tiroideas y Elegibilidad"),
        ("medicamentos", "Medicamentos Tiroideos Aceptados"),
        ("screening", "Que Esperar en el Screening"),
        ("consejos", "Consejos para Donantes con Tiroides"),
        ("cuando-no", "Cuando NO Puedes Donar"),
        ("faq", "Preguntas Frecuentes"),
    ]

    content_html = f'''
<div class="highlight-box" id="respuesta">
<h3>Respuesta Rapida</h3>
<p><strong>Si, puedes donar plasma con enfermedad tiroidea</strong> en la mayoria de los casos. El <strong>hipotiroidismo tratado con levotiroxina (Synthroid)</strong> es completamente aceptado en todos los centros de plasma. El <strong>hipertiroidismo</strong> tambien es aceptado si esta controlado. Las condiciones autoinmunes como <strong>Hashimoto y Graves</strong> generalmente son aceptadas mientras estes estable y tomando tu medicamento regularmente.</p>
</div>

<h2 id="condiciones">Condiciones Tiroideas y Elegibilidad para Donar</h2>
<p>Las enfermedades tiroideas son extremadamente comunes — afectan a mas de 20 millones de personas en los Estados Unidos. La buena noticia es que la mayoria de estas condiciones <strong>no te descalifican</strong> para donar plasma.</p>

<h3>Hipotiroidismo (Tiroides Baja)</h3>
<p>El hipotiroidismo es la condicion tiroidea mas comun y es <strong>completamente aceptada</strong> para donacion de plasma:</p>
<ul>
<li><strong>Estado:</strong> Aceptado en todos los centros principales (CSL, BioLife, Octapharma, Grifols)</li>
<li><strong>Requisito:</strong> Dosis estable de medicamento tiroideo por al menos 30 dias</li>
<li><strong>Medicamento:</strong> Levotiroxina (Synthroid, Levoxyl, Tirosint) es 100% aceptada</li>
<li><strong>Impacto en donacion:</strong> Ninguno si esta bien controlado</li>
</ul>

<h3>Hipertiroidismo (Tiroides Alta)</h3>
<p>El hipertiroidismo requiere un poco mas de evaluacion, pero generalmente es aceptado:</p>
<ul>
<li><strong>Estado:</strong> Aceptado si esta controlado con medicamento</li>
<li><strong>Requisito:</strong> Condicion estable sin sintomas severos (temblores, taquicardia, perdida de peso rapida)</li>
<li><strong>Medicamentos:</strong> Metimazol (Tapazol) y propiltiouracilo (PTU) son generalmente aceptados</li>
<li><strong>Post-tratamiento:</strong> Si recibiste yodo radioactivo, hay un periodo de diferimiento de varias semanas</li>
</ul>

<h3>Tiroiditis de Hashimoto</h3>
<p>Hashimoto es una condicion autoinmune que causa hipotiroidismo. Es <strong>aceptada para donacion</strong>:</p>
<ul>
<li><strong>Estado:</strong> Aceptado — se trata igual que hipotiroidismo regular</li>
<li><strong>Tratamiento:</strong> Levotiroxina para mantener niveles normales de TSH</li>
<li><strong>Nota:</strong> Aunque es autoinmune, no afecta la calidad del plasma de forma que impida la donacion</li>
</ul>

<h3>Enfermedad de Graves</h3>
<p>La enfermedad de Graves causa hipertiroidismo autoinmune:</p>
<ul>
<li><strong>Estado:</strong> Generalmente aceptado si esta controlado</li>
<li><strong>Activo sin tratar:</strong> No aceptado — puede afectar la frecuencia cardiaca y presion arterial</li>
<li><strong>Tratado y estable:</strong> Si, puedes donar con medicamento estable</li>
<li><strong>Post-cirugia tiroidea:</strong> Aceptado con medicamento de reemplazo estable</li>
</ul>

{AFFILIATE_ES}

<h2 id="medicamentos">Medicamentos Tiroideos y Donacion de Plasma</h2>
<table>
<thead><tr><th>Medicamento</th><th>Marca Comun</th><th>Estado</th><th>Notas</th></tr></thead>
<tbody>
<tr><td><strong>Levotiroxina</strong></td><td>Synthroid, Levoxyl</td><td>Aceptado</td><td>El mas comun, sin restricciones</td></tr>
<tr><td><strong>Liotironina</strong></td><td>Cytomel</td><td>Aceptado</td><td>T3 sintetica, generalmente aceptada</td></tr>
<tr><td><strong>Armour Thyroid</strong></td><td>Tiroides desecada</td><td>Aceptado</td><td>Tiroides natural de cerdo, aceptada</td></tr>
<tr><td><strong>Metimazol</strong></td><td>Tapazol</td><td>Generalmente aceptado</td><td>Para hipertiroidismo, dosis estable</td></tr>
<tr><td><strong>Propiltiouracilo</strong></td><td>PTU</td><td>Generalmente aceptado</td><td>Consulta con tu centro especifico</td></tr>
<tr><td><strong>Yodo radioactivo</strong></td><td>I-131</td><td>Diferimiento temporal</td><td>Espera varias semanas despues del tratamiento</td></tr>
</tbody>
</table>

<p><strong>Punto clave:</strong> La levotiroxina es uno de los medicamentos mas recetados en el mundo y es universalmente aceptada para donacion de plasma. Si la tomas, no tienes de que preocuparte.</p>

{PRO_TOOLKIT_ES}

<h2 id="screening">Que Esperar en el Screening con Enfermedad Tiroidea</h2>
<p>Durante tu screening medico, el tecnico te preguntara sobre condiciones medicas y medicamentos. Para enfermedad tiroidea:</p>

<h3>Lo Que Debes Mencionar</h3>
<ul>
<li><strong>Tu diagnostico:</strong> "Tengo hipotiroidismo" o "Tengo Hashimoto"</li>
<li><strong>Tu medicamento y dosis:</strong> "Tomo levotiroxina 75mcg diariamente"</li>
<li><strong>Estabilidad:</strong> "Mi dosis ha sido la misma por 6 meses"</li>
<li><strong>Ultimo laboratorio:</strong> Si te preguntan, menciona que tus niveles de TSH estan en rango normal</li>
</ul>

<h3>Signos Vitales</h3>
<p>Los centros revisan tu frecuencia cardiaca y presion arterial. Si tu condicion tiroidea esta bien controlada, estos valores seran normales. El hipertiroidismo no controlado puede causar taquicardia (frecuencia cardiaca elevada), lo que podria descalificarte temporalmente.</p>

<h2 id="consejos">Consejos para Donantes con Enfermedad Tiroidea</h2>
<ol>
<li><strong>Toma tu medicamento a la misma hora:</strong> La consistencia ayuda a mantener niveles estables de hormona tiroidea</li>
<li><strong>No cambies la hora por la donacion:</strong> Toma tu levotiroxina como normalmente lo harias</li>
<li><strong>Hidratacion extra:</strong> Las personas con hipotiroidismo pueden deshidratarse mas facilmente — bebe 64+ oz de agua el dia anterior</li>
<li><strong>Monitorea tu energia:</strong> Si sientes fatiga excesiva despues de donar, habla con tu medico sobre ajustar tu dosis</li>
<li><strong>Mantente al dia con laboratorios:</strong> Hazte analisis de TSH cada 6-12 meses para confirmar que tu dosis es correcta</li>
<li><strong>Lleva informacion:</strong> Tener el nombre y dosis exacta de tu medicamento agiliza el screening</li>
</ol>

<h2 id="cuando-no">Cuando NO Puedes Donar con Enfermedad Tiroidea</h2>
<p>Hay situaciones donde la enfermedad tiroidea SI puede descalificarte temporalmente:</p>
<ul>
<li><strong>Diagnostico reciente:</strong> Si te acaban de diagnosticar y aun estan ajustando tu medicamento (espera 30+ dias con dosis estable)</li>
<li><strong>Cambio de dosis reciente:</strong> Espera al menos 30 dias despues de cualquier cambio de dosis</li>
<li><strong>Hipertiroidismo no controlado:</strong> Frecuencia cardiaca mayor a 100 bpm o presion arterial elevada te descalificara en el screening</li>
<li><strong>Yodo radioactivo reciente:</strong> Espera el periodo de diferimiento indicado por tu centro</li>
<li><strong>Cancer de tiroides activo:</strong> Cualquier cancer activo descalifica para donacion de plasma</li>
<li><strong>Tormenta tiroidea reciente:</strong> Emergencia medica que requiere estabilizacion completa antes de considerar donar</li>
</ul>

{related_es([
    ('/es/blog/medicamentos-donar-plasma-lista-2026.html', 'Lista de Medicamentos Aceptados para Donar'),
    ('/es/blog/que-descalifica-donar-plasma-2026.html', 'Que Te Descalifica para Donar Plasma'),
    ('/es/blog/efectos-secundarios-donar-plasma-2026.html', 'Efectos Secundarios de Donar Plasma'),
    ('/es/blog/donar-plasma-con-ansiedad-depresion-2026.html', 'Donar Plasma con Ansiedad o Depresion'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
<h3>Puedo donar plasma si tomo levotiroxina?</h3>
<p>Si, la levotiroxina (Synthroid, Levoxyl) es completamente aceptada en todos los centros de plasma. Es uno de los medicamentos mas comunes entre donantes y no afecta la calidad del plasma.</p>

<h3>El hipotiroidismo me descalifica para donar plasma?</h3>
<p>No. El hipotiroidismo tratado y estable es aceptado en todos los centros principales. Solo necesitas tener una dosis estable de medicamento por al menos 30 dias.</p>

<h3>Puedo donar plasma con Hashimoto?</h3>
<p>Si. La tiroiditis de Hashimoto se trata igual que el hipotiroidismo para propositos de donacion. Si estas tomando levotiroxina y tu condicion esta estable, puedes donar sin problemas.</p>

<h3>Puedo donar plasma con enfermedad de Graves?</h3>
<p>Si, siempre que tu condicion este controlada con medicamento y tus signos vitales esten normales. El hipertiroidismo no controlado puede causar taquicardia que te descalificaria temporalmente.</p>

<h3>Donar plasma afecta mi tiroides?</h3>
<p>No, donar plasma no afecta la funcion tiroidea ni la efectividad de tus medicamentos tiroideos. El proceso de aferesis separa el plasma pero no interfiere con tus hormonas tiroideas.</p>
'''

    faqs = [
        make_faq("Puedo donar plasma si tomo levotiroxina?", "Si, la levotiroxina (Synthroid, Levoxyl) es completamente aceptada en todos los centros de plasma. No afecta la calidad del plasma."),
        make_faq("El hipotiroidismo me descalifica para donar plasma?", "No. El hipotiroidismo tratado y estable es aceptado en todos los centros principales. Necesitas dosis estable por al menos 30 dias."),
        make_faq("Puedo donar plasma con Hashimoto?", "Si. Hashimoto se trata igual que hipotiroidismo para donacion. Con levotiroxina y condicion estable, puedes donar sin problemas."),
        make_faq("Puedo donar plasma con enfermedad de Graves?", "Si, siempre que tu condicion este controlada con medicamento y tus signos vitales esten normales."),
        make_faq("Donar plasma afecta mi tiroides?", "No, donar plasma no afecta la funcion tiroidea ni la efectividad de tus medicamentos tiroideos."),
    ]

    return make_es_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faqs, en_equivalent="can-you-donate-plasma-with-thyroid-disease-2026.html")


if __name__ == '__main__':
    os.makedirs(ES_BLOG_DIR, exist_ok=True)
    pages = [
        ("donar-plasma-con-ansiedad-depresion-2026", gen_ansiedad_depresion),
        ("donar-plasma-despues-vacuna-2026", gen_despues_vacuna),
        ("donar-plasma-con-enfermedad-tiroidea-2026", gen_enfermedad_tiroidea),
    ]
    count = 0
    for slug, gen_func in pages:
        html = gen_func()
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1
    print(f"\nDone! Generated {count} Spanish medical condition pages.")
