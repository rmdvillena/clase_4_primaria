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
        height: 85px; /* Botones más altos */
        font-size: 22px;
        border-radius: 15px;
        border: 2px solid #81C784; /* Verde suave */
        background-color: #ffffff;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s;
        margin-bottom: 15px; /* Espacio vertical entre filas de botones */
    }
    .stButton>button:hover {
        background-color: #f1f8e9;
        transform: translateY(-3px);
        border-color: #2E7D32;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.2);
    }
    
    /* CAJA DE ANALOGÍAS (TEXTO LITERARIO) */
    .historia-ciencia {
        background-color: #fff8e1; /* Amarillo muy suave */
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
        padding: 30px; /* Más relleno interno */
        text-align: center;
        background: linear-gradient(to bottom, #ffffff 10%, #e1f5fe 100%);
        min-height: 200px; /* Vaso más alto */
        margin-top: 10px;
        box-shadow: 0px 8px 15px rgba(0,0,0,0.1);
    }
    
    /* TÍTULOS */
    h1 { color: #2E7D32; font-family: 'Comic Sans MS', sans-serif; }
    h3 { color: #1565C0; }
    
    /* SEPARADORES VISUALES */
    .espacio { margin-bottom: 40px; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO (MEMORIA) ---
if 'vaso' not in st.session_state:
    st.session_state.vaso = []

# --- DATOS: AHORA CON MÁS "LITERATURA" ---
teoria = {
    "Filtración": {
        "titulo": "El Arte de Colar",
        "narrativa": "Imagínate que eres un portero de fútbol. La red de la portería deja pasar el aire, pero atrapa el balón porque es demasiado grande. ¡La filtración es igual! Usamos un papel con agujeros microscópicos (el filtro). El líquido es tan pequeño que se escapa por los huecos, pero los trozos sólidos, grandes y torpes, se quedan atrapados arriba.",
        "ejemplo": "🍝 **En casa:** Ocurre cuando colamos los macarrones. El agua se escapa, ¡pero la cena se queda!",
        "icono": "🛒"
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
    }
}

# --- INGREDIENTES ---
ingredientes = {
    "Agua 💧": {"tipo": "liquido", "desc": "Líquido transparente"},
    "Aceite 🫒": {"tipo": "liquido_graso", "desc": "Líquido denso que flota"},
    "Alcohol 🍶": {"tipo": "liquido_alcohol", "desc": "Líquido transparente"},
    "Vinagre 🍇": {"tipo": "liquido", "desc": "Líquido ácido"},
    "Arena 🏜️": {"tipo": "solido_insoluble", "desc": "Granos sólidos"},
    "Piedras 🪨": {"tipo": "solido_insoluble", "desc": "Sólido pesado"},
    "Sal 🧂": {"tipo": "solido_soluble", "desc": "Polvo que se disuelve"},
    "Azúcar 🍬": {"tipo": "solido_soluble", "desc": "Cristales dulces"},
    "Arroz 🍚": {"tipo": "solido_insoluble", "desc": "Granos duros"},
    "Zumo 🍊": {"tipo": "liquido_pulpa", "desc": "Líquido con trocitos"}
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
    if "Agua" in i2: i1, i2 = i2, i1 
    
    # 1. Filtración
    if ("Zumo" in i1 or "Zumo" in i2): return "Filtración"
    if (ingredientes[i1]["tipo"].startswith("liquido") and ingredientes[i2]["tipo"] == "solido_insoluble") or \
       (ingredientes[i2]["tipo"].startswith("liquido") and ingredientes[i1]["tipo"] == "solido_insoluble"):
        return "Filtración"

    # 2. Evaporación
    if (ingredientes[i1]["tipo"] == "liquido" and ingredientes[i2]["tipo"] == "solido_soluble") or \
       (ingredientes[i2]["tipo"] == "liquido" and ingredientes[i1]["tipo"] == "solido_soluble"):
        return "Evaporación"

    # 3. Decantación
    if ("Agua" in i1 and "Aceite" in i2) or ("Vinagre" in i1 and "Aceite" in i2):
        return "Decantación"

    # 4. Destilación
    if ("Agua" in i1 and "Alcohol" in i2) or ("Vinagre" in i1 and "Agua" in i2):
        return "Destilación"

    return "Desconocido"

# --- INTERFAZ ---
st.sidebar.title("📚 Menú")
modo = st.sidebar.radio("Elige actividad:", ["🧪 Laboratorio Interactivo", "📖 Leer el Libro de Ciencias", "📝 Examen Final"])

# ==========================================
# MODO LABORATORIO (CON MÁS ESPACIO)
# ==========================================
if modo == "🧪 Laboratorio Interactivo":
    st.markdown("<h1>⚗️ Laboratorio de Mezclas</h1>", unsafe_allow_html=True)
    st.write("Haz clic en dos ingredientes para añadirlos al vaso. ¡Fíjate bien en qué ocurre!")
    
    # Espaciador
    st.markdown("<div class='espacio'></div>", unsafe_allow_html=True)

    # 1. ESTANTERÍA (Con espacio vertical entre filas gracias al CSS)
    st.markdown("### 1. La Estantería de Ingredientes")
    
    c1, c2, c3, c4, c5 = st.columns(5, gap="medium") # GAP MEDIUM separa las columnas
    
    with c1:
        if st.button("Agua 💧"): agregar("Agua 💧")
        if st.button("Arena 🏜️"): agregar("Arena 🏜️")
    with c2:
        if st.button("Aceite 🫒"): agregar("Aceite 🫒")
        if st.button("Sal 🧂"): agregar("Sal 🧂")
    with c3:
        if st.button("Alcohol 🍶"): agregar("Alcohol 🍶")
        if st.button("Arroz 🍚"): agregar("Arroz 🍚")
    with c4:
        if st.button("Vinagre 🍇"): agregar("Vinagre 🍇")
        if st.button("Azúcar 🍬"): agregar("Azúcar 🍬")
    with c5:
        if st.button("Zumo 🍊"): agregar("Zumo 🍊")
        if st.button("Piedras 🪨"): agregar("Piedras 🪨")

    # GRAN ESPACIO SEPARADOR
    st.markdown("<br><br><hr><br>", unsafe_allow_html=True)

    # 2. ZONA DE TRABAJO (Diseño ancho)
    col_vaso, col_hueco, col_analisis = st.columns([1.5, 0.2, 2.5]) # Columna hueca para separar

    with col_vaso:
        st.markdown("### 2. Tu Vaso")
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
        st.markdown("### 3. Panel de Análisis")
        
        if len(st.session_state.vaso) == 2:
            resultado = analizar(st.session_state.vaso)
            
            if resultado != "Desconocido":
                st.info(f"🧪 **Mezcla creada:** {st.session_state.vaso[0]} + {st.session_state.vaso[1]}")
                st.write("¿Qué técnica mágica usamos para separarlos?")
                
                # Botones de herramientas
                b1, b2, b3, b4 = st.columns(4)
                eleccion = None
                with b1:
                    if st.button("🛒\nFiltrar"): eleccion = "Filtración"
                with b2:
                    if st.button("🏺\nDecantar"): eleccion = "Decantación"
                with b3:
                    if st.button("🔥\nEvaporar"): eleccion = "Evaporación"
                with b4:
                    if st.button("🌡️\nDestilar"): eleccion = "Destilación"
                
                # RESPUESTA CON NARRATIVA
                if eleccion:
                    if eleccion == resultado:
                        st.balloons()
                        t = teoria[resultado]
                        # Aquí mostramos la "Literatura"
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
# MODO EXAMEN
# ==========================================
elif modo == "📝 Examen Final":
    st.header("📝 Reto Científico")
    
    preguntas = [
        {"q": "Tienes un vaso con agua y piedras del río.", "a": "Filtración", "hint": "Las piedras son sólidas y grandes."},
        {"q": "Se ha derramado aceite en un cubo de agua.", "a": "Decantación", "hint": "El aceite flota."},
        {"q": "Quieres recuperar la sal del agua de mar.", "a": "Evaporación", "hint": "El agua se tiene que ir volando."},
        {"q": "Queremos separar alcohol del vino.", "a": "Destilación", "hint": "Calentar y enfriar."},
        {"q": "Tu zumo tiene demasiada pulpa y no te gusta.", "a": "Filtración", "hint": "Usas un colador."}
    ]

    score = 0
    with st.form("quiz"):
        for i, p in enumerate(preguntas):
            st.markdown(f"**{i+1}. {p['q']}**")
            # Un poco de ayuda visual
            st.caption(f"👀 Pista: {p['hint']}")
            sel = st.radio(f"R{i}", ["Filtración", "Decantación", "Evaporación", "Destilación"], horizontal=True, key=i)
            if sel == p['a']:
                score += 1
            st.markdown("---")
        
        if st.form_submit_button("Entregar Examen"):
            if score == 5:
                st.balloons()
                st.success("¡5/5! ¡Eres un Maestro de la Ciencia!")
            else:
                st.warning(f"Has sacado un {score}/5. ¡Lee el libro de nuevo!")