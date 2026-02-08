import streamlit as st
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="🇬🇧 English Exam: Jobs!", page_icon="👨‍🚒", layout="centered")

# --- ESTILOS VISUALES (CSS) PARA NIÑOS ---
st.markdown("""
    <style>
    .big-font { font-size:22px !important; color: #154360; font-weight: bold; }
    .question-box { background-color: #E8F8F5; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 2px solid #A3E4D7; }
    .stButton>button {
        background-color: #F1C40F; color: black; border-radius: 12px; font-weight: bold; border: 2px solid #D4AC0D;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #D6EAF8; border-radius: 5px; }
    .stTabs [aria-selected="true"] { background-color: #AED6F1; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO (SCORE Y RESPUESTAS) ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = set() # Para guardar qué IDs ya se respondieron

# --- FUNCIÓN PARA VERIFICAR RESPUESTAS ---
def check_answer(q_id, user_ans, correct_ans, explanation=""):
    """
    q_id: identificador único de la pregunta
    user_ans: respuesta del usuario
    correct_ans: respuesta correcta (o lista de correctas)
    explanation: texto para explicar por qué
    """
    if q_id in st.session_state.answered:
        st.warning("⚠️ Ya respondiste esta pregunta.")
        return

    # Normalizar para comparaciones de texto
    if isinstance(user_ans, str):
        is_correct = user_ans.strip().lower().replace('?','').replace('.','') == correct_ans.strip().lower().replace('?','').replace('.','')
    elif isinstance(user_ans, list): # Para el ejercicio de ordenar
        is_correct = user_ans == correct_ans
    else:
        is_correct = user_ans == correct_ans

    if is_correct:
        st.canvas = st.balloons()
        st.success("✅ ¡CORRECTO! ¡Muy bien!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Casi... La respuesta era: {correct_ans}")
        if explanation:
            st.info(f"💡 {explanation}")
    
    st.session_state.answered.add(q_id)

# --- CABECERA ---
st.title("👨‍⚕️ Examen de Inglés: Jobs & Routines 👩‍🌾")
st.markdown("¡Hola! 👋 Vamos a demostrar todo lo que sabes.")
st.markdown(f"**Puntuación actual:** {st.session_state.score} puntos ⭐")
st.markdown("---")

# --- PESTAÑAS ---
tab1, tab2 = st.tabs(["📝 Ejercicios Prácticos", "🚀 Test Rápido (10 Preguntas)"])

# ==========================================
# PESTAÑA 1: LOS 5 TIPOS DE EJERCICIOS
# ==========================================
with tab1:
    st.header("Parte 1: Práctica Variada")

    # 1. GRAMÁTICA
    st.markdown('<div class="question-box"><p class="big-font">1. Elige: Do o Does</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        ans1 = st.radio("She _____ work in a hospital?", ["Do", "Does"], key="p1_q1")
        if st.button("Comprobar #1", key="btn_p1_1"):
            check_answer("ex1_1", ans1, "Does", "She es 3ª persona -> Does.")
    with c2:
        ans2 = st.radio("_____ you wear a uniform?", ["Do", "Does"], key="p1_q2")
        if st.button("Comprobar #2", key="btn_p1_2"):
            check_answer("ex1_2", ans2, "Do", "You usa Do.")

    st.markdown("---")

    # 2. ORDENAR (TIPO DUOLINGO)
    st.markdown('<div class="question-box"><p class="big-font">2. Ordena la frase (Estilo Duolingo)</p></div>', unsafe_allow_html=True)
    st.write("Frase meta: *¿Trabaja él fuera?*")
    options_scramble = ["outdoors", "Does", "he", "work", "?"]
    user_order = st.multiselect("Selecciona las palabras en orden:", options=options_scramble, key="p1_q3")
    correct_order = ["Does", "he", "work", "outdoors", "?"]
    
    if st.button("Comprobar Orden", key="btn_p1_3"):
        check_answer("ex2", user_order, correct_order, "Orden: Auxiliar (Does) + Persona (he) + Verbo (work) + Lugar.")

    st.markdown("---")

    # 3. TRADUCIR A ESPAÑOL
    st.markdown('<div class="question-box"><p class="big-font">3. Traduce al Español</p></div>', unsafe_allow_html=True)
    st.info("Does she wear a uniform?")
    ans3 = st.text_input("Escribe en español:", key="p1_q4")
    if st.button("Comprobar Traducción", key="btn_p1_4"):
        # Aceptamos variaciones
        validas = ["ella lleva uniforme", "¿ella lleva uniforme?", "lleva uniforme", "¿lleva uniforme?", "usa uniforme"]
        # Lógica manual simple para aceptar varias
        normalized = ans3.lower().strip().replace('¿','').replace('?','')
        match = False
        for v in validas:
            if v.replace('¿','').replace('?','') in normalized:
                match = True
        if match:
             check_answer("ex3", "ok", "ok") # Truco para reutilizar la funcion
        else:
             check_answer("ex3", "fail", "ok", "Respuesta: ¿Lleva ella uniforme?")

    st.markdown("---")

    # 4. TRADUCIR A INGLÉS
    st.markdown('<div class="question-box"><p class="big-font">4. Traduce al Inglés</p></div>', unsafe_allow_html=True)
    st.info("¿Trabaja él con animales?")
    ans4 = st.text_input("Escribe en inglés (Usa 'Does'):", key="p1_q5")
    if st.button("Comprobar Inglés", key="btn_p1_5"):
        check_answer("ex4", ans4, "Does he work with animals", "Recuerda: Does + he + work + with animals")

    st.markdown("---")

    # 5. SHORT ANSWERS
    st.markdown('<div class="question-box"><p class="big-font">5. Respuesta Corta</p></div>', unsafe_allow_html=True)
    st.write("**Pregunta:** Does a firefighter work in an office? 🚒")
    ans5 = st.selectbox("Elige la respuesta:", ["Select...", "Yes, he does", "No, he doesn't", "Yes, he is"], key="p1_q6")
    if st.button("Comprobar Respuesta", key="btn_p1_6"):
        check_answer("ex5", ans5, "No, he doesn't")


# ==========================================
# PESTAÑA 2: EL TEST DE 10 PREGUNTAS
# ==========================================
with tab2:
    st.header("Parte 2: Quiz de 10 Preguntas")
    
    # Base de datos de preguntas
    quiz_data = [
        {"q": "1. Completa: '_____ she work in a hospital?'", "opts": ["Do", "Does", "Is"], "corr": "Does", "exp": "She es 3ª persona."},
        {"q": "2. Traduce: '¿Lleva él uniforme?'", "opts": ["Do he wear a uniform?", "Does he wears a uniform?", "Does he wear a uniform?"], "corr": "Does he wear a uniform?", "exp": "Con Does, el verbo no lleva 's'."},
        {"q": "3. Responde: 'Does a firefighter work in an office?'", "opts": ["Yes, he does.", "No, he doesn't.", "No, he don't."], "corr": "No, he doesn't.", "exp": "Los bomberos no trabajan en oficinas."},
        {"q": "4. Orden correcto:", "opts": ["Does she work with animals?", "Does work she with animals?", "She does work with animals?"], "corr": "Does she work with animals?", "exp": "Does + Sujeto + Verbo..."},
        {"q": "5. Completa: '_____ you work at night?'", "opts": ["Does", "Do", "Are"], "corr": "Do", "exp": "Con 'You' usamos Do."},
        {"q": "6. ¿Qué significa 'work outdoors'?", "opts": ["Trabajar en oficina", "Trabajar de noche", "Trabajar al aire libre"], "corr": "Trabajar al aire libre", "exp": "Outdoors = Fuera."},
        {"q": "7. Negativa correcta: 'She _____ in a hospital.'", "opts": ["don't work", "doesn't works", "doesn't work"], "corr": "doesn't work", "exp": "Doesn't + verbo infinitivo."},
        {"q": "8. Si la respuesta es 'Yes, I do', la pregunta es...", "opts": ["Does she...?", "Do you...?", "Do they...?"], "corr": "Do you...?", "exp": "Pregunta a ti (you) -> Respondes yo (I)."},
        {"q": "9. ¿Quién trabaja 'outdoors'?", "opts": ["Doctor", "Farmer", "Secretary"], "corr": "Farmer", "exp": "El granjero trabaja en el campo."},
        {"q": "10. Afirmativa: 'He _____ a uniform.'", "opts": ["wear", "wears", "wearing"], "corr": "wears", "exp": "En afirmativa, He/She lleva 's'."}
    ]

    # Bucle para generar las preguntas automáticamente
    for i, item in enumerate(quiz_data):
        st.markdown(f"**{item['q']}**")
        # Usamos radio buttons con claves únicas basadas en el índice 'i'
        user_choice = st.radio(f"Opción pregunta {i+1}:", item['opts'], key=f"quiz_radio_{i}", label_visibility="collapsed")
        
        if st.button(f"Responder P{i+1}", key=f"btn_quiz_{i}"):
            check_answer(f"quiz_{i}", user_choice, item['corr'], item['exp'])
        st.divider()

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.header("🏆 Tu Progreso")
total_questions = 6 + 10 # 6 del ej 1, 10 del quiz
st.sidebar.metric("Puntos Totales", f"{st.session_state.score} / {total_questions}")

if st.session_state.score > 5:
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/190/190411.png", width=100)
    st.sidebar.write("¡Lo estás haciendo genial!")

# Botón de reinicio
if st.sidebar.button("🔄 Empezar de cero"):
    st.session_state.score = 0
    st.session_state.answered = set()
    st.rerun()