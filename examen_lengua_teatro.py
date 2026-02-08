import streamlit as st

def check_answer_text(user_answer, correct_answers):
    """Verifica si la respuesta del usuario contiene alguna de las palabras clave correctas."""
    if not user_answer:
        return False
    user_answer = user_answer.lower().strip()
    for ans in correct_answers:
        if ans in user_answer:
            return True
    return False

def main():
    st.set_page_config(page_title="Gran Examen de Lengua 4º", page_icon="🎭", layout="wide")

    st.title("🎭 Gran Examen: El Teatro y la Gramática")
    st.subheader("4º de Primaria - Unidad: ¡Es puro teatro!")
    st.markdown("""
    **Instrucciones:**
    Este examen consta de **20 preguntas**:
    * **1-10:** Teoría (Conceptos sobre teatro, adjetivos e interjecciones).
    * **11-20:** Práctica (Análisis de textos, escritura y gramática).
    """)
    st.divider()

    score = 0
    total_questions = 20

    with st.form("examen_completo"):
        
        # ==========================================
        # BLOQUE 1: TEORÍA (10 Preguntas)
        # ==========================================
        st.header("I. Teoría: Conceptos Clave")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # P1: Acotaciones
            st.write("**1. ¿Qué son las acotaciones en una obra de teatro?**")
            r1 = st.radio("Elige:", 
                          ["Lo que dicen los actores en voz alta.",
                           "Las aclaraciones sobre gestos, vestuario y decorado.",
                           "El título de la obra."], key="t1")
            
            # P2: Estructura
            st.write("**2. Las partes grandes en las que se divide una obra se llaman 'Actos'. ¿Cómo se llaman las partes más pequeñas dentro de un acto?**")
            r2 = st.selectbox("Respuesta 2:", ["Capítulos", "Escenas", "Versos", "Párrafos"], key="t2")

            # P3: Adjetivo Concordancia
            st.write("**3. Si el sustantivo es 'Las jirafas' (femenino plural), ¿cómo debe ser el adjetivo?**")
            r3 = st.radio("Elige:", ["Masculino singular", "Femenino singular", "Femenino plural"], key="t3")

            # P4: Grado Superlativo
            st.write("**4. ¿Qué indica el grado superlativo del adjetivo?**")
            r4 = st.radio("Elige:", 
                          ["Una cualidad en su intensidad más alta.",
                           "Una comparación entre dos cosas.",
                           "Una cualidad normal sin intensidad."], key="t4")

            # P5: Interjecciones
            st.write("**5. ¿Qué signo de puntuación acompaña SIEMPRE a las interjecciones?**")
            r5 = st.selectbox("Respuesta 5:", ["Interrogación (¿?)", "Exclamación (¡!)", "Paréntesis ()"], key="t5")

        with col2:
            # P6: Definición Personajes
            st.write("**6. ¿Quiénes son los encargados de representar la historia en el teatro?**")
            r6 = st.radio("Elige:", ["El público", "El narrador", "Los personajes/actores"], key="t6")

            # P7: Definición Desenlace
            st.write("**7. ¿Qué es el 'desenlace' de una obra?**")
            r7 = st.radio("Elige:", 
                          ["El principio de la historia.",
                           "El momento donde se resuelve el conflicto o problema.",
                           "La presentación de los personajes."], key="t7")

            # P8: Grado Comparativo
            st.write("**8. ¿Cuáles son los tres tipos de grado comparativo?**")
            r8 = st.selectbox("Respuesta 8:", 
                              ["Alto, bajo y medio", 
                               "Superioridad, igualdad e inferioridad", 
                               "Positivo, negativo y neutro"], key="t8")

            # P9: Texto Teatral
            st.write("**9. En un texto teatral, ¿qué suele aparecer en mayúsculas antes de cada frase?**")
            r9 = st.text_input("Respuesta 9 (una palabra):", key="t9")

            # P10: Sufijos Superlativos
            st.write("**10. ¿Qué sufijos se añaden al adjetivo para formar el superlativo?**")
            r10 = st.radio("Elige:", ["-ito, -ita", "-ísimo, -ísima", "-oso, -osa"], key="t10")

        st.divider()

        # ==========================================
        # BLOQUE 2: PRÁCTICA (10 Preguntas)
        # ==========================================
        st.header("II. Práctica: Análisis y Escritura")

        col3, col4 = st.columns(2)

        with col3:
            st.info("Lee este fragmento:\n\n**RINO:** (Temblando) ¡Ay! ¡Ese ruido me da miedo!\n**AVISPA:** No seas miedica, Rino. Es solo el viento.")
            
            # P11: Identificar Acotación
            st.write("**11. Copia exactamente la acotación que aparece en el texto:**")
            r11 = st.text_input("Respuesta 11:", key="p11")

            # P12: Identificar Interjección
            st.write("**12. ¿Qué interjección utiliza Rino para expresar su sentimiento?**")
            r12 = st.text_input("Respuesta 12:", key="p12")

            # P13: Análisis del Conflicto
            st.write("**13. Analiza el conflicto: ¿Qué le pasa a Rino?**")
            r13 = st.radio("Elige:", ["Está enfadado", "Tiene miedo del ruido", "Quiere comer"], key="p13")

            # P14: Grados del adjetivo
            st.write("**14. En la frase 'El viento es muy fuerte', ¿en qué grado está el adjetivo?**")
            r14 = st.selectbox("Respuesta 14:", ["Positivo", "Comparativo", "Superlativo"], key="p14")

            # P15: Formar Comparativo
            st.write("**15. Completa: 'La moto es ______ rápida ______ la bici' (Superioridad).**")
            r15 = st.radio("Elige:", ["tan ... como", "menos ... que", "más ... que"], key="p15")

        with col4:
            # P16: Análisis Morfológico
            st.write("**16. Analiza 'Gatos sigilosos'. Indica género y número.**")
            r16 = st.radio("Elige:", ["Masc. Singular", "Fem. Plural", "Masc. Plural"], key="p16")

            # P17: Superlativo irregular/regla
            st.write("**17. Escribe el superlativo de 'Largo' usando el sufijo -ísimo:**")
            r17 = st.text_input("Respuesta 17:", key="p17")

            # P18: Escritura Creativa - Desenlace
            st.write("**18. Inventa un final (desenlace) de una frase para Rino y Avispa. ¿Qué pasa al final?**")
            r18 = st.text_area("Escribe tu final:", key="p18")

            # P19: Identificar Adjetivo
            st.write("**19. Encuentra el adjetivo en: 'El hongo vive bajo tierra húmeda'.**")
            r19 = st.text_input("Respuesta 19:", key="p19")

            # P20: Interjección Contextual
            st.write("**20. Si se te cae un helado al suelo, ¿qué dirías? (Usa una interjección: ¡Oh!, ¡Vaya!, ¡Uf!)**")
            r20 = st.text_input("Respuesta 20:", key="p20")

        st.divider()
        submitted = st.form_submit_button("Corrección Final")

    # ==========================================
    # LÓGICA DE CORRECCIÓN
    # ==========================================
    if submitted:
        st.header("📝 Resultados del Examen")
        
        # --- Corrección Teoría ---
        if r1 == "Las aclaraciones sobre gestos, vestuario y decorado.": score += 1
        else: st.error("1. Mal. Las acotaciones son las aclaraciones (paréntesis).")

        if r2 == "Escenas": score += 1
        else: st.error("2. Mal. Los actos se dividen en Escenas.")

        if r3 == "Femenino plural": score += 1
        else: st.error("3. Mal. Debe concordar: Femenino plural.")

        if "intensidad más alta" in r4: score += 1
        else: st.error("4. Mal. El superlativo es la intensidad máxima.")

        if "Exclamación" in r5: score += 1
        else: st.error("5. Mal. Siempre van entre signos de exclamación (¡!).")

        if "Los personajes" in r6: score += 1
        else: st.error("6. Mal. Son los personajes o actores.")

        if "resuelve el conflicto" in r7: score += 1
        else: st.error("7. Mal. El desenlace es el final donde se resuelve todo.")

        if "Superioridad, igualdad" in r8: score += 1
        else: st.error("8. Mal. Son superioridad, igualdad e inferioridad.")

        if check_answer_text(r9, ["nombre", "personaje", "nombres"]): score += 1
        else: st.error("9. Mal. Se pone el NOMBRE del personaje.")

        if "-ísimo" in r10: score += 1
        else: st.error("10. Mal. Los sufijos son -ísimo, -ísima.")

        # --- Corrección Práctica ---
        if check_answer_text(r11, ["temblando", "(temblando)"]): score += 1
        else: st.error("11. Mal. La acotación es '(Temblando)'.")

        if check_answer_text(r12, ["¡ay!", "ay"]): score += 1
        else: st.error("12. Mal. La interjección es '¡Ay!'.")

        if "miedo" in r13: score += 1
        else: st.error("13. Mal. El conflicto es que tiene miedo.")

        if r14 == "Superlativo": score += 1
        else: st.error("14. Mal. 'Muy fuerte' es superlativo.")

        if "más ... que" in r15: score += 1
        else: st.error("15. Mal. Superioridad es 'más... que'.")

        if r16 == "Masc. Plural": score += 1
        else: st.error("16. Mal. Gatos es Masculino Plural.")

        if check_answer_text(r17, ["larguísimo", "larguisimo"]): score += 1
        else: st.error("17. Mal. Es 'Larguísimo'.")

        # P18 es creativa, damos punto si escribió algo razonable (>5 letras)
        if len(r18) > 5: 
            score += 1
            st.success("18. ¡Bien! Has escrito un desenlace.")
        else: st.warning("18. Escribe un final un poco más completo.")

        if check_answer_text(r19, ["húmeda", "humeda"]): score += 1
        else: st.error("19. Mal. El adjetivo es 'húmeda'.")

        if len(r20) > 1: score += 1 # Aceptamos cualquier interjección válida
        else: st.error("20. Escribe una interjección.")

        # --- Nota Final ---
        st.markdown("---")
        st.metric(label="Tu Nota", value=f"{score} / {total_questions}")
        
        if score >= 18:
            st.balloons()
            st.success("¡IMPRESIONANTE! ¡Eres un maestro del teatro!")
        elif score >= 10:
            st.info("¡Aprobado! Buen trabajo.")
        else:
            st.error("Hay que repasar un poquito más.")

if __name__ == "__main__":
    main()