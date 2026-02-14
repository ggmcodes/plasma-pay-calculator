#!/usr/bin/env python3
"""Generate Round 3 Spanish blog pages: 15 Medical Condition pages"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch5_spanish_template import make_es_page, make_faq, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es
ES_BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'es', 'blog')

# ============================================================
# Medical condition page definitions
# Each tuple: (slug, en_equivalent, condition_es, condition_en,
#               can_donate, key_info, medications_section, screening_tips, extra_content)
# ============================================================

def gen_medical_page(slug, en_equiv, condition_es, title, meta_desc, can_donate_text,
                     meds_html, screening_html, extra_html, faq_list):
    toc = [
        ('respuesta', 'Respuesta Rapida'),
        ('elegibilidad', 'Elegibilidad'),
        ('medicamentos', 'Medicamentos'),
        ('screening', 'En el Screening'),
        ('consejos', 'Consejos'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = f'''
<div class="highlight-box" id="respuesta">
<h3>Respuesta Rapida</h3>
{can_donate_text}
</div>

<h2 id="elegibilidad">Elegibilidad para Donar con {condition_es}</h2>
{extra_html}

{AFFILIATE_ES}

<h2 id="medicamentos">Medicamentos y Donacion de Plasma</h2>
{meds_html}

{PRO_TOOLKIT_ES}

<h2 id="screening">Que Decir en el Screening Medico</h2>
{screening_html}

<h2 id="consejos">Consejos para Donantes con {condition_es}</h2>
<ul>
<li><strong>Hidratacion:</strong> Toma al menos 64 oz de agua el dia anterior y el dia de la donacion</li>
<li><strong>Alimentacion:</strong> Come una comida rica en proteina 2-3 horas antes de donar</li>
<li><strong>Descanso:</strong> Duerme bien la noche anterior a tu cita</li>
<li><strong>Medicamentos:</strong> Toma tus medicamentos como de costumbre a menos que el centro indique lo contrario</li>
<li><strong>Honestidad:</strong> Se transparente sobre tu condicion y medicamentos en el screening</li>
</ul>

{related_es([
    ('/es/blog/que-descalifica-donar-plasma-2026.html', 'Que Descalifica para Donar Plasma'),
    ('/es/blog/medicamentos-donar-plasma-lista-2026.html', 'Lista de Medicamentos'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos de Donacion'),
    ('/es/blog/', 'Blog en Espanol'),
])}

<h2 id="faq">Preguntas Frecuentes</h2>
''' + '\n'.join(f'<h3>{fq["name"]}</h3>\n<p>{fq["acceptedAnswer"]["text"]}</p>' for fq in faq_list) + '''

<div class="related-articles">
<h3>Guias Relacionadas</h3>
<div class="related-grid">
<a href="/es/blog/requisitos-donacion-plasma.html" class="related-link">Requisitos</a>
<a href="/es/blog/medicamentos-donar-plasma-lista-2026.html" class="related-link">Medicamentos</a>
<a href="/es/blog/que-descalifica-donar-plasma-2026.html" class="related-link">Descalificaciones</a>
<a href="/es/" class="related-link">Calculadora</a>
</div>
</div>'''

    return make_es_page(slug, title, meta_desc, 'Condiciones Medicas', 9, toc, content, faq_list, en_equiv)


# ============ 1. LUPUS ============
def page_lupus():
    slug = 'donar-plasma-con-lupus-2026'
    en = 'can-you-donate-plasma-with-lupus-2026.html'
    condition = 'Lupus'
    title = 'Donar Plasma con Lupus 2026: Elegibilidad y Guia Completa'
    meta = 'Puedes donar plasma si tienes lupus? En la mayoria de los casos no es posible. Conoce las reglas, excepciones y alternativas para personas con lupus eritematoso.'

    can_donate = '''<p><strong>En la mayoria de los casos, no puedes donar plasma si tienes lupus eritematoso sistemico (LES)</strong>. El lupus es una enfermedad autoinmune que afecta directamente las proteinas del plasma sanguineo. La mayoria de los centros de plasma en Estados Unidos <strong>descalifican permanentemente</strong> a personas con lupus activo debido al riesgo para el receptor y para el donante.</p>'''

    meds = '''<p>Los medicamentos comunes para lupus generalmente son <strong>descalificantes</strong> para la donacion de plasma:</p>
<ul>
<li><strong>Inmunosupresores (metotrexato, azatioprina, micofenolato)</strong> — Descalificacion permanente en la mayoria de centros</li>
<li><strong>Corticosteroides (prednisona) en dosis altas</strong> — Descalificacion temporal o permanente segun la dosis</li>
<li><strong>Biologicos (belimumab/Benlysta)</strong> — Descalificacion por tratamiento biologico</li>
<li><strong>Hidroxicloroquina (Plaquenil)</strong> — Algunos centros pueden considerar casos muy leves solo con este medicamento</li>
<li><strong>AINEs (ibuprofeno, naproxeno)</strong> — Aceptados pero no cambian la descalificacion por lupus</li>
</ul>
<p><strong>Nota importante:</strong> Incluso si tu lupus esta en remision, la mayoria de los centros mantienen la descalificacion porque los anticuerpos en tu plasma pueden causar reacciones en los receptores de productos de plasma.</p>'''

    screening = '''<p>Si tienes lupus y quieres intentar donar plasma:</p>
<ol>
<li><strong>Llama al centro antes de ir</strong> — Pregunta especificamente si aceptan donantes con lupus para ahorrarte el viaje</li>
<li><strong>Lleva documentacion medica</strong> — Si tu medico confirma remision completa, lleva esa carta</li>
<li><strong>Se honesto</strong> — Menciona tu diagnostico de lupus directamente; ocultar informacion es peligroso</li>
<li><strong>Pregunta por alternativas</strong> — Algunos centros de investigacion buscan plasma de personas con enfermedades autoinmunes especificamente</li>
</ol>'''

    extra = '''<p>El lupus eritematoso sistemico es una enfermedad autoinmune que causa que el sistema inmunologico ataque los propios tejidos del cuerpo. Esto afecta directamente la composicion del plasma sanguineo, lo que presenta problemas tanto para el donante como para los receptores:</p>
<ul>
<li><strong>Riesgo para receptores:</strong> Los autoanticuerpos en el plasma pueden causar reacciones adversas</li>
<li><strong>Riesgo para el donante:</strong> La donacion puede desencadenar brotes de lupus</li>
<li><strong>Lupus leve en remision:</strong> Algunos centros pueden evaluar caso por caso, pero es raro</li>
<li><strong>Lupus cutaneo vs sistemico:</strong> El lupus cutaneo (solo piel) tiene ligeramente mejores probabilidades de aceptacion</li>
</ul>

<h3>Alternativas para Personas con Lupus</h3>
<ul>
<li><strong>Estudios clinicos:</strong> Algunos laboratorios pagan por plasma de personas con lupus para investigacion</li>
<li><strong>Donacion de sangre completa:</strong> Algunas organizaciones pueden aceptar donantes con lupus leve en remision</li>
<li><strong>Referir amigos:</strong> Gana bonos de referencia ($50-$100) enviando amigos elegibles a donar</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo lupus?",
                 "En la mayoria de los casos, no. El lupus es una enfermedad autoinmune que afecta las proteinas del plasma, y la mayoria de los centros descalifican permanentemente a personas con lupus activo."),
        make_faq("¿Que pasa si mi lupus esta en remision?",
                 "Incluso con lupus en remision, la mayoria de los centros mantienen la descalificacion. Algunos pueden evaluar caso por caso si tu medico certifica remision completa y solo tomas hidroxicloroquina."),
        make_faq("¿Puedo donar plasma si tengo lupus cutaneo?",
                 "El lupus cutaneo (que afecta solo la piel) tiene ligeramente mejores probabilidades de aceptacion que el lupus sistemico. Consulta directamente con el centro de tu area."),
        make_faq("¿Hay alternativas para ganar dinero si tengo lupus?",
                 "Si. Puedes ganar bonos de referencia ($50-$100) enviando amigos elegibles a donar. Tambien hay estudios clinicos que pagan por plasma de personas con enfermedades autoinmunes."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 2. ARTHRITIS ============
def page_artritis():
    slug = 'donar-plasma-con-artritis-2026'
    en = 'can-you-donate-plasma-with-arthritis-2026.html'
    condition = 'Artritis'
    title = 'Donar Plasma con Artritis 2026: Guia de Elegibilidad y Medicamentos'
    meta = 'Puedes donar plasma si tienes artritis? Depende del tipo. Artritis reumatoide vs osteoartritis, medicamentos permitidos y consejos para donantes con artritis en 2026.'

    can_donate = '''<p><strong>Depende del tipo de artritis.</strong> Si tienes <strong>osteoartritis</strong> (artritis degenerativa), generalmente <strong>si puedes donar plasma</strong> sin problemas. Si tienes <strong>artritis reumatoide</strong> u otra artritis autoinmune, la elegibilidad depende de tus medicamentos y la severidad de tu condicion. La clave esta en si tomas inmunosupresores o biologicos.</p>'''

    meds = '''<p>Tu elegibilidad depende mas de tus medicamentos que del diagnostico de artritis:</p>
<h3>Generalmente Aceptados</h3>
<ul>
<li><strong>AINEs (ibuprofeno, naproxeno, diclofenaco)</strong> — Aceptados en todos los centros</li>
<li><strong>Acetaminofen (Tylenol)</strong> — Sin restricciones</li>
<li><strong>Glucosamina y condroitina</strong> — Suplementos aceptados</li>
<li><strong>Prednisona en dosis bajas (menos de 10mg)</strong> — Generalmente aceptada</li>
</ul>

<h3>Pueden Descalificarte</h3>
<ul>
<li><strong>Metotrexato</strong> — Descalificacion en la mayoria de centros</li>
<li><strong>Biologicos (Humira, Enbrel, Remicade)</strong> — Descalificacion permanente</li>
<li><strong>Leflunomida (Arava)</strong> — Descalificacion por inmunosupresor</li>
<li><strong>Tofacitinib (Xeljanz)</strong> — Descalificacion en todos los centros principales</li>
<li><strong>Prednisona en dosis altas (mas de 20mg)</strong> — Descalificacion temporal</li>
</ul>'''

    screening = '''<p>Consejos para el screening medico con artritis:</p>
<ol>
<li><strong>Especifica el tipo de artritis</strong> — Di claramente si es osteoartritis o artritis reumatoide</li>
<li><strong>Lista tus medicamentos</strong> — Lleva una lista con nombres y dosis de todos tus medicamentos</li>
<li><strong>Menciona la estabilidad</strong> — Si tu condicion esta estable y controlada, resalta eso</li>
<li><strong>Comodidad del brazo:</strong> Si la artritis afecta tus brazos o manos, menciona si puedes mantener el brazo extendido durante 45-90 minutos</li>
</ol>'''

    extra = '''<h3>Osteoartritis (Artritis Degenerativa)</h3>
<p>La osteoartritis es la forma mas comun de artritis y <strong>generalmente no descalifica</strong> para donar plasma. Es una condicion mecanica, no autoinmune, que afecta el cartilago de las articulaciones:</p>
<ul>
<li><strong>Elegibilidad:</strong> Si en la mayoria de centros</li>
<li><strong>Medicamentos comunes:</strong> AINEs y acetaminofen son aceptados</li>
<li><strong>Consideracion:</strong> Si el dolor dificulta mantener el brazo extendido, consulta con el personal</li>
</ul>

<h3>Artritis Reumatoide</h3>
<p>La artritis reumatoide es autoinmune y la elegibilidad es mas complicada:</p>
<ul>
<li><strong>Sin inmunosupresores:</strong> Posible en algunos centros si solo tomas AINEs</li>
<li><strong>Con metotrexato o biologicos:</strong> Descalificacion en la mayoria de centros</li>
<li><strong>En remision sin medicamentos:</strong> Posible con documentacion medica</li>
</ul>

<h3>Artritis Psoriasica</h3>
<ul>
<li>Similar a la artritis reumatoide en terminos de elegibilidad</li>
<li>Los biologicos (comunes para esta condicion) descalifican</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo artritis?",
                 "Depende del tipo. Con osteoartritis generalmente si puedes donar. Con artritis reumatoide depende de tus medicamentos — los inmunosupresores y biologicos descalifican."),
        make_faq("¿Los medicamentos para artritis me descalifican?",
                 "Los AINEs como ibuprofeno son aceptados. Los inmunosupresores como metotrexato y biologicos como Humira o Enbrel generalmente descalifican."),
        make_faq("¿Puedo donar plasma si tomo metotrexato para artritis?",
                 "No, el metotrexato es un inmunosupresor que descalifica en la mayoria de los centros de plasma. Consulta con tu centro especifico para confirmar."),
        make_faq("¿La artritis afecta el proceso de donacion?",
                 "Si la artritis afecta tus brazos, puede ser incomodo mantener el brazo extendido 45-90 minutos. Pide una almohada de soporte y menciona tu condicion al personal."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 3. FIBROMYALGIA ============
def page_fibromialgia():
    slug = 'donar-plasma-con-fibromialgia-2026'
    en = 'can-you-donate-plasma-with-fibromyalgia-2026.html'
    condition = 'Fibromialgia'
    title = 'Donar Plasma con Fibromialgia 2026: Elegibilidad, Medicamentos y Consejos'
    meta = 'Puedes donar plasma si tienes fibromialgia? Si, en la mayoria de los casos. Guia sobre medicamentos como Lyrica, Cymbalta, gabapentina y consejos para manejar el dolor.'

    can_donate = '''<p><strong>Si, generalmente puedes donar plasma si tienes fibromialgia.</strong> La fibromialgia no es una enfermedad autoinmune ni infecciosa, por lo que <strong>no descalifica automaticamente</strong> para la donacion. La elegibilidad depende principalmente de tus medicamentos y de que tu condicion este suficientemente controlada para tolerar el procedimiento de donacion.</p>'''

    meds = '''<p>La mayoria de los medicamentos comunes para fibromialgia son <strong>aceptados</strong>:</p>
<h3>Generalmente Aceptados</h3>
<ul>
<li><strong>Pregabalina (Lyrica)</strong> — Aceptada en la mayoria de centros</li>
<li><strong>Gabapentina (Neurontin)</strong> — Generalmente aceptada</li>
<li><strong>Duloxetina (Cymbalta)</strong> — Antidepresivo SNRI aceptado</li>
<li><strong>Milnacipran (Savella)</strong> — Generalmente aceptado</li>
<li><strong>Amitriptilina</strong> — Aceptada con dosis estable</li>
<li><strong>AINEs (ibuprofeno, naproxeno)</strong> — Aceptados sin restricciones</li>
<li><strong>Acetaminofen (Tylenol)</strong> — Aceptado</li>
<li><strong>Ciclobenzaprina (Flexeril)</strong> — Relajante muscular generalmente aceptado</li>
</ul>

<h3>Posibles Problemas</h3>
<ul>
<li><strong>Opioides (tramadol, oxicodona)</strong> — Varia por centro; algunos descalifican por opioides</li>
<li><strong>Medicamentos controlados Schedule II</strong> — Pueden requerir revision adicional</li>
<li><strong>Cannabis medicinal</strong> — Aceptado en algunos centros; consulta la politica local</li>
</ul>'''

    screening = '''<ol>
<li><strong>Menciona tu diagnostico:</strong> Di que tienes fibromialgia y que esta controlada</li>
<li><strong>Lista tus medicamentos:</strong> Incluye nombre, dosis y tiempo que llevas tomandolos</li>
<li><strong>Describe tu nivel de dolor:</strong> Si puedes mantener el brazo extendido 45-90 minutos sin dolor severo</li>
<li><strong>Se honesto sobre brotes:</strong> Si estas en medio de un brote severo, considera posponer la donacion</li>
</ol>'''

    extra = '''<p>La fibromialgia es un sindrome de dolor cronico que afecta los musculos y tejidos blandos. No cambia la composicion del plasma, lo que significa que tu plasma es seguro para uso medico:</p>
<ul>
<li><strong>No autoinmune:</strong> Aunque antes se creia lo contrario, la fibromialgia no es clasificada como autoinmune</li>
<li><strong>No infecciosa:</strong> No hay riesgo de transmision por plasma</li>
<li><strong>Principal preocupacion:</strong> Comodidad del donante durante el procedimiento</li>
</ul>

<h3>Tips para Donar con Fibromialgia</h3>
<ul>
<li><strong>Elige dias buenos:</strong> Dona cuando tus sintomas esten mas controlados, no durante brotes</li>
<li><strong>Pide comodidades:</strong> Almohada extra, manta si tienes frio, ajuste de la silla</li>
<li><strong>Mangas largas opcionales:</strong> Si tienes sensibilidad al frio, lleva algo para cubrirte (pero el brazo de donacion debe estar descubierto)</li>
<li><strong>Horarios:</strong> Si tus sintomas son peores por la manana, programa citas por la tarde</li>
</ul>

<h3>Ganancia Potencial con Fibromialgia</h3>
<p>Si puedes donar regularmente, puedes ganar lo mismo que cualquier otro donante:</p>
<ul>
<li><strong>Nuevos donantes:</strong> $700-$1,200 en el primer mes con bonos</li>
<li><strong>Donantes regulares:</strong> $400-$800 mensuales donando dos veces por semana</li>
<li><strong>Ingreso anual:</strong> $4,800-$9,600 por ano</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo fibromialgia?",
                 "Si, en la mayoria de los casos. La fibromialgia no es autoinmune ni infecciosa, asi que generalmente no descalifica. Tu elegibilidad depende de tus medicamentos y tu capacidad de tolerar el procedimiento."),
        make_faq("¿Lyrica o gabapentina me descalifican para donar plasma?",
                 "No, pregabalina (Lyrica) y gabapentina (Neurontin) son generalmente aceptados en los centros de plasma. Informa al personal sobre tu medicamento y dosis."),
        make_faq("¿Donar plasma puede empeorar mi fibromialgia?",
                 "Algunas personas reportan fatiga temporal despues de donar, lo cual puede agravar sintomas de fibromialgia. Hidratate bien, come proteina y descansa despues de donar."),
        make_faq("¿Que hago si tengo un brote durante la donacion?",
                 "Informa al tecnico inmediatamente. Pueden pausar o detener el procedimiento. Es mejor posponer la donacion si estas en medio de un brote severo."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 4. EPILEPSY ============
def page_epilepsia():
    slug = 'donar-plasma-con-epilepsia-2026'
    en = 'can-you-donate-plasma-with-epilepsy-2026.html'
    condition = 'Epilepsia'
    title = 'Donar Plasma con Epilepsia 2026: Requisitos, Medicamentos y Reglas'
    meta = 'Puedes donar plasma si tienes epilepsia? Depende del control de convulsiones. Guia sobre medicamentos antiepilepticos, periodos de espera y reglas de los centros de plasma.'

    can_donate = '''<p><strong>Depende de tu historial de convulsiones.</strong> Si tu epilepsia esta <strong>bien controlada y no has tenido convulsiones en los ultimos 12 meses</strong>, muchos centros de plasma te permiten donar. Sin embargo, si has tenido una convulsion reciente o tus convulsiones no estan controladas, la mayoria de los centros te <strong>descalificaran temporalmente</strong>.</p>'''

    meds = '''<p>Los medicamentos antiepilepticos tienen reglas variadas:</p>
<h3>Generalmente Aceptados (con epilepsia controlada)</h3>
<ul>
<li><strong>Levetiracetam (Keppra)</strong> — Generalmente aceptado si no hay convulsiones recientes</li>
<li><strong>Lamotrigina (Lamictal)</strong> — Aceptada con epilepsia controlada</li>
<li><strong>Oxcarbazepina (Trileptal)</strong> — Generalmente aceptada</li>
<li><strong>Topiramato (Topamax)</strong> — Aceptado en la mayoria de centros</li>
<li><strong>Zonisamida (Zonegran)</strong> — Generalmente aceptada</li>
</ul>

<h3>Pueden Presentar Problemas</h3>
<ul>
<li><strong>Valproato (Depakote)</strong> — Algunos centros restringen por efectos en el higado</li>
<li><strong>Fenitoina (Dilantin)</strong> — Varia por centro; algunos requieren niveles estables</li>
<li><strong>Fenobarbital</strong> — Barbiturico que puede ser descalificante en algunos centros</li>
<li><strong>Carbamazepina (Tegretol)</strong> — Generalmente aceptada pero puede afectar conteos sanguineos</li>
<li><strong>Clobazam (Onfi)</strong> — Benzodiacepina que varia por centro</li>
</ul>'''

    screening = '''<ol>
<li><strong>Menciona tu ultima convulsion:</strong> La fecha exacta es importante — necesitas al menos 12 meses sin convulsiones</li>
<li><strong>Lista tus medicamentos antiepilepticos:</strong> Nombre, dosis, y cuanto tiempo llevas tomandolos</li>
<li><strong>Trae carta de tu neurologo:</strong> Una carta confirmando epilepsia controlada puede ayudar mucho</li>
<li><strong>Pregunta sobre el periodo de espera:</strong> Algunos centros requieren 6 meses, otros 12 meses sin convulsiones</li>
</ol>'''

    extra = '''<p>Las reglas sobre epilepsia y donacion de plasma varian significativamente entre centros:</p>

<h3>Reglas por Centro</h3>
<table><thead><tr><th>Centro</th><th>Requisito</th><th>Medicamentos</th></tr></thead><tbody>
<tr><td>CSL Plasma</td><td>12 meses sin convulsiones</td><td>Antiepilepticos aceptados si controlados</td></tr>
<tr><td>BioLife</td><td>12 meses sin convulsiones</td><td>Evaluacion caso por caso</td></tr>
<tr><td>Octapharma</td><td>6-12 meses sin convulsiones</td><td>La mayoria aceptados</td></tr>
<tr><td>Grifols</td><td>12 meses sin convulsiones</td><td>Requiere estabilidad de medicacion</td></tr>
</tbody></table>

<h3>Tipos de Convulsiones y Elegibilidad</h3>
<ul>
<li><strong>Epilepsia controlada (sin convulsiones 12+ meses):</strong> Elegible en la mayoria de centros</li>
<li><strong>Convulsiones febriles infantiles:</strong> Si no has tenido convulsiones desde la infancia, generalmente elegible</li>
<li><strong>Convulsiones parciales/focales controladas:</strong> Evaluacion caso por caso</li>
<li><strong>Convulsiones tonico-clonicas recientes:</strong> Descalificacion temporal (6-12 meses)</li>
</ul>

<h3>Preocupaciones de Seguridad</h3>
<p>La principal preocupacion no es la calidad del plasma, sino la seguridad del donante:</p>
<ul>
<li>Una convulsion durante la donacion podria causar lesiones por la aguja</li>
<li>La deshidratacion post-donacion podria reducir el umbral de convulsiones</li>
<li>Por eso la hidratacion es especialmente critica para donantes con epilepsia</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo epilepsia?",
                 "Si, si tu epilepsia esta controlada y no has tenido convulsiones en los ultimos 12 meses. La mayoria de centros requieren al menos 6-12 meses sin convulsiones y medicacion estable."),
        make_faq("¿Los medicamentos antiepilepticos descalifican para donar plasma?",
                 "La mayoria de antiepilepticos como levetiracetam (Keppra) y lamotrigina (Lamictal) son aceptados si tu epilepsia esta controlada. Algunos como fenobarbital pueden ser problematicos."),
        make_faq("¿Cuanto tiempo debo esperar despues de una convulsion para donar?",
                 "La mayoria de centros requieren 12 meses sin convulsiones. Algunos centros aceptan despues de 6 meses. Consulta directamente con el centro de tu area."),
        make_faq("¿Es seguro donar plasma con epilepsia?",
                 "Si tu epilepsia esta bien controlada, si. La principal precaucion es mantenerte muy bien hidratado ya que la deshidratacion puede reducir el umbral de convulsiones."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 5. MULTIPLE SCLEROSIS ============
def page_esclerosis_multiple():
    slug = 'donar-plasma-con-esclerosis-multiple-2026'
    en = 'can-you-donate-plasma-with-multiple-sclerosis-2026.html'
    condition = 'Esclerosis Multiple'
    title = 'Donar Plasma con Esclerosis Multiple 2026: Elegibilidad y Reglas'
    meta = 'Puedes donar plasma si tienes esclerosis multiple (EM)? En la mayoria de los casos, no. Conoce las reglas, excepciones y alternativas para personas con EM.'

    can_donate = '''<p><strong>En la mayoria de los casos, no puedes donar plasma si tienes esclerosis multiple (EM).</strong> La EM es una enfermedad autoinmune que afecta el sistema nervioso central. La mayoria de los centros de plasma <strong>descalifican permanentemente</strong> a personas con EM, principalmente por los medicamentos inmunosupresores utilizados para el tratamiento y por la naturaleza autoinmune de la enfermedad.</p>'''

    meds = '''<p>Los medicamentos para EM son generalmente <strong>descalificantes</strong>:</p>
<h3>Descalificacion Permanente</h3>
<ul>
<li><strong>Interferones (Avonex, Rebif, Betaseron)</strong> — Modificadores de la enfermedad, descalifican</li>
<li><strong>Acetato de glatiramer (Copaxone)</strong> — Descalificacion por tratamiento autoinmune</li>
<li><strong>Fingolimod (Gilenya)</strong> — Inmunosupresor, descalificacion permanente</li>
<li><strong>Natalizumab (Tysabri)</strong> — Biologico, descalificacion permanente</li>
<li><strong>Ocrelizumab (Ocrevus)</strong> — Anticuerpo monoclonal, descalificacion permanente</li>
<li><strong>Dimetilfumarato (Tecfidera)</strong> — Inmunomodulador, descalificacion</li>
</ul>

<h3>Casos Excepcionales</h3>
<ul>
<li><strong>EM diagnosticada pero sin tratamiento:</strong> Aun asi, la mayoria de centros descalifican por el diagnostico</li>
<li><strong>Sindrome clinicamente aislado (CIS):</strong> Puede evaluarse caso por caso en algunos centros</li>
</ul>'''

    screening = '''<ol>
<li><strong>Llama antes de ir:</strong> Es casi seguro que seras descalificado, ahorra tiempo llamando primero</li>
<li><strong>Pregunta por programas de investigacion:</strong> Algunos centros buscan plasma de personas con EM para estudios</li>
<li><strong>Se honesto:</strong> Nunca ocultes un diagnostico de EM — es peligroso para ti y para los receptores</li>
<li><strong>Explora alternativas:</strong> Hay otras formas de ingreso complementario disponibles</li>
</ol>'''

    extra = '''<p>La esclerosis multiple es una enfermedad autoinmune cronica donde el sistema inmunologico ataca la mielina (capa protectora) de los nervios:</p>
<ul>
<li><strong>Razon principal de descalificacion:</strong> Los medicamentos modificadores de la enfermedad son todos descalificantes</li>
<li><strong>El diagnostico en si:</strong> Incluso sin medicamentos, la naturaleza autoinmune es problematica</li>
<li><strong>Seguridad del donante:</strong> La fatiga post-donacion podria empeorar sintomas de EM</li>
</ul>

<h3>Alternativas para Personas con EM</h3>
<ul>
<li><strong>Estudios clinicos:</strong> Algunos laboratorios pagan $50-$200 por plasma de personas con EM para investigacion</li>
<li><strong>Programas de referencia:</strong> Gana $50-$100 por referir amigos elegibles a centros de plasma</li>
<li><strong>Encuestas medicas:</strong> Empresas de investigacion pagan por participacion en encuestas sobre EM</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo esclerosis multiple?",
                 "En la mayoria de los casos, no. La EM es una enfermedad autoinmune y los medicamentos utilizados para tratarla (interferones, inmunosupresores, biologicos) descalifican permanentemente en la mayoria de centros."),
        make_faq("¿Que pasa si mi EM esta en remision?",
                 "Incluso con EM en remision, la mayoria de centros mantienen la descalificacion. Los medicamentos modificadores de la enfermedad y la naturaleza autoinmune de la EM son las razones principales."),
        make_faq("¿Puedo donar plasma para investigacion con EM?",
                 "Si, algunos laboratorios y centros de investigacion buscan plasma de personas con enfermedades autoinmunes como la EM. Pregunta en tu centro sobre programas de investigacion."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 6. PSORIASIS ============
def page_psoriasis():
    slug = 'donar-plasma-con-psoriasis-2026'
    en = 'can-you-donate-plasma-with-psoriasis-2026.html'
    condition = 'Psoriasis'
    title = 'Donar Plasma con Psoriasis 2026: Elegibilidad, Tratamientos y Reglas'
    meta = 'Puedes donar plasma si tienes psoriasis? Si, en casos leves a moderados. Guia sobre tratamientos topicos, biologicos, metotrexato y reglas para donantes con psoriasis.'

    can_donate = '''<p><strong>Si, puedes donar plasma si tienes psoriasis leve a moderada</strong> que se controla con tratamientos topicos. Sin embargo, si tu psoriasis requiere <strong>biologicos o inmunosupresores</strong> (como Humira, Enbrel, o metotrexato), la mayoria de los centros te <strong>descalificaran</strong>. La clave esta en tu tratamiento actual, no en el diagnostico en si.</p>'''

    meds = '''<h3>Generalmente Aceptados</h3>
<ul>
<li><strong>Cremas con corticosteroides topicos</strong> — Aceptadas en todos los centros</li>
<li><strong>Calcipotriol (Dovonex)</strong> — Tratamiento topico aceptado</li>
<li><strong>Alquitran de hulla (coal tar)</strong> — Tratamiento topico aceptado</li>
<li><strong>Acido salicilico topico</strong> — Sin restricciones</li>
<li><strong>Retinoides topicos (tazarotene)</strong> — Generalmente aceptados</li>
<li><strong>Fototerapia (UVB)</strong> — No afecta la elegibilidad</li>
</ul>

<h3>Descalificantes</h3>
<ul>
<li><strong>Metotrexato</strong> — Inmunosupresor, descalificacion</li>
<li><strong>Adalimumab (Humira)</strong> — Biologico, descalificacion permanente</li>
<li><strong>Etanercept (Enbrel)</strong> — Biologico, descalificacion permanente</li>
<li><strong>Ustekinumab (Stelara)</strong> — Biologico, descalificacion</li>
<li><strong>Secukinumab (Cosentyx)</strong> — Biologico, descalificacion</li>
<li><strong>Acitretina (Soriatane)</strong> — Retinoide oral, varia por centro</li>
<li><strong>Apremilast (Otezla)</strong> — Inmunomodulador, consulta con el centro</li>
<li><strong>Ciclosporina</strong> — Inmunosupresor, descalificacion</li>
</ul>'''

    screening = '''<ol>
<li><strong>Menciona solo los medicamentos actuales:</strong> Si antes tomabas biologicos pero ahora solo usas cremas, menciona tu tratamiento actual</li>
<li><strong>Muestra tus brazos:</strong> El personal necesita ver que tienes venas accesibles y que no hay placas severas en el area de puncion</li>
<li><strong>Explica la severidad:</strong> Si tu psoriasis es leve y controlada con topicos, enfatiza eso</li>
<li><strong>Periodo de espera post-biologicos:</strong> Si dejaste de tomar biologicos, pregunta cuanto tiempo debes esperar antes de ser elegible</li>
</ol>'''

    extra = '''<p>La psoriasis es una condicion autoinmune de la piel, pero su impacto en la donacion de plasma depende de la severidad y el tratamiento:</p>

<h3>Psoriasis Leve (Elegible)</h3>
<ul>
<li>Afecta menos del 3% del cuerpo</li>
<li>Controlada con cremas y topicos</li>
<li>No afecta el area del brazo donde se inserta la aguja</li>
<li><strong>Puedes donar normalmente</strong></li>
</ul>

<h3>Psoriasis Moderada (Posiblemente Elegible)</h3>
<ul>
<li>Afecta 3-10% del cuerpo</li>
<li>Si solo usas topicos y fototerapia, posiblemente elegible</li>
<li>Si el area del brazo esta afectada, puede ser problematico</li>
</ul>

<h3>Psoriasis Severa (Probablemente No Elegible)</h3>
<ul>
<li>Afecta mas del 10% del cuerpo</li>
<li>Requiere biologicos o inmunosupresores orales</li>
<li>Los medicamentos sistemicos descalifican</li>
</ul>

<h3>Consideracion Importante sobre el Sitio de Puncion</h3>
<p>Incluso con psoriasis leve, si tienes placas activas en la fosa antecubital (la parte interior del codo donde insertan la aguja), el centro podria rechazarte por esa visita hasta que la piel sane.</p>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo psoriasis?",
                 "Si, si tu psoriasis es leve a moderada y se controla con tratamientos topicos (cremas). Si tomas biologicos como Humira o Enbrel, o inmunosupresores como metotrexato, seras descalificado."),
        make_faq("¿Los biologicos para psoriasis descalifican para donar plasma?",
                 "Si. Biologicos como Humira, Enbrel, Stelara y Cosentyx descalifican permanentemente. Si dejaste de tomarlos, pregunta por el periodo de espera requerido."),
        make_faq("¿Que pasa si tengo psoriasis en los brazos?",
                 "Si tienes placas activas en el area donde insertan la aguja (fosa antecubital), pueden rechazarte para esa visita. Si la psoriasis esta en otras partes del cuerpo y tus brazos estan limpios, generalmente no hay problema."),
        make_faq("¿Donar plasma puede empeorar mi psoriasis?",
                 "No hay evidencia de que la donacion de plasma empeore la psoriasis. Sin embargo, si notas brotes despues de donar, consulta con tu dermatologo."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 7. SLEEP APNEA ============
def page_apnea_sueno():
    slug = 'donar-plasma-con-apnea-sueno-2026'
    en = 'can-you-donate-plasma-with-sleep-apnea-2026.html'
    condition = 'Apnea del Sueno'
    title = 'Donar Plasma con Apnea del Sueno 2026: Elegibilidad y Guia'
    meta = 'Puedes donar plasma si tienes apnea del sueno? Si, en la mayoria de los casos. Guia sobre CPAP, somnolencia, medicamentos y consejos para donantes con apnea del sueno.'

    can_donate = '''<p><strong>Si, generalmente puedes donar plasma si tienes apnea del sueno.</strong> La apnea obstructiva del sueno (AOS) <strong>no descalifica</strong> para la donacion de plasma en la mayoria de los centros. El uso de CPAP no afecta tu elegibilidad. La unica preocupacion seria si tienes complicaciones graves como insuficiencia cardiaca o si tomas medicamentos que afecten la coagulacion.</p>'''

    meds = '''<p>Los tratamientos comunes para apnea del sueno son <strong>compatibles con la donacion</strong>:</p>
<h3>Aceptados</h3>
<ul>
<li><strong>CPAP/BiPAP</strong> — Dispositivo de presion positiva, no es un medicamento, no afecta</li>
<li><strong>Dispositivos orales/mandibulares</strong> — No afectan la donacion</li>
<li><strong>Modafinilo (Provigil)</strong> — Generalmente aceptado para somnolencia diurna</li>
<li><strong>Armodafinilo (Nuvigil)</strong> — Generalmente aceptado</li>
</ul>

<h3>Posibles Problemas</h3>
<ul>
<li><strong>Medicamentos para complicaciones cardiacas</strong> — Si tienes problemas cardiacos por la apnea, esos medicamentos pueden ser descalificantes</li>
<li><strong>Solriamfetol (Sunosi)</strong> — Relativamente nuevo, consulta con el centro</li>
<li><strong>Estimulantes fuertes</strong> — Algunos centros tienen restricciones</li>
</ul>'''

    screening = '''<ol>
<li><strong>Menciona tu diagnostico:</strong> Apnea del sueno generalmente no causa preocupacion en el screening</li>
<li><strong>Confirma que usas CPAP:</strong> Mostrar que tratas tu condicion es positivo</li>
<li><strong>Menciona complicaciones:</strong> Si tienes hipertension o problemas cardiacos relacionados, mencionalo</li>
<li><strong>Estado de alerta:</strong> Si la somnolencia diurna es severa, considera donar cuando estes mas alerta</li>
</ol>'''

    extra = '''<p>La apnea del sueno es un trastorno del sueno donde la respiracion se detiene y reinicia repetidamente durante el sueno. No afecta la composicion del plasma:</p>
<ul>
<li><strong>Apnea obstructiva del sueno:</strong> La mas comun, generalmente elegible para donar</li>
<li><strong>Apnea central del sueno:</strong> Menos comun, puede requerir evaluacion adicional si hay condiciones cardiacas asociadas</li>
<li><strong>CPAP:</strong> El uso de CPAP muestra que manejas tu condicion activamente</li>
</ul>

<h3>Consejos Especificos para Donantes con Apnea</h3>
<ul>
<li><strong>Duerme con tu CPAP la noche anterior:</strong> Llega descansado para que la donacion sea mas comoda</li>
<li><strong>Evita donar si estas extremadamente cansado:</strong> La fatiga excesiva puede empeorar con la donacion</li>
<li><strong>Hidratacion extra:</strong> La deshidratacion puede empeorar la fatiga diurna</li>
<li><strong>Programa citas temprano:</strong> Cuando tu nivel de energia esta mas alto</li>
</ul>

<h3>Cuanto Puedes Ganar</h3>
<p>Con apnea del sueno controlada, puedes ganar igual que cualquier donante:</p>
<ul>
<li><strong>$50-$100 por visita</strong> como donante regular</li>
<li><strong>$700-$1,200 el primer mes</strong> con bonos de nuevo donante</li>
<li><strong>$400-$800 mensuales</strong> donando dos veces por semana</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo apnea del sueno?",
                 "Si, la apnea del sueno generalmente no descalifica para donar plasma. El uso de CPAP no afecta tu elegibilidad. Solo podria haber problemas si tienes complicaciones cardiacas graves."),
        make_faq("¿El uso de CPAP afecta la donacion de plasma?",
                 "No. El CPAP es un dispositivo, no un medicamento, y no afecta la composicion de tu plasma ni tu elegibilidad para donar."),
        make_faq("¿Puedo donar plasma si tomo modafinilo para la somnolencia?",
                 "Generalmente si. Modafinilo y armodafinilo son aceptados en la mayoria de centros de plasma. Informa al personal sobre tu medicamento."),
        make_faq("¿La donacion de plasma puede empeorar mi fatiga?",
                 "La donacion puede causar fatiga temporal. Si ya tienes somnolencia por la apnea, hidratate extra y descansa despues de donar. Dona en dias cuando estes mas descansado."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 8. KIDNEY DISEASE ============
def page_enfermedad_renal():
    slug = 'donar-plasma-con-enfermedad-renal-2026'
    en = 'can-you-donate-plasma-with-kidney-disease-2026.html'
    condition = 'Enfermedad Renal'
    title = 'Donar Plasma con Enfermedad Renal 2026: Elegibilidad y Restricciones'
    meta = 'Puedes donar plasma si tienes enfermedad renal? En la mayoria de los casos no. Conoce las reglas para enfermedad renal cronica, calculos renales, y dialisis.'

    can_donate = '''<p><strong>En general, no puedes donar plasma si tienes enfermedad renal cronica (ERC).</strong> La funcion renal comprometida afecta la capacidad del cuerpo para recuperarse despues de la donacion de plasma. Sin embargo, si tienes <strong>calculos renales resueltos</strong> o <strong>una infeccion renal pasada</strong> completamente tratada, podrias ser elegible despues de un periodo de espera.</p>'''

    meds = '''<p>Los medicamentos para enfermedad renal son generalmente <strong>descalificantes</strong>:</p>
<h3>Descalificacion</h3>
<ul>
<li><strong>Dialisis (hemodialisis o peritoneal)</strong> — Descalificacion permanente</li>
<li><strong>Inmunosupresores post-trasplante renal</strong> — Descalificacion permanente</li>
<li><strong>Eritropoyetina (EPO)</strong> — Descalificacion</li>
<li><strong>Calcitriol para ERC</strong> — Indica enfermedad avanzada, descalificacion</li>
</ul>

<h3>Posiblemente Aceptados</h3>
<ul>
<li><strong>Alopurinol (para calculos de acido urico)</strong> — Generalmente aceptado si no hay ERC</li>
<li><strong>Tamsulosina (Flomax, para calculos)</strong> — Puede ser aceptado</li>
<li><strong>Antibioticos (para infeccion renal pasada)</strong> — Aceptado despues de completar tratamiento</li>
<li><strong>Antihipertensivos (para proteger los rinones)</strong> — Depende de la funcion renal</li>
</ul>'''

    screening = '''<ol>
<li><strong>Se especifico sobre tu condicion:</strong> Distingue entre calculos renales, infeccion renal y enfermedad renal cronica</li>
<li><strong>Conoce tu nivel de funcion renal:</strong> Si tu GFR (tasa de filtracion glomerular) es normal, mencionalo</li>
<li><strong>Historial de calculos:</strong> Si tuviste un calculo renal pero se resolvio completamente, eso es muy diferente a ERC</li>
<li><strong>Llama antes:</strong> Si tienes cualquier condicion renal, llama al centro antes de ir</li>
</ol>'''

    extra = '''<h3>Calculos Renales vs Enfermedad Renal Cronica</h3>
<p>Es importante distinguir entre estas condiciones:</p>

<h4>Calculos Renales (Posiblemente Elegible)</h4>
<ul>
<li>Si el calculo ya paso o fue removido quirurgicamente</li>
<li>Sin problemas renales residuales</li>
<li>Generalmente puedes donar despues de recuperarte completamente</li>
<li>Periodo de espera tipico: 30-90 dias despues de la resolucion</li>
</ul>

<h4>Infeccion Renal (Pielonefritis) — Elegible Despues de Tratamiento</h4>
<ul>
<li>Completar todos los antibioticos</li>
<li>Esperar al menos 30 dias despues de finalizar tratamiento</li>
<li>Confirmacion de que la infeccion se resolvio</li>
</ul>

<h4>Enfermedad Renal Cronica (No Elegible)</h4>
<ul>
<li>ERC estadio 3-5: Descalificacion permanente</li>
<li>Pacientes en dialisis: Descalificacion permanente</li>
<li>Post-trasplante renal: Descalificacion permanente (inmunosupresores)</li>
</ul>

<h3>Por Que la Enfermedad Renal Descalifica</h3>
<p>La donacion de plasma requiere que los rinones funcionen normalmente para:</p>
<ul>
<li>Filtrar y reemplazar las proteinas perdidas en la donacion</li>
<li>Manejar el equilibrio de liquidos despues de la donacion</li>
<li>Procesar el citrato (anticoagulante) usado durante el procedimiento</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo enfermedad renal?",
                 "Generalmente no. La enfermedad renal cronica descalifica permanentemente porque los rinones necesitan funcionar normalmente para recuperarse de la donacion. Los calculos renales resueltos si pueden permitir la donacion."),
        make_faq("¿Puedo donar plasma despues de un calculo renal?",
                 "Si, generalmente puedes donar plasma despues de que un calculo renal se resuelva completamente. El periodo de espera tipico es 30-90 dias. Necesitas que tu funcion renal sea normal."),
        make_faq("¿La dialisis descalifica para donar plasma?",
                 "Si, la dialisis (hemodialisis o peritoneal) descalifica permanentemente para la donacion de plasma. Tu cuerpo no puede manejar la perdida y recuperacion de proteinas que requiere la donacion."),
        make_faq("¿Puedo donar plasma con un solo rinon?",
                 "Depende. Si tienes un solo rinon que funciona normalmente, algunos centros pueden aceptarte. Consulta directamente con el medico del centro de plasma."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 9. HERPES ============
def page_herpes():
    slug = 'donar-plasma-con-herpes-2026'
    en = 'can-you-donate-plasma-with-herpes-2026.html'
    condition = 'Herpes'
    title = 'Donar Plasma con Herpes 2026: Reglas, Brotes y Elegibilidad'
    meta = 'Puedes donar plasma si tienes herpes (HSV-1 o HSV-2)? Si, cuando no tienes brote activo. Guia sobre reglas, medicamentos antivirales y periodos de espera.'

    can_donate = '''<p><strong>Si, puedes donar plasma si tienes herpes (HSV-1 o HSV-2)</strong> siempre que <strong>no tengas un brote activo</strong> al momento de la donacion. El herpes es extremadamente comun (mas del 50% de la poblacion tiene HSV-1) y no descalifica permanentemente. Solo necesitas esperar hasta que cualquier brote activo se resuelva completamente.</p>'''

    meds = '''<h3>Generalmente Aceptados</h3>
<ul>
<li><strong>Valaciclovir (Valtrex)</strong> — Antiviral aceptado en todos los centros principales</li>
<li><strong>Aciclovir (Zovirax)</strong> — Aceptado sin restricciones</li>
<li><strong>Famciclovir (Famvir)</strong> — Generalmente aceptado</li>
<li><strong>Terapia supresiva diaria</strong> — Tomar antivirales diarios no descalifica</li>
<li><strong>Cremas antivirales topicas</strong> — Aceptadas</li>
</ul>

<h3>Notas Importantes</h3>
<ul>
<li>Los antivirales para herpes <strong>no descalifican</strong> para donar plasma</li>
<li>Puedes tomar tu medicamento el dia de la donacion</li>
<li>La terapia supresiva diaria es preferida porque reduce la probabilidad de brotes</li>
</ul>'''

    screening = '''<ol>
<li><strong>No necesitas revelar el herpes si no preguntan:</strong> Muchos centros no preguntan especificamente sobre herpes oral (HSV-1)</li>
<li><strong>Si preguntan, se honesto:</strong> Menciona que tienes herpes y que no tienes brote activo</li>
<li><strong>Lista tus antivirales:</strong> Los antivirales para herpes son aceptados, no tengas miedo de mencionarlos</li>
<li><strong>Verifica tu piel:</strong> Asegurate de que no tengas lesiones activas visibles, especialmente cerca de la boca o en los brazos</li>
</ol>'''

    extra = '''<h3>HSV-1 vs HSV-2 y la Donacion</h3>
<table><thead><tr><th>Tipo</th><th>Ubicacion Comun</th><th>Elegibilidad</th><th>Nota</th></tr></thead><tbody>
<tr><td>HSV-1 (oral)</td><td>Labios/boca</td><td>Si, sin brote activo</td><td>Muy comun, no preguntan en muchos centros</td></tr>
<tr><td>HSV-2 (genital)</td><td>Area genital</td><td>Si, sin brote activo</td><td>Mencionar si preguntan sobre ETS</td></tr>
<tr><td>Herpes zoster (culebrilla)</td><td>Torso/cara</td><td>Si, despues del brote</td><td>Esperar a que las lesiones sanen completamente</td></tr>
</tbody></table>

<h3>Cuando NO Puedes Donar</h3>
<ul>
<li><strong>Brote activo actual:</strong> Espera hasta que las lesiones sanen completamente</li>
<li><strong>Sintomas prodromicos:</strong> Si sientes hormigueo o ardor que precede un brote, espera</li>
<li><strong>Herpes zoster activo (culebrilla):</strong> Espera hasta resolucion completa, tipicamente 2-4 semanas</li>
</ul>

<h3>Cuanto Esperar Despues de un Brote</h3>
<ul>
<li><strong>Herpes oral:</strong> Espera hasta que el fuego/ampolla este completamente sanado (tipicamente 7-14 dias)</li>
<li><strong>Herpes genital:</strong> Espera hasta resolucion completa de lesiones</li>
<li><strong>Herpes zoster:</strong> Espera 2-4 semanas despues de que las lesiones sanen</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo herpes?",
                 "Si, puedes donar plasma con herpes (HSV-1 o HSV-2) siempre que no tengas un brote activo. Espera hasta que las lesiones sanen completamente antes de donar."),
        make_faq("¿Los medicamentos para herpes descalifican para donar plasma?",
                 "No. Los antivirales como valaciclovir (Valtrex), aciclovir (Zovirax) y famciclovir (Famvir) son aceptados en todos los centros principales. Puedes tomarlos el dia de la donacion."),
        make_faq("¿Cuanto tiempo esperar despues de un brote de herpes para donar?",
                 "Espera hasta que las lesiones esten completamente sanadas. Para herpes oral, tipicamente 7-14 dias. Para herpes genital, hasta resolucion completa. Para herpes zoster, 2-4 semanas."),
        make_faq("¿Tengo que decir que tengo herpes en el screening?",
                 "Solo si preguntan directamente sobre herpes o ETS. Lo mas importante es que no tengas un brote activo y que declares cualquier medicamento antiviral que tomes."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 10. POST-COVID ============
def page_despues_covid():
    slug = 'donar-plasma-despues-covid-2026'
    en = 'can-you-donate-plasma-after-covid-2026.html'
    condition = 'COVID-19'
    title = 'Donar Plasma Despues de COVID 2026: Reglas y Tiempo de Espera'
    meta = 'Puedes donar plasma despues de tener COVID-19? Si, despues del periodo de espera. Guia sobre reglas actualizadas 2026, sintomas de COVID largo y cuando puedes volver a donar.'

    can_donate = '''<p><strong>Si, puedes donar plasma despues de tener COVID-19</strong> una vez que cumplas con el periodo de espera requerido. En 2026, la mayoria de los centros requieren que estes <strong>completamente recuperado y sin sintomas por al menos 14 dias</strong>. El COVID ya no requiere prueba negativa en la mayoria de centros — solo necesitas estar asintomatico.</p>'''

    meds = '''<p>Los medicamentos relacionados con COVID tienen diferentes reglas:</p>
<h3>Aceptados Despues de Completar Tratamiento</h3>
<ul>
<li><strong>Paxlovid (nirmatrelvir/ritonavir)</strong> — Esperar 14 dias despues de completar el curso</li>
<li><strong>Antibioticos para infecciones secundarias</strong> — Esperar hasta completar el tratamiento</li>
<li><strong>Inhaladores para sintomas respiratorios</strong> — Generalmente aceptados</li>
<li><strong>Medicamentos de venta libre (Tylenol, ibuprofeno)</strong> — Aceptados</li>
</ul>

<h3>Puede Requerir Espera Adicional</h3>
<ul>
<li><strong>Molnupiravir (Lagevrio)</strong> — Consultar periodo de espera especifico del centro</li>
<li><strong>Anticuerpos monoclonales</strong> — Tipicamente 90 dias de espera despues del tratamiento</li>
<li><strong>Plasma convaleciente previo:</strong> Si recibiste transfusion de plasma, esperar 90 dias</li>
</ul>'''

    screening = '''<ol>
<li><strong>Confirma que estas asintomatico:</strong> Sin fiebre, tos, dolor de garganta, perdida de olfato/gusto</li>
<li><strong>Menciona la fecha de tus sintomas:</strong> El centro calculara si cumpliste el periodo de espera</li>
<li><strong>Declara tratamientos recibidos:</strong> Menciona si tomaste Paxlovid u otros antivirales</li>
<li><strong>COVID largo:</strong> Si tienes sintomas persistentes, el centro evaluara caso por caso</li>
</ol>'''

    extra = '''<h3>Periodos de Espera por Situacion</h3>
<table><thead><tr><th>Situacion</th><th>Periodo de Espera</th><th>Requisito</th></tr></thead><tbody>
<tr><td>COVID leve (sin tratamiento)</td><td>14 dias sin sintomas</td><td>Completamente asintomatico</td></tr>
<tr><td>COVID con Paxlovid</td><td>14 dias despues de completar</td><td>Sin sintomas residuales</td></tr>
<tr><td>COVID con anticuerpos monoclonales</td><td>90 dias</td><td>Sin sintomas</td></tr>
<tr><td>Vacuna COVID reciente</td><td>0-48 horas</td><td>Sin reacciones adversas</td></tr>
<tr><td>COVID largo (sintomas persistentes)</td><td>Evaluacion caso por caso</td><td>Depende de los sintomas</td></tr>
</tbody></table>

<h3>COVID Largo y Donacion de Plasma</h3>
<p>Si tienes sintomas persistentes de COVID (COVID largo), tu elegibilidad depende de los sintomas especificos:</p>
<ul>
<li><strong>Fatiga persistente leve:</strong> Posiblemente elegible si los demas indicadores son normales</li>
<li><strong>Problemas respiratorios continuos:</strong> Probablemente descalificacion temporal</li>
<li><strong>Niebla mental:</strong> Generalmente no descalifica si los signos vitales son normales</li>
<li><strong>Problemas cardiacos post-COVID:</strong> Descalificacion hasta evaluacion medica completa</li>
</ul>

<h3>Reglas 2026 vs Reglas Anteriores</h3>
<p>Las reglas de COVID para donacion de plasma se han relajado significativamente desde la pandemia:</p>
<ul>
<li><strong>Ya no se requiere prueba negativa</strong> en la mayoria de centros</li>
<li><strong>Periodo de espera reducido:</strong> 14 dias vs 28 dias anteriores</li>
<li><strong>Vacunacion:</strong> Las vacunas COVID no requieren periodo de espera significativo</li>
</ul>'''

    faqs = [
        make_faq("¿Cuanto tiempo despues de COVID puedo donar plasma?",
                 "Debes esperar al menos 14 dias despues de que tus sintomas desaparezcan completamente. Si recibiste anticuerpos monoclonales, el periodo de espera es de 90 dias."),
        make_faq("¿Necesito una prueba negativa de COVID para donar plasma?",
                 "En 2026, la mayoria de centros ya no requieren prueba negativa. Solo necesitas estar completamente asintomatico por al menos 14 dias."),
        make_faq("¿Puedo donar plasma si tengo COVID largo?",
                 "Depende de tus sintomas. Si tu fatiga es leve y tus signos vitales son normales, posiblemente si. Problemas respiratorios o cardiacos continuos probablemente descalifican temporalmente."),
        make_faq("¿La vacuna de COVID afecta la donacion de plasma?",
                 "Minimamente. La mayoria de centros solo requieren 0-48 horas de espera despues de la vacuna COVID, siempre que no tengas reacciones adversas significativas."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 11. HEART CONDITION ============
def page_enfermedad_corazon():
    slug = 'donar-plasma-con-enfermedad-corazon-2026'
    en = 'can-you-donate-plasma-with-heart-disease-2026.html'
    condition = 'Enfermedad del Corazon'
    title = 'Donar Plasma con Enfermedad del Corazon 2026: Riesgos y Elegibilidad'
    meta = 'Puedes donar plasma si tienes enfermedad cardiaca? En la mayoria de los casos no. Guia sobre insuficiencia cardiaca, arritmias, soplos, y reglas de los centros de plasma.'

    can_donate = '''<p><strong>En la mayoria de los casos, no puedes donar plasma si tienes una enfermedad cardiaca significativa.</strong> Los centros de plasma descalifican a personas con <strong>insuficiencia cardiaca, arritmias no controladas, enfermedad coronaria activa y antecedentes de infarto</strong>. Sin embargo, condiciones leves como <strong>soplo cardiaco benigno</strong> o <strong>prolapso de valvula mitral asintomatico</strong> pueden ser aceptadas.</p>'''

    meds = '''<h3>Generalmente Descalificantes</h3>
<ul>
<li><strong>Anticoagulantes (warfarina, eliquis, xarelto)</strong> — Descalificacion por riesgo de sangrado</li>
<li><strong>Antiarritmicos (amiodarona, flecainida)</strong> — Indica arritmia significativa, descalificacion</li>
<li><strong>Digoxina</strong> — Indica insuficiencia cardiaca, descalificacion</li>
<li><strong>Nitroglicerina</strong> — Indica angina activa, descalificacion</li>
</ul>

<h3>Posiblemente Aceptados</h3>
<ul>
<li><strong>Antihipertensivos (lisinopril, amlodipino)</strong> — Aceptados si la presion esta controlada</li>
<li><strong>Estatinas (atorvastatina, rosuvastatina)</strong> — Aceptadas para colesterol</li>
<li><strong>Beta-bloqueadores en dosis baja</strong> — Depende de la razon de prescripcion</li>
<li><strong>Aspirina en dosis baja (81mg)</strong> — Generalmente aceptada</li>
</ul>'''

    screening = '''<ol>
<li><strong>Se especifico sobre tu condicion cardiaca:</strong> Un soplo benigno es muy diferente de insuficiencia cardiaca</li>
<li><strong>Lleva documentacion:</strong> Si tu cardiologo confirma que tu condicion es leve, una carta puede ayudar</li>
<li><strong>Menciona todos tus medicamentos cardiacos:</strong> Los anticoagulantes son un factor decisivo</li>
<li><strong>Llama antes:</strong> No vayas sin confirmar primero si tu condicion especifica es aceptada</li>
</ol>'''

    extra = '''<h3>Condiciones Cardiacas y Elegibilidad</h3>
<table><thead><tr><th>Condicion</th><th>Elegibilidad</th><th>Nota</th></tr></thead><tbody>
<tr><td>Soplo cardiaco benigno</td><td>Generalmente si</td><td>Con documentacion del cardiologo</td></tr>
<tr><td>Prolapso de valvula mitral (asintomatico)</td><td>Posiblemente si</td><td>Evaluacion caso por caso</td></tr>
<tr><td>Hipertension controlada</td><td>Si</td><td>Presion debe estar en rango aceptable el dia de la donacion</td></tr>
<tr><td>Arritmia no controlada</td><td>No</td><td>Descalificacion hasta que se controle</td></tr>
<tr><td>Insuficiencia cardiaca</td><td>No</td><td>Descalificacion permanente</td></tr>
<tr><td>Infarto previo</td><td>No</td><td>Descalificacion permanente en la mayoria de centros</td></tr>
<tr><td>Cirugia de bypass</td><td>No</td><td>Descalificacion permanente</td></tr>
<tr><td>Stent coronario</td><td>Probablemente no</td><td>Consulta con el centro</td></tr>
</tbody></table>

<h3>Riesgos de Donar con Enfermedad Cardiaca</h3>
<p>La donacion de plasma afecta el sistema cardiovascular:</p>
<ul>
<li><strong>Volumen de sangre:</strong> Se extrae temporalmente un volumen significativo de sangre</li>
<li><strong>Citrato:</strong> El anticoagulante usado puede afectar el ritmo cardiaco</li>
<li><strong>Estres cardiovascular:</strong> La donacion pone estres temporal en el corazon</li>
<li><strong>Cambios de presion:</strong> La presion arterial puede fluctuar durante la donacion</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo enfermedad del corazon?",
                 "En la mayoria de los casos, no. Insuficiencia cardiaca, arritmias, infarto previo y uso de anticoagulantes descalifican. Condiciones leves como soplo benigno pueden ser aceptadas."),
        make_faq("¿Los anticoagulantes descalifican para donar plasma?",
                 "Si. Warfarina, eliquis, xarelto y otros anticoagulantes descalifican porque la donacion requiere coagulacion normal para cerrar el sitio de puncion y prevenir complicaciones."),
        make_faq("¿Puedo donar plasma con un soplo cardiaco?",
                 "Si el soplo es benigno (funcional) y tu cardiologo confirma que es inofensivo, muchos centros te aceptaran. Lleva documentacion medica."),
        make_faq("¿La hipertension me descalifica para donar plasma?",
                 "No necesariamente. Si tu hipertension esta controlada con medicamentos y tu presion esta en rango aceptable el dia de la donacion (generalmente menos de 180/100), puedes donar."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 12. AUTOIMMUNE DISEASE ============
def page_enfermedad_autoinmune():
    slug = 'donar-plasma-con-enfermedad-autoinmune-2026'
    en = 'can-you-donate-plasma-with-autoimmune-disease-2026.html'
    condition = 'Enfermedades Autoinmunes'
    title = 'Donar Plasma con Enfermedad Autoinmune 2026: Guia Completa de Elegibilidad'
    meta = 'Puedes donar plasma con una enfermedad autoinmune? Depende del tipo. Guia sobre lupus, AR, Hashimoto, celiaca, Crohn y mas condiciones autoinmunes.'

    can_donate = '''<p><strong>Depende del tipo de enfermedad autoinmune y tus medicamentos.</strong> Algunas condiciones autoinmunes leves que se controlan con medicamentos no inmunosupresores <strong>permiten la donacion</strong>. Sin embargo, enfermedades autoinmunes que requieren <strong>biologicos, inmunosupresores o que afectan directamente la composicion de la sangre</strong> generalmente descalifican.</p>'''

    meds = '''<h3>Medicamentos Descalificantes (Comunes en Autoinmunes)</h3>
<ul>
<li><strong>Biologicos (Humira, Enbrel, Remicade, Stelara, Cosentyx)</strong> — Descalificacion permanente</li>
<li><strong>Metotrexato</strong> — Inmunosupresor, descalificacion</li>
<li><strong>Azatioprina (Imuran)</strong> — Inmunosupresor, descalificacion</li>
<li><strong>Micofenolato (CellCept)</strong> — Inmunosupresor, descalificacion</li>
<li><strong>Ciclosporina</strong> — Inmunosupresor, descalificacion</li>
<li><strong>Tacrolimus</strong> — Inmunosupresor, descalificacion</li>
</ul>

<h3>Medicamentos Generalmente Aceptados</h3>
<ul>
<li><strong>Levotiroxina (para Hashimoto)</strong> — Aceptada en todos los centros</li>
<li><strong>AINEs (ibuprofeno, naproxeno)</strong> — Aceptados</li>
<li><strong>Hidroxicloroquina (Plaquenil)</strong> — Puede ser aceptada en casos leves</li>
<li><strong>Sulfasalazina</strong> — Generalmente aceptada</li>
<li><strong>Mesalamina (para colitis ulcerosa)</strong> — Generalmente aceptada</li>
</ul>'''

    screening = '''<ol>
<li><strong>Nombra tu condicion especifica:</strong> "Enfermedad autoinmune" es muy amplio — se especifico (Hashimoto, celiaca, etc.)</li>
<li><strong>Lista TODOS tus medicamentos:</strong> Los medicamentos son el factor mas importante en la decision</li>
<li><strong>Enfatiza estabilidad:</strong> Si tu condicion esta bien controlada, resalta eso</li>
<li><strong>Llama antes de ir:</strong> Con enfermedades autoinmunes, siempre confirma por telefono primero</li>
</ol>'''

    extra = '''<h3>Enfermedades Autoinmunes por Elegibilidad</h3>
<table><thead><tr><th>Condicion</th><th>Elegibilidad Tipica</th><th>Factor Clave</th></tr></thead><tbody>
<tr><td>Hashimoto (hipotiroidismo)</td><td>Si, con levotiroxina</td><td>Solo reemplazo hormonal</td></tr>
<tr><td>Enfermedad celiaca</td><td>Si, con dieta sin gluten</td><td>Sin medicamentos inmunosupresores</td></tr>
<tr><td>Psoriasis leve</td><td>Si, con topicos</td><td>Sin biologicos</td></tr>
<tr><td>Vitiligo</td><td>Generalmente si</td><td>Condicion cosmetica</td></tr>
<tr><td>Artritis reumatoide</td><td>Depende</td><td>Sin metotrexato ni biologicos</td></tr>
<tr><td>Lupus</td><td>Generalmente no</td><td>Anticuerpos en plasma</td></tr>
<tr><td>Esclerosis multiple</td><td>Generalmente no</td><td>Medicamentos modificadores</td></tr>
<tr><td>Enfermedad de Crohn</td><td>Depende</td><td>Sin biologicos ni inmunosupresores</td></tr>
<tr><td>Colitis ulcerosa</td><td>Depende</td><td>Sin biologicos; mesalamina OK</td></tr>
<tr><td>Diabetes tipo 1</td><td>Si, si controlada</td><td>Insulina es aceptada</td></tr>
<tr><td>Enfermedad de Graves</td><td>Depende</td><td>Si esta controlada y estable</td></tr>
<tr><td>Sindrome de Sjogren</td><td>Generalmente no</td><td>Anticuerpos problematicos</td></tr>
</tbody></table>

<h3>Regla General para Enfermedades Autoinmunes</h3>
<p>La regla mas importante es:</p>
<ul>
<li><strong>Sin inmunosupresores ni biologicos = posiblemente elegible</strong></li>
<li><strong>Con inmunosupresores o biologicos = probablemente descalificado</strong></li>
<li><strong>Anticuerpos que afectan el plasma = probablemente descalificado</strong></li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo una enfermedad autoinmune?",
                 "Depende del tipo. Condiciones como Hashimoto (con levotiroxina), celiaca (con dieta) y vitiligo generalmente permiten donar. Lupus, EM y condiciones que requieren biologicos o inmunosupresores generalmente descalifican."),
        make_faq("¿Los biologicos descalifican para donar plasma?",
                 "Si. Los biologicos como Humira, Enbrel, Remicade y Stelara descalifican permanentemente para la donacion de plasma porque alteran significativamente el sistema inmunologico."),
        make_faq("¿Puedo donar plasma si tengo Hashimoto?",
                 "Si. El hipotiroidismo de Hashimoto tratado con levotiroxina (Synthroid) es aceptado en todos los centros principales. Solo necesitas que tus niveles de tiroides esten estables."),
        make_faq("¿Puedo donar plasma si tengo enfermedad celiaca?",
                 "Si, la enfermedad celiaca controlada con dieta sin gluten generalmente es aceptada. Si solo sigues la dieta y no tomas inmunosupresores, puedes donar normalmente."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 13. HIGH CHOLESTEROL ============
def page_colesterol_alto():
    slug = 'donar-plasma-con-colesterol-alto-2026'
    en = 'can-you-donate-plasma-with-high-cholesterol-2026.html'
    condition = 'Colesterol Alto'
    title = 'Donar Plasma con Colesterol Alto 2026: Estatinas y Elegibilidad'
    meta = 'Puedes donar plasma si tienes colesterol alto? Si, en la mayoria de los casos. Guia sobre estatinas, trigliceridos, plasma lipemico y como mejorar tu plasma.'

    can_donate = '''<p><strong>Si, generalmente puedes donar plasma si tienes colesterol alto.</strong> El colesterol alto por si solo <strong>no descalifica</strong> para la donacion de plasma. Las estatinas y otros medicamentos para el colesterol son aceptados en todos los centros principales. Sin embargo, si tu plasma es <strong>lipemico</strong> (turbio/lechoso por exceso de grasa), tu donacion podria ser rechazada ese dia.</p>'''

    meds = '''<h3>Aceptados en Todos los Centros</h3>
<ul>
<li><strong>Atorvastatina (Lipitor)</strong> — Aceptada</li>
<li><strong>Rosuvastatina (Crestor)</strong> — Aceptada</li>
<li><strong>Simvastatina (Zocor)</strong> — Aceptada</li>
<li><strong>Pravastatina (Pravachol)</strong> — Aceptada</li>
<li><strong>Ezetimiba (Zetia)</strong> — Aceptada</li>
<li><strong>Fenofibrato (Tricor)</strong> — Aceptado</li>
<li><strong>Aceite de pescado/omega-3</strong> — Aceptado</li>
<li><strong>Niacina</strong> — Aceptada</li>
</ul>

<h3>Casos Especiales</h3>
<ul>
<li><strong>Inhibidores de PCSK9 (Repatha, Praluent)</strong> — Inyectables, consultar con el centro (generalmente aceptados)</li>
<li><strong>Colestiramina (Questran)</strong> — Generalmente aceptada</li>
</ul>'''

    screening = '''<ol>
<li><strong>Lista tus medicamentos:</strong> Las estatinas son comunes y aceptadas, no te preocupes por mencionarlas</li>
<li><strong>Cuida tu dieta pre-donacion:</strong> Evita comidas grasosas 24-48 horas antes de donar para reducir el riesgo de plasma lipemico</li>
<li><strong>Menciona si tu colesterol esta controlado:</strong> Los niveles controlados con medicamento no son problema</li>
<li><strong>Pregunta sobre plasma lipemico:</strong> Si tu plasma ha sido rechazado antes por ser lipemico, pregunta al personal por consejos</li>
</ol>'''

    extra = '''<h3>El Problema del Plasma Lipemico</h3>
<p>El colesterol alto no te descalifica, pero puede causar un problema practico:</p>
<ul>
<li><strong>Plasma lipemico:</strong> Es plasma que se ve turbio, lechoso o amarillo oscuro por exceso de grasa</li>
<li><strong>Consecuencia:</strong> Tu donacion puede ser rechazada (descartada) si el plasma es muy lipemico</li>
<li><strong>Frecuencia:</strong> No sucede siempre, pero es mas probable con colesterol alto no controlado</li>
<li><strong>Pago:</strong> Algunos centros te pagan aunque descarten tu plasma; otros no</li>
</ul>

<h3>Como Evitar Plasma Lipemico</h3>
<ul>
<li><strong>Evita comidas grasosas:</strong> No comas pizza, hamburguesas, frituras o comida rapida 24-48 horas antes</li>
<li><strong>Come proteinas magras:</strong> Pollo a la plancha, pescado, huevos, legumbres</li>
<li><strong>Hidratatate bien:</strong> El agua ayuda a diluir los lipidos en el plasma</li>
<li><strong>Toma tu estatina regularmente:</strong> No saltes dosis antes de donar</li>
<li><strong>Ejercicio regular:</strong> Ayuda a reducir trigliceridos</li>
</ul>

<h3>Cuanto Puedes Ganar</h3>
<p>Con colesterol controlado, ganas lo mismo que cualquier donante:</p>
<ul>
<li><strong>$50-$100 por visita</strong> como donante regular</li>
<li><strong>$700-$1,200 el primer mes</strong> con bonos de nuevo donante</li>
<li><strong>$400-$800 mensuales</strong> donando dos veces por semana</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo colesterol alto?",
                 "Si, el colesterol alto no descalifica para donar plasma. Las estatinas y otros medicamentos para el colesterol son aceptados. El unico problema posible es el plasma lipemico."),
        make_faq("¿Las estatinas descalifican para donar plasma?",
                 "No. Estatinas como atorvastatina (Lipitor), rosuvastatina (Crestor) y simvastatina (Zocor) son aceptadas en todos los centros de plasma."),
        make_faq("¿Que es plasma lipemico y como lo evito?",
                 "Plasma lipemico es plasma turbio o lechoso por exceso de grasa. Evitalo comiendo proteinas magras y evitando comidas grasosas 24-48 horas antes de donar. Toma tu estatina regularmente."),
        make_faq("¿Donar plasma ayuda a bajar el colesterol?",
                 "No directamente. La donacion de plasma no reduce significativamente los niveles de colesterol. Sigue tu tratamiento medico y dieta recomendada por tu doctor."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 14. ECZEMA ============
def page_eczema():
    slug = 'donar-plasma-con-eczema-2026'
    en = 'can-you-donate-plasma-with-eczema-2026.html'
    condition = 'Eczema'
    title = 'Donar Plasma con Eczema 2026: Elegibilidad, Cremas y Reglas'
    meta = 'Puedes donar plasma si tienes eczema? Si, en la mayoria de los casos. Guia sobre cremas con esteroides, Dupixent, y como donar si tienes dermatitis atopica.'

    can_donate = '''<p><strong>Si, generalmente puedes donar plasma si tienes eczema (dermatitis atopica)</strong> siempre que tu tratamiento sea <strong>topico</strong> (cremas y pomadas) y no tengas eczema activo severo en el <strong>area de la fosa antecubital</strong> (interior del codo donde insertan la aguja). Si tu eczema requiere <strong>biologicos como Dupixent</strong>, la elegibilidad varia por centro.</p>'''

    meds = '''<h3>Generalmente Aceptados</h3>
<ul>
<li><strong>Cremas con corticosteroides (hidrocortisona, betametasona, triamcinolona)</strong> — Aceptadas</li>
<li><strong>Inhibidores de calcineurina topicos (tacrolimus/Protopic, pimecrolimus/Elidel)</strong> — Generalmente aceptados (topicos)</li>
<li><strong>Emolientes y humectantes</strong> — Sin restricciones</li>
<li><strong>Antihistaminicos (cetirizina, loratadina, difenhidramina)</strong> — Aceptados</li>
<li><strong>Cremas con ceramidas</strong> — Sin restricciones</li>
</ul>

<h3>Pueden Causar Problemas</h3>
<ul>
<li><strong>Dupilumab (Dupixent)</strong> — Biologico inyectable; algunos centros lo aceptan, otros no. Consulta con tu centro</li>
<li><strong>Ciclosporina oral</strong> — Inmunosupresor, descalificacion</li>
<li><strong>Metotrexato (para eczema severo)</strong> — Inmunosupresor, descalificacion</li>
<li><strong>JAK inhibidores orales (Rinvoq, Cibinqo)</strong> — Inmunosupresores, descalificacion</li>
<li><strong>Prednisona oral (para brotes severos)</strong> — Depende de la dosis y duracion</li>
</ul>'''

    screening = '''<ol>
<li><strong>Muestra tus brazos:</strong> El personal necesita verificar que el area de puncion este libre de eczema activo</li>
<li><strong>Explica tu tratamiento:</strong> Si solo usas cremas topicas, enfatiza eso</li>
<li><strong>Si usas Dupixent:</strong> Menciona especificamente y pregunta si lo aceptan</li>
<li><strong>Lleva mangas cortas:</strong> Para que puedan inspeccionar facilmente tus brazos</li>
</ol>'''

    extra = '''<h3>La Regla del Area de Puncion</h3>
<p>La consideracion principal para donantes con eczema es el <strong>area de la fosa antecubital</strong> (interior del codo):</p>
<ul>
<li><strong>Sin eczema en el area:</strong> Puedes donar normalmente</li>
<li><strong>Eczema leve en el area:</strong> Algunos centros aceptan, otros piden que vuelvas cuando sane</li>
<li><strong>Eczema activo/abierto en el area:</strong> No pueden insertar la aguja — vuelve cuando sane</li>
<li><strong>Eczema en otras partes del cuerpo:</strong> Generalmente no afecta la elegibilidad</li>
</ul>

<h3>Consejos para Donantes con Eczema</h3>
<ul>
<li><strong>Hidrata tus brazos:</strong> Usa emolientes abundantes los dias previos para mantener la piel suave</li>
<li><strong>No te rasques:</strong> La piel irritada o con rasgunos puede impedir la donacion</li>
<li><strong>Trae tu crema:</strong> Aplica tu humectante despues de la donacion para proteger la piel</li>
<li><strong>Clima seco:</strong> Si tu eczema empeora en invierno, considera donar mas en verano cuando tu piel este mejor</li>
<li><strong>Evita irritantes:</strong> No uses jabones fuertes o alcohol en gel cerca del sitio de puncion antes de ir</li>
</ul>

<h3>Dupixent y Donacion de Plasma</h3>
<p>Dupixent (dupilumab) es un caso especial. Es un biologico, pero no es inmunosupresor en el sentido tradicional:</p>
<ul>
<li><strong>Algunos centros lo aceptan:</strong> Porque no suprime ampliamente el sistema inmune</li>
<li><strong>Otros lo rechazan:</strong> Porque sigue siendo un biologico inyectable</li>
<li><strong>Consejo:</strong> Llama al centro antes de ir si tomas Dupixent</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo eczema?",
                 "Si, en la mayoria de los casos puedes donar plasma con eczema. Lo mas importante es que no tengas eczema activo severo en el area del brazo donde insertan la aguja, y que tu tratamiento sea topico (cremas)."),
        make_faq("¿Las cremas con esteroides para eczema me descalifican?",
                 "No. Las cremas topicas con corticosteroides como hidrocortisona y betametasona son aceptadas en todos los centros de plasma."),
        make_faq("¿Puedo donar plasma si tomo Dupixent?",
                 "Varia por centro. Dupixent es un biologico, pero algunos centros lo aceptan porque no es un inmunosupresor tradicional. Llama a tu centro antes de ir para confirmar."),
        make_faq("¿Que pasa si tengo eczema en el brazo donde donan?",
                 "Si hay eczema activo severo o piel abierta en la fosa antecubital, no podran insertar la aguja. Espera a que sane y vuelve cuando el area este limpia."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ 15. MIGRAINES ============
def page_migranas():
    slug = 'donar-plasma-con-migranas-2026'
    en = 'can-you-donate-plasma-with-migraines-2026.html'
    condition = 'Migranas'
    title = 'Donar Plasma con Migranas 2026: Medicamentos y Consejos'
    meta = 'Puedes donar plasma si tienes migranas? Si, en la mayoria de los casos. Guia sobre triptanes, topiramato, Aimovig, y como prevenir migranas despues de donar plasma.'

    can_donate = '''<p><strong>Si, generalmente puedes donar plasma si tienes migranas.</strong> Las migranas no descalifican para la donacion de plasma en la mayoria de los centros. La mayoria de los medicamentos para migranas son aceptados. Sin embargo, <strong>no dones si estas en medio de un episodio de migrana</strong> — espera hasta que pase. Algunos donantes reportan que la deshidratacion post-donacion puede desencadenar migranas.</p>'''

    meds = '''<h3>Aceptados</h3>
<ul>
<li><strong>Triptanes (sumatriptan, rizatriptan, eletriptan)</strong> — Aceptados en todos los centros</li>
<li><strong>AINEs (ibuprofeno, naproxeno, aspirina)</strong> — Aceptados</li>
<li><strong>Acetaminofen (Tylenol)</strong> — Aceptado</li>
<li><strong>Topiramato (Topamax)</strong> — Aceptado</li>
<li><strong>Propranolol (para prevencion)</strong> — Generalmente aceptado</li>
<li><strong>Amitriptilina (para prevencion)</strong> — Aceptada</li>
<li><strong>Venlafaxina (para prevencion)</strong> — Aceptada</li>
<li><strong>Magnesio, CoQ10, riboflavina</strong> — Suplementos aceptados</li>
</ul>

<h3>Posibles Problemas</h3>
<ul>
<li><strong>Anticuerpos anti-CGRP inyectables (Aimovig, Ajovy, Emgality)</strong> — Algunos centros los aceptan, otros no (son biologicos)</li>
<li><strong>Gepantes (Ubrelvy, Nurtec)</strong> — Relativamente nuevos, consulta con el centro</li>
<li><strong>Esteroides orales (para clusters severos)</strong> — Depende de la dosis y frecuencia</li>
<li><strong>Botox para migranas cronicas</strong> — Generalmente aceptado (no sistemico)</li>
</ul>'''

    screening = '''<ol>
<li><strong>No dones durante una migrana:</strong> Espera hasta que el episodio pase completamente</li>
<li><strong>Menciona tus medicamentos:</strong> La mayoria de medicamentos para migranas son aceptados</li>
<li><strong>Si usas inyectables anti-CGRP:</strong> Menciona especificamente el nombre (Aimovig, Ajovy, etc.)</li>
<li><strong>Hidratacion previa:</strong> Menciona que entiendes la importancia de hidratarte extra por tus migranas</li>
</ol>'''

    extra = '''<h3>Migranas y Donacion de Plasma: La Conexion</h3>
<p>Hay una relacion importante entre la donacion de plasma y las migranas:</p>
<ul>
<li><strong>Deshidratacion:</strong> Es el desencadenante de migrana mas comun post-donacion</li>
<li><strong>Cambios de volumen sanguineo:</strong> Pueden desencadenar migranas en personas susceptibles</li>
<li><strong>Estres/ansiedad:</strong> La primera donacion puede causar ansiedad, otro desencadenante comun</li>
<li><strong>Citrato:</strong> El anticoagulante puede causar sintomas similares a aura en algunas personas</li>
</ul>

<h3>Como Prevenir Migranas Post-Donacion</h3>
<ul>
<li><strong>Hidratacion extrema:</strong> Toma 80+ oz de agua el dia anterior y el dia de la donacion</li>
<li><strong>Come bien:</strong> No dones con estomago vacio — come proteina y carbohidratos complejos</li>
<li><strong>Evita desencadenantes conocidos:</strong> Si la cafeina es un factor, toma tu cafe habitual (no saltes)</li>
<li><strong>Lleva tus medicamentos:</strong> Ten tus abortivos de migrana disponibles por si acaso</li>
<li><strong>Descansa despues:</strong> No planifiques actividades extenuantes despues de donar</li>
<li><strong>Electrolitos:</strong> Toma una bebida con electrolitos despues de la donacion</li>
</ul>

<h3>Cuando No Donar</h3>
<ul>
<li>No dones si estas en medio de un episodio de migrana</li>
<li>No dones si sientes un aura o sintomas prodromicos</li>
<li>No dones si tuviste una migrana severa en las ultimas 24 horas</li>
<li>No dones si estas en un periodo de migranas frecuentes (clusters)</li>
</ul>'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo migranas?",
                 "Si, las migranas no descalifican para donar plasma. La mayoria de medicamentos para migranas son aceptados. Solo evita donar durante un episodio activo de migrana."),
        make_faq("¿Los triptanes descalifican para donar plasma?",
                 "No. Los triptanes como sumatriptan, rizatriptan y eletriptan son aceptados en todos los centros de plasma. Puedes tomarlos segun sea necesario."),
        make_faq("¿Donar plasma puede causar migranas?",
                 "La donacion no causa migranas directamente, pero la deshidratacion y los cambios de volumen sanguineo pueden desencadenar migranas en personas susceptibles. Hidratate extra antes y despues de donar."),
        make_faq("¿Puedo donar plasma si uso Aimovig u otro anti-CGRP?",
                 "Varia por centro. Los anticuerpos anti-CGRP como Aimovig, Ajovy y Emgality son biologicos inyectables. Algunos centros los aceptan, otros no. Llama a tu centro para confirmar."),
    ]
    return gen_medical_page(slug, en, condition, title, meta, can_donate, meds, screening, extra, faqs)


# ============ MAIN ============
if __name__ == '__main__':
    os.makedirs(ES_BLOG_DIR, exist_ok=True)
    pages = [
        page_lupus,
        page_artritis,
        page_fibromialgia,
        page_epilepsia,
        page_esclerosis_multiple,
        page_psoriasis,
        page_apnea_sueno,
        page_enfermedad_renal,
        page_herpes,
        page_despues_covid,
        page_enfermedad_corazon,
        page_enfermedad_autoinmune,
        page_colesterol_alto,
        page_eczema,
        page_migranas,
    ]

    print(f"Generating Round 3 Spanish Medical pages ({len(pages)} pages)...")
    count = 0
    for fn in pages:
        html = fn()
        # Extract slug from the function name pattern
        slug = fn.__name__.replace('page_', 'donar-plasma-con-')
        # Actually extract slug from the HTML (canonical URL)
        import re
        m = re.search(r'<link rel="canonical" href="https://plasmapaycalculator\.com/es/blog/([^"]+)"', html)
        if m:
            slug = m.group(1)
        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1

    print(f"Done! Generated {count} Spanish medical pages.")
