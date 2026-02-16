import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Examen 4º Primaria - Sociales", page_icon="🌍", layout="wide")

# Título y bienvenida
st.title("🌍 ¡Gran Examen de Ciencias Sociales!")
st.subheader("Repaso para 4º de Primaria")
st.markdown("""
¡Hola! Vamos a repasar todo lo que has aprendido sobre la población, el territorio, las normas, el dinero y el planeta.
**Instrucciones:**
* 📝 **Escribir:** Escribe la respuesta correcta (cuidado con las tildes).
* 🔽 **Seleccionar:** Elige la opción correcta del desplegable o lista.
* 🤔 **Pensar:** Reflexiona sobre la pregunta y luego abre la solución para ver si acertaste.
""")

# Inicializar contador de aciertos en la sesión si no existe
if 'score' not in st.session_state:
    st.session_state.score = 0

# Dividimos el examen en Pestañas por Temas para que sea más ameno
tab1, tab2, tab3, tab4, tab5 = st.tabs(["👥 La Población", "🗺️ El Territorio", "🛑 Normas y Señales", "💰 El Dinero", "🌳 El Planeta"])

def check_text_answer(user_input, correct_answers, key_suffix):
    """Función para verificar respuestas de texto (insensible a mayúsculas)"""
    if user_input.strip().lower() in [a.lower() for a in correct_answers]:
        st.success("¡Correcto! 🎉")
        return 1
    elif user_input:
        st.error(f"Incorrecto. La respuesta era: {correct_answers[0]}")
    return 0

def check_select_answer(user_choice, correct_option, key_suffix):
    """Función para verificar respuestas de selección"""
    if user_choice == correct_option:
        st.success("¡Muy bien! ✅")
        return 1
    elif user_choice and user_choice != "Elige una opción...":
        st.error("Inténtalo de nuevo ❌")
    return 0

# --- TEMA 1: LA POBLACIÓN ---
with tab1:
    st.header("La Población y el Padrón")
    score_t1 = 0
    
    # P1 - Selección
    st.write("1. ¿Cómo se llama el registro de habitantes que se actualiza cada 10 años?")
    r1 = st.radio("Selecciona:", ["El Padrón", "El Censo", "La Constitución"], key="p1", index=None)
    if r1 == "El Censo": score_t1 += 1
    
    # P2 - Escribir
    st.write("2. ¿Cómo se llama el registro que llevan los ayuntamientos y se actualiza cuando alguien se muda?")
    r2 = st.text_input("Escribe tu respuesta:", key="p2")
    if r2: score_t1 += check_text_answer(r2, ["Padrón", "El padrón"], "p2_check")

    # P3 - Selección
    st.write("3. Si una persona se va de su país para vivir en otro, es un...")
    r3 = st.selectbox("Elige:", ["Elige una opción...", "Inmigrante", "Emigrante"], key="p3")
    if r3 == "Emigrante": 
        st.success("Correcto")
        score_t1 += 1
    elif r3 != "Elige una opción...": st.error("Incorrecto")

    # P4 - Escribir
    st.write("4. Para saber si una zona está muy poblada dividimos habitantes entre superficie. ¿Cómo se llama esto?")
    r4 = st.text_input("Densidad de...", key="p4")
    if r4: score_t1 += check_text_answer(r4, ["población", "poblacion"], "p4_check")

    # P5 - Pensar
    st.info("5. 🤔 PREGUNTA DE PENSAR: Observando los gráficos del libro, España tiene una población 'envejecida'. ¿Por qué crees que pasa esto?")
    st.text_area("Escribe tu razonamiento aquí:", key="p5")
    with st.expander("Ver respuesta modelo"):
        st.write("Porque nacen pocos niños (baja natalidad) y la gente vive más años (alta esperanza de vida).")

    # P6 - Selección
    st.write("6. ¿Dónde suele haber mayor densidad de población?")
    r6 = st.radio("Elige:", ["En las zonas rurales (pueblos)", "En las zonas urbanas (ciudades)"], key="p6", index=None)
    if r6 == "En las zonas urbanas (ciudades)": score_t1 += 1

    # P7 - Selección
    st.write("7. La 'Esperanza de vida' es...")
    r7 = st.selectbox("Significado:", ["Elige una opción...", "El número de bebés que nacen", "La media de años que viven las personas"], key="p7")
    if r7 == "La media de años que viven las personas": score_t1 += 1

    # P8 - Escribir
    st.write("8. Si llegas a vivir a un país nuevo, eres un...")
    r8 = st.text_input("Respuesta:", key="p8")
    if r8: score_t1 += check_text_answer(r8, ["inmigrante"], "p8_check")

# --- TEMA 2: EL TERRITORIO ---
with tab2:
    st.header("Organización Territorial")
    score_t2 = 0
    
    # P9 - Selección
    st.write("9. ¿Quién es la máxima autoridad de un Ayuntamiento?")
    r9 = st.radio("Elige:", ["El Concejal", "El Alcalde o Alcaldesa", "El Presidente"], key="p9", index=None)
    if r9 == "El Alcalde o Alcaldesa": score_t2 += 1

    # P10 - Escribir
    st.write("10. Los ciudadanos eligen a los concejales en las elecciones...")
    r10 = st.text_input("Elecciones mu...", key="p10")
    if r10: score_t2 += check_text_answer(r10, ["municipales"], "p10_check")

    # P11 - Selección
    st.write("11. Varios municipios agrupados forman una...")
    r11 = st.selectbox("Elige:", ["Elige una opción...", "Provincia", "Comunidad Autónoma", "País"], key="p11")
    if r11 == "Provincia": score_t2 += 1

    # P12 - Escribir
    st.write("12. ¿Cuántas provincias tiene aproximadamente España? (Escribe el número)")
    r12 = st.text_input("Número:", key="p12")
    if r12: score_t2 += check_text_answer(r12, ["50", "cincuenta"], "p12_check")

    # P13 - Pensar
    st.info("13. 🤔 PREGUNTA DE PENSAR: ¿Para qué sirve el Ayuntamiento?")
    st.text_area("Tu respuesta:", key="p13")
    with st.expander("Ver respuesta modelo"):
        st.write("Para organizar los servicios del municipio: limpieza, alumbrado, agua, transporte y parques.")

    # P14 - Selección
    st.write("14. España es un país miembro de la...")
    r14 = st.radio("Organización:", ["ONU", "Unión Europea (UE)", "OTAN"], key="p14", index=None)
    if r14 == "Unión Europea (UE)": score_t2 += 1

    # P15 - Escribir
    st.write("15. ¿Cómo se llama la moneda que compartimos con muchos países de Europa?")
    r15 = st.text_input("Moneda:", key="p15")
    if r15: score_t2 += check_text_answer(r15, ["euro", "euros"], "p15_check")

    # P16 - Selección
    st.write("16. El territorio formado por varias provincias se llama...")
    r16 = st.selectbox("Elige:", ["Elige una opción...", "Comunidad Autónoma", "Municipio", "Continente"], key="p16")
    if r16 == "Comunidad Autónoma": score_t2 += 1

# --- TEMA 3: NORMAS Y SEÑALES ---
with tab3:
    st.header("Convivencia y Señales")
    score_t3 = 0

    col1, col2 = st.columns(2)
    
    with col1:
        # P17 - Selección
        st.write("17. Una señal de tráfico TRIANGULAR con borde rojo indica...")
        r17 = st.radio("Significado:", ["Prohibición", "Peligro", "Información"], key="p17", index=None)
        if r17 == "Peligro": score_t3 += 1

        # P18 - Selección
        st.write("18. Una señal REDONDA con borde ROJO indica...")
        r18 = st.radio("Significado:", ["Prohibición", "Obligación", "Peligro"], key="p18", index=None)
        if r18 == "Prohibición": score_t3 += 1

    with col2:
        # P19 - Selección
        st.write("19. Una señal REDONDA y AZUL indica...")
        r19 = st.selectbox("Elige:", ["Elige...", "Obligación", "Información"], key="p19")
        if r19 == "Obligación": score_t3 += 1

        # P20 - Selección
        st.write("20. Una señal CUADRADA suele indicar...")
        r20 = st.selectbox("Elige:", ["Elige...", "Peligro", "Información"], key="p20")
        if r20 == "Información": score_t3 += 1

    # P21 - Escribir
    st.write("21. Las reglas que sirven para llevarnos bien y respetarnos se llaman...")
    r21 = st.text_input("Nor...", key="p21")
    if r21: score_t3 += check_text_answer(r21, ["normas", "normas sociales"], "p21_check")

    # P22 - Pensar
    st.info("22. 🤔 PREGUNTA DE PENSAR: ¿Por qué crees que son importantes las normas de educación vial?")
    st.text_area("Reflexiona:", key="p22")
    with st.expander("Ver respuesta modelo"):
        st.write("Para evitar accidentes y para que tanto peatones como vehículos puedan circular con seguridad.")

    # P23 - Selección
    st.write("23. Respetar el turno de palabra es una norma de...")
    r23 = st.radio("Tipo:", ["Seguridad Vial", "Convivencia"], key="p23", index=None)
    if r23 == "Convivencia": score_t3 += 1

    # P24 - Escribir
    st.write("24. Los peatones deben cruzar siempre por el paso de...")
    r24 = st.text_input("Paso de...", key="p24")
    if r24: score_t3 += check_text_answer(r24, ["cebra", "peatones"], "p24_check")

# --- TEMA 4: EL DINERO ---
with tab4:
    st.header("El Dinero y el Consumo")
    score_t4 = 0

    # P25 - Selección
    st.write("25. Antes de que existiera el dinero, la gente intercambiaba cosas. ¿Cómo se llamaba eso?")
    r25 = st.radio("Nombre:", ["Compra", "Trueque", "Préstamo"], key="p25", index=None)
    if r25 == "Trueque": score_t4 += 1

    # P26 - Pensar
    st.info("26. 🤔 PREGUNTA DE PENSAR: ¿Qué problemas tenía el trueque?")
    st.text_area("Escribe:", key="p26")
    with st.expander("Ver respuesta modelo"):
        st.write("Que era difícil ponerse de acuerdo en el valor de las cosas o encontrar a alguien que quisiera lo que tú tenías.")

    # P27 - Selección
    st.write("27. El dinero sirve como medio de pago, unidad de cuenta y...")
    r27 = st.selectbox("Función:", ["Elige...", "Depósito de valor (ahorro)", "Juguete"], key="p27")
    if r27 == "Depósito de valor (ahorro)": score_t4 += 1

    # P28 - Escribir
    st.write("28. La cantidad de dinero que cuesta un producto se llama...")
    r28 = st.text_input("Pre...", key="p28")
    if r28: score_t4 += check_text_answer(r28, ["precio"], "p28_check")

    # P29 - Selección (Lógica del libro)
    st.write("29. Si hay POCOS productos y MUCHA gente quiere comprarlos, el precio...")
    r29 = st.radio("¿Qué pasa?", ["Sube", "Baja"], key="p29", index=None)
    if r29 == "Sube": score_t4 += 1

    # P30 - Escribir
    st.write("30. Guardar parte del dinero que tenemos para el futuro se llama...")
    r30 = st.text_input("Aho...", key="p30")
    if r30: score_t4 += check_text_answer(r30, ["ahorrar", "ahorro"], "p30_check")

    # P31 - Selección
    st.write("31. Cuando el banco te deja dinero, te está haciendo un...")
    r31 = st.selectbox("Acción:", ["Elige...", "Regalo", "Préstamo"], key="p31")
    if r31 == "Préstamo": score_t4 += 1

    # P32 - Pensar
    st.info("32. 🤔 PREGUNTA DE PENSAR: ¿Cuál es la diferencia entre un gasto necesario y un deseo?")
    st.text_area("Explica:", key="p32")
    with st.expander("Ver respuesta modelo"):
        st.write("Necesario es imprescindible para vivir (comida, luz). Deseo es algo que queremos pero podemos vivir sin ello (juguetes extra, chuches).")

# --- TEMA 5: EL PLANETA ---
with tab5:
    st.header("Cuidamos el Planeta")
    score_t5 = 0

    # P33 - Selección
    st.write("33. Las energías que NO se agotan (como el sol o el viento) se llaman...")
    r33 = st.radio("Tipo:", ["Renovables", "No renovables"], key="p33", index=None)
    if r33 == "Renovables": score_t5 += 1

    # P34 - Escribir
    st.write("34. El petróleo y el carbón son energías...")
    r34 = st.text_input("No ren...", key="p34")
    if r34: score_t5 += check_text_answer(r34, ["no renovables", "contaminantes"], "p34_check")

    # P35 - Selección
    st.write("35. El impacto que tiene nuestro modo de vida sobre el planeta se llama...")
    r35 = st.selectbox("Concepto:", ["Elige...", "Huella ecológica", "Censo"], key="p35")
    if r35 == "Huella ecológica": score_t5 += 1

    # P36 - Selección
    st.write("36. ¿Cuál de estas es una acción de las '3 R'?")
    r36 = st.radio("Acción:", ["Romper", "Reciclar", "Rápido"], key="p36", index=None)
    if r36 == "Reciclar": score_t5 += 1

    # P37 - Escribir
    st.write("37. El agua que podemos beber se llama agua...")
    r37 = st.text_input("Agua po...", key="p37")
    if r37: score_t5 += check_text_answer(r37, ["potable"], "p37_check")

    # P38 - Pensar
    st.info("38. 🤔 PREGUNTA DE PENSAR: ¿Cómo puedes reducir tu huella ecológica en casa?")
    st.text_area("Ideas:", key="p38")
    with st.expander("Ver respuesta modelo"):
        st.write("Apagando luces, cerrando el grifo al lavarse los dientes, reciclando basura, usando menos plástico.")

    # P39 - Selección
    st.write("39. Los recursos naturales son...")
    r39 = st.radio("Cantidad:", ["Ilimitados (nunca se acaban)", "Limitados (se pueden acabar)"], key="p39", index=None)
    if r39 == "Limitados (se pueden acabar)": score_t5 += 1

    # P40 - Escribir
    st.write("40. Debemos cuidar el planeta para las generaciones...")
    r40 = st.text_input("Futu...", key="p40")
    if r40: score_t5 += check_text_answer(r40, ["futuras"], "p40_check")

st.markdown("---")
if st.button("🏁 Calcular mi Nota Final"):
    # Nota: Las preguntas de "Pensar" no suman puntos automáticos aquí, 
    # solo las de selección y escritura (Total 35 puntos automáticos aprox)
    total_score = score_t1 + score_t2 + score_t3 + score_t4 + score_t5
    st.balloons()
    st.header(f"Tu puntuación automática es: {total_score} aciertos")
    
    if total_score >= 30:
        st.success("¡EXCELENTE TRABAJO! Eres un experto en Sociales. 🌟")
    elif total_score >= 20:
        st.warning("¡Buen trabajo! Pero repasa un poco más los fallos. 👍")
    else:
        st.error("Hay que estudiar un poquito más. ¡Ánimo! 💪")