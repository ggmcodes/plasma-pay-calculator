#!/usr/bin/env python3
"""Generate Round 4: Spanish topic/guide pages (5 pages) - Teachers, Single Parents, Retirees, Do's and Don'ts, Keto"""
import os
from generate_batch5_spanish_template import make_es_page, make_faq, AFFILIATE_ES, PRO_TOOLKIT_ES, related_es

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ES_BLOG_DIR = os.path.join(BASE_DIR, 'es', 'blog')

# ============ SPANISH TOPIC PAGES ============

def gen_maestros():
    """Teachers guide - summer vacation, school schedules, extra income"""
    slug = 'donar-plasma-para-maestros-profesores-2026'
    title = 'Donar Plasma para Maestros y Profesores 2026: Guía de Ingresos Extra'
    meta = 'Guía completa para maestros y educadores que donan plasma. Horarios flexibles, vacaciones de verano, bonos de hasta $1,200. Gana dinero extra compatible con tu carrera docente.'
    category = 'Educadores'
    read_time = 9
    toc = [
        ('respuesta', 'Respuesta Rápida'),
        ('horarios', 'Horarios para Maestros'),
        ('verano', 'Vacaciones de Verano'),
        ('ingresos', 'Potencial de Ingresos'),
        ('tabla', 'Tabla de Ganancias'),
        ('consejos', 'Consejos para Maestros'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rápida</h3>
    <p>Los maestros pueden donar plasma durante <strong>vacaciones escolares y fines de semana</strong>, ganando <strong>$50-$100 por visita</strong>. En el verano, donando dos veces por semana durante 8-10 semanas, puedes ganar <strong>$800-$2,000</strong>. Los nuevos donantes ganan bonos de <strong>$700-$1,200</strong> en el primer mes, perfectos para suplementar el salario de educador.</p>
</div>

<h2 id="horarios">Horarios Compatibles con la Educación</h2>
<p>La donación de plasma es flexible y perfecta para maestros. Aquí tienes opciones según tu calendario escolar:</p>

<h3>Durante el Año Escolar</h3>
<ul>
    <li><strong>Viernes por la tarde:</strong> Después de salir de la escuela (3-4 PM)</li>
    <li><strong>Fines de semana:</strong> Sábado por la mañana para completar dos donaciones semanales</li>
    <li><strong>Vacaciones escolares:</strong> Semanas completas con horarios más flexibles</li>
    <li><strong>Días de desarrollo profesional:</strong> Aprovecha estos días sin estudiantes</li>
    <li><strong>Descansos largos:</strong> Invierno y primavera - dona más frecuentemente</li>
</ul>

<h3>Limitaciones Importantes</h3>
<ul>
    <li>Cada donación toma <strong>45-90 minutos</strong> en el centro</li>
    <li>Necesitas <strong>2-3 días entre donaciones</strong> para recuperarte</li>
    <li>La primera visita puede tomar <strong>2-3 horas</strong> para examen médico</li>
    <li>Algunos maestros prefieren iniciar durante verano antes del nuevo año escolar</li>
</ul>

<h2 id="verano">Estrategia de Verano para Maximizar Ingresos</h2>
<p>El verano es el período perfecto para que los maestros ganen dinero extra donando plasma. Con 10-12 semanas de descanso escolar, aquí está el plan óptimo:</p>

<table>
    <thead>
        <tr>
            <th>Período</th>
            <th>Semanas</th>
            <th>Donaciones</th>
            <th>Ganancias Estimadas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Primeras 2 semanas (Bonificación nueva)</td>
            <td>2</td>
            <td>4 donaciones</td>
            <td>$400-$600</td>
        </tr>
        <tr>
            <td>Semanas 3-10 (Donante regular)</td>
            <td>8</td>
            <td>16 donaciones</td>
            <td>$800-$1,600</td>
        </tr>
        <tr>
            <td><strong>Total verano</strong></td>
            <td><strong>10</strong></td>
            <td><strong>20 donaciones</strong></td>
            <td><strong>$1,200-$2,200</strong></td>
        </tr>
    </tbody>
</table>

<h2 id="ingresos">Potencial de Ingresos por Mes</h2>
<p>Aquí te mostramos cuánto pueden ganar los maestros donando plasma según su dedicación:</p>

<table>
    <thead>
        <tr>
            <th>Frecuencia</th>
            <th>Donaciones/Mes</th>
            <th>Pago Regular</th>
            <th>Bonificaciones</th>
            <th>Total Mensual</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1 vez por semana (fin de semana)</td>
            <td>4</td>
            <td>$200-$400</td>
            <td>Solo nuevos: $175-$300</td>
            <td>$200-$700</td>
        </tr>
        <tr>
            <td>2 veces por semana (estándar)</td>
            <td>8</td>
            <td>$400-$800</td>
            <td>Solo nuevos: $350-$500</td>
            <td>$400-$1,300</td>
        </tr>
        <tr>
            <td>3 veces por semana (máximo)</td>
            <td>12</td>
            <td>$600-$1,200</td>
            <td>Solo nuevos: $525-$800</td>
            <td>$600-$2,000</td>
        </tr>
    </tbody>
</table>

''' + AFFILIATE_ES + '''

<h2 id="tabla">Plan de Ingresos de Verano - Desglose Detallado</h2>
<table>
    <thead>
        <tr>
            <th>Semana</th>
            <th>Donaciones</th>
            <th>Ganancia Semana</th>
            <th>Acumulado</th>
            <th>Notas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>$200-$300</td>
            <td>$200-$300</td>
            <td>Primera semana (primer bono)</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td>$200-$300</td>
            <td>$400-$600</td>
            <td>Continúa bono nuevo</td>
        </tr>
        <tr>
            <td>3-10</td>
            <td>2 cada</td>
            <td>$100-$200 cada</td>
            <td>$400-$1,200+</td>
            <td>Donante regular</td>
        </tr>
        <tr>
            <td>10+</td>
            <td>Opcional</td>
            <td>$100-$200</td>
            <td>$1,200-$2,200</td>
            <td>Ganancias adicionales</td>
        </tr>
    </tbody>
</table>

''' + PRO_TOOLKIT_ES + '''

<h2 id="consejos">Consejos Específicos para Maestros</h2>
<h3>Antes de Empezar</h3>
<ul>
    <li><strong>Planifica antes del semestre:</strong> Considera donar durante verano cuando tengas más tiempo</li>
    <li><strong>Verifica requisitos médicos:</strong> Asegúrate de cumplir peso mínimo (110 libras) y edad (18-69)</li>
    <li><strong>Informa a tu familia:</strong> La donación de plasma es segura pero requiere descanso</li>
    <li><strong>Mantén hidratación:</strong> Bebe agua extra todo el tiempo durante el verano</li>
</ul>

<h3>Durante el Año Escolar</h3>
<ul>
    <li><strong>Limita a 1-2 veces/semana:</strong> No afectes tu energía en el aula</li>
    <li><strong>Elige días estratégicos:</strong> Viernes tarde o fin de semana para recuperarte</li>
    <li><strong>Come bien antes:</strong> Comidas altas en proteína 2-3 horas antes de donar</li>
    <li><strong>No sobrecargues:</strong> Los bonos no valen sacrificar tu salud docente</li>
</ul>

<h3>Salud y Bienestar</h3>
<ul>
    <li>Consume proteína adicional durante la semana</li>
    <li>Duerme 7-8 horas entre donaciones</li>
    <li>Evita el alcohol 24 horas antes y después</li>
    <li>Toma multivitamínicos con hierro si donas frecuentemente</li>
    <li>Descansa en fin de semana si donas viernes</li>
</ul>

''' + related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuánto Pagan por Donar Plasma 2026'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos para Donar'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guía Completa de Donación'),
]) + '''

<h2 id="faq">Preguntas Frecuentes para Maestros</h2>
<h3>¿Cuánto pueden ganar los maestros en verano donando plasma?</h3>
<p>Un maestro puede ganar $1,200-$2,200 durante 10 semanas de verano donando dos veces por semana. El bono inicial para nuevos donantes añade $700-$1,200 adicionales, haciendo posible ganar $2,000-$3,400 en el primer verano.</p>

<h3>¿Afectará la donación mi energía para enseñar?</h3>
<p>No, si donas estratégicamente. Durante el año escolar, mantén 1-2 donaciones por semana los viernes o fin de semana para recuperarte completamente antes del lunes. Asegúrate de dormir bien, beber mucha agua y comer proteína suficiente.</p>

<h3>¿Puedo donar si estoy bajo medicamentos recetados?</h3>
<p>Depende del medicamento. Algunos antibióticos, antihistamínicos y medicamentos para la presión arterial son permitidos. Otros (como anticoagulantes) pueden descalificarte. Informa al personal del centro sobre cualquier medicamento que tomes.</p>

<h3>¿Es seguro donar plasma como maestro de profesión?</h3>
<p>Sí, es completamente seguro. Miles de maestros donan plasma. El procedimiento es regulado por la FDA, utiliza equipo estéril y solo requiere de tu plasma, que tu cuerpo regenera rápidamente. Consulta con tu médico si tienes preocupaciones de salud específicas.</p>
'''

    faqs = [
        make_faq("¿Cuánto pueden ganar los maestros en verano donando plasma?", "$1,200-$2,200 durante 10 semanas donando dos veces por semana. Nuevos donantes pueden ganar $2,000-$3,400 incluyendo bonos."),
        make_faq("¿Afectará la donación mi energía para enseñar?", "No si donas estratégicamente. Durante el año escolar, limita a 1-2 donaciones por semana en fin de semana para recuperarte completamente."),
        make_faq("¿Puedo donar si estoy bajo medicamentos recetados?", "Depende del medicamento. Algunos medicamentos comunes son permitidos, otros no. Informa al centro sobre tus medicamentos."),
        make_faq("¿Es seguro donar plasma como maestro?", "Sí, es completamente seguro y regulado por la FDA. Miles de maestros donan plasma sin problemas."),
    ]

    return make_es_page(slug, title, meta, category, read_time, toc, content, faqs)


def gen_padres_solteros():
    """Single parents guide - childcare, flexible hours, income planning"""
    slug = 'donar-plasma-para-padres-solteros-guia-2026'
    title = 'Donar Plasma para Padres Solteros 2026: Guía de Ingresos Flexibles'
    meta = 'Guía para padres solteros que donan plasma. Horarios flexibles, cuidado de hijos, ingresos extra, bonos hasta $1,200. Equilibra la crianza con dinero extra.'
    category = 'Padres e Hijos'
    read_time = 9
    toc = [
        ('respuesta', 'Respuesta Rápida'),
        ('cuidado', 'Cuidado de Hijos'),
        ('horarios', 'Horarios Flexibles'),
        ('ingresos', 'Potencial de Ingresos'),
        ('tabla', 'Ganancias Mensual'),
        ('consejos', 'Consejos Prácticos'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rápida</h3>
    <p>Los padres solteros pueden donar plasma <strong>con horarios flexibles que trabajan alrededor del cuidado de hijos</strong>. Gana <strong>$50-$100 por visita</strong>, con potencial de <strong>$800-$2,000 mensuales</strong> con las dos donaciones semanales típicas. Nuevos donantes reciben bonos de <strong>$700-$1,200</strong>, dinero extra invaluable para familias monoparentales.</p>
</div>

<h2 id="cuidado">Soluciones de Cuidado de Niños Mientras Donas</h2>
<p>La donación de plasma toma 45-90 minutos. Aquí están tus opciones para cuidado de los hijos:</p>

<h3>Opciones de Cuidado Familiar</h3>
<ul>
    <li><strong>Pareja o cónyuge:</strong> La opción más común para padres solteros (puede ser ex pareja en arreglo amigable)</li>
    <li><strong>Padres/abuelos:</strong> Si viven cerca, pueden cuidar durante tus visitas</li>
    <li><strong>Hermanos adultos:</strong> Hermanos o hermanas que pueden ayudar en emergencia</li>
    <li><strong>Amigos de confianza:</strong> Padres amigos con hijos que pueden supervizar en grupo</li>
</ul>

<h3>Opciones de Cuidado Pago</h3>
<ul>
    <li><strong>Niñera de corto plazo:</strong> $10-20 por hora, deducible del pago de donación</li>
    <li><strong>Centros de cuidado diurno:</strong> Algunos ofrecen cuidado por horas</li>
    <li><strong>Estudiantes universitarios:</strong> Opción más económica, $8-15 por hora</li>
    <li><strong>Programas comunitarios:</strong> Algunos centros tienen áreas de juego gratuitas</li>
</ul>

<h3>Edades de los Hijos y Opciones</h3>
<ul>
    <li><strong>0-5 años:</strong> Requiere cuidado supervizado (familia o niñera)</li>
    <li><strong>5-10 años:</strong> Cuidado supervizado durante la donación, algunos centros permiten niños en áreas de espera</li>
    <li><strong>10+ años:</strong> Puede esperar contigo en áreas de espera o quedarse en casa con adulto responsable</li>
</ul>

<h2 id="horarios">Horarios que Funcionan para Padres Solteros</h2>
<p>Planifica tus donaciones alrededor de la escuela y actividades de tus hijos:</p>

<table>
    <thead>
        <tr>
            <th>Horario</th>
            <th>Ventajas</th>
            <th>Desventajas</th>
            <th>Mejor Para</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Mañanas (8-11 AM)</strong></td>
            <td>Después de dejar en escuela, donación rápida</td>
            <td>Puede correr si se retrasa</td>
            <td>Hijos en escuela completa</td>
        </tr>
        <tr>
            <td><strong>Tardes (2-5 PM)</strong></td>
            <td>Después de escuela, esperas cortas</td>
            <td>A veces tiene mucha gente</td>
            <td>Trabajo flexible</td>
        </tr>
        <tr>
            <td><strong>Sábado mañana</strong></td>
            <td>Sin presión de escuela, padre cuida</td>
            <td>Menos abierto los sábados</td>
            <td>Custodia compartida</td>
        </tr>
        <tr>
            <td><strong>Después de trabajo</strong></td>
            <td>Después de recoger de escuela/guardería</td>
            <td>Cansancio del día</td>
            <td>Trabajo estable 9-5</td>
        </tr>
    </tbody>
</table>

<h2 id="ingresos">Potencial de Ingresos para Padres Solteros</h2>
<p>Aquí está lo que pueden realísticamente ganar padres solteros considerando restricciones de tiempo:</p>

<table>
    <thead>
        <tr>
            <th>Escenario</th>
            <th>Donaciones/Mes</th>
            <th>Ingresos Base</th>
            <th>Bonos (Mes 1)</th>
            <th>Total Mensual</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Minimal (1x/semana)</strong></td>
            <td>4</td>
            <td>$200-$400</td>
            <td>$175-$300</td>
            <td>$200-$700</td>
        </tr>
        <tr>
            <td><strong>Moderado (1.5x/semana)</strong></td>
            <td>6</td>
            <td>$300-$600</td>
            <td>$263-$450</td>
            <td>$300-$1,050</td>
        </tr>
        <tr>
            <td><strong>Óptimo (2x/semana)</strong></td>
            <td>8</td>
            <td>$400-$800</td>
            <td>$350-$600</td>
            <td>$400-$1,400</td>
        </tr>
    </tbody>
</table>

''' + AFFILIATE_ES + '''

<h2 id="tabla">Planificador de Ingresos de 3 Meses para Padres Solteros</h2>
<table>
    <thead>
        <tr>
            <th>Período</th>
            <th>Donaciones</th>
            <th>Ingresos</th>
            <th>Bonificaciones</th>
            <th>Total</th>
            <th>Notas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Mes 1 (Nuevo)</strong></td>
            <td>8</td>
            <td>$400-$800</td>
            <td>$700-$1,200</td>
            <td>$1,100-$2,000</td>
            <td>Máximas bonificaciones</td>
        </tr>
        <tr>
            <td><strong>Mes 2</strong></td>
            <td>8</td>
            <td>$400-$800</td>
            <td>$0</td>
            <td>$400-$800</td>
            <td>Sin bonificación</td>
        </tr>
        <tr>
            <td><strong>Mes 3</strong></td>
            <td>8</td>
            <td>$400-$800</td>
            <td>$0</td>
            <td>$400-$800</td>
            <td>Ingresos estables</td>
        </tr>
        <tr>
            <td><strong>Total 3 Meses</strong></td>
            <td>24</td>
            <td>$1,200-$2,400</td>
            <td>$700-$1,200</td>
            <td>$1,900-$3,600</td>
            <td>Dinero extra real</td>
        </tr>
    </tbody>
</table>

''' + PRO_TOOLKIT_ES + '''

<h2 id="consejos">Consejos Prácticos para Padres Solteros</h2>
<h3>Logística Familiar</h3>
<ul>
    <li><strong>Establece rutina:</strong> Elige mismo día/hora cada semana para que hijos sepan qué esperar</li>
    <li><strong>Planifica con cuidador:</strong> Avisa con antelación para que cuidador se prepare</li>
    <li><strong>Ten plan B:</strong> Si cuidador falla, llama al centro para reprogramar (NO pierdas el bono)</li>
    <li><strong>Explica a hijos mayores:</strong> Diles que donas para ayudar gente y ganar dinero extra</li>
</ul>

<h3>Manejo Financiero</h3>
<ul>
    <li><strong>Abre cuenta separada:</strong> Mantén dinero de donaciones separado para control</li>
    <li><strong>Presupuesta bonos:</strong> Usa bono inicial para necesidad (reparación carro, depósito vivienda)</li>
    <li><strong>Ahorra ingresos regulares:</strong> $400-800 mensuales pueden ser ahorro de emergencia para hijos</li>
    <li><strong>No dependas de esto:</strong> Úsalo como complemento a ingreso principal</li>
</ul>

<h3>Salud Durante Donaciones</h3>
<ul>
    <li>Mantén energía: duerme 7+ horas para estar disponible para hijos</li>
    <li>Hidratación: bebe mucha agua, especialmente antes de donación</li>
    <li>Nutrición: come proteína adicional para recuperarte de donaciones</li>
    <li>Evita alcohol: 24 horas antes y después para salud óptima</li>
    <li>Descansa días de donación: no hagas ejercicio intenso ese día</li>
</ul>

''' + related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuánto Pagan por Donar Plasma 2026'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guía Completa de Donación'),
]) + '''

<h2 id="faq">Preguntas Frecuentes para Padres Solteros</h2>
<h3>¿Puedo donar plasma si tengo hijos pequeños?</h3>
<p>Sí, siempre que tengas cuidado para ellos durante la donación. Muchos padres solteros donan durante horarios escolares o cuando pueden dejar hijos con familia. Algunos centros permiten niños pequeños en áreas de espera supervisionadas.</p>

<h3>¿Cuánto puedo realísticamente ganar como padre soltero?</h3>
<p>Donando dos veces por semana (horario típico), puedes ganar $400-$800 mensuales después del primer mes. En el mes 1, con bonos de nuevo donante, suma $1,100-$2,000. Esto equivale a $50-100 por hora de tiempo invertido.</p>

<h3>¿Qué pasa si me enfermo durante el bono de nuevo donante?</h3>
<p>Si te enfermas, puedes reprogramar tu donación. El período de bonificación (30-45 días) es lo suficientemente largo para permitir algunos retrasos. Llama al centro inmediatamente si no puedes ir.</p>

<h3>¿Afectará la donación mi capacidad para cuidar a mis hijos?</h3>
<p>No notarás grandes cambios si comes bien, duermes suficiente e hidratas adecuadamente. La mayoría de padres solteros sienten que tienen más energía con el dinero extra que con cualquier fatiga de la donación.</p>
'''

    faqs = [
        make_faq("¿Puedo donar plasma si tengo hijos pequeños?", "Sí, siempre que tengas cuidado. Muchos padres donan durante horas escolares o con ayuda de familia."),
        make_faq("¿Cuánto puedo realísticamente ganar como padre soltero?", "Donando 2x/semana: $400-$800/mes. Mes 1 con bonos: $1,100-$2,000. Total 3 meses: $1,900-$3,600."),
        make_faq("¿Qué pasa si me enfermo durante el bono?", "Puedes reprogramar tu donación. El período de bonificación es lo suficientemente largo para permitir retrasos."),
        make_faq("¿Afectará la donación mi energía para mis hijos?", "No si cuidas tu salud. Come bien, duerme 7+ horas, mantente hidratado y evita alcohol 24h antes/después."),
    ]

    return make_es_page(slug, title, meta, category, read_time, toc, content, faqs)


def gen_jubilados():
    """Retirees guide - no age limit, Social Security safe, Medicare, health"""
    slug = 'donar-plasma-para-jubilados-mayores-2026'
    title = 'Donar Plasma para Jubilados y Personas Mayores 2026: Guía Completa'
    meta = 'Guía para jubilados y adultos mayores. Sin límite de edad, seguro social no afectado, Medicare aceptado, ingresos extra. Donación de plasma segura para mayores de 65 años.'
    category = 'Jubilación y Mayores'
    read_time = 9
    toc = [
        ('respuesta', 'Respuesta Rápida'),
        ('edad', 'Sin Límite de Edad'),
        ('seguro', 'Seguro Social y Medicare'),
        ('salud', 'Consideraciones de Salud'),
        ('ingresos', 'Potencial de Ingresos'),
        ('tabla', 'Tabla Comparativa'),
        ('consejos', 'Consejos para Mayores'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rápida</h3>
    <p>Los jubilados y adultos mayores <strong>pueden donar plasma a cualquier edad</strong> (sin límite máximo) si están saludables y pesan 110+ libras. Gana <strong>$50-$100 por visita</strong>. El dinero NO afecta el Seguro Social ni Medicare. Nuevos donantes reciben <strong>$700-$1,200</strong> en bonos. Donando 1-2 veces por semana, puedes ganar <strong>$200-$800 mensuales</strong> de ingresos extra completamente legales.</p>
</div>

<h2 id="edad">No Hay Límite de Edad para Donar Plasma</h2>
<p>A diferencia de muchas otras cosas, donar plasma NO tiene límite de edad superior. Personas de 70, 80, incluso 90+ años han donado plasma exitosamente.</p>

<h3>Requisitos de Edad</h3>
<ul>
    <li><strong>Mínimo:</strong> 18 años (obligatorio por ley federal)</li>
    <li><strong>Máximo:</strong> SIN LÍMITE - donate a los 65, 75, 85+ años si eres saludable</li>
    <li><strong>Consideración médica:</strong> Tu salud importa más que tu edad</li>
    <li><strong>Evaluación individual:</strong> Cada donante evalúa individualmente, no por edad</li>
</ul>

<h3>Ventajas para Jubilados</h3>
<ul>
    <li>Horarios flexibles que trabajan con actividades de jubilación</li>
    <li>Dinero extra sin afectar beneficios de retiro</li>
    <li>Oportunidad social - conocer personal y otros donantes</li>
    <li>Sensación de propósito - ayudas gente enferma</li>
    <li>Actividad física leve beneficiosa para salud</li>
</ul>

<h2 id="seguro">Seguro Social, Medicare y Beneficios de Jubilación</h2>
<p>Una preocupación común: ¿afectará donar plasma mis beneficios de retiro? La respuesta es claramente NO.</p>

<h3>Impacto en Seguro Social</h3>
<ul>
    <li><strong>¿Cuenta como ingreso?</strong> SÍ, técnicamente es ingreso reportable</li>
    <li><strong>¿Reduce mis beneficios?</strong> NO para jubilados de edad plena (66+), posiblemente SÍ si aún trabajas y tienes menos de 66</li>
    <li><strong>¿Debo reportarlo?</strong> SÍ en impuestos, pero dinero en mano generalmente no requiere reporte especial a SS</li>
    <li><strong>Límite de ingresos 2026:</strong> Si naciste en 1960+, puedes ganar dinero ilimitado sin penalidad</li>
</ul>

<h3>Medicare - Completamente Seguro</h3>
<ul>
    <li><strong>¿Afecta Medicare?</strong> NO, de ninguna manera</li>
    <li><strong>¿Requiere aprobación?</strong> NO, no necesitas informar a Medicare</li>
    <li><strong>¿Cubre problemas?</strong> SÍ, si desarrollas cualquier problema, Medicare cubre evaluaciones/tratamiento</li>
    <li><strong>Recomendación:</strong> Simplemente informa a tu médico que donas plasma, es seguro</li>
</ul>

<h3>Otros Beneficios de Jubilación</h3>
<ul>
    <li><strong>Pensiones privadas:</strong> No afectadas por ingresos de plasma</li>
    <li><strong>IRA/401k:</strong> No afectadas</li>
    <li><strong>Beneficios de veterano:</strong> No afectados</li>
    <li><strong>Medicaid (si aplicas):</strong> Reporta como ingreso, podría afectar si tienes límites de activos</li>
</ul>

<h2 id="salud">Consideraciones de Salud para Donantes Mayores</h2>
<p>Donar plasma es seguro para personas mayores saludables. Aquí está qué esperar:</p>

<h3>Condiciones Médicas Comunes y Donación</h3>
<table>
    <thead>
        <tr>
            <th>Condición</th>
            <th>¿Puedo Donar?</th>
            <th>Precauciones</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Presión arterial alta (controlada)</strong></td>
            <td>SÍ</td>
            <td>Mantén medicamentos, hidratación</td>
        </tr>
        <tr>
            <td><strong>Diabetes tipo 2</strong></td>
            <td>SÍ</td>
            <td>Come antes, monitorea glucosa</td>
        </tr>
        <tr>
            <td><strong>Problemas cardíacos leves</strong></td>
            <td>POSIBLEMENTE</td>
            <td>Requiere aprobación médica</td>
        </tr>
        <tr>
            <td><strong>Artritis/Dolor crónico</strong></td>
            <td>SÍ</td>
            <td>Cómo en centro, descanso después</td>
        </tr>
        <tr>
            <td><strong>Medicamentos anticoagulantes</strong></td>
            <td>NO</td>
            <td>Incompatible con donación</td>
        </tr>
    </tbody>
</table>

''' + AFFILIATE_ES + '''

<h2 id="ingresos">Potencial de Ingresos para Jubilados</h2>
<p>Dependiendo de salud y disponibilidad, aquí está qué pueden ganar jubilados:</p>

<table>
    <thead>
        <tr>
            <th>Nivel de Actividad</th>
            <th>Donaciones/Mes</th>
            <th>Ingresos Base</th>
            <th>Bono Mes 1</th>
            <th>Total Mes 1</th>
            <th>Mensual Regular</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Ligero (1x/sem)</strong></td>
            <td>4</td>
            <td>$200-$400</td>
            <td>$175-$300</td>
            <td>$375-$700</td>
            <td>$200-$400</td>
        </tr>
        <tr>
            <td><strong>Moderado (1.5x/sem)</strong></td>
            <td>6</td>
            <td>$300-$600</td>
            <td>$263-$450</td>
            <td>$563-$1,050</td>
            <td>$300-$600</td>
        </tr>
        <tr>
            <td><strong>Regular (2x/sem)</strong></td>
            <td>8</td>
            <td>$400-$800</td>
            <td>$350-$600</td>
            <td>$750-$1,400</td>
            <td>$400-$800</td>
        </tr>
    </tbody>
</table>

''' + PRO_TOOLKIT_ES + '''

<h2 id="tabla">Planificador de Ingresos Anual para Jubilados</h2>
<table>
    <thead>
        <tr>
            <th>Período</th>
            <th>Donaciones</th>
            <th>Ingresos</th>
            <th>Bonos</th>
            <th>Total</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Mes 1 (Nuevo)</strong></td>
            <td>8</td>
            <td>$400-$800</td>
            <td>$700-$1,200</td>
            <td>$1,100-$2,000</td>
        </tr>
        <tr>
            <td><strong>Meses 2-12</strong></td>
            <td>96 (8/mes)</td>
            <td>$4,800-$9,600</td>
            <td>$0</td>
            <td>$4,800-$9,600</td>
        </tr>
        <tr>
            <td><strong>TOTAL AÑO 1</strong></td>
            <td>104</td>
            <td>$5,200-$10,400</td>
            <td>$700-$1,200</td>
            <td>$5,900-$11,600</td>
        </tr>
    </tbody>
</table>

<h2 id="consejos">Consejos Especiales para Donantes Mayores</h2>
<h3>Antes de Empezar</h3>
<ul>
    <li><strong>Aprobación médica:</strong> Habla con tu médico principal antes de empezar</li>
    <li><strong>Examen físico:</strong> Centro hará examen completo en primera visita (2-3 horas)</li>
    <li><strong>Medicamentos:</strong> Lleva lista de todos tus medicamentos actuales</li>
    <li><strong>Historial médico:</strong> Prepárate para hablar de condiciones previas</li>
</ul>

<h3>Durante Donaciones</h3>
<ul>
    <li><strong>Descanso:</strong> Requiere menos energía que ejercicio, pero necesita descanso después</li>
    <li><strong>Comodidad:</strong> Siéntate cómodamente durante 45-90 minutos - lleva libro o audiolibro</li>
    <li><strong>Hidratación:</strong> Bebe agua extra los días de donación</li>
    <li><strong>Nutrición:</strong> Come proteína 2-3 horas antes de donar</li>
    <li><strong>Transporte:</strong> Arranjos de transporte seguros (conducción lenta, no intenso después)</li>
</ul>

<h3>Recuperación y Salud</h3>
<ul>
    <li>Duerme extra la noche después de donar</li>
    <li>Evita actividades intensas el día de donación</li>
    <li>Toma multivitamínicos con hierro regularmente</li>
    <li>Mantén consumo de proteína alto</li>
    <li>Sigue monitoreando condiciones existentes como hipertensión</li>
</ul>

''' + related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuánto Pagan por Donar Plasma 2026'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guía Completa de Donación'),
]) + '''

<h2 id="faq">Preguntas Frecuentes para Jubilados</h2>
<h3>¿Hay límite de edad para donar plasma?</h3>
<p>No hay límite de edad superior. Personas de 70, 80, incluso 90+ años donan plasma. Solo necesitas estar saludable, pesar 110+ libras y pasar evaluación médica. Tu edad no te descalifica automáticamente.</p>

<h3>¿Afectará el dinero de plasma mi Seguro Social o Medicare?</h3>
<p>No afecta Medicare de ninguna forma. Con Seguro Social, si tienes 66+ años (edad plena), puedes ganar dinero ilimitado sin penalidad. Si eres más joven, hay límites de ingreso, pero la mayoría de jubilados están en edad plena.</p>

<h3>¿Es seguro para alguien con presión arterial alta o diabetes?</h3>
<p>Sí, si está controlada. Muchos donantes tienen estas condiciones. Simplemente informa al centro, mantén medicamentos, come bien, y mantente hidratado. Tu presión/glucosa se monitoreará.</p>

<h3>¿Cuánta energía requiere donar plasma?</h3>
<p>Muy poca. Simplemente te sientas durante 45-90 minutos mientras la máquina extrae plasma. Requiere menos esfuerzo que hacer compras. Puedes leer, escuchar audiolibros, o simplemente descansar.</p>
'''

    faqs = [
        make_faq("¿Hay límite de edad para donar plasma?", "No hay límite superior. Personas de 70, 80, 90+ años donan plasma si están saludables y pesan 110+ libras."),
        make_faq("¿Afectará mi Seguro Social o Medicare?", "No afecta Medicare. Con Seguro Social, si tienes 66+, ganas ilimitadamente sin penalidad."),
        make_faq("¿Es seguro con presión alta o diabetes?", "Sí, si está controlada. Muchos donantes tienen estas condiciones. Mantén medicamentos e hidratación."),
        make_faq("¿Cuánta energía requiere?", "Muy poca. Te sientas 45-90 minutos mientras máquina extrae plasma. Menos esfuerzo que compras."),
    ]

    return make_es_page(slug, title, meta, category, read_time, toc, content, faqs)


def gen_no_hacer():
    """Do's and Don'ts guide - alcohol, fatty foods, dehydration, intense exercise"""
    slug = 'donar-plasma-que-no-hacer-antes-guia-2026'
    title = '¿Qué NO Hacer Antes de Donar Plasma? Guía Completa 2026'
    meta = 'Qué evitar antes de donar plasma. No alcohol 24h, no grasa, no deshidratarse, no ejercicio intenso. Guía completa de restricciones previas a donación.'
    category = 'Consejos de Salud'
    read_time = 9
    toc = [
        ('respuesta', 'Respuesta Rápida'),
        ('alcohol', 'Alcohol - 24 Horas'),
        ('comida', 'Alimentos Grasosos'),
        ('hidratacion', 'Deshidratación'),
        ('ejercicio', 'Ejercicio Intenso'),
        ('tabla', 'Tabla de Restricciones'),
        ('checklist', 'Checklist Previo'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rápida</h3>
    <p>NO hagas esto 24 horas ANTES de donar plasma: <strong>alcohol, ejercicio intenso, ayunar completamente, comidas grasosas</strong>. TAMBIÉN NO: conduzcas si te sientes mareado, dones con fiebre/enfermedad, tomes ciertos medicamentos, deshidrátate. Las violaciones pueden resultar en <strong>rechazo, lipemia (plasma nublado), o riesgo de salud</strong>. Sigue esta guía y tus donaciones serán lisas, plasma de calidad, y ganancias máximas.</p>
</div>

<h2 id="alcohol">NO ALCOHOL 24 Horas Antes</h2>
<p>Esta es la regla número uno. El alcohol afecta tu plasma de múltiples formas:</p>

<h3>Por Qué: El Impacto del Alcohol</h3>
<ul>
    <li><strong>Deshidratación:</strong> El alcohol deshidrata severamente - malo para donación</li>
    <li><strong>Calidad de plasma:</strong> Alcohol afecta proteína de plasma, haciéndolo menos útil medicalmente</li>
    <li><strong>Retraso de recuperación:</strong> Tu cuerpo tarda más en recuperarse</li>
    <li><strong>Presión baja:</strong> Aumenta riesgo de mareos/desmayos durante donación</li>
    <li><strong>Rechazo potencial:</strong> Centro puede rechazar donación si detectan alcohol</li>
</ul>

<h3>Cuándo Puedes Beber de Nuevo</h3>
<ul>
    <li><strong>ANTES:</strong> NO alcohol 24 horas antes de donación</li>
    <li><strong>DÍA DE:</strong> NO el día de donación</li>
    <li><strong>DESPUÉS:</strong> Puedes beber moderadamente 24 horas después de donación</li>
    <li><strong>REGLA FÁCIL:</strong> Si donaste hoy, no bebas hasta mañana por la noche</li>
</ul>

<h3>Tipos de Alcohol a Evitar</h3>
<ul>
    <li><strong>Cerveza:</strong> Deshidrata, especialmente con donación</li>
    <li><strong>Licor fuerte:</strong> Peor efecto deshidratante</li>
    <li><strong>Vino:</strong> Moderado pero aún afecta</li>
    <li><strong>Cócteles:</strong> Peor si tienen azúcar</li>
    <li><strong>Bebidas energéticas alcohólicas:</strong> Extremadamente malas</li>
</ul>

<h2 id="comida">NO ALIMENTOS GRASOSOS</h2>
<p>Comer grasa 24 horas antes puede causar "lipemia" - plasma nublado que centros rechazarán.</p>

<h3>Por Qué: Lipemia Explicada</h3>
<ul>
    <li><strong>Qué es:</strong> Plasma nublado/turbio debido a grasa en sangre</li>
    <li><strong>Causa:</strong> Alimentos grasosos aumentan lípidos en plasma</li>
    <li><strong>Problema:</strong> Plasma nublado no es médicamente útil - centros pueden rechazarlo</li>
    <li><strong>Costo:</strong> Si rechazado, no ganas esa donación ($50-100 perdidos)</li>
    <li><strong>Récord:</strong> Múltiples rechazos pueden resultar en descalificación</li>
</ul>

<h3>Alimentos a EVITAR 24 Horas Antes</h3>
<table>
    <thead>
        <tr>
            <th>Categoría</th>
            <th>EVITAR Estos</th>
            <th>OK - Estas Alternativas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Carnes</strong></td>
            <td>Carnes grasosas, tocino, salchichas</td>
            <td>Pechuga pollo, pavo magro</td>
        </tr>
        <tr>
            <td><strong>Lácteos</strong></td>
            <td>Queso completo, leche completa, helado</td>
            <td>Yogur bajo grasa, leche desnatada</td>
        </tr>
        <tr>
            <td><strong>Fritos</strong></td>
            <td>Papas fritas, alitas, comida rápida</td>
            <td>Pollo asado, papas al horno</td>
        </tr>
        <tr>
            <td><strong>Postres</strong></td>
            <td>Pasteles, donuts, chocolate, helado</td>
            <td>Frutas, galletas integrales</td>
        </tr>
        <tr>
            <td><strong>Grasas</strong></td>
            <td>Mantequilla, aceite de coco, mayonesa</td>
            <td>Aceite de oliva moderado, sin grasas</td>
        </tr>
    </tbody>
</table>

<h3>Plan de Comidas 24 Horas Antes (Ejemplo)</h3>
<ul>
    <li><strong>Desayuno:</strong> Avena con frutas bajas en grasa, pan tostado integral</li>
    <li><strong>Almuerzo:</strong> Pollo asado, arroz, verduras - SIN mantequilla/aceite</li>
    <li><strong>Snacks:</strong> Manzana, plátano, galletas integrales, palomitas sin mantequilla</li>
    <li><strong>Cena:</strong> Pescado magro, pasta, verduras - preparado sin aceite/grasa</li>
    <li><strong>Hidratación:</strong> Agua, jugo, té - NO bebidas grasosas</li>
</ul>

<h2 id="hidratacion">NO DESHIDRATACIÓN</h2>
<p>La deshidratación es crítica para donación segura. Tu plasma es 90% agua.</p>

<h3>Por Qué: Importancia de Hidratación</h3>
<ul>
    <li><strong>Volumen:</strong> Necesitas agua para producir plasma suficiente</li>
    <li><strong>Presión sanguínea:</strong> Deshidratación causa presión baja, mareos</li>
    <li><strong>Extracción:</strong> Máquina necesita plasma hidratado para fluir correctamente</li>
    <li><strong>Recuperación:</strong> Hidratación adecuada acelera recuperación</li>
    <li><strong>Rechazo:</strong> Muy deshidratado = rechazo de donación</li>
</ul>

<h3>Guía de Hidratación Antes de Donar</h3>
<ul>
    <li><strong>Normal (3+ días antes):</strong> 8-10 vasos agua diariamente</li>
    <li><strong>2 días antes:</strong> 12-14 vasos de agua</li>
    <li><strong>Día anterior:</strong> 16 vasos de agua o más</li>
    <li><strong>Mañana de donación:</strong> 8 vasos antes de ir al centro</li>
    <li><strong>En centro:</strong> Bebe agua mientras esperas</li>
</ul>

<h3>Bebidas Recomendadas vs Evitar</h3>
<table>
    <thead>
        <tr>
            <th>Recomendadas</th>
            <th>Moderar</th>
            <th>EVITAR</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Agua simple</td>
            <td>Jugo de fruta</td>
            <td>Café (deshidrata)</td>
        </tr>
        <tr>
            <td>Agua con electrolitos (Liquid IV)</td>
            <td>Té sin cafeína</td>
            <td>Alcohol</td>
        </tr>
        <tr>
            <td>Bebidas deportivas (bajo azúcar)</td>
            <td>Agua de coco</td>
            <td>Bebidas con cafeína</td>
        </tr>
        <tr>
            <td>Caldo de pollo claro</td>
            <td>Leche baja grasa</td>
            <td>Cerveza/licor</td>
        </tr>
    </tbody>
</table>

<h2 id="ejercicio">NO EJERCICIO INTENSO</h2>
<p>Evita ejercicio vigoroso 24 horas antes de donar plasma.</p>

<h3>Por Qué: Ejercicio es Problemático</h3>
<ul>
    <li><strong>Deshidratación:</strong> Sudor durante ejercicio deshidrata</li>
    <li><strong>Músculos:</strong> Ejercicio crea pequeños daños musculares que requieren plasma</li>
    <li><strong>Presión baja:</strong> Aumenta riesgo de mareos/desmayos</li>
    <li><strong>Recuperación:</strong> Tu cuerpo necesita recuperarse de ejercicio Y donación</li>
    <li><strong>Calidad de plasma:</strong> Plasma de alguien que ejercitó intensamente es de menor calidad</li>
</ul>

<h3>Actividades a EVITAR 24 Horas Antes</h3>
<ul>
    <li><strong>Gym/Entrenamiento de fuerza:</strong> NO levantamiento pesado</li>
    <li><strong>Cardio intenso:</strong> NO correr, ciclismo duro, HIIT</li>
    <li><strong>Deportes competitivos:</strong> NO fútbol, basketball, tenis</li>
    <li><strong>Clases de fitness:</strong> NO Zumba, spinning, CrossFit</li>
    <li><strong>Actividad manual pesada:</strong> NO jardinería pesada, trabajos de construcción</li>
</ul>

<h3>Actividades Permitidas (Ligeras)</h3>
<ul>
    <li>Caminar lentamente (paseo tranquilo)</li>
    <li>Yoga suave/estiramientos</li>
    <li>Natación ligera</li>
    <li>Tareas domésticas normales</li>
    <li>Trabajo de oficina regular</li>
</ul>

''' + AFFILIATE_ES + '''

<h2 id="tabla">Tabla Completa: QUÉ NO HACER 24 HORAS ANTES</h2>
<table>
    <thead>
        <tr>
            <th>Categoría</th>
            <th>NO HAGAS ESTO</th>
            <th>CONSECUENCIA</th>
            <th>Alternativa OK</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Alcohol</strong></td>
            <td>Alcohol de cualquier tipo</td>
            <td>Rechazo, mareos, baja calidad</td>
            <td>Agua, jugo sin azúcar</td>
        </tr>
        <tr>
            <td><strong>Grasa</strong></td>
            <td>Carnes grasosas, fritos, lácteos</td>
            <td>Lipemia, rechazo de plasma</td>
            <td>Pollo magro, pescado, arroz</td>
        </tr>
        <tr>
            <td><strong>Deshidratación</strong></td>
            <td>Beber poco, tomar café/alcohol</td>
            <td>Mareos, rechazo, baja presión</td>
            <td>16+ vasos agua, Liquid IV</td>
        </tr>
        <tr>
            <td><strong>Ejercicio</strong></td>
            <td>Gym, correr, cardio duro</td>
            <td>Baja presión, mala recuperación</td>
            <td>Caminar lentamente, yoga</td>
        </tr>
        <tr>
            <td><strong>Medicamentos</strong></td>
            <td>Ciertos medicamentos (ver lista)</td>
            <td>Descalificación temporal/permanente</td>
            <td>Informa médico, espera o alterna</td>
        </tr>
        <tr>
            <td><strong>Enfermedad</strong></td>
            <td>Donar con fiebre/resfriado</td>
            <td>Rechazo, riesgo para pacientes</td>
            <td>Espera a recuperación completa</td>
        </tr>
    </tbody>
</table>

''' + PRO_TOOLKIT_ES + '''

<h2 id="checklist">CHECKLIST: 24 Horas Antes de Tu Donación</h2>
<p><strong>Imprime esto o guárdalo en tu teléfono - verifica cada ítem:</strong></p>

<h3>Día Anterior (24 horas antes)</h3>
<ul>
    <li>☐ NO alcohol - evita completamente</li>
    <li>☐ NO ejercicio intenso - solo actividades ligeras</li>
    <li>☐ SÍ hidratación - bebe 16+ vasos de agua</li>
    <li>☐ NO alimentos grasosos - come proteína magra, carbohidratos</li>
    <li>☐ Revisa medicamentos - asegúrate que son permitidos</li>
    <li>☐ Duerme bien - 7-8 horas de descanso</li>
</ul>

<h3>Mañana de Donación</h3>
<ul>
    <li>☐ Desayuno nutritivo - proteína, carbohidratos, LIGERO en grasa</li>
    <li>☐ Bebe agua - 8 vasos antes de ir</li>
    <li>☐ Permanece hidratado - sigue bebiendo agua</li>
    <li>☐ Ropa cómoda - mangas cortas para fácil acceso</li>
    <li>☐ Documentación - ID, SSN, prueba de domicilio</li>
    <li>☐ Transporte - manejo seguro o transporte alternativo</li>
</ul>

<h3>A EVITAR</h3>
<ul>
    <li>☐ NO alcohol último minuto</li>
    <li>☐ NO café intenso (deshidrata)</li>
    <li>☐ NO ejercicio esta mañana</li>
    <li>☐ NO ayuno completo (come algo ligero)</li>
    <li>☐ NO nuevos medicamentos sin informar centro</li>
</ul>

''' + related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuánto Pagan por Donar Plasma 2026'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guía Completa de Donación'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos'),
]) + '''

<h2 id="faq">Preguntas Frecuentes: QUÉ NO HACER</h2>
<h3>¿Qué pasa si bebo alcohol 24 horas antes?</h3>
<p>Tu donación puede ser rechazada, especialmente si se detecta alcohol en el examen. Incluso si se acepta, el plasma será de baja calidad. Pierdes potencial de $50-100. Mejor: espera 24 horas después de tu última bebida.</p>

<h3>¿Por qué no puedo comer grasa? Pensé que necesitaba proteína.</h3>
<p>Necesitas proteína SÍ, pero de fuentes MAGRAS. Pollo, pavo, pescado, huevos claros - proteína sin grasa. La grasa causa lipemia (plasma nublado) que centros rechazan. Proteína magra = plasma de calidad.</p>

<h3>¿Cuánta agua necesito beber antes?</h3>
<p>Idealamente 16+ vasos el día anterior, 8 vasos la mañana de. Si pesas más, bebe más. Si tienes condición médica, consulta doctor. Mejor: lleva botella agua al centro y sigue bebiendo mientras esperas.</p>

<h3>¿Puedo ejercitar si lo hago ligero?</h3>
<p>Ligero SÍ (caminar lentamente, yoga suave). Intenso NO (gym, correr, cardio duro). Si hiciste ejercicio ayer, hidratate extra hoy. Tu cuerpo necesita recuperarse de ambos - donación Y ejercicio.</p>
'''

    faqs = [
        make_faq("¿Qué pasa si bebo alcohol 24 horas antes?", "Tu donación puede rechazarse, plasma será baja calidad. Pierdes $50-100. Espera 24 horas después de tu última bebida."),
        make_faq("¿Por qué no puedo comer grasa?", "Grasa causa lipemia (plasma nublado) que centros rechazan. Come proteína MAGRA: pollo, pavo, pescado."),
        make_faq("¿Cuánta agua necesito beber?", "16+ vasos el día anterior, 8 vasos mañana de donación. Mejor: lleva botella al centro y sigue bebiendo."),
        make_faq("¿Puedo ejercitar si es ligero?", "Ligero SÍ (caminar, yoga suave). Intenso NO (gym, correr, cardio). Tu cuerpo necesita recuperarse de ambos."),
    ]

    return make_es_page(slug, title, meta, category, read_time, toc, content, faqs)


def gen_keto():
    """Keto diet guide - high protein advantage, lipemia risk, hydration, pre-donation meals"""
    slug = 'donar-plasma-y-dieta-keto-cetogenica-2026'
    title = 'Donar Plasma y Dieta Keto/Cetogénica 2026: Guía Completa'
    meta = 'Dieta keto y donación de plasma. Alto proteína ventaja, riesgo de lipemia, hidratación crítica, comidas previas. Guía para donantes en dieta cetogénica.'
    category = 'Dieta y Nutrición'
    read_time = 9
    toc = [
        ('respuesta', 'Respuesta Rápida'),
        ('ventajas', 'Ventajas Keto'),
        ('riesgos', 'Riesgos de Lipemia'),
        ('adaptar', 'Cómo Adaptar Keto'),
        ('hidratacion', 'Hidratación Critical'),
        ('comidas', 'Comidas Pre-Donación'),
        ('tabla', 'Plan Semanal'),
        ('faq', 'Preguntas Frecuentes'),
    ]

    content = '''
<div class="highlight-box" id="respuesta">
    <h3>Respuesta Rápida</h3>
    <p>Puedes donar plasma EN dieta keto, pero <strong>requiere preparación especial</strong>. VENTAJA: alto proteína de keto es ideal para plasma. RIESGO: ketosis severa causa lipemia (plasma nublado) que centros rechazan. SOLUCIÓN: Modifica keto 48 horas antes: <strong>come carbohidratos limpios, reduce grasa extrema, hidratate agresivamente</strong>. Resultado: plasma de calidad + ganancias garantizadas + mantén mayoría de beneficios keto.</p>
</div>

<h2 id="ventajas">VENTAJAS: Por Qué Keto ES Bueno para Plasma</h2>
<p>La dieta keto tiene características naturalmente beneficiosas para donantes de plasma:</p>

<h3>Alto Proteína = Plasma de Calidad Superior</h3>
<ul>
    <li><strong>Proteína es base de plasma:</strong> La proteína en la sangre es un componente crítico del plasma</li>
    <li><strong>Keto es alto proteína:</strong> Típicamente 30-35% de calorías de proteína</li>
    <li><strong>Resultado:</strong> Tu plasma contiene más proteína que donantes regulares</li>
    <li><strong>Ventaja médica:</strong> Plasma alto proteína es más valioso para pacientes</li>
    <li><strong>Ventaja financiera:</strong> Algunos centros pueden pagar MÁS por plasma premium</li>
</ul>

<h3>Ketosis Reduce Inflamación</h3>
<ul>
    <li>Ketosis disminuye marcadores inflamatorios en sangre</li>
    <li>Plasma menos inflamado es más limpio</li>
    <li>Menos probabilidad de rechazo en centros</li>
    <li>Recuperación potencialmente más rápida</li>
</ul>

<h3>Peso Estable / Control de Peso</h3>
<ul>
    <li>Keto mantiene peso estable sin fluctuaciones extremas</li>
    <li>Peso consistente = compensación de plasma consistente</li>
    <li>No necesitas preocuparte sobre cambios de volumen donación</li>
</ul>

<h3>Energía y Enfoque Mejorados</h3>
<ul>
    <li>Keto proporciona energía estable sin picos de azúcar</li>
    <li>Mejor enfoque = mejor experiencia de donación</li>
    <li>Menos probabilidad de mareos/náuseas</li>
</ul>

<h2 id="riesgos">RIESGO PRINCIPAL: Lipemia por Ketosis</h2>
<p>El riesgo principal es lipemia - plasma graso/turbio que centros rechazan. Así es cómo ocurre:</p>

<h3>Qué es Lipemia en Contexto Keto</h3>
<ul>
    <li><strong>Definición:</strong> Exceso de lípidos (grasa) en sangre causando plasma turbio/lechoso</li>
    <li><strong>En Keto:</strong> Ketosis severa incrementa triglicéridos en sangre</li>
    <li><strong>Problema:</strong> Plasma lipémico es rechazado por centros porque:</li>
    <li>No es médicamente útil para pacientes</li>
    <li>Máquinas centrifugadoras no pueden procesarlo</li>
    <li>Indica salud potencialmente comprometida</li>
</ul>

<h3>Síntomas de Que Podrías Tener Lipemia</h3>
<ul>
    <li><strong>En casa (predictor):</strong> Sangre después de pinchazo parece turbia/lechosa</li>
    <li><strong>En centro:</strong> Técnico señala que plasma parece graso/turbio</li>
    <li><strong>Después de rechazo:</strong> Centro dice "lipemia" o "plasma nublado"</li>
    <li><strong>Test de laboratorio:</strong> Niveles de triglicéridos >400 mg/dL</li>
</ul>

<h3>Riesgos de Rechazo Repetido</h3>
<ul>
    <li>Un rechazo: sin pago esa vez ($50-100 perdidos)</li>
    <li>Dos rechazos: centro puede investigar</li>
    <li>Tres+ rechazos: posible descalificación temporal o permanente</li>
    <li>Consecuencia: pierdes oportunidad de ganar dinero</li>
</ul>

<h2 id="adaptar">SOLUCIÓN: Cómo Adaptar Keto para Donaciones</h2>
<p>No necesitas DEJAR keto. Solo modifícalo estratégicamente antes de donar:</p>

<h3>Modificación de Keto: Protocolo de 48 Horas Antes</h3>
<p><strong>2 días antes de donación:</strong> Haz estos cambios temporales:</p>

<h4>1. Aumenta Carbohidratos (pero limpios)</h4>
<ul>
    <li><strong>Cantidad:</strong> 50-100g carbohidratos netos (no todo el día)</li>
    <li><strong>Timing:</strong> Distribuye durante el día, mayoría en lunch/dinner</li>
    <li><strong>Tipos BUENOS:</strong>
        <ul>
            <li>Arroz blanco o integral (1 taza)</li>
            <li>Papas blancas al horno o hervidas (1 mediana)</li>
            <li>Avena (1/2 taza)</li>
            <li>Pan integral (1-2 rebanadas)</li>
            <li>Frutas limpias: manzanas, plátanos, naranjas</li>
        </ul>
    </li>
    <li><strong>Tipos a EVITAR:</strong> azúcar procesado, donuts, sodas, dulces</li>
</ul>

<h4>2. REDUCE Grasa Extrema</h4>
<ul>
    <li><strong>Problema:</strong> Alto grasa en keto + carbs bajos = triglicéridos muy altos</li>
    <li><strong>Solución:</strong> Reduce grasa 48 horas antes de donación</li>
    <li><strong>Cómo:</strong>
        <ul>
            <li>Menos aceite de coco y MCT (grasas saturadas)</li>
            <li>Menos carnes grasosas (toma magras en su lugar)</li>
            <li>Menos productos lácteos enteros (toma light)</li>
            <li>Come proteína magra: pollo pechuga, pavo, pescado blanco</li>
        </ul>
    </li>
    <li><strong>Meta:</strong> 30-40% calorías de grasa (vs 70% típico keto)</li>
</ul>

<h4>3. Mantén o Aumenta Proteína</h4>
<ul>
    <li>Mantén alto proteína (que es punto fuerte keto)</li>
    <li>Pero de fuentes MAGRAS</li>
    <li>Proteína no causa lipemia - ¡es beneficiosa para plasma!</li>
</ul>

<h4>4. Hidratación Agresiva</h3>
<ul>
    <li>20+ vasos de agua 48 horas antes</li>
    <li>Ayuda diluir triglicéridos</li>
    <li>Necesario de todas formas para donación</li>
</ul>

<h3>Cronograma Específico</h3>
<table>
    <thead>
        <tr>
            <th>Tiempo</th>
            <th>Acción</th>
            <th>Detalles</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>72+ horas antes</strong></td>
            <td>Keto normal</td>
            <td>Mantén tu keto regular 70/25/5 o similar</td>
        </tr>
        <tr>
            <td><strong>48 horas antes</strong></td>
            <td>Comienza transición</td>
            <td>Agrega carbohidratos limpios, reduce grasas extremas, hidratación comienza</td>
        </tr>
        <tr>
            <td><strong>24 horas antes</strong></td>
            <td>Carbohidratos moderados</td>
            <td>50g carbs netos, proteína alta, grasa moderada, NO alcohol</td>
        </tr>
        <tr>
            <td><strong>12 horas antes</strong></td>
            <td>Comida pre-donación</td>
            <td>Proteína + carbohidratos limpios, sin grasas</td>
        </tr>
        <tr>
            <td><strong>2-3 horas antes</strong></td>
            <td>Comida ligera</td>
            <td>Bocadillo pequeño proteína + carbohidrato</td>
        </tr>
        <tr>
            <td><strong>Mañana de donación</strong></td>
            <td>Hidratación continuada</td>
            <td>8 vasos agua antes de salir, bebe en centro</td>
        </tr>
        <tr>
            <td><strong>Después de donación</strong></td>
            <td>Vuelta gradual a keto</td>
            <td>Puedes volver a keto regular ese día, pero hidratate más</td>
        </tr>
    </tbody>
</table>

<h2 id="hidratacion">CRÍTICO: Hidratación en Dieta Keto</h2>
<p>Keto es naturalmente deshidratante. Donación también. Juntos = riesgo grave.</p>

<h3>Por Qué Keto Deshidrata</h3>
<ul>
    <li><strong>Menos carbohidratos:</strong> Carbohidratos retienen agua - menos carbs = menos retención</li>
    <li><strong>Diurético natural:</strong> Cetosis aumenta producción de orina</li>
    <li><strong>Pérdida de electrolitos:</strong> Keto causa pérdida de sodio/potasio</li>
    <li><strong>Resultado:</strong> Deshidratación crónica leve en keto sin cuidado</li>
</ul>

<h3>Protocolo de Hidratación para Donantes Keto</h3>
<ul>
    <li><strong>Diariamente (en keto):</strong> 4 litros (16 vasos) mínimo agua</li>
    <li><strong>Agua con electrolitos:</strong> Liquid IV, DripDrop, o agua de coco (cero azúcar)</li>
    <li><strong>48 horas antes donación:</strong> 5+ litros agua</li>
    <li><strong>Mañana de donación:</strong> 2 litros antes de ir al centro</li>
    <li><strong>En centro:</strong> Bebe agua mientras esperas y durante donación</li>
    <li><strong>Después de donación:</strong> 2+ litros agua para recuperación</li>
</ul>

''' + AFFILIATE_ES + '''

<h2 id="comidas">Plan de Comidas Pre-Donación (Keto Modificado)</h2>
<p><strong>48 horas antes de tu donación - comer así:</strong></p>

<h3>Opción A: Plan Diario 48 Horas Antes</h3>
<table>
    <thead>
        <tr>
            <th>Comida</th>
            <th>Ejemplo</th>
            <th>Beneficios</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Desayuno</strong></td>
            <td>Avena (1/2 taza) con proteína en polvo, fruta fresca</td>
            <td>Carbohidrato + proteína + hidratación inicio</td>
        </tr>
        <tr>
            <td><strong>Snack</strong></td>
            <td>Plátano + pechuga pollo magra</td>
            <td>Carbohidrato + proteína magra</td>
        </tr>
        <tr>
            <td><strong>Almuerzo</strong></td>
            <td>Pollo a la brasa, arroz blanco, brócoli con salsa limón</td>
            <td>Proteína + carbohidrato limpios, sin grasa</td>
        </tr>
        <tr>
            <td><strong>Snack tarde</strong></td>
            <td>Manzana + queso bajo grasa</td>
            <td>Fibra + proteína</td>
        </tr>
        <tr>
            <td><strong>Cena</strong></td>
            <td>Salmón (graso pero saludable), papa al horno, ensalada</td>
            <td>Proteína + ácidos grasos omega, carbohidrato</td>
        </tr>
        <tr>
            <td><strong>Bebida todo día</strong></td>
            <td>Agua + Liquid IV (electrolitos)</td>
            <td>Hidratación + reposición electrolitos</td>
        </tr>
    </tbody>
</table>

<h3>Opción B: Comidas Específicas 24 Horas Antes (Día de Donación)</h3>
<table>
    <thead>
        <tr>
            <th>Cuándo</th>
            <th>Qué Comer</th>
            <th>Macros Aprox</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Desayuno (7 AM)</strong></td>
            <td>Huevos (claras 3 + 1 yema), tostada integral, fruta</td>
            <td>25g proteína, 30g carb, 5g grasa</td>
        </tr>
        <tr>
            <td><strong>Almuerzo (12 PM)</strong></td>
            <td>Pollo a la brasa (4 oz), arroz blanco (1 taza), verduras</td>
            <td>35g proteína, 45g carb, 3g grasa</td>
        </tr>
        <tr>
            <td><strong>Merienda (3 PM)</strong></td>
            <td>Plátano pequeño + 2 oz queso bajo grasa</td>
            <td>12g proteína, 25g carb, 3g grasa</td>
        </tr>
        <tr>
            <td><strong>Bebida continua</strong></td>
            <td>Agua, té sin cafeína, agua con electrolitos</td>
            <td>0 macros, máxima hidratación</td>
        </tr>
    </tbody>
</table>

''' + PRO_TOOLKIT_ES + '''

<h2 id="tabla">Plan Semanal: Keto + Donación de Plasma</h2>
<p><strong>Estructura una semana cuando donas dos veces (miércoles y domingo típicamente):</strong></p>

<table>
    <thead>
        <tr>
            <th>Día</th>
            <th>Estado</th>
            <th>Dieta</th>
            <th>Actividad</th>
            <th>Notas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Lunes</strong></td>
            <td>Normal post-donación</td>
            <td>Keto normal (puedes regresar)</td>
            <td>Descanso ligero</td>
            <td>Recuperándote de domingo</td>
        </tr>
        <tr>
            <td><strong>Martes</strong></td>
            <td>Preparación</td>
            <td>Keto modificado - comienza cambios</td>
            <td>Sin ejercicio intenso</td>
            <td>48 horas antes de miércoles</td>
        </tr>
        <tr>
            <td><strong>Miércoles</strong></td>
            <td><strong>DONACIÓN 1</strong></td>
            <td>Carbohidrato + proteína magra, sin grasa</td>
            <td>Descanso</td>
            <td>Plan comidas pre-donación</td>
        </tr>
        <tr>
            <td><strong>Jueves</strong></td>
            <td>Recuperación</td>
            <td>Keto normal gradualmente</td>
            <td>Ligero, más agua</td>
            <td>Volviendo a keto después donación</td>
        </tr>
        <tr>
            <td><strong>Viernes</strong></td>
            <td>Normal</td>
            <td>Keto completo</td>
            <td>Actividad normal</td>
            <td>Totalmente recuperado</td>
        </tr>
        <tr>
            <td><strong>Sábado</strong></td>
            <td>Preparación</td>
            <td>Keto modificado - comienza cambios</td>
            <td>Sin ejercicio intenso</td>
            <td>48 horas antes de domingo</td>
        </tr>
        <tr>
            <td><strong>Domingo</strong></td>
            <td><strong>DONACIÓN 2</strong></td>
            <td>Carbohidrato + proteína magra, sin grasa</td>
            <td>Descanso</td>
            <td>Plan comidas pre-donación</td>
        </tr>
    </tbody>
</table>

''' + related_es([
    ('/es/blog/cuanto-pagan-por-donar-plasma-2026.html', 'Cuánto Pagan por Donar Plasma 2026'),
    ('/es/blog/requisitos-donacion-plasma.html', 'Requisitos Completos para Donar'),
    ('/es/blog/guia-completa-donacion-plasma.html', 'Guía Completa de Donación'),
]) + '''

<h2 id="faq">Preguntas Frecuentes: Keto y Donación</h2>
<h3>¿Puedo donar plasma en keto estricto sin modificar?</h3>
<p>Técnicamente sí, pero alto riesgo de lipemia (plasma turbio) y rechazo. Si lo haces: hidrata MUCHO, mantén electrolitos, y espera que el 30-50% de tus donaciones podrían rechazarse. Mejor: modifica 48 horas antes como indicado.</p>

<h3>¿El plasma de alguien en keto es mejor calidad?</h3>
<p>Sí, potencialmente. Alto proteína de keto es beneficioso. PERO solo si no tienes lipemia. Si tienes lipemia severa, es peor calidad. Por eso la modificación pre-donación es clave.</p>

<h3>¿Perderé resultados de keto si como carbohidratos 48 horas antes?</h3>
<p>Mínimamente. 50-100g carbohidratos durante 48 horas podría sacarte de ketosis, pero retornarás rápidamente (1-2 días) después que vuelvas a keto normal. Pérdida de peso mínima, completamente recuperable.</p>

<h3>¿Necesito suplemento de electrolitos si hago keto?</h3>
<p>SÍ recomendado, especialmente si donas. Keto + donación = doble deshidratación. Liquid IV, DripDrop, o electrolitos caseros (sal + potasio) son buenos. Al mínimo, toma caldo de hueso o agua de coco.</p>
'''

    faqs = [
        make_faq("¿Puedo donar plasma en keto estricto?", "Sí pero alto riesgo de lipemia (30-50% rechazo). Mejor: modifica 48 horas antes - agrega carbohidratos, reduce grasa extrema."),
        make_faq("¿El plasma de keto es mejor calidad?", "Sí potencialmente - alto proteína es bueno. PERO solo si no tienes lipemia. Modifica pre-donación para evitar lipemia."),
        make_faq("¿Perderé resultados de keto?", "No mucho. 50-100g carbs durante 48 horas causa salida mínima de ketosis, retornas rápidamente después."),
        make_faq("¿Necesito electrolitos si hago keto?", "SÍ recomendado. Keto + donación = doble deshidratación. Usa Liquid IV, DripDrop, o agua de coco cero azúcar."),
    ]

    return make_es_page(slug, title, meta, category, read_time, toc, content, faqs)


if __name__ == '__main__':
    print("Generating Round 4: Spanish topic/guide pages (5 pages)...")
    count = 0

    # Create pages
    pages = [
        ("Maestros", gen_maestros()),
        ("Padres Solteros", gen_padres_solteros()),
        ("Jubilados", gen_jubilados()),
        ("Qué NO Hacer", gen_no_hacer()),
        ("Keto", gen_keto()),
    ]

    for name, html in pages:
        # Extract slug from HTML to save with correct name
        if 'maestros' in html.lower():
            slug = 'donar-plasma-para-maestros-profesores-2026'
        elif 'padres' in html.lower():
            slug = 'donar-plasma-para-padres-solteros-guia-2026'
        elif 'jubilados' in html.lower():
            slug = 'donar-plasma-para-jubilados-mayores-2026'
        elif 'no hacer' in html.lower() or 'que no' in html.lower():
            slug = 'donar-plasma-que-no-hacer-antes-guia-2026'
        elif 'keto' in html.lower():
            slug = 'donar-plasma-y-dieta-keto-cetogenica-2026'
        else:
            continue

        path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: es/blog/{slug}.html")
        count += 1

    print(f"Done! Generated {count} Spanish topic/guide pages.")
