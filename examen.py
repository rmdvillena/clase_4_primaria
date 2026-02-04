import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Examen Matemáticas 4º (20 Preguntas)", page_icon="📝", layout="centered")

st.title("📝 Gran Examen de Matemáticas: Geometría y Datos")
st.markdown("""
**Nivel:** 4.º de Primaria  
**Instrucciones:** Examen completo de **20 preguntas**.  
Las figuras se generan automáticamente. ¡A por el 10!
""")
st.divider()

# Diccionario para guardar respuestas
respuestas = {}

# --- FUNCIONES DE DIBUJO NUEVAS Y ANTERIORES ---

def dibujar_elementos_poligono():
    fig, ax = plt.subplots(figsize=(3, 3))
    theta = np.linspace(0, 2*np.pi, 6, endpoint=True)
    x = np.cos(theta); y = np.sin(theta)
    ax.plot(x, y, 'b-', lw=2) 
    ax.plot(x[:-1], y[:-1], 'ro', markersize=8) 
    ax.plot([x[0], x[2]], [y[0], y[2]], 'g--', lw=2) 
    ax.axis('off')
    return fig

def dibujar_circulo_circunferencia():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
    circ1 = patches.Circle((0, 0), 0.8, fill=False, edgecolor='blue', lw=3)
    ax1.add_patch(circ1); ax1.set_title("Figura A"); ax1.axis('off')
    circ2 = patches.Circle((0, 0), 0.8, color='orange', alpha=0.6)
    ax2.add_patch(circ2); ax2.set_title("Figura B"); ax2.axis('off')
    return fig

def dibujar_hexagono_medida():
    fig, ax = plt.subplots(figsize=(3, 3))
    theta = np.linspace(0, 2*np.pi, 7, endpoint=True)
    x = np.cos(theta); y = np.sin(theta)
    ax.plot(x, y, color='purple', lw=3)
    ax.text(0, 0, "Lado = 5 cm", ha='center', fontweight='bold')
    ax.axis('off')
    return fig

def dibujar_triangulo_irregular():
    fig, ax = plt.subplots(figsize=(4, 2.5))
    pts = np.array([[0, 0], [4, 0], [1, 3]])
    t = patches.Polygon(pts, closed=True, facecolor='lightgreen', edgecolor='black')
    ax.add_patch(t)
    ax.text(2, -0.5, "12 m", ha='center'); ax.text(-0.5, 1.5, "10 m"); ax.text(3, 1.5, "8 m")
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 4); ax.axis('off')
    return fig

def dibujar_huerto():
    fig, ax = plt.subplots(figsize=(4, 2))
    rect = patches.Rectangle((0,0), 20, 5, facecolor='brown', alpha=0.5, edgecolor='black')
    ax.add_patch(rect)
    ax.text(10, 2.5, "Largo: 20m\nAncho: 5m", ha='center', va='center')
    ax.set_xlim(-1, 21); ax.set_ylim(-1, 6); ax.axis('off')
    return fig

def dibujar_quesito():
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie([10, 20, 50, 20], colors=['gold', 'green', 'red', 'blue'], startangle=90)
    ax.axis('equal')
    return fig

def dibujar_cuadrado_diagonal():
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.add_patch(patches.Rectangle((0,0), 1, 1, fill=False, lw=2))
    ax.plot([0, 1], [1, 0], 'b--', lw=2)
    ax.axis('off')
    return fig

# --- NUEVOS DIBUJOS (Preguntas 11-20) ---

def dibujar_triangulo_equilatero():
    fig, ax = plt.subplots(figsize=(3, 3))
    pts = np.array([[0, 0], [2, 0], [1, 1.73]])
    t = patches.Polygon(pts, color='cyan', ec='black', lw=2)
    ax.add_patch(t)
    # Marcas de igualdad
    ax.text(1, -0.2, "|", color='red', fontweight='bold', ha='center')
    ax.text(0.4, 0.9, "/", color='red', fontweight='bold')
    ax.text(1.6, 0.9, "\\", color='red', fontweight='bold')
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(-0.5, 2.5); ax.axis('off')
    return fig

def dibujar_lineas(tipo):
    fig, ax = plt.subplots(figsize=(3, 2))
    if tipo == 'paralelas':
        ax.plot([0, 3], [1, 1], 'k-', lw=2)
        ax.plot([0, 3], [2, 2], 'k-', lw=2)
    else:
        ax.plot([0, 3], [0, 2], 'k-', lw=2)
        ax.plot([0, 3], [2, 0], 'k-', lw=2)
    ax.axis('off')
    return fig

def dibujar_rombo():
    fig, ax = plt.subplots(figsize=(3, 3))
    pts = np.array([[1, 0], [2, 1], [1, 2], [0, 1]])
    p = patches.Polygon(pts, color='yellow', ec='black', lw=2)
    ax.add_patch(p)
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(-0.5, 2.5); ax.axis('off')
    return fig

def dibujar_reloj_300():
    fig, ax = plt.subplots(figsize=(3, 3))
    circ = patches.Circle((0,0), 1, fill=False, lw=2)
    ax.add_patch(circ)
    # Manecillas
    ax.arrow(0, 0, 0, 0.8, head_width=0.1, color='black') # 12
    ax.arrow(0, 0, 0.8, 0, head_width=0.1, color='black') # 3
    # Arco ángulo
    rect = patches.Rectangle((0,0), 0.3, 0.3, fill=False, ec='red')
    ax.add_patch(rect)
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.axis('off')
    return fig

def dibujar_radio_diametro():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
    # Radio
    ax1.add_patch(patches.Circle((0,0), 1, fill=False, lw=1))
    ax1.plot([0, 1], [0, 0], 'r-', lw=2)
    ax1.plot(0,0, 'ko')
    ax1.set_title("Línea A")
    ax1.axis('off')
    # Diámetro
    ax2.add_patch(patches.Circle((0,0), 1, fill=False, lw=1))
    ax2.plot([-1, 1], [0, 0], 'b-', lw=2)
    ax2.plot(0,0, 'ko')
    ax2.set_title("Línea B")
    ax2.axis('off')
    return fig

def dibujar_cuadrado_perimetro():
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.add_patch(patches.Rectangle((0,0), 2, 2, facecolor='pink', ec='black'))
    ax.text(1, 1, "Perímetro\nTOTAL = 20 cm", ha='center', va='center')
    ax.text(1, -0.3, "?", ha='center', fontsize=14, color='red')
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(-0.5, 2.5); ax.axis('off')
    return fig

# ==========================================
#              INICIO DEL EXAMEN
# ==========================================

# --- PARTE 1: VOCABULARIO Y CONCEPTOS (1-3) ---
st.header("1. Conceptos Básicos")
c1, c2 = st.columns([1, 2])
with c1: st.pyplot(dibujar_elementos_poligono())
with c2:
    respuestas['p1'] = st.selectbox("1. Los puntos rojos son:", ["", "Lados", "Vértices", "Radios"], key='k1')
    respuestas['p2'] = st.text_input("2. Un polígono de 7 lados se llama:", key='k2').lower().strip()

st.divider()

c3, c4 = st.columns(2)
with c3: st.pyplot(dibujar_circulo_circunferencia())
with c4:
    respuestas['p3'] = st.radio("3. ¿Cuál es la Circunferencia?", ["Figura A", "Figura B"], key='k3')

st.divider()

# --- PARTE 2: ÁNGULOS Y LÍNEAS (4-7) ---
st.header("2. Ángulos y Líneas")

col_ang, col_rel = st.columns(2)
with col_ang:
    st.write("4. Clasifica estos ángulos:")
    respuestas['p4_a'] = st.selectbox("Menos de 90º:", ["Agudo", "Recto", "Obtuso"], key='k4a')
    respuestas['p4_b'] = st.selectbox("Exactamente 90º:", ["Agudo", "Recto", "Obtuso"], key='k4b')
with col_rel:
    st.pyplot(dibujar_reloj_300())
    respuestas['p5'] = st.radio("5. ¿Qué ángulo forman las agujas a las 3:00?", ["Agudo", "Recto", "Obtuso"], key='k5')

st.divider()

c5, c6 = st.columns(2)
with c5: st.pyplot(dibujar_lineas('paralelas'))
with c6:
    respuestas['p6'] = st.radio("6. Estas líneas que nunca se cruzan son:", ["Secantes", "Paralelas", "Perpendiculares"], key='k6')

st.divider()

st.write("7. Si un ángulo mide 120º, ¿qué tipo de ángulo es?")
respuestas['p7'] = st.selectbox("Respuesta:", ["Agudo", "Recto", "Obtuso"], key='k7')

st.divider()

# --- PARTE 3: POLÍGONOS Y CLASIFICACIÓN (8-13) ---
st.header("3. Clasificación de Polígonos")

c7, c8 = st.columns(2)
with c7: st.pyplot(dibujar_triangulo_equilatero())
with c8:
    st.write("8. Este triángulo tiene sus 3 lados iguales.")
    respuestas['p8'] = st.selectbox("¿Cómo se llama?", ["Isósceles", "Escaleno", "Equilátero"], key='k8')

c9, c10 = st.columns(2)
with c9: st.pyplot(dibujar_rombo())
with c10:
    st.write("9. Esta figura es un cuadrilátero.")
    respuestas['p9'] = st.radio("¿Qué nombre recibe?", ["Trapecio", "Rombo", "Rectángulo"], key='k9')

st.write("10. Verdadero o Falso: 'Para ser Regular, solo importa que los lados sean iguales'.")
respuestas['p10'] = st.radio("Respuesta:", ["Verdadero", "Falso"], key='k10')

c11, c12, c13 = st.columns(3)
with c11: respuestas['p11'] = st.text_input("11. Polígono de 9 lados:", key='k11').lower().strip()
with c12: respuestas['p12'] = st.text_input("12. Polígono de 10 lados:", key='k12').lower().strip()
with c13: respuestas['p13'] = st.number_input("13. ¿Cuántos vértices tiene un Octógono?", min_value=0, step=1, key='k13')

st.divider()

# --- PARTE 4: ELEMENTOS DEL CÍRCULO (14) ---
st.header("4. Dentro del Círculo")
c14, c15 = st.columns([1, 1])
with c14: st.pyplot(dibujar_radio_diametro())
with c15:
    st.write("14. Observa las líneas A (roja) y B (azul).")
    respuestas['p14_a'] = st.selectbox("La línea Roja (del centro al borde) es:", ["Radio", "Diámetro", "Cuerda"], key='k14a')
    respuestas['p14_b'] = st.selectbox("La línea Azul (lado a lado por el centro) es:", ["Radio", "Diámetro"], key='k14b')

st.divider()

# --- PARTE 5: PERÍMETROS (15-18) ---
st.header("5. Cálculo de Perímetros")

# Directo
c16, c17 = st.columns(2)
with c16: st.pyplot(dibujar_hexagono_medida())
with c17:
    st.write("15. Hexágono Regular (6 lados). Lado = 5 cm.")
    respuestas['p15'] = st.number_input("Perímetro (cm):", key='k15')

# Irregular
c18, c19 = st.columns(2)
with c18: st.pyplot(dibujar_triangulo_irregular())
with c19:
    st.write("16. Finca triangular (10, 12, 8).")
    respuestas['p16'] = st.number_input("Perímetro Total (m):", key='k16')

# Problema
st.write("17. Vallar el huerto (Largo 20m, Ancho 5m).")
respuestas['p17'] = st.number_input("Metros totales de valla:", key='k17')

# Inverso (Nuevo)
c20, c21 = st.columns(2)
with c20: st.pyplot(dibujar_cuadrado_perimetro())
with c21:
    st.write("18. ¡Reto! Sabemos que el perímetro TOTAL es 20 cm.")
    st.write("Como es un cuadrado, tiene 4 lados iguales.")
    respuestas['p18'] = st.number_input("¿Cuánto mide UN solo lado?", key='k18')

st.divider()

# --- PARTE 6: GRÁFICOS Y FIGURAS (19-20) ---
st.header("6. Gráficos y Lógica")

c22, c23 = st.columns(2)
with c22: st.pyplot(dibujar_quesito())
with c23:
    respuestas['p19'] = st.radio("19. El sector ROJO es el más grande. Eso significa:", 
                                ["Que hay menos cantidad.", "Que hay más cantidad.", "Que son iguales."], key='k19')

c24, c25 = st.columns(2)
with c24: st.pyplot(dibujar_cuadrado_diagonal())
with c25:
    respuestas['p20'] = st.selectbox("20. Al trazar la diagonal, ¿qué dos figuras se crean?", 
                                    ["Rectángulos", "Triángulos", "Círculos"], key='k20')

st.divider()

# --- CORRECCIÓN FINAL ---
if st.button("✅ CORREGIR EXAMEN (20 Puntos)", type="primary"):
    score = 0
    st.balloons()
    st.write("### Resultados Detallados:")

    # 1-3
    if respuestas['p1'] == "Vértices": score+=1
    if "hepta" in respuestas['p2'] or "heptágono" in respuestas['p2']: score+=1
    if respuestas['p3'] == "Figura A": score+=1
    
    # 4-7
    if respuestas['p4_a'] == "Agudo" and respuestas['p4_b'] == "Recto": score+=1
    else: st.error("Fallo en pregunta 4 (Ángulos).")
    
    if respuestas['p5'] == "Recto": score+=1
    else: st.error("Fallo en pregunta 5 (Reloj).")
    
    if respuestas['p6'] == "Paralelas": score+=1
    else: st.error("Fallo en pregunta 6 (Líneas).")
    
    if respuestas['p7'] == "Obtuso": score+=1
    else: st.error("Fallo en pregunta 7 (>90º es Obtuso).")

    # 8-13
    if respuestas['p8'] == "Equilátero": score+=1
    else: st.error("Fallo en pregunta 8 (Triángulo).")
    
    if respuestas['p9'] == "Rombo": score+=1
    else: st.error("Fallo en pregunta 9 (Figura amarilla).")
    
    if respuestas['p10'] == "Falso": score+=1
    else: st.error("Fallo en pregunta 10 (Deben tener también ángulos iguales).")
    
    if "enea" in respuestas['p11']: score+=1
    if "deca" in respuestas['p12']: score+=1
    if respuestas['p13'] == 8: score+=1
    else: st.error("Fallo en pregunta 13 (Octógono = 8).")

    # 14
    if respuestas['p14_a'] == "Radio" and respuestas['p14_b'] == "Diámetro": score+=1
    else: st.error("Fallo en pregunta 14 (Radio vs Diámetro).")

    # 15-18
    if respuestas['p15'] == 30: score+=1
    if respuestas['p16'] == 30: score+=1
    if respuestas['p17'] == 50: score+=1
    if respuestas['p18'] == 5: score+=1 # 20 / 4 = 5
    else: st.error("Fallo en pregunta 18 (Reto inverso: 20 entre 4 es 5).")

    # 19-20
    if "más cantidad" in respuestas['p19']: score+=1
    if respuestas['p20'] == "Triángulos": score+=1

    # NOTA
    st.markdown(f"# TU NOTA: {score} / 20")
    if score >= 18: st.success("¡SOBRESALIENTE! 🌟")
    elif score >= 10: st.info("¡APROBADO! 👍")
    else: st.error("Hay que repasar un poco más.")