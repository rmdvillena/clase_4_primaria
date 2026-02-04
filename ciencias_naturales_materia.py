import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Súper Examen de Ciencias: La Materia (55 Preguntas)",
    page_icon="⚗️",
    layout="centered"
)

# --- ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    h1 { color: #2e8b57; text-align: center; font-family: 'Comic Sans MS', sans-serif; }
    h2 { color: #4682b4; border-bottom: 2px solid #4682b4; padding-bottom: 10px; margin-top: 30px; }
    .lab-box { 
        background-color: #e6f7ff; 
        padding: 20px; 
        border: 2px dashed #1e90ff; 
        border-radius: 15px; 
        margin-bottom: 20px; 
    }
    .question-box {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .success { color: green; font-weight: bold; font-size: 1.1em; }
    .error { color: #d9534f; font-weight: bold; }
    .new-section { background-color: #d4edda; padding: 10px; border-radius: 5px; margin-bottom: 15px; color: #155724; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

st.title("🧪 Súper Examen: La Materia Completo 🧪")
st.markdown("""
**¡Hola científico/a!** 👩‍🔬👨‍🔬
Hemos ampliado el examen. ¡Ahora son 55 preguntas para demostrar que lo sabes TODO!
* **Parte 1:** Teoría Extendida (45 preguntas)
* **Parte 2:** Laboratorio Virtual (10 preguntas prácticas)
""")

# --- BASE DE DATOS DE PREGUNTAS (TOTAL 55) ---

# PARTE 1: TEORÍA (1-45)
theory_questions = [
    # --- BLOQUE ORIGINAL (1-30) ---
    {"id": 1, "q": "1. ¿Qué es la materia?", "type": "choice", "opts": ["Luz y calor", "Todo lo que tiene masa y volumen", "Solo lo que se puede tocar"], "ans": "Todo lo que tiene masa y volumen"},
    {"id": 2, "q": "2. Las propiedades generales son el volumen y la...", "type": "text", "ans": "masa"},
    {"id": 3, "q": "3. ¿Qué instrumento usamos para medir la masa?", "type": "choice", "opts": ["Balanza o báscula", "Probeta", "Termómetro"], "ans": "Balanza o báscula"},
    {"id": 4, "q": "4. El espacio que ocupa un cuerpo se llama...", "type": "choice", "opts": ["Peso", "Masa", "Volumen"], "ans": "Volumen"},
    {"id": 5, "q": "5. La resistencia a romperse se llama...", "type": "choice", "opts": ["Dureza", "Fragilidad", "Elasticidad"], "ans": "Dureza"},
    {"id": 6, "q": "6. Si un material recupera su forma después de estirarlo, tiene...", "type": "text", "ans": "elasticidad"},
    {"id": 7, "q": "7. ¿Qué propiedad permite ver a través de un objeto (como el vidrio)?", "type": "text", "ans": "transparencia"},
    {"id": 8, "q": "8. Si una piedra se hunde en agua es porque su densidad es...", "type": "choice", "opts": ["Mayor que el agua", "Menor que el agua", "Igual que el agua"], "ans": "Mayor que el agua"},
    {"id": 9, "q": "9. La capacidad de atraer metales se llama...", "type": "text", "ans": "magnetismo"},
    {"id": 10, "q": "10. El paso de SÓLIDO a LÍQUIDO se llama...", "type": "choice", "opts": ["Fusión", "Solidificación", "Vaporización"], "ans": "Fusión"},
    {"id": 11, "q": "11. Cuando el agua hierve y se hace vapor, es una...", "type": "choice", "opts": ["Condensación", "Vaporización", "Fusión"], "ans": "Vaporización"},
    {"id": 12, "q": "12. De líquido a sólido (hacer hielo) se llama...", "type": "choice", "opts": ["Fusión", "Solidificación", "Sublimación"], "ans": "Solidificación"},
    {"id": 13, "q": "13. Cuando la materia cambia de estado, ¿su masa cambia?", "type": "choice", "opts": ["Sí, pesa menos", "Sí, pesa más", "No, la masa no cambia"], "ans": "No, la masa no cambia"},
    {"id": 14, "q": "14. Si la materia puede volver a su estado inicial, el cambio es...", "type": "text", "ans": "reversible"},
    {"id": 15, "q": "15. Quemar madera es un cambio...", "type": "choice", "opts": ["Físico", "Químico", "Reversible"], "ans": "Químico"},
    {"id": 16, "q": "16. Cuando el hierro reacciona con el oxígeno se produce...", "type": "text", "ans": "oxidacion"},
    {"id": 17, "q": "17. La combustión desprende luz y...", "type": "text", "ans": "calor"},
    {"id": 18, "q": "18. Una sustancia formada por un solo componente (ej. oro puro) es...", "type": "choice", "opts": ["Sustancia pura", "Mezcla homogénea", "Mezcla heterogénea"], "ans": "Sustancia pura"},
    {"id": 19, "q": "19. Una ensalada es una mezcla...", "type": "choice", "opts": ["Homogénea", "Heterogénea", "Pura"], "ans": "Heterogénea"},
    {"id": 20, "q": "20. Agua con sal (no se distingue la sal) es una mezcla...", "type": "text", "ans": "homogenea"},
    {"id": 21, "q": "21. Separar sólidos de distinto tamaño (arena y piedras) se hace por...", "type": "choice", "opts": ["Filtración", "Tamizado", "Evaporación"], "ans": "Tamizado"},
    {"id": 22, "q": "22. Separar líquidos de distinta densidad (agua y aceite) se hace por...", "type": "choice", "opts": ["Decantación", "Filtración", "Imantación"], "ans": "Decantación"},
    {"id": 23, "q": "23. Para sacar la sal del agua de mar usamos la...", "type": "text", "ans": "evaporacion"},
    {"id": 24, "q": "24. La lana y la madera son materiales de origen...", "type": "choice", "opts": ["Natural", "Artificial", "Mineral"], "ans": "Natural"},
    {"id": 25, "q": "25. El plástico y el papel son materiales...", "type": "choice", "opts": ["Naturales", "Artificiales", "Mágicos"], "ans": "Artificiales"},
    {"id": 26, "q": "26. El calor es una forma de...", "type": "text", "ans": "energia"},
    {"id": 27, "q": "27. Al recibir calor, la temperatura de un cuerpo...", "type": "choice", "opts": ["Baja", "Sube", "Se queda igual"], "ans": "Sube"},
    {"id": 28, "q": "28. Un material que NO deja pasar el calor es un...", "type": "text", "ans": "aislante"},
    {"id": 29, "q": "29. Si cambian las sustancias que componen la materia, es un cambio...", "type": "choice", "opts": ["Físico", "Químico"], "ans": "Químico"},
    {"id": 30, "q": "30. Método para separar mezclas homogéneas calentando:", "type": "choice", "opts": ["Destilación", "Filtración", "Tamizado"], "ans": "Destilación"},
    
    # --- NUEVAS PREGUNTAS AÑADIDAS (31-45) ---
    
    # Basadas en la nueva imagen (Arcilla, cambios reversibles/irreversibles)
    {"id": 31, "q": "31. (Basado en imagen) Al moldear una bola de arcilla para hacer una taza, solo cambiamos su forma. ¿Es un cambio físico o químico?", "type": "choice", "opts": ["Físico", "Químico"], "ans": "Físico"},
    {"id": 32, "q": "32. (Basado en imagen) Quemar leña en una hoguera es un cambio IRREVERSIBLE porque...", "type": "choice", "opts": ["La madera solo cambia de forma", "La madera se transforma en ceniza y humo y no puede volver a ser leña"], "ans": "La madera se transforma en ceniza y humo y no puede volver a ser leña"},
    {"id": 33, "q": "33. (Basado en imagen) Hornear la masa de un bizcocho es un cambio químico irreversible, pero congelar agua en una cubitera es un cambio físico...", "type": "text", "ans": "reversible"},

    # Más Propiedades (Escribir)
    {"id": 34, "q": "34. La propiedad por la que el cristal se rompe fácilmente al golpearlo se llama...", "type": "text", "ans": "fragilidad"},
    {"id": 35, "q": "35. El diamante es el material natural más difícil de rayar. Tiene mucha...", "type": "text", "ans": "dureza"},
    {"id": 36, "q": "36. Un material que NO permite que veamos a través de él (como la madera) es...", "type": "text", "ans": "opaco"},

    # Más Cambios Físicos vs Químicos
    {"id": 37, "q": "37. Cortar un papel en trocitos muy pequeños es un cambio...", "type": "choice", "opts": ["Físico (sigue siendo papel)", "Químico (ya no es papel)"], "ans": "Físico (sigue siendo papel)"},
    {"id": 38, "q": "38. Cuando se oxida un clavo de hierro y se pone marrón, es un cambio...", "type": "choice", "opts": ["Físico", "Químico"], "ans": "Químico"},
    {"id": 39, "q": "39. Disolver azúcar en un vaso de leche es un cambio...", "type": "text", "ans": "fisico"},

    # Más Mezclas y Estados
    {"id": 40, "q": "40. Una pizza con ingredientes visibles (queso, jamón, tomate) es una mezcla...", "type": "text", "ans": "heterogenea"},
    {"id": 41, "q": "41. El aire que respiramos es una mezcla de gases que no se distinguen a simple vista. Es una mezcla...", "type": "text", "ans": "homogenea"},
    {"id": 42, "q": "42. ¿Cuál de estas opciones es una mezcla homogénea?", "type": "choice", "opts": ["Agua con arena", "Un batido de fresa bien mezclado", "Una macedonia de frutas"], "ans": "Un batido de fresa bien mezclado"},
    {"id": 43, "q": "43. Cuando sacas una botella fría de la nevera y se forman gotitas de agua por fuera (el gas pasa a líquido), se llama...", "type": "text", "ans": "condensacion"},
    {"id": 44, "q": "44. El paso directo de estado SÓLIDO a estado GASEOSO (sin pasar por líquido) se llama...", "type": "text", "ans": "sublimacion"},
    {"id": 45, "q": "45. La cantidad de materia que tiene un cuerpo (medida en kg o g) es su...", "type": "text", "ans": "masa"}
]

# PARTE 2: LABORATORIO (Renumeradas de 46 a 55)
lab_questions = [
    {
        "id": 46,
        "q": "46. GRÁFICO: Mira la curva de temperatura. ¿A qué grados hierve este líquido?",
        "type": "chart_boiling",
        "opts": ["A 50°C", "A 100°C", "A 0°C"],
        "ans": "A 100°C"
    },
    {
        "id": 47,
        "q": "47. DENSIDAD: Tiramos una moneda de oro 🪙 y un trozo de corcho 🍾 al agua. ¿Qué dibujo es el real?",
        "type": "visual_density",
        "opts": ["A: Los dos flotan", "B: La moneda se hunde, el corcho flota", "C: La moneda flota, el corcho se hunde"],
        "ans": "B: La moneda se hunde, el corcho flota"
    },
    {
        "id": 48,
        "q": "48. MATEMÁTICAS: Si la balanza está equilibrada con una sandía 🍉 a un lado y dos pesas de 1kg al otro, ¿cuánto masa la sandía?",
        "type": "visual_balance",
        "opts": ["1 kg", "2 kg", "5 kg"],
        "ans": "2 kg"
    },
    {
        "id": 49,
        "q": "49. PARTÍCULAS: ¿Qué caja representa un GAS (partículas locas y separadas)?",
        "type": "visual_particles",
        "opts": ["Caja A", "Caja B"],
        "ans": "Caja B"
    },
    {
        "id": 50,
        "q": "50. FILTRACIÓN: Tenemos agua sucia con arena. Usamos un filtro. ¿Qué pasa al vaso de abajo?",
        "type": "visual_filter",
        "opts": ["Solo el agua limpia", "El agua y la arena", "Nada"],
        "ans": "Solo el agua limpia"
    },
    {
        "id": 51,
        "q": "51. VOLUMEN: La probeta marca 20ml. Metemos una canica y sube a 25ml. ¿Cuál es el volumen de la canica?",
        "type": "visual_probeta",
        "input_type": "number",
        "ans": "5"
    },
    {
        "id": 52,
        "q": "52. IMANES: ¿Cuál de estos objetos se quedará pegado al imán?",
        "type": "visual_magnet",
        "opts": ["Goma de borrar", "Clip de hierro", "Lápiz de madera"],
        "ans": "Clip de hierro"
    },
    {
        "id": 53,
        "q": "53. SOL: Un cubito de hielo 🧊 se queda al sol y se vuelve agua 💧. Este cambio es...",
        "type": "choice",
        "opts": ["Fusión", "Solidificación", "Vaporización"],
        "ans": "Fusión"
    },
    {
        "id": 54,
        "q": "54. CALOR: Tocas una cuchara de metal que estaba en la sopa caliente. ¡Te quemas! El metal es...",
        "type": "choice",
        "opts": ["Aislante", "Conductor", "Transparente"],
        "ans": "Conductor"
    },
    {
        "id": 55,
        "q": "55. MEZCLAS: ¿Cuál de estas imágenes sería una mezcla HETEROGÉNEA?",
        "type": "visual_mixture",
        "opts": ["Vaso A (Agua y Aceite)", "Vaso B (Agua con sal disuelta)"],
        "ans": "Vaso A (Agua y Aceite)"
    }
]

# Función para normalizar texto (ignorar mayúsculas y tildes)
def normalize(text):
    text = str(text).lower().strip()
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in replacements:
        text = text.replace(a, b)
    return text

# --- INICIO DEL FORMULARIO ---
with st.form("full_exam_extended"):
    user_answers = {}
    
    # --- RENDERIZADO PARTE 1: TEORÍA ---
    st.header("📚 Parte 1: Teoría Extendida (45 Preguntas)")
    
    for i, item in enumerate(theory_questions):
        # Separador visual para las nuevas preguntas
        if i == 30:
             st.markdown("<div class='new-section'>✨ ¡A partir de aquí son las preguntas nuevas! ✨</div>", unsafe_allow_html=True)

        st.markdown(f"**{item['q']}**")
        if item['type'] == 'choice':
            user_answers[item['id']] = st.radio("Elige una opción:", item['opts'], index=None, key=f"q{item['id']}")
        elif item['type'] == 'text':
            user_answers[item['id']] = st.text_input("Escribe tu respuesta:", key=f"q{item['id']}")
        st.markdown("---")

    # --- RENDERIZADO PARTE 2: LABORATORIO ---
    st.header("🔬 Parte 2: Laboratorio Virtual (10 Preguntas)")
    
    for item in lab_questions:
        st.markdown(f"<div class='lab-box'>", unsafe_allow_html=True)
        st.markdown(f"**{item['q']}**")
        
        # Lógica visual específica por tipo de pregunta de laboratorio
        if item['type'] == 'chart_boiling':
            data = pd.DataFrame({'Minutos': [0, 2, 4, 6, 8], 'Temp (°C)': [20, 60, 90, 100, 100]})
            st.line_chart(data, x='Minutos', y='Temp (°C)')
            
        elif item['type'] == 'visual_density':
            c1, c2 = st.columns(2)
            with c1: st.info("💧 Vaso con Moneda"); st.write("¿Flota o se hunde?")
            with c2: st.info("💧 Vaso con Corcho"); st.write("¿Flota o se hunde?")
            
        elif item['type'] == 'visual_balance':
            c1, c2, c3 = st.columns([1,1,1])
            with c1: st.write("Plato A: 🍉 (Sandía)")
            with c2: st.markdown("### ⚖️ Equilibrada")
            with c3: st.write("Plato B: 🏋️1kg + 🏋️1kg")
            
        elif item['type'] == 'visual_particles':
            c1, c2 = st.columns(2)
            with c1: st.code("CAJA A\n[🟥🟥🟥]\n[🟥🟥🟥]")
            with c2: st.code("CAJA B\n[ 🟥    ]\n[    🟥 ]")
            
        elif item['type'] == 'visual_filter':
            st.code("""
              💧+🏖️ (Agua sucia)
                 ⬇️
               \\~~~~/  (Filtro)
                \\  /
                 ⬇️
               [ 💧 ] (Vaso limpio)
            """)
            
        elif item['type'] == 'visual_probeta':
            st.write("Agua sola: 20ml")
            st.progress(20)
            st.write("Agua + Canica: 25ml")
            st.progress(25)
            
        elif item['type'] == 'visual_mixture':
            c1, c2 = st.columns(2)
            with c1: st.warning("Vaso A: Se ven dos capas separadas 🟨🟦"); 
            with c2: st.info("Vaso B: Se ve todo transparente 🟦")

        elif item['type'] == 'visual_magnet':
             st.write("🧲 <--- Acercando imán a los objetos...")

        # Inputs de laboratorio
        if 'opts' in item:
            user_answers[item['id']] = st.radio("Observa y responde:", item['opts'], index=None, key=f"q{item['id']}")
        elif 'input_type' in item and item['input_type'] == 'number':
            user_answers[item['id']] = st.text_input("Escribe el número:", key=f"q{item['id']}")

        st.markdown("</div>", unsafe_allow_html=True)

    # Botón final
    submitted = st.form_submit_button("📝 CORREGIR EXAMEN COMPLETO (55 Preguntas)")

# --- LÓGICA DE CORRECCIÓN ---

if submitted:
    score = 0
    all_questions = theory_questions + lab_questions
    total = len(all_questions)
    
    st.markdown("## 📊 Resultados")
    
    for item in all_questions:
        user_input = user_answers.get(item['id'])
        correct_ans = item['ans']
        is_correct = False
        
        # Comprobar respuesta
        if user_input:
            if normalize(user_input) == normalize(correct_ans):
                is_correct = True
            # Truco para selección múltiple (si la respuesta correcta está dentro del texto seleccionado)
            elif str(correct_ans) in str(user_input): 
                is_correct = True
        
        # Mostrar resultado visual
        with st.expander(f"Pregunta {item['id']}: {item['q']}", expanded=False):
            if is_correct:
                st.markdown(f"✅ <span class='success'>¡CORRECTO!</span>", unsafe_allow_html=True)
                score += 1
            else:
                st.markdown(f"❌ <span class='error'>Incorrecto</span>", unsafe_allow_html=True)
                st.write(f"👉 Tu respuesta: {user_input if user_input else '(Vacia)'}")
                st.write(f"💡 Solución: **{correct_ans}**")

    # Nota final y celebración
    nota_final = (score / total) * 10
    st.divider()
    st.markdown(f"<h1 style='color:black;'>Nota Final: {score}/{total} aciertos ({nota_final:.1f} sobre 10)</h1>", unsafe_allow_html=True)

    if score == total:
        st.balloons()
        st.success("🏆 ¡PERFECCIÓN ABSOLUTA! ¡Eres el científico supremo!")
    elif score >= 45:
        st.success("🌟 ¡Excelente trabajo! Un resultado fantástico.")
    elif score >= 28:
        st.warning("🙂 ¡Aprobado! Buen esfuerzo, pero revisa los fallos.")
    else:
        st.error("📚 Tienes que estudiar más. Revisa el libro y los esquemas.")