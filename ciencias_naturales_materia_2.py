import streamlit as st

st.set_page_config(page_title="Repaso 4º Primaria - Sociales", page_icon="📝", layout="wide")

st.title("📝 Gran Repaso de Ciencias Sociales - 4º Primaria")
st.markdown("""
¡Hola! Lee bien cada pregunta. La mayoría son de elegir la opción correcta, pero en algunas tendrás que escribir. 
**No sabrás tu nota hasta que termines todo y pulses el botón del final.** ¡Mucha suerte!
""")

# Base de datos de 50 preguntas (60% desplegables, 40% escribir)
preguntas = [
    # --- LA POBLACIÓN ---
    {"id": 1, "tipo": "seleccion", "preg": "¿Cada cuántos años se realiza el Censo en España?", "opciones": ["Elige...", "Cada 5 años", "Cada 10 años", "Cada año"], "correcta": "Cada 10 años", "explicacion": "El censo se realiza cada 10 años."},
    {"id": 2, "tipo": "seleccion", "preg": "¿Quién se encarga de llevar el Padrón?", "opciones": ["Elige...", "El Gobierno de España", "Los Ayuntamientos", "Los colegios"], "correcta": "Los Ayuntamientos", "explicacion": "El padrón lo llevan los ayuntamientos."},
    {"id": 3, "tipo": "seleccion", "preg": "Una persona que se va de su país para vivir en otro es un...", "opciones": ["Elige...", "Inmigrante", "Emigrante", "Turista"], "correcta": "Emigrante", "explicacion": "Cuando salen de su país se llaman emigrantes."},
    {"id": 4, "tipo": "seleccion", "preg": "La 'esperanza de vida' nos indica...", "opciones": ["Elige...", "Los bebés que nacen", "La media de años que vive la gente", "La gente que se muda"], "correcta": "La media de años que vive la gente", "explicacion": "Es la media de años que viven las personas."},
    {"id": 5, "tipo": "seleccion", "preg": "¿Dónde vive la mayor parte de la población en España?", "opciones": ["Elige...", "En las áreas rurales (pueblos)", "En las áreas urbanas (ciudades)"], "correcta": "En las áreas urbanas (ciudades)", "explicacion": "La mayor parte reside en áreas urbanas."},
    {"id": 6, "tipo": "seleccion", "preg": "Para saber la densidad de población, dividimos los habitantes entre...", "opciones": ["Elige...", "El número de casas", "El territorio o superficie", "Los años que tienen"], "correcta": "El territorio o superficie", "explicacion": "Se divide el número de habitantes por el territorio."},
    {"id": 7, "tipo": "corta", "preg": "Escribe: Una persona que llega a un país nuevo a vivir es un...", "resp_corta": ["inmigrante"], "explicacion": "Se denomina inmigrante."},
    {"id": 8, "tipo": "corta", "preg": "Escribe: El número de niños y niñas que nacen se llama...", "resp_corta": ["natalidad"], "explicacion": "Se llama natalidad."},
    {"id": 9, "tipo": "larga", "preg": "Define con tus palabras: ¿Qué es el Padrón?", "explicacion": "Es un registro del ayuntamiento para saber cuántas personas viven en el municipio. Se anota si alguien se muda."},
    {"id": 10, "tipo": "larga", "preg": "¿Por qué decimos que la población española está 'envejecida'?", "explicacion": "Porque nacen pocos niños (baja natalidad) y la gente vive muchos años (alta esperanza de vida)."},

    # --- EL TERRITORIO ---
    {"id": 11, "tipo": "seleccion", "preg": "¿Quién gobierna un municipio?", "opciones": ["Elige...", "El Presidente", "El Rey", "El Ayuntamiento"], "correcta": "El Ayuntamiento", "explicacion": "El municipio está gobernado por el Ayuntamiento."},
    {"id": 12, "tipo": "seleccion", "preg": "El Ayuntamiento está formado por los concejales y...", "opciones": ["Elige...", "El alcalde o alcaldesa", "Los policías", "Los jueces"], "correcta": "El alcalde o alcaldesa", "explicacion": "Formado por la alcaldesa o el alcalde y los concejales."},
    {"id": 13, "tipo": "seleccion", "preg": "¿A partir de qué edad se puede votar en las elecciones municipales?", "opciones": ["Elige...", "16 años", "18 años", "21 años"], "correcta": "18 años", "explicacion": "Los mayores de 18 años votan para elegir a los concejales."},
    {"id": 14, "tipo": "seleccion", "preg": "Varios municipios agrupados forman una...", "opciones": ["Elige...", "Provincia", "Comunidad Autónoma", "Región"], "correcta": "Provincia", "explicacion": "Los municipios se agrupan en provincias."},
    {"id": 15, "tipo": "seleccion", "preg": "Varias provincias agrupadas forman una...", "opciones": ["Elige...", "Nación", "Comunidad Autónoma", "Ciudad"], "correcta": "Comunidad Autónoma", "explicacion": "Las provincias forman comunidades autónomas."},
    {"id": 16, "tipo": "seleccion", "preg": "¿Cuántos países forman la Unión Europea?", "opciones": ["Elige...", "15", "27", "50"], "correcta": "27", "explicacion": "Un grupo de 27 países unidos."},
    {"id": 17, "tipo": "corta", "preg": "Escribe: ¿Qué ciudad tiene el término municipal más grande de España?", "resp_corta": ["caceres", "cáceres"], "explicacion": "La ciudad de Cáceres."},
    {"id": 18, "tipo": "corta", "preg": "Escribe: ¿Cuál es la moneda que comparten muchos países de la UE?", "resp_corta": ["euro", "el euro"], "explicacion": "Es el euro."},
    {"id": 19, "tipo": "larga", "preg": "Nombra tres servicios de los que se encarga el Ayuntamiento:", "explicacion": "Alumbrado, recogida de basuras, agua potable, parques, bibliotecas, policía municipal..."},
    {"id": 20, "tipo": "larga", "preg": "¿Para qué sirve el Parlamento Europeo?", "explicacion": "Para que los ciudadanos elijan a sus representantes y se mejore la vida en Europa."},

    # --- NORMAS Y SEÑALES ---
    {"id": 21, "tipo": "seleccion", "preg": "Las normas surgen para...", "opciones": ["Elige...", "Fastidiar a la gente", "Cubrir una necesidad y convivir mejor", "Ganar dinero"], "correcta": "Cubrir una necesidad y convivir mejor", "explicacion": "Surgen para cubrir una necesidad y convivir mejor."},
    {"id": 22, "tipo": "seleccion", "preg": "¿Dónde se recogen los derechos y deberes de la sociedad española?", "opciones": ["Elige...", "En el Censo", "En la Constitución", "En el Ayuntamiento"], "correcta": "En la Constitución", "explicacion": "En la Constitución se recogen los derechos."},
    {"id": 23, "tipo": "seleccion", "preg": "Una señal de tráfico TRIANGULAR con borde rojo indica...", "opciones": ["Elige...", "Prohibición", "Obligación", "Peligro"], "correcta": "Peligro", "explicacion": "Peligro: avisan de un posible peligro."},
    {"id": 24, "tipo": "seleccion", "preg": "Una señal CIRCULAR con borde ROJO indica...", "opciones": ["Elige...", "Prohibición", "Obligación", "Información"], "correcta": "Prohibición", "explicacion": "Prohibición: indican algo que no se puede hacer."},
    {"id": 25, "tipo": "seleccion", "preg": "Una señal CIRCULAR y de color AZUL indica...", "opciones": ["Elige...", "Prohibición", "Obligación", "Peligro"], "correcta": "Obligación", "explicacion": "Obligación: son circulares de color azul."},
    {"id": 26, "tipo": "seleccion", "preg": "Un paso de cebra es una norma de...", "opciones": ["Elige...", "Educación vial", "Educación física", "Norma de casa"], "correcta": "Educación vial", "explicacion": "Pertenece a la educación vial."},
    {"id": 27, "tipo": "corta", "preg": "Escribe: Si el semáforo para peatones está en rojo, tienes la obligación de...", "resp_corta": ["parar", "esperar"], "explicacion": "Parar y esperar a que se ponga verde."},
    {"id": 28, "tipo": "corta", "preg": "Escribe: Respetar el turno de palabra es una norma de...", "resp_corta": ["convivencia", "educacion"], "explicacion": "Es una norma de convivencia."},
    {"id": 29, "tipo": "larga", "preg": "¿Por qué es tan importante la educación vial?", "explicacion": "Para que peatones y vehículos puedan moverse con precaución y evitar accidentes o peligros."},
    {"id": 30, "tipo": "larga", "preg": "Escribe dos normas importantes que debes cumplir en el colegio:", "explicacion": "Levantar la mano para hablar, respetar a los compañeros, cuidar el material, no correr en pasillos..."},

    # --- EL DINERO ---
    {"id": 31, "tipo": "seleccion", "preg": "Antes de que existiera el dinero, se usaba el...", "opciones": ["Elige...", "Préstamo", "Trueque", "Ahorro"], "correcta": "Trueque", "explicacion": "Se usaba el trueque (intercambiar cosas)."},
    {"id": 32, "tipo": "seleccion", "preg": "El dinero que recibimos a cambio de nuestro trabajo se llama...", "opciones": ["Elige...", "Sueldo o salario", "Interés", "Precio"], "correcta": "Sueldo o salario", "explicacion": "Se llama salario o sueldo."},
    {"id": 33, "tipo": "seleccion", "preg": "Si hay pocos productos y mucha gente quiere comprarlos, el precio...", "opciones": ["Elige...", "Sube", "Baja", "Se queda igual"], "correcta": "Sube", "explicacion": "Cuando un producto es escaso y la gente lo quiere, su precio sube."},
    {"id": 34, "tipo": "seleccion", "preg": "Si hay muchos productos y poca gente quiere comprarlos, el precio...", "opciones": ["Elige...", "Sube", "Baja", "Desaparece"], "correcta": "Baja", "explicacion": "Cuando hay exceso de producción y pocos compradores, el precio baja."},
    {"id": 35, "tipo": "seleccion", "preg": "Guardar parte del dinero para imprevistos se llama...", "opciones": ["Elige...", "Gastar", "Prestar", "Ahorrar"], "correcta": "Ahorrar", "explicacion": "Es importante ahorrar parte del sueldo para imprevistos."},
    {"id": 36, "tipo": "seleccion", "preg": "Cuando el banco te deja dinero para comprar una casa, te da un...", "opciones": ["Elige...", "Regalo", "Préstamo", "Sueldo"], "correcta": "Préstamo", "explicacion": "Acudimos al banco a pedir un préstamo."},
    {"id": 37, "tipo": "corta", "preg": "Escribe: El dinero extra que le devuelves al banco por haberte dado un préstamo se llama...", "resp_corta": ["interes", "interés"], "explicacion": "Se llama interés."},
    {"id": 38, "tipo": "corta", "preg": "Escribe: El valor o dinero que cuesta un producto es su...", "resp_corta": ["precio"], "explicacion": "Es el precio."},
    {"id": 39, "tipo": "larga", "preg": "¿Por qué se inventó el dinero y se dejó de usar el trueque?", "explicacion": "Porque el trueque era muy complicado, era difícil poner de acuerdo a las personas sobre lo que valían las cosas."},
    {"id": 40, "tipo": "larga", "preg": "Explica la diferencia entre un gasto necesario y un deseo (gasto prescindible):", "explicacion": "Lo necesario hace falta para vivir (comida, casa, ropa). Un deseo es algo que queremos pero no es vital (juguetes, chuches)."},

    # --- CUIDAMOS EL PLANETA ---
    {"id": 41, "tipo": "seleccion", "preg": "Los recursos naturales del planeta son...", "opciones": ["Elige...", "Limitados (se pueden acabar)", "Ilimitados (nunca se acaban)", "Infinitos"], "correcta": "Limitados (se pueden acabar)", "explicacion": "Los recursos naturales son limitados."},
    {"id": 42, "tipo": "seleccion", "preg": "Las energías que no contaminan y no se agotan son las...", "opciones": ["Elige...", "No renovables", "Renovables", "Fósiles"], "correcta": "Renovables", "explicacion": "Las energías renovables no contaminan y no se agotan."},
    {"id": 43, "tipo": "seleccion", "preg": "¿Cuál de estas es una energía renovable?", "opciones": ["Elige...", "El petróleo", "El carbón", "La energía eólica (viento)"], "correcta": "La energía eólica (viento)", "explicacion": "La energía eólica (viento) es renovable."},
    {"id": 44, "tipo": "seleccion", "preg": "¿Cuál de estas energías contamina mucho?", "opciones": ["Elige...", "El sol", "El petróleo", "El viento"], "correcta": "El petróleo", "explicacion": "El petróleo contamina poco... espera, en tu libro dice 'El petróleo contamina poco. Es una energía renovable' (Nota: ¡Hay una errata en la foto 1 de tu libro! El petróleo es muy contaminante y no renovable, pero para el examen marcaremos el petróleo como contaminante en el mundo real)."},
    {"id": 45, "tipo": "seleccion", "preg": "El impacto que nuestro modo de vida tiene sobre el planeta se llama...", "opciones": ["Elige...", "Huella ecológica", "Censo natural", "Padrón ecológico"], "correcta": "Huella ecológica", "explicacion": "Se llama huella ecológica."},
    {"id": 46, "tipo": "seleccion", "preg": "El agua lista para que las personas la puedan beber es el agua...", "opciones": ["Elige...", "Salada", "Potable", "Residual"], "correcta": "Potable", "explicacion": "Es el agua potable."},
    {"id": 47, "tipo": "corta", "preg": "Escribe: Una acción beneficiosa para el planeta que empieza por la letra R es...", "resp_corta": ["reciclar", "reutilizar", "reducir"], "explicacion": "Reciclar, reducir o reutilizar."},
    {"id": 48, "tipo": "corta", "preg": "Escribe: Los seres vivos como las plantas nos dan un gas necesario para respirar, el...", "resp_corta": ["oxigeno", "oxígeno"], "explicacion": "Nos proporcionan grandes beneficios como el oxígeno."},
    {"id": 49, "tipo": "larga", "preg": "¿Por qué no toda la gente del mundo tiene fácil acceso al agua potable?", "explicacion": "Por la falta de lluvias (sequías), la contaminación o porque en algunos países no hay grifos ni tuberías cerca."},
    {"id": 50, "tipo": "larga", "preg": "¿Qué tres cosas podrías hacer tú en tu día a día para cuidar el planeta?", "explicacion": "Apagar las luces, cerrar el grifo mientras me lavo los dientes, reciclar la basura, usar menos plástico..."}
]

# Formulario principal del examen
with st.form("examen_form"):
    respuestas_usuario = {}
    
    st.header("1️⃣ Preguntas de Elegir (Desplegables)")
    for p in preguntas:
        if p["tipo"] == "seleccion":
            respuestas_usuario[p["id"]] = st.selectbox(f"{p['id']}. {p['preg']}", p["opciones"], key=f"q_{p['id']}")
            
    st.markdown("---")
    st.header("2️⃣ Preguntas de Escribir una o dos palabras")
    for p in preguntas:
        if p["tipo"] == "corta":
            respuestas_usuario[p["id"]] = st.text_input(f"{p['id']}. {p['preg']}", key=f"q_{p['id']}")

    st.markdown("---")
    st.header("3️⃣ Preguntas de Definición (Escribe con tus palabras)")
    for p in preguntas:
        if p["tipo"] == "larga":
            respuestas_usuario[p["id"]] = st.text_area(f"{p['id']}. {p['preg']}", key=f"q_{p['id']}")
            
    st.markdown("---")
    submitted = st.form_submit_button("🏁 Corregir mi examen", type="primary")

# Lógica de corrección al pulsar el botón
if submitted:
    st.balloons()
    st.header("📊 Resultados de tu Examen")
    
    aciertos_auto = 0
    total_auto = sum(1 for p in preguntas if p["tipo"] in ["seleccion", "corta"]) # 40 preguntas automáticas
    
    st.subheader("Corrección de Desplegables y Respuestas Cortas")
    
    for p in preguntas:
        if p["tipo"] == "seleccion":
            if respuestas_usuario[p["id"]] == p["correcta"]:
                aciertos_auto += 1
                st.success(f"**{p['id']}.** ¡Correcto! ✅ ({p['correcta']})")
            else:
                st.error(f"**{p['id']}.** ❌ Elegiste '{respuestas_usuario[p['id']]}'. **La correcta era: {p['correcta']}**")
                
        elif p["tipo"] == "corta":
            ans = respuestas_usuario[p["id"]].strip().lower()
            # Quitamos tildes para no ser estrictos
            ans_limpia = ans.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
            validas = [r.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') for r in p["resp_corta"]]
            
            if ans_limpia in validas and ans_limpia != "":
                aciertos_auto += 1
                st.success(f"**{p['id']}.** ¡Correcto! ✅ ({respuestas_usuario[p['id']]})")
            else:
                st.error(f"**{p['id']}.** ❌ Escribiste '{respuestas_usuario[p['id']]}'. **La correcta era: {p['resp_corta'][0].capitalize()}**")

    # Nota sobre 10 de la parte automática (regla de 3: aciertos * 10 / 40)
    nota_test = (aciertos_auto * 10) / total_auto
    st.metric(label="Nota de la parte tipo test y corta (sobre 10)", value=f"{nota_test:.1f}")

    st.markdown("---")
    st.subheader("🧠 Corrección de Definiciones (¡Compara tus respuestas!)")
    st.info("Aquí tienes las respuestas correctas del libro. Compara lo que has escrito con la solución para ver si lo sabías bien.")
    
    for p in preguntas:
        if p["tipo"] == "larga":
            with st.expander(f"Pregunta {p['id']}. {p['preg']}"):
                st.write("**Lo que tú escribiste:**")
                st.markdown(f"> *{respuestas_usuario[p['id']]}*")
                st.write("**La respuesta correcta para estudiar:**")
                st.success(p['explicacion'])