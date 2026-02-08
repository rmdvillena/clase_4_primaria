import streamlit as st

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="🇬🇧 English Master Class", page_icon="🎓", layout="wide")

# --- ESTILOS CSS (Para que se vea bonito) ---
st.markdown("""
    <style>
    .big-font { font-size:20px !important; color: #154360; font-weight: bold; }
    .theory-box { background-color: #D4E6F1; padding: 20px; border-radius: 10px; border-left: 5px solid #2980B9; margin-bottom: 20px; }
    .correct { background-color: #D5F5E3; padding: 10px; border-radius: 5px; border: 1px solid #2ECC71; color: #186A3B; margin-top: 5px;}
    .incorrect { background-color: #FADBD8; padding: 10px; border-radius: 5px; border: 1px solid #CB4335; color: #943126; margin-top: 5px;}
    .stButton>button { width: 100%; background-color: #F1C40F; font-size: 20px; font-weight: bold; color: black; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO DE LA APLICACIÓN ---
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# --- PESTAÑAS PRINCIPALES ---
tab_teoria, tab_examen = st.tabs(["📚 1. LECCIÓN (Estudia aquí)", "✍️ 2. EXAMEN (20 Preguntas)"])

# ==============================================================================
# PESTAÑA 1: TEORÍA (Basada en la foto del libro)
# ==============================================================================
with tab_teoria:
    st.title("🎓 Lección: Present Simple & Jobs")
    
    st.markdown("""
    <div class="theory-box">
        <h3>1️⃣ La Regla de Oro: DO vs DOES</h3>
        <p>Para hacer preguntas en inglés, necesitamos un ayudante (Auxiliar). Depende de la persona:</p>
        <ul>
            <li><b>DOES</b> 👉 Se usa con la "Tercera Persona" (El jefe/a): <b>He, She, It</b>.</li>
            <li><b>DO</b> 👉 Se usa con el resto: <b>I, You, We, They</b>.</li>
        </ul>
        <p><i>Ejemplo:</i> <b>Does</b> she work? / <b>Do</b> you work?</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.info("🚨 **¡OJO!** Cuando usas **DOES**, el verbo principal **NO** lleva la 's'.\n\n* MAL: Does she works?\n* BIEN: Does she **work**?")
    with c2:
        st.warning("🗣️ **Respuestas Cortas (Short Answers)**\n\n* Yes, he does.\n* No, he doesn't.\n* Yes, I do.\n* No, I don't.")

    st.markdown("---")
    st.subheader("2️⃣ Vocabulario del Libro (Jobs)")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063823.png", width=50)
        st.markdown("**Work outdoors**\n\n(Trabajar fuera/aire libre)")
    with col_b:
        st.image("https://cdn-icons-png.flaticon.com/512/1995/1995667.png", width=50)
        st.markdown("**Wear a uniform**\n\n(Llevar uniforme)")
    with col_c:
        st.image("https://cdn-icons-png.flaticon.com/512/4829/4829988.png", width=50)
        st.markdown("**Work at night**\n\n(Trabajar de noche)")

# ==============================================================================
# PESTAÑA 2: EL EXAMEN (20 Preguntas)
# ==============================================================================
with tab_examen:
    st.header("📝 ¡A demostrar lo que sabes!")
    st.write("Responde las 20 preguntas. Al final, pulsa el botón amarillo para corregir todo.")
    st.divider()

    # --- BLOQUE 1: RELLENAR HUECOS (DO/DOES) ---
    st.subheader("Parte 1: ¿Do o Does? (Gramática)")
    
    col1, col2 = st.columns(2)
    with col1:
        q1 = st.radio("1. _____ she work in a hospital?", ["Do", "Does", "Is"], key="q1", horizontal=True)
        q2 = st.radio("2. _____ you wear a uniform?", ["Do", "Does", "Are"], key="q2", horizontal=True)
        q3 = st.radio("3. _____ he work with animals?", ["Do", "Does", "Is"], key="q3", horizontal=True)
    with col2:
        q4 = st.radio("4. _____ they work at night?", ["Do", "Does", "Have"], key="q4", horizontal=True)
        q5 = st.radio("5. _____ the doctor work indoors?", ["Do", "Does", "Is"], key="q5", horizontal=True)

    st.divider()

    # --- BLOQUE 2: VOCABULARIO Y RESPUESTAS CORTAS ---
    st.subheader("Parte 2: Vocabulario y Respuestas")
    
    col3, col4 = st.columns(2)
    with col3:
        q6 = st.selectbox("6. Un granjero (Farmer) trabaja...", ["indoors", "outdoors", "in an office"], key="q6")
        q7 = st.selectbox("7. Pregunta: Does he work? -> Respuesta Negativa:", ["No, he don't", "No, he doesn't", "No, he isn't"], key="q7")
        q8 = st.selectbox("8. Traduce: 'Work at night'", ["Trabajar de día", "Trabajar de noche", "Trabajar en casa"], key="q8")
    with col4:
        q9 = st.selectbox("9. ¿Quién lleva uniforme (wears a uniform)?", ["A firefighter", "A writer", "A baby"], key="q9")
        q10 = st.selectbox("10. Pregunta: Do you like apples? -> Respuesta Afirmativa:", ["Yes, I does", "Yes, I like", "Yes, I do"], key="q10")

    st.divider()

    # --- BLOQUE 3: ORDENAR FRASES (TIPO DUOLINGO) ---
    st.subheader("Parte 3: Ordena la frase (Estilo Duolingo)")
    st.info("Selecciona las palabras en el orden correcto para formar la frase.")

    st.markdown("**11. ¿Trabaja ella fuera?**")
    opts_11 = ["outdoors", "Does", "she", "work", "?"]
    q11 = st.multiselect("Construye la frase 11:", opts_11, key="q11")

    st.markdown("**12. ¿Llevan ellos uniforme?**")
    opts_12 = ["uniform", "Do", "wear", "they", "a", "?"]
    q12 = st.multiselect("Construye la frase 12:", opts_12, key="q12")

    st.markdown("**13. Él no trabaja en un zoo.**")
    opts_13 = ["He", "work", "doesn't", "in a zoo", "."]
    q13 = st.multiselect("Construye la frase 13:", opts_13, key="q13")

    st.markdown("**14. ¿Trabajas tú de noche?**")
    opts_14 = ["at", "night", "work", "you", "Do", "?"]
    q14 = st.multiselect("Construye la frase 14:", opts_14, key="q14")

    st.markdown("**15. Ella trabaja con animales.**")
    opts_15 = ["works", "She", "with", "animals", "."]
    q15 = st.multiselect("Construye la frase 15:", opts_15, key="q15")

    st.divider()

    # --- BLOQUE 4: TRADUCCIÓN / ESCRITURA ---
    st.subheader("Parte 4: Escribe la frase (Writing)")
    st.caption("Escribe en Inglés o Español según se pida. Cuidado con la ortografía.")

    q16 = st.text_input("16. Traduce al español: 'Does she wear a uniform?'", key="q16")
    q17 = st.text_input("17. Traduce al inglés: '¿Trabaja él en una oficina?' (Pista: in an office)", key="q17")
    q18 = st.text_input("18. Escribe la pregunta para esta respuesta: '________? Yes, I do.' (Pista: Pregunta con You)", key="q18")
    q19 = st.text_input("19. Pon en negativa: 'He works'", key="q19")
    q20 = st.text_input("20. Pon en afirmativa: 'Does she play?' -> 'Yes, she ____'", key="q20")

    st.divider()

    # ==============================================================================
    # LÓGICA DE CORRECCIÓN (AL PULSAR EL BOTÓN)
    # ==============================================================================
    
    if st.button("🏁 CORREGIR EXAMEN AHORA"):
        st.session_state.submitted = True
        score = 0
        
        st.success("¡Examen entregado! Mira abajo tus correcciones 👇")

        # --- RESPUESTAS CORRECTAS ---
        # Bloque 1
        r1, r2, r3, r4, r5 = "Does", "Do", "Does", "Do", "Does"
        # Bloque 2
        r6, r7, r8, r9, r10 = "outdoors", "No, he doesn't", "Trabajar de noche", "A firefighter", "Yes, I do"
        # Bloque 3 (Listas)
        r11 = ["Does", "she", "work", "outdoors", "?"]
        r12 = ["Do", "they", "wear", "a", "uniform", "?"]
        r13 = ["He", "doesn't", "work", "in a zoo", "."]
        r14 = ["Do", "you", "work", "at", "night", "?"]
        r15 = ["She", "works", "with", "animals", "."] # OJO: works con S
        
        # FUNCION HELPER PARA MOSTRAR RESULTADO
        def show_result(user, correct, num, explanation=""):
            is_ok = False
            # Comparación flexible para texto
            if isinstance(user, str):
                if user.lower().strip().replace('?','').replace('.','') == correct.lower().strip().replace('?','').replace('.',''):
                    is_ok = True
                # Excepciones manuales para traducciones
                if num == 16 and "lleva uniforme" in user.lower(): is_ok = True
                if num == 19 and "doesn't work" in user.lower(): is_ok = True
                if num == 20 and "plays" in user.lower(): is_ok = True
                if num == 18 and "do you" in user.lower(): is_ok = True
            elif isinstance(user, list):
                if user == correct: is_ok = True
            
            if is_ok:
                st.markdown(f"<div class='correct'>✅ <b>Pregunta {num}:</b> ¡Correcto!</div>", unsafe_allow_html=True)
                return 1
            else:
                correct_str = correct if isinstance(correct, str) else " ".join(correct)
                st.markdown(f"<div class='incorrect'>❌ <b>Pregunta {num}:</b> Mal. La respuesta era: <b>{correct_str}</b>. <br><i>{explanation}</i></div>", unsafe_allow_html=True)
                return 0

        # --- CORRECCIÓN BLOQUE A BLOQUE ---
        st.subheader("📊 Resultados:")
        
        # Bloque 1
        score += show_result(q1, r1, 1, "She es 3ª persona (Does).")
        score += show_result(q2, r2, 2, "You usa Do.")
        score += show_result(q3, r3, 3, "He es 3ª persona (Does).")
        score += show_result(q4, r4, 4, "They usa Do.")
        score += show_result(q5, r5, 5, "The doctor = He/She -> Does.")
        
        # Bloque 2
        score += show_result(q6, r6, 6)
        score += show_result(q7, r7, 7, "Negativa de Does -> Doesn't.")
        score += show_result(q8, r8, 8)
        score += show_result(q9, r9, 9)
        score += show_result(q10, r10, 10, "Pregunta con Do -> Respuesta con do.")

        # Bloque 3
        score += show_result(q11, r11, 11, "Orden: Auxiliar + Sujeto + Verbo + Lugar.")
        score += show_result(q12, r12, 12, "Wear a uniform = llevar uniforme.")
        score += show_result(q13, r13, 13, "Negativa: He doesn't work.")
        score += show_result(q14, r14, 14, "Do you work...?")
        score += show_result(q15, r15, 15, "Afirmativa con She -> El verbo lleva 'S' (works).")

        # Bloque 4
        score += show_result(q16, "Ella lleva uniforme", 16)
        score += show_result(q17, "Does he work in an office", 17)
        score += show_result(q18, "Do you work", 18, "Si respondo 'yo', la pregunta es a 'ti'.")
        score += show_result(q19, "He doesn't work", 19, "Doesn't + verbo sin S.")
        score += show_result(q20, "plays", 20, "She plays (con S).")

        # --- NOTA FINAL ---
        st.markdown("---")
        final_score = score
        st.metric(label="NOTA FINAL", value=f"{final_score} / 20")
        
        if final_score == 20:
            st.balloons()
            st.success("🏆 ¡PERFECTO! Eres un maestro del inglés.")
        elif final_score >= 15:
            st.success("🌟 ¡Muy bien! Casi perfecto.")
        elif final_score >= 10:
            st.warning("🙂 Aprobado. Repasa los fallos en rojo.")
        else:
            st.error("💪 Hay que estudiar un poco más la lección de la pestaña 1.")