import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Laboratorio de Ciencias 4º Primaria",
    page_icon="⚗️",
    layout="wide"
)

# --- ESTILOS CSS (Mejorados con más espacio) ---
st.markdown("""
    <style>
    /* ESPACIADO GENERAL */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }
    
    /* BOTONES DE LA ESTANTERÍA */
    .stButton>button {
        width: 100%;
        height: 85px;
        font-size: 22px;
        border-radius: 15px;
        border: 2px solid #81C784;
        background-color: #ffffff;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s;
        margin-bottom: 15px;
    }
    .stButton>button:hover {
        background-color: #f1f8e9;
        transform: translateY(-3px);
        border-color: #2E7D32;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.2);
    }
    
    /* CAJA DE ANALOGÍAS (TEXTO LITERARIO) */
    .historia-ciencia {
        background-color: #fff8e1;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #ffb300;
        font-size: 18px;
        line-height: 1.6;
        color: #4e342e;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* EL VASO DE MEZCLAS */
    .vaso-mezcla {
        border: 5px solid #455A64;
        border-radius: 0 0 40px 40px;
        border-top: none;
        padding: 30px;
        text-align: center;
        background: linear-gradient(to bottom, #ffffff 10%, #e1f5fe 100%);
        min-height: 200px;
        margin-top: 10px;
        box-shadow: 0px 8px 15px rgba(0,0,0,0.1);
    }
    
    /* TÍTULOS */
    h1 { color: #2E7D32; font-family: 'Comic Sans MS', sans-serif; }
    h3 { color: #1565C0; }
    
    /* SEPARADORES VISUALES */
    .espacio { margin-bottom: 40px; }
    
    /* ESTANTERÍA */
    .estanteria-titulo {
        background-color: #e8f5e9;
        padding: 8px 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-weight: bold;
        color: #2E7D32;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO (MEMORIA) ---
if 'vaso' not in st.session_state:
    st.session_state.vaso = []

# --- DATOS: TEORÍA CON NARRATIVA ---
teoria = {
    "Filtración": {
        "titulo": "El Arte de Colar",
        "narrativa": "Imagínate que eres un portero de fútbol. La red de la portería deja pasar el aire, pero atrapa el balón porque es demasiado grande. ¡La filtración es igual! Usamos un papel con agujeros microscópicos (el filtro). El líquido es tan pequeño que se escapa por los huecos, pero los trozos sólidos, grandes y torpes, se quedan atrapados arriba.",
        "ejemplo": "🍝 **En casa:** Ocurre cuando colamos los macarrones. El agua se escapa, ¡pero la cena se queda!",
        "icono": "🛡"
    },
    "Decantación": {
        "titulo": "La Danza de los Pesos",
        "narrativa": "Aquí jugamos con la gravedad y la paciencia. Imagina dos líquidos que se llevan mal, como el agua y el aceite. Si los agitas, parecen mezclarse, pero si esperas un rato... ¡Magia! El líquido más pesado se hunde hasta el fondo y el más ligero flota encima, como un barco. Entonces, con mucho cuidado, abrimos una llavecita y dejamos caer solo el de abajo.",
        "ejemplo": "🥗 **En casa:** Mira una botella de vinagreta que lleva tiempo quieta. Verás el aceite arriba y el vinagre abajo.",
        "icono": "🏺"
    },
    "Evaporación": {
        "titulo": "El Truco de la Desaparición",
        "narrativa": "A veces, un sólido (como la sal) se esconde tan bien dentro del agua que parece que ha desaparecido. Para encontrarlo, necesitamos la ayuda del Calor. Al calentar la mezcla, el agua se convierte en vapor y se va volando hacia las nubes. ¿Y qué queda en el fondo del recipiente? ¡Sorpresa! Los cristales de sal aparecen de nuevo, secos y solos.",
        "ejemplo": "👕 **En casa:** Como cuando tiendes una camiseta mojada al sol. El agua se va al cielo y la tela se queda seca.",
        "icono": "🔥"
    },
    "Destilación": {
        "titulo": "El Viaje del Vapor",
        "narrativa": "Esta es la técnica de los alquimistas. Tenemos dos líquidos mezclados y queremos separarlos. Los calentamos y, como cada uno hierve a una temperatura distinta, el primero se convierte en gas y escapa por un tubo. Luego, enfriamos ese tubo rápidamente para que el gas vuelva a convertirse en líquido, cayendo gota a gota en otro vaso limpio. ¡Es como crear lluvia artificial!",
        "ejemplo": "🌧️ **En la naturaleza:** El sol calienta el mar, el agua sube (sin sal) y luego se enfría en las nubes para llover agua dulce.",
        "icono": "🌡️"
    },
    "Tamizado": {
        "titulo": "El Colador Gigante",
        "narrativa": "Imagina que tienes una caja de juguetes con piezas grandes y piezas pequeñas mezcladas. Si usas una rejilla con agujeros medianos, las piezas pequeñas caen por los huecos y las grandes se quedan arriba. ¡Eso es tamizar! Es como usar un colador de cocina para separar cosas sólidas de distinto tamaño.",
        "ejemplo": "🏖️ **En la playa:** Los niños usan un tamiz para separar la arena fina de las piedrecitas y las conchas.",
        "icono": "🔲"
    },
    "Imantación": {
        "titulo": "El Poder Magnético",
        "narrativa": "Los imanes son como superhéroes que solo atraen a ciertos metales (hierro, níquel, cobalto). Si tienes una mezcla con trocitos de metal mezclados con otras cosas, solo necesitas acercar un imán y... ¡ZAS! Los trocitos de metal salen volando hacia el imán, dejando el resto limpio. Es como tener un superpoder selectivo.",
        "ejemplo": "🧲 **En casa:** Si se te caen clips y gomas de borrar al suelo, un imán recoge los clips pero deja las gomas.",
        "icono": "🧲"
    }
}

# --- 20 INGREDIENTES ---
ingredientes = {
    # LÍQUIDOS (Fila superior)
    "Agua 💧": {"tipo": "liquido", "desc": "Líquido transparente"},
    "Aceite 🫒": {"tipo": "liquido_graso", "desc": "Líquido denso que flota"},
    "Alcohol 🍶": {"tipo": "liquido_alcohol", "desc": "Líquido transparente"},
    "Vinagre 🍇": {"tipo": "liquido", "desc": "Líquido ácido"},
    "Zumo 🍊": {"tipo": "liquido_pulpa", "desc": "Líquido con trocitos"},
    "Leche 🥛": {"tipo": "liquido", "desc": "Líquido blanco nutritivo"},
    "Miel 🍯": {"tipo": "liquido_denso", "desc": "Líquido muy espeso y dulce"},
    "Jabón líquido 🧴": {"tipo": "liquido_jabon", "desc": "Líquido espumoso"},
    "Agua salada 🌊": {"tipo": "liquido_salado", "desc": "Agua con sal disuelta"},
    "Tinta 🖋️": {"tipo": "liquido_color", "desc": "Líquido de color intenso"},
    # SÓLIDOS (Fila inferior)
    "Arena 🏜️": {"tipo": "solido_insoluble", "desc": "Granos sólidos"},
    "Piedras 🪨": {"tipo": "solido_insoluble", "desc": "Sólido pesado"},
    "Sal 🧂": {"tipo": "solido_soluble", "desc": "Polvo que se disuelve"},
    "Azúcar 🍬": {"tipo": "solido_soluble", "desc": "Cristales dulces"},
    "Arroz 🍚": {"tipo": "solido_insoluble", "desc": "Granos duros"},
    "Limaduras hierro ⚙️": {"tipo": "solido_magnetico", "desc": "Trocitos de metal magnético"},
    "Harina 🌾": {"tipo": "solido_insoluble_fino", "desc": "Polvo blanco muy fino"},
    "Lentejas 🫘": {"tipo": "solido_insoluble", "desc": "Legumbres pequeñas"},
    "Grava 🪨": {"tipo": "solido_insoluble_grueso", "desc": "Piedras pequeñas"},
    "Bicarbonato ⚪": {"tipo": "solido_reactivo", "desc": "Polvo blanco que reacciona"},
}

# --- LÓGICA ---
def agregar(nombre):
    if len(st.session_state.vaso) < 2:
        st.session_state.vaso.append(nombre)
    else:
        st.toast("⚠️ El vaso está lleno. ¡Vacíalo primero!", icon="🛑")

def reiniciar():
    st.session_state.vaso = []

def analizar(items):
    i1, i2 = items[0], items[1]
    # Poner agua primero si hay
    if "Agua" in i2 and "Agua" not in i1:
        i1, i2 = i2, i1

    t1 = ingredientes[i1]["tipo"]
    t2 = ingredientes[i2]["tipo"]

    # --- IMANTACIÓN: si hay limaduras de hierro ---
    if "Limaduras" in i1 or "Limaduras" in i2:
        return "Imantación"

    # --- TAMIZADO: dos sólidos insolubles de distinto tamaño ---
    solidos_tamiz = {"solido_insoluble", "solido_insoluble_fino", "solido_insoluble_grueso"}
    if t1 in solidos_tamiz and t2 in solidos_tamiz and t1 != t2:
        return "Tamizado"
    # Arena + Grava / Lentejas + Arena tipo combinaciones
    if ("Arena" in i1 or "Arena" in i2) and ("Grava" in i1 or "Grava" in i2 or "Piedras" in i1 or "Piedras" in i2 or "Lentejas" in i1 or "Lentejas" in i2):
        return "Tamizado"
    if ("Harina" in i1 or "Harina" in i2) and ("Arroz" in i1 or "Arroz" in i2 or "Lentejas" in i1 or "Lentejas" in i2):
        return "Tamizado"

    # --- FILTRACIÓN: líquido + sólido insoluble ---
    if "Zumo" in i1 or "Zumo" in i2:
        return "Filtración"
    solidos_insolubles = {"solido_insoluble", "solido_insoluble_fino", "solido_insoluble_grueso"}
    if (t1.startswith("liquido") and t2 in solidos_insolubles) or \
       (t2.startswith("liquido") and t1 in solidos_insolubles):
        return "Filtración"

    # --- EVAPORACIÓN: líquido + sólido soluble ---
    if (t1.startswith("liquido") and t2 == "solido_soluble") or \
       (t2.startswith("liquido") and t1 == "solido_soluble"):
        return "Evaporación"

    # --- DECANTACIÓN: dos líquidos inmiscibles ---
    if ("Agua" in i1 or "Leche" in i1 or "Vinagre" in i1) and ("Aceite" in i2):
        return "Decantación"
    if ("Aceite" in i1) and ("Agua" in i2 or "Leche" in i2 or "Vinagre" in i2):
        return "Decantación"
    if ("Miel" in i1 or "Miel" in i2) and ("Aceite" in i1 or "Aceite" in i2):
        return "Decantación"

    # --- DESTILACIÓN: dos líquidos miscibles ---
    if ("Agua" in i1 and "Alcohol" in i2) or ("Alcohol" in i1 and "Agua" in i2):
        return "Destilación"
    if ("Agua" in i1 and "Vinagre" in i2) or ("Vinagre" in i1 and "Agua" in i2):
        return "Destilación"
    if ("Agua salada" in i1 or "Agua salada" in i2) and ("Agua" in i1 or "Agua" in i2) and i1 != i2:
        return "Destilación"

    # --- REACCIÓN QUÍMICA (caso especial bicarbonato + vinagre) ---
    if ("Bicarbonato" in i1 or "Bicarbonato" in i2) and ("Vinagre" in i1 or "Vinagre" in i2):
        return "Reacción"

    return "Desconocido"

# --- INTERFAZ ---
st.sidebar.title("📚 Menú")
modo = st.sidebar.radio("Elige actividad:", ["🧪 Laboratorio Interactivo", "📖 Leer el Libro de Ciencias", "📝 Examen Final"])

# ==========================================
# MODO LABORATORIO (CON 20 INGREDIENTES)
# ==========================================
if modo == "🧪 Laboratorio Interactivo":
    st.markdown("<h1>⚗️ Laboratorio de Mezclas</h1>", unsafe_allow_html=True)
    st.write("Haz clic en dos ingredientes para añadirlos al vaso. ¡Fíjate bien en qué ocurre!")

    st.markdown("<div class='espacio'></div>", unsafe_allow_html=True)

    # --- ESTANTERÍA SUPERIOR: LÍQUIDOS ---
    st.markdown("<div class='estanteria-titulo'>🧪 Estante de Líquidos (fila superior)</div>", unsafe_allow_html=True)
    
    c1, c2, c3, c4, c5 = st.columns(5, gap="medium")
    with c1:
        if st.button("Agua 💧"): agregar("Agua 💧")
        if st.button("Leche 🥛"): agregar("Leche 🥛")
    with c2:
        if st.button("Aceite 🫒"): agregar("Aceite 🫒")
        if st.button("Miel 🍯"): agregar("Miel 🍯")
    with c3:
        if st.button("Alcohol 🍶"): agregar("Alcohol 🍶")
        if st.button("Jabón líquido 🧴"): agregar("Jabón líquido 🧴")
    with c4:
        if st.button("Vinagre 🍇"): agregar("Vinagre 🍇")
        if st.button("Agua salada 🌊"): agregar("Agua salada 🌊")
    with c5:
        if st.button("Zumo 🍊"): agregar("Zumo 🍊")
        if st.button("Tinta 🖋️"): agregar("Tinta 🖋️")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ESTANTERÍA INFERIOR: SÓLIDOS ---
    st.markdown("<div class='estanteria-titulo'>🧱 Estante de Sólidos (fila inferior)</div>", unsafe_allow_html=True)
    
    s1, s2, s3, s4, s5 = st.columns(5, gap="medium")
    with s1:
        if st.button("Arena 🏜️"): agregar("Arena 🏜️")
        if st.button("Limaduras hierro ⚙️"): agregar("Limaduras hierro ⚙️")
    with s2:
        if st.button("Piedras 🪨"): agregar("Piedras 🪨")
        if st.button("Harina 🌾"): agregar("Harina 🌾")
    with s3:
        if st.button("Sal 🧂"): agregar("Sal 🧂")
        if st.button("Lentejas 🫘"): agregar("Lentejas 🫘")
    with s4:
        if st.button("Azúcar 🍬"): agregar("Azúcar 🍬")
        if st.button("Grava 🪨", key="grava_btn"): agregar("Grava 🪨")
    with s5:
        if st.button("Arroz 🍚"): agregar("Arroz 🍚")
        if st.button("Bicarbonato ⚪"): agregar("Bicarbonato ⚪")

    # GRAN ESPACIO SEPARADOR
    st.markdown("<br><br><hr><br>", unsafe_allow_html=True)

    # 2. ZONA DE TRABAJO
    col_vaso, col_hueco, col_analisis = st.columns([1.5, 0.2, 2.5])

    with col_vaso:
        st.markdown("### 🥃 Tu Vaso")
        contenido_html = ""
        if len(st.session_state.vaso) == 0:
            contenido_html = "<br><p style='color:#bbb; font-size:18px;'>El vaso está vacío...<br>Añade cosas arriba 👆</p>"
        else:
            for item in st.session_state.vaso:
                contenido_html += f"<h2 style='margin:10px 0;'>{item}</h2>"

        st.markdown(f"<div class='vaso-mezcla'>{contenido_html}</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ LIMPIAR VASO", type="primary"):
            reiniciar()

    with col_analisis:
        st.markdown("### 🔬 Panel de Análisis")

        if len(st.session_state.vaso) == 2:
            resultado = analizar(st.session_state.vaso)

            if resultado == "Reacción":
                st.info(f"🧪 **Mezcla creada:** {st.session_state.vaso[0]} + {st.session_state.vaso[1]}")
                st.markdown("""
                <div class='historia-ciencia' style='border-left-color: #e53935;'>
                    <h3 style='color:#c62828'>💥 ¡REACCIÓN QUÍMICA!</h3>
                    <p><strong>¡Cuidado!</strong> Al mezclar vinagre con bicarbonato se produce una <strong>reacción química</strong>: 
                    aparecen burbujas de gas (CO₂), espuma y burbujeo. ¡No es una simple mezcla, se ha creado 
                    una sustancia nueva! Este cambio es <strong>irreversible</strong>.</p>
                    <p style='font-size:16px; color:#555;'><em>🌋 <strong>En casa:</strong> ¡Es el famoso volcán de los experimentos caseros!</em></p>
                </div>
                """, unsafe_allow_html=True)

            elif resultado != "Desconocido":
                st.info(f"🧪 **Mezcla creada:** {st.session_state.vaso[0]} + {st.session_state.vaso[1]}")
                st.write("¿Qué técnica mágica usamos para separarlos?")

                # Botones de herramientas (ahora 6)
                b1, b2, b3 = st.columns(3)
                b4, b5, b6 = st.columns(3)
                eleccion = None
                with b1:
                    if st.button("🛡\nFiltrar"): eleccion = "Filtración"
                with b2:
                    if st.button("🏺\nDecantar"): eleccion = "Decantación"
                with b3:
                    if st.button("🔥\nEvaporar"): eleccion = "Evaporación"
                with b4:
                    if st.button("🌡️\nDestilar"): eleccion = "Destilación"
                with b5:
                    if st.button("🔲\nTamizar"): eleccion = "Tamizado"
                with b6:
                    if st.button("🧲\nImantar"): eleccion = "Imantación"

                # RESPUESTA CON NARRATIVA
                if eleccion:
                    if eleccion == resultado:
                        st.balloons()
                        t = teoria[resultado]
                        st.markdown(f"""
                        <div class='historia-ciencia'>
                            <h3 style='color:#E65100'>¡CORRECTO! Usamos {t['titulo']}</h3>
                            <p><strong>Lo que ocurre:</strong> {t['narrativa']}</p>
                            <p style='font-size:16px; color:#555;'><em>{t['ejemplo']}</em></p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("❌ Mmm... esa máquina no funciona con esta mezcla. ¡Prueba otra!")
            else:
                st.warning("¡Vaya mezcla más rara! Prueba con ingredientes más normales (ej. Agua y Arena).")

        elif len(st.session_state.vaso) == 1:
            st.info("💧 Tienes un ingrediente. ¡Necesitas otro para hacer una mezcla!")
        else:
            st.write("Esperando ingredientes...")

# ==========================================
# MODO LECTURA (TEORÍA PURA)
# ==========================================
elif modo == "📖 Leer el Libro de Ciencias":
    st.header("📖 El Gran Libro de las Mezclas")
    st.write("Aquí tienes las historias de cómo separamos las cosas.")

    for clave, valor in teoria.items():
        st.markdown(f"""
        <div class='historia-ciencia' style='border-left-color: #2196F3; margin-bottom: 30px;'>
            <h3>{valor['icono']} {clave}: {valor['titulo']}</h3>
            <p>{valor['narrativa']}</p>
            <p><em>{valor['ejemplo']}</em></p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODO EXAMEN (NUEVAS PREGUNTAS)
# ==========================================
elif modo == "📝 Examen Final":
    st.header("📝 Reto Científico")
    st.write("¡Demuestra todo lo que has aprendido en el laboratorio!")

    preguntas = [
        {"q": "Tu madre ha hecho un caldo y quiere quitar los trozos de verdura del líquido.",
         "a": "Filtración", "hint": "Los trozos son sólidos grandes y el caldo es líquido."},
        {"q": "En un charco después de la lluvia hay barro en el fondo y agua limpia arriba.",
         "a": "Decantación", "hint": "El barro pesado se hunde solo con el tiempo."},
        {"q": "Los marineros antiguos querían conseguir sal del agua del mar.",
         "a": "Evaporación", "hint": "Necesitan que el agua desaparezca y quede solo la sal."},
        {"q": "En una fábrica de perfumes necesitan separar la esencia de flores del agua.",
         "a": "Destilación", "hint": "Son dos líquidos mezclados que hierven a diferente temperatura."},
        {"q": "Has mezclado lentejas y arroz sin querer. ¿Cómo los separas rápido?",
         "a": "Filtración", "hint": "Un colador con agujeros del tamaño justo."},
        {"q": "Tu hermano ha tirado clips de metal dentro de un bote lleno de botones de plástico.",
         "a": "Imantación", "hint": "Solo los clips son de metal..."},
        {"q": "Quieres recuperar el azúcar que has disuelto en un vaso de leche.",
         "a": "Evaporación", "hint": "El azúcar está disuelto, no lo puedes colar."},
        {"q": "En el taller de tu abuelo hay arena fina mezclada con tornillos y clavos de hierro.",
         "a": "Imantación", "hint": "Los tornillos son metálicos y la arena no."},
        {"q": "Has mezclado agua y aceite de girasol en una botella.",
         "a": "Decantación", "hint": "Se forman dos capas porque no se mezclan."},
        {"q": "En una destilería quieren separar el alcohol del agua para hacer licor.",
         "a": "Destilación", "hint": "El alcohol hierve antes que el agua."},
    ]

    score = 0
    with st.form("quiz"):
        for i, p in enumerate(preguntas):
            st.markdown(f"**{i+1}. {p['q']}**")
            st.caption(f"👀 Pista: {p['hint']}")
            sel = st.radio(
                f"R{i}",
                ["Filtración", "Decantación", "Evaporación", "Destilación", "Tamizado", "Imantación"],
                horizontal=True, key=i
            )
            if sel == p['a']:
                score += 1
            st.markdown("---")

        if st.form_submit_button("📝 Entregar Examen"):
            total = len(preguntas)
            if score == total:
                st.balloons()
                st.success(f"¡{score}/{total}! 🏆 ¡Eres un Maestro de la Ciencia!")
            elif score >= 7:
                st.success(f"¡{score}/{total}! 🌟 ¡Muy buen trabajo! Repasa los que has fallado.")
            elif score >= 5:
                st.warning(f"Has sacado un {score}/{total}. 🙂 ¡Aprobado justo! Lee el libro de nuevo.")
            else:
                st.error(f"Has sacado un {score}/{total}. 📚 Tienes que estudiar más. ¡Vuelve al laboratorio!")