import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Examen 4º Primaria (30 Preguntas)", page_icon="🧠", layout="centered")

st.title("🧠 Examen Máster: Geometría y Razonamiento")
st.markdown("""
**Nivel:** 4.º de Primaria - Avanzado
**Contenido:** 30 Preguntas.
* Parte 1-20: Conceptos básicos.
* **Parte 21-30: CASOS PRÁCTICOS Y RETOS (¡NUEVO!)**
""")
st.divider()

if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

# ==========================================
#              FUNCIONES DE DIBUJO
# ==========================================

# --- DIBUJOS BÁSICOS (1-20) ---
def dibujar_poligono(lados, color='cyan', label=None):
    fig, ax = plt.subplots(figsize=(2, 2))
    theta = np.linspace(0, 2*np.pi, lados, endpoint=False)
    if lados % 2 != 0: theta += np.pi/2
    x, y = np.cos(theta), np.sin(theta)
    ax.add_patch(patches.Polygon(np.column_stack([x, y]), color=color, ec='black', lw=2))
    if label: ax.text(0, 0, label, ha='center', fontweight='bold', fontsize=12)
    ax.axis('off'); ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    return fig

def dibujar_angulo(tipo):
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(-0.5, 2.5); ax.axis('off')
    ax.plot([0, 2], [0, 0], 'k-', lw=2)
    if tipo == 'agudo': ax.plot([0, 1.5], [0, 1.5], 'k-', lw=2)
    elif tipo == 'recto': 
        ax.plot([0, 0], [0, 2], 'k-', lw=2)
        ax.add_patch(patches.Rectangle((0,0), 0.3, 0.3, fill=False, ec='red'))
    elif tipo == 'obtuso': ax.plot([0, -1], [0, 1.5], 'k-', lw=2)
    return fig

def dibujar_reloj(hora, minuto):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.add_patch(patches.Circle((0,0), 1, fill=False, lw=2, ec='black'))
    ang_h = np.pi/2 - (hora + minuto/60)*2*np.pi/12
    ax.plot([0, 0.6*np.cos(ang_h)], [0, 0.6*np.sin(ang_h)], 'k-', lw=4)
    ang_m = np.pi/2 - minuto*2*np.pi/60
    ax.plot([0, 0.9*np.cos(ang_m)], [0, 0.9*np.sin(ang_m)], 'k-', lw=2)
    ax.axis('off'); ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    return fig

def dibujar_grafico():
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.bar(['A', 'B', 'C'], [12, 5, 8], color=['green', 'orange', 'purple'])
    ax.set_title("Datos"); ax.grid(axis='y', linestyle='--')
    return fig

# --- DIBUJOS AVANZADOS (21-30) ---

def dibujar_hexagono_triangulos():
    fig, ax = plt.subplots(figsize=(3, 3))
    theta = np.linspace(0, 2*np.pi, 6, endpoint=False)
    x, y = np.cos(theta), np.sin(theta)
    # Hexágono exterior
    ax.add_patch(patches.Polygon(np.column_stack([x, y]), fill=False, ec='black', lw=3))
    # Triángulos interiores
    for i in range(6):
        ax.plot([0, x[i]], [0, y[i]], 'b--', lw=1) # Líneas al centro
    ax.text(0.6, 0.9, "Lado=2cm", fontsize=10, color='red')
    ax.axis('off'); ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    return fig

def dibujar_alambre_deformado():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
    # Cuadrado
    ax1.add_patch(patches.Rectangle((0,0), 2, 2, fill=False, ec='blue', lw=3))
    ax1.set_title("1. Cuadrado de Alambre\nPerímetro = 20 cm")
    ax1.axis('off'); ax1.set_xlim(-0.5, 3); ax1.set_ylim(-0.5, 3)
    # Rombo (deformado)
    pts = [[1,0], [3,1], [2,3], [0,2]] # Romboide
    ax2.add_patch(patches.Polygon(pts, fill=False, ec='blue', lw=3))
    ax2.set_title("2. Lo 'aplastamos' un poco\n(Mismo alambre)")
    ax2.text(1.5, 1.5, "?", fontsize=20, ha='center', color='red')
    ax2.axis('off'); ax2.set_xlim(-1, 4); ax2.set_ylim(-1, 4)
    return fig

def dibujar_corte_rectangulo():
    fig, ax = plt.subplots(figsize=(4, 2))
    # Rectángulo original 10x4
    ax.add_patch(patches.Rectangle((0,0), 10, 4, facecolor='lightgreen', ec='black'))
    # Línea de corte
    ax.plot([5, 5], [0, 4], 'r--', lw=3) 
    ax.text(5, 4.2, "TIJERAS", color='red', ha='center', fontweight='bold')
    
    ax.text(2.5, -0.8, "5 cm", ha='center') # Base mitad
    ax.text(7.5, -0.8, "5 cm", ha='center') # Base mitad
    ax.text(-0.8, 2, "4 cm", va='center') # Altura
    
    ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 5)
    return fig

def dibujar_casa_compuesta():
    fig, ax = plt.subplots(figsize=(3, 3))
    # Cuadrado base
    ax.add_patch(patches.Rectangle((0,0), 2, 2, facecolor='orange', ec='black'))
    # Techo triángulo
    pts = [[0,2], [2,2], [1,3.5]]
    ax.add_patch(patches.Polygon(pts, facecolor='brown', ec='black'))
    
    # Cotas
    ax.text(1, -0.3, "4 m", ha='center') # Base casa
    ax.text(-0.3, 1, "4 m", va='center') # Pared izq
    ax.text(2.1, 1, "4 m", va='center') # Pared der
    ax.text(0.2, 2.8, "4 m", color='brown') # Techo
    ax.text(1.5, 2.8, "4 m", color='brown') # Techo
    
    ax.axis('off'); ax.set_xlim(-1, 3); ax.set_ylim(-1, 4)
    return fig

# ==========================================
#              PREGUNTAS 1-20 (RESUMIDAS)
# ==========================================
st.info("⬇️ PARTE 1: Conceptos Básicos (Preguntas 1-20) ⬇️")

c1, c2 = st.columns(2)
with c1: 
    st.pyplot(dibujar_poligono(7, 'violet'))
    st.session_state.respuestas['p1'] = st.text_input("1. Nombre polígono 7 lados:", key='k1').strip().lower()
with c2: 
    st.pyplot(dibujar_poligono(8, 'gold'))
    st.session_state.respuestas['p2'] = st.text_input("2. Nombre polígono 8 lados:", key='k2').strip().lower()

c3, c4, c5 = st.columns(3)
st.session_state.respuestas['p3'] = c3.text_input("3. Nombre 9 lados:", key='k3').lower()
st.session_state.respuestas['p4'] = c4.text_input("4. Nombre 10 lados:", key='k4').lower()
st.session_state.respuestas['p5'] = c5.selectbox("5. Puntos de unión:", ["Lados", "Vértices"], key='k5')

# Ángulos rápidos
c6, c7, c8 = st.columns(3)
with c6: 
    st.pyplot(dibujar_angulo('agudo'))
    st.session_state.respuestas['p6'] = st.text_input("6. Ángulo:", key='k6').lower()
with c7: 
    st.pyplot(dibujar_angulo('recto'))
    st.session_state.respuestas['p7'] = st.text_input("7. Ángulo:", key='k7').lower()
with c8: 
    st.pyplot(dibujar_angulo('obtuso'))
    st.session_state.respuestas['p8'] = st.text_input("8. Ángulo:", key='k8').lower()

# Reloj, líneas, círculo
c9, c10 = st.columns(2)
with c9: st.pyplot(dibujar_reloj(3,0))
with c10: st.session_state.respuestas['p9'] = st.selectbox("9. Ángulo a las 3:00:", ["Agudo", "Recto"], key='k9')

st.session_state.respuestas['p10'] = st.selectbox("10. Líneas que no se cruzan:", ["Paralelas", "Secantes"], key='k10')
st.session_state.respuestas['p11'] = st.text_input("11. Instrumento para medir ángulos:", key='k11').lower()
st.session_state.respuestas['p12'] = st.text_input("12. Línea centro-borde del círculo:", key='k12').lower()
st.session_state.respuestas['p13'] = st.text_input("13. Triángulo 3 lados iguales:", key='k13').lower()
st.session_state.respuestas['p14'] = st.radio("14. ¿Qué es solo el borde?", ["Círculo", "Circunferencia"], key='k14')

# Perímetros Básicos
st.session_state.respuestas['p15'] = st.text_input("15. Perímetro Pentágono (lado 5):", key='k15')
st.session_state.respuestas['p16'] = st.text_input("16. Perímetro Triángulo (10, 8, 8):", key='k16')
st.session_state.respuestas['p17'] = st.text_input("17. Perímetro Rectángulo (6 y 3):", key='k17') # 18
st.session_state.respuestas['p18'] = st.text_input("18. Si P=20 en cuadrado, lado es:", key='k18') # 5

# Gráfico
col_g1, col_g2 = st.columns([1,2])
with col_g1: st.pyplot(dibujar_grafico())
with col_g2:
    st.session_state.respuestas['p19'] = st.text_input("19. Valor de barra verde:", key='k19')
    st.session_state.respuestas['p20'] = st.text_input("20. Diferencia Verde - Naranja:", key='k20') # 12-5=7

st.divider()

# ==========================================
#      PARTE 2: CASOS PRÁCTICOS (NUEVO)
# ==========================================
st.error("🚀 PARTE 2: CASOS PRÁCTICOS Y RETOS (Preguntas 21-30)")

# --- CASO 1: HEXÁGONO Y TRIÁNGULOS ---
st.subheader("Caso 1: Construyendo Polígonos")
col_c1, col_c2 = st.columns([1, 2])
with col_c1:
    st.pyplot(dibujar_hexagono_triangulos())
with col_c2:
    st.write("21. Mira el dibujo. Un hexágono regular se puede formar uniendo triángulos equiláteros.")
    st.session_state.respuestas['p21'] = st.text_input("¿Cuántos triángulos ves dentro del hexágono?", key='k21').strip()
    
    st.write("22. Si el lado de cada triángulo mide **2 cm**, ¿cuál es el perímetro TOTAL del hexágono exterior?")
    st.write("*(Pista: Cuenta solo los lados de fuera)*")
    st.session_state.respuestas['p22'] = st.text_input("Respuesta (número):", key='k22').strip()

st.divider()

# --- CASO 2: EL ALAMBRE DEFORMADO ---
st.subheader("Caso 2: El Alambre Flexible")
col_c3, col_c4 = st.columns([1, 2])
with col_c3:
    st.pyplot(dibujar_alambre_deformado())
with col_c4:
    st.write("Tenemos un cuadrado hecho de alambre. Su perímetro es 20 cm.")
    st.write("Lo aplastamos un poco para convertirlo en un rombo, pero **NO cortamos ni estiramos** el alambre.")
    
    st.write("23. ¿Cuál es el perímetro del nuevo rombo?")
    st.session_state.respuestas['p23'] = st.text_input("Respuesta:", key='k23').strip()
    
    st.write("24. ¿Por qué?")
    st.session_state.respuestas['p24'] = st.radio("Elige la correcta:", 
        ["Porque el área se hace más pequeña.", "Porque la longitud del alambre (lados) no cambia."], key='k24')

st.divider()

# --- CASO 3: CORTANDO FIGURAS ---
st.subheader("Caso 3: Las Tijeras")
col_c5, col_c6 = st.columns([1, 2])
with col_c5:
    st.pyplot(dibujar_corte_rectangulo())
with col_c6:
    st.write("Tenemos un rectángulo de 10 cm de largo y 4 cm de ancho.")
    st.write("Lo cortamos por la mitad (línea roja) y separamos las dos piezas.")
    
    st.write("25. Ahora tenemos dos rectángulos más pequeños. ¿Cuánto mide el perímetro de **UNO SOLITO** de esos rectángulos nuevos?")
    st.write("*(Pista: El nuevo rectángulo mide 5 cm de base y 4 cm de altura. Suma sus 4 lados)*")
    st.session_state.respuestas['p25'] = st.text_input("Perímetro de una pieza:", key='k25').strip() # 5+5+4+4 = 18

    st.write("26. Si sumas el perímetro de las dos piezas sueltas (18 + 18 = 36), da MÁS que el perímetro original (28). ¿Por qué?")
    st.session_state.respuestas['p26'] = st.radio("Razón:", ["Es magia.", "Porque al cortar hemos creado dos lados nuevos por donde pasaron las tijeras."], key='k26')

st.divider()

# --- CASO 4: FIGURAS COMPUESTAS ---
st.subheader("Caso 4: La Casa")
col_c7, col_c8 = st.columns([1, 2])
with col_c7:
    st.pyplot(dibujar_casa_compuesta())
with col_c8:
    st.write("Hemos construido una casa juntando un cuadrado y un triángulo.")
    st.write("Queremos poner una cinta navideña por todo el **borde exterior**.")
    st.write("27. Calcula el perímetro exterior (suma solo lo de fuera).")
    st.write("Lados: Base(4) + Pared(4) + Pared(4) + Techo(4) + Techo(4).")
    st.session_state.respuestas['p27'] = st.text_input("Total cinta:", key='k27').strip() # 20

# --- CASO 5: LÓGICA FINAL ---
st.subheader("Caso 5: Cuerdas y Formas")
st.write("28. Tienes una cuerda de 1 metro atada por los extremos formando un círculo. Si con esa misma cuerda formas un cuadrado...")
st.session_state.respuestas['p28'] = st.radio("¿El perímetro cambia?", ["Sí, el cuadrado es más grande.", "No, el perímetro sigue siendo 1 metro (la cuerda)."], key='k28')

st.write("29. Un hexágono regular tiene perímetro 60 cm. ¿Cuánto mide cada lado?")
st.session_state.respuestas['p29'] = st.text_input("Respuesta:", key='k29').strip() # 10

st.write("30. Si partimos un hexágono por la mitad uniendo dos vértices opuestos, obtenemos dos...")
st.session_state.respuestas['p30'] = st.selectbox("Figuras:", ["Triángulos", "Cuadrados", "Trapecios"], key='k30')

st.divider()

# --- CORRECCIÓN ---
if st.button("🏆 CORREGIR TODO EL EXAMEN", type="primary"):
    score = 0
    errores = []

    # Validaciones Parte 1 (Simplificadas)
    if "hept" in st.session_state.respuestas['p1']: score+=1
    if "oct" in st.session_state.respuestas['p2']: score+=1
    if "enea" in st.session_state.respuestas['p3']: score+=1
    if "deca" in st.session_state.respuestas['p4']: score+=1
    if st.session_state.respuestas['p5'] == "Vértices": score+=1
    if "agud" in st.session_state.respuestas['p6']: score+=1
    if "rect" in st.session_state.respuestas['p7']: score+=1
    if "obtus" in st.session_state.respuestas['p8']: score+=1
    if st.session_state.respuestas['p9'] == "Recto": score+=1
    if st.session_state.respuestas['p10'] == "Paralelas": score+=1
    if "transport" in st.session_state.respuestas['p11']: score+=1
    if "radio" in st.session_state.respuestas['p12']: score+=1
    if "equil" in st.session_state.respuestas['p13']: score+=1
    if st.session_state.respuestas['p14'] == "Circunferencia": score+=1
    if st.session_state.respuestas['p15'] == "25": score+=1
    if st.session_state.respuestas['p16'] == "26": score+=1
    if st.session_state.respuestas['p17'] == "18": score+=1
    if st.session_state.respuestas['p18'] == "5": score+=1
    if st.session_state.respuestas['p19'] == "12": score+=1
    if st.session_state.respuestas['p20'] == "7": score+=1

    # Validaciones Parte 2 (Nuevas)
    # P21: 6 triángulos
    if st.session_state.respuestas['p21'] == "6": score+=1
    else: errores.append("P21: En un hexágono caben 6 triángulos.")
    
    # P22: 12 cm (2x6)
    if st.session_state.respuestas['p22'] == "12": score+=1
    else: errores.append("P22: Perímetro Hexágono = 2 cm x 6 lados = 12 cm.")

    # P23: 20 cm (Conserva perímetro)
    if st.session_state.respuestas['p23'] == "20": score+=1
    else: errores.append("P23: El alambre no cambia de tamaño, sigue siendo 20 cm.")

    # P24: Lados no cambian
    if "no cambia" in st.session_state.respuestas['p24']: score+=1
    else: errores.append("P24: La longitud del alambre se conserva.")

    # P25: 18 cm (5+5+4+4)
    if st.session_state.respuestas['p25'] == "18": score+=1
    else: errores.append("P25: Rectángulo nuevo (5x4) -> 5+5+4+4 = 18.")

    # P26: Lados nuevos
    if "lados nuevos" in st.session_state.respuestas['p26']: score+=1
    else: errores.append("P26: Al cortar creamos bordes nuevos.")

    # P27: 20 m (4x5)
    if st.session_state.respuestas['p27'] == "20": score+=1
    else: errores.append("P27: Casa: 4+4+4+4+4 = 20.")

    # P28: No cambia
    if "No" in st.session_state.respuestas['p28']: score+=1
    else: errores.append("P28: La cuerda mide lo mismo sea círculo o cuadrado.")

    # P29: 10 (60/6)
    if st.session_state.respuestas['p29'] == "10": score+=1
    else: errores.append("P29: 60 entre 6 lados = 10.")

    # P30: Trapecios
    if st.session_state.respuestas['p30'] == "Trapecios": score+=1
    else: errores.append("P30: Hexágono por la mitad = 2 Trapecios.")

    st.balloons()
    st.markdown(f"# 📊 NOTA FINAL: {score} / 30")
    
    if len(errores) > 0:
        st.error("Fallos en la Parte Práctica:")
        for e in errores:
            st.write(f"❌ {e}")
    else:
        st.success("¡PERFECTO! Has dominado la teoría y la práctica.")