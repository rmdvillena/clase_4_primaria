import streamlit as st

def check_answer_text(user_answer, correct_answers):
    """Verifica si la respuesta del usuario contiene alguna de las palabras clave correctas."""
    if not user_answer:
        return False
    user_answer = user_answer.lower().strip()
    # Limpiamos tildes básicas para ser flexibles
    user_answer = user_answer.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    for ans in correct_answers:
        ans_clean = ans.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        if ans_clean in user_answer:
            return True
    return False

def main():
    st.set_page_config(page_title="Gran Examen Lengua 4º", page_icon="📝", layout="wide")

    st.title("🎭 Gran Examen Final: Teatro y Gramática")
    st.subheader("4º de Primaria - Unidad: ¡Es puro teatro!")
    
    st.info("""
    **Estructura del Examen (30 Preguntas):**
    * **Parte I:** Teoría General (1-10)
    * **Parte II:** Práctica Teatral (11-20)
    * **Parte III (NUEVO):** Especialista en Adjetivos y Grados (21-30)
    """)
    st.divider()

    score = 0
    total_questions = 30

    with st.form("examen_completo"):
        
        # ==========================================
        # PARTE I & II (RESUMEN DE LO ANTERIOR)
        # ==========================================
        st.write("### 🔽 Partes I y II: Repaso General")
        with st.expander("Ver preguntas 1 a 20 (Haz clic para desplegar)", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**1. ¿Qué son las acotaciones?**")
                r1 = st.radio("R1:", ["Diálogos", "Aclaraciones (gestos/decorado) entre paréntesis"], key="t1")
                
                st.write("**2. ¿Cómo se llaman las partes pequeñas de un acto?**")
                r2 = st.selectbox("R2:", ["Capítulos", "Escenas"], key="t2")
                
                st.write("**3. El adjetivo concuerda en...**")
                r3 = st.radio("R3:", ["Género y número", "Tiempo y persona"], key="t3")

                st.write("**4. ¿Grado que indica intensidad máxima?**")
                r4 = st.selectbox("R4:", ["Positivo", "Superlativo"], key="t4")

                st.write("**5. Signo de las interjecciones:**")
                r5 = st.radio("R5:", ["¿?", "¡!"], key="t5")

                st.write("**6. ¿Quién representa la obra?**")
                r6 = st.radio("R6:", ["Narrador", "Actores/Personajes"], key="t6")

                st.write("**7. El final de la obra se llama...**")
                r7 = st.selectbox("R7:", ["Nudo", "Desenlace"], key="t7")

                st.write("**8. Tipos de comparativo:**")
                r8 = st.radio("R8:", ["Alto/Bajo/Medio", "Superioridad/Igualdad/Inferioridad"], key="t8")

                st.write("**9. ¿Qué va en mayúscula antes del diálogo?**")
                r9 = st.text_input("R9 (Nombre del...):", key="t9")

                st.write("**10. Sufijo del superlativo:**")
                r10 = st.radio("R10:", ["-ito", "-ísimo"], key="t10")

            with col2:
                st.write("**11. Acotación en: 'ANA: (Riendo) ¡Hola!'**")
                r11 = st.text_input("R11:", key="p11")

                st.write("**12. Interjección de dolor:**")
                r12 = st.text_input("R12:", key="p12")

                st.write("**13. Conflicto: ¿Qué suele ser?**")
                r13 = st.radio("R13:", ["Un problema a resolver", "La presentación"], key="p13")

                st.write("**14. Grado de: 'Muy alto'**")
                r14 = st.selectbox("R14:", ["Comparativo", "Superlativo"], key="p14")

                st.write("**15. Comparativo: 'Más rápido ... la bici'**")
                r15 = st.radio("R15:", ["que", "como"], key="p15")

                st.write("**16. Género/Número: 'Gatas negras'**")
                r16 = st.radio("R16:", ["Fem. Plural", "Masc. Plural"], key="p16")

                st.write("**17. Superlativo de 'Rico':**")
                r17 = st.text_input("R17 (terminado en -ísimo):", key="p17")

                st.write("**18. Escribe un desenlace breve:**")
                r18 = st.text_input("R18:", key="p18")

                st.write("**19. Adjetivo en: 'Cielo azul'**")
                r19 = st.text_input("R19:", key="p19")

                st.write("**20. Interjección de sorpresa:**")
                r20 = st.text_input("R20:", key="p20")

        st.divider()

        # ==========================================
        # PARTE III: AMPLIACIÓN ADJETIVOS (NUEVO)
        # ==========================================
        st.header("III. Especialista en Adjetivos y Grados")
        st.caption("Demuestra que dominas todos los grados: positivo, comparativo y superlativo.")

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("#### 🧠 Teoría y Definiciones")
            
            # P21: Definición Grado Positivo
            st.write("**21. ¿Qué es el GRADO POSITIVO del adjetivo?**")
            r21 = st.radio("Selecciona:", 
                           ["Cuando compara dos cosas.", 
                            "Cuando expresa una cualidad tal cual es, sin intensidad.",
                            "Cuando exagera la cualidad."], key="n21")

            # P22: Estructura Inferioridad
            st.write("**22. Para formar el comparativo de INFERIORIDAD usamos:**")
            r22 = st.selectbox("Fórmula:", ["Más ... que", "Tan ... como", "Menos ... que"], key="n22")

            # P23: Estructura Igualdad
            st.write("**23. Para formar el comparativo de IGUALDAD usamos:**")
            r23 = st.selectbox("Fórmula:", ["Más ... que", "Tan ... como", "Menos ... que"], key="n23")
            
            # P24: Formas del Superlativo
            st.write("**24. Hay dos formas de hacer el superlativo. Una es con el sufijo '-ísimo'. ¿Cuál es la otra?**")
            r24 = st.radio("Selecciona:", ["Poniendo 'MUY' delante.", "Poniendo 'POCO' delante.", "Poniendo 'TAN' delante."], key="n24")

            # P25: Concordancia trampa
            st.write("**25. Si digo 'Los niños son...', ¿qué adjetivo es correcto?**")
            r25 = st.radio("Opciones:", ["listo", "listas", "listos"], key="n25")

        with col4:
            st.markdown("#### ✍️ Casos Prácticos")

            # P26: Identificar Inferioridad
            st.write("**26. Lee: 'Este patinete es menos rápido que tu bici'. ¿Qué grado es?**")
            r26 = st.selectbox("Tipo:", ["Positivo", "Comp. Superioridad", "Comp. Inferioridad"], key="n26")

            # P27: Crear Superlativo
            st.write("**27. Escribe el superlativo de 'GRANDE' usando el sufijo -ísimo:**")
            r27 = st.text_input("Escribe la palabra:", key="n27")

            # P28: Identificar Igualdad
            st.write("**28. Lee: 'Pedro es tan alto como Juan'. ¿Qué grado es?**")
            r28 = st.selectbox("Tipo:", ["Comp. Igualdad", "Comp. Superioridad", "Positivo"], key="n28")

            # P29: Transformación
            st.write("**29. Convierte esta frase a GRADO POSITIVO: 'El examen es facilísimo'.**")
            st.caption("Pista: Quita la intensidad.")
            r29 = st.text_input("Escribe la frase simple (Ej: El examen es...):", key="n29")

            # P30: Crear Inferioridad
            st.write("**30. Inventa una frase de INFERIORIDAD usando 'menos' y 'que' con la palabra 'alto'.**")
            r30 = st.text_input("Tu frase:", key="n30")

        st.divider()
        submitted = st.form_submit_button("✅ Corregir Examen Completo")

    # ==========================================
    # LÓGICA DE CORRECCIÓN
    # ==========================================
    if submitted:
        # --- Corrección Rápida I y II ---
        if "Aclaraciones" in r1: score += 1
        if r2 == "Escenas": score += 1
        if "Género" in r3: score += 1
        if r4 == "Superlativo": score += 1
        if "¡!" in r5: score += 1
        if "Actores" in r6: score += 1
        if r7 == "Desenlace": score += 1
        if "Superioridad" in r8: score += 1
        if check_answer_text(r9, ["nombre", "personaje"]): score += 1
        if "-ísimo" in r10: score += 1
        if check_answer_text(r11, ["riendo", "(riendo)"]): score += 1
        if check_answer_text(r12, ["ay", "uf", "au"]): score += 1
        if "problema" in r13: score += 1
        if r14 == "Superlativo": score += 1
        if r15 == "que": score += 1
        if "Fem. Plural" in r16: score += 1
        if check_answer_text(r17, ["riquisimo", "riquísimo"]): score += 1
        if len(r18) > 3: score += 1
        if check_answer_text(r19, ["azul"]): score += 1
        if len(r20) > 1: score += 1

        # --- Corrección Nueva Parte III ---
        st.header("📊 Resultados Parte III (Adjetivos)")
        
        # 21
        if "sin intensidad" in r21:
            score += 1
            st.success("21. Correcto. El grado positivo no compara ni exagera.")
        else: st.error("21. Fallo. El positivo es la cualidad normal.")

        # 22
        if "Menos ... que" in r22:
            score += 1
            st.success("22. Correcto. Inferioridad = Menos... que.")
        else: st.error("22. Fallo. Inferioridad usa 'menos'.")

        # 23
        if "Tan ... como" in r23:
            score += 1
            st.success("23. Correcto. Igualdad = Tan... como.")
        else: st.error("23. Fallo. Igualdad usa 'tan... como'.")

        # 24
        if "MUY" in r24:
            score += 1
            st.success("24. Correcto. 'Muy alto' es superlativo.")
        else: st.error("24. Fallo. Se usa 'muy'.")

        # 25
        if r25 == "listos":
            score += 1
            st.success("25. Correcto. Concordancia Masculino Plural.")
        else: st.error("25. Fallo. 'Niños' es masculino plural.")

        # 26
        if "Inferioridad" in r26:
            score += 1
            st.success("26. Correcto.")
        else: st.error("26. Fallo. Es inferioridad.")

        # 27
        if check_answer_text(r27, ["grandisimo", "grandísimo"]):
            score += 1
            st.success("27. Correcto (Grandísimo).")
        else: st.error(f"27. Fallo. Era Grandísimo. Tú pusiste: {r27}")

        # 28
        if "Igualdad" in r28:
            score += 1
            st.success("28. Correcto.")
        else: st.error("28. Fallo. Es igualdad.")

        # 29
        if check_answer_text(r29, ["el examen es facil", "el examen es fácil"]):
            score += 1
            st.success("29. Correcto. Has quitado la intensidad.")
        else: st.error("29. Fallo. Simplemente: 'El examen es fácil'.")

        # 30 (Flexible)
        if "menos" in r30.lower() and "que" in r30.lower():
            score += 1
            st.success("30. Correcto. Has usado la estructura de inferioridad.")
        else: st.error("30. Revisa. Debes usar la palabra 'menos' y 'que'.")

        # --- Nota Final Global ---
        st.markdown("---")
        st.subheader(f"🏆 Nota Final: {score} / 30")
        
        if score >= 27:
            st.balloons()
            st.success("¡MATRÍCULA DE HONOR! ¡Lo sabes todo!")
        elif score >= 15:
            st.info("¡Aprobado! Vas por buen camino.")
        else:
            st.warning("Hay que repasar los comparativos y superlativos.")

if __name__ == "__main__":
    main()