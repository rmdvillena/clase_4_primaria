import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations # Para comparar todos los pares

# Configuración de la página
st.set_page_config(layout="wide", page_title="Dibujo de Múltiples Líneas")

st.title("🖌️ Creador de 4 Líneas Interactivas")
st.write("Define dos puntos para cada una de las 4 líneas. La aplicación analizará la relación entre todos los pares.")

# --- BARRA LATERAL (CONTROLES) ---
st.sidebar.header("⚙️ Definir Puntos de las Líneas")

# --- Funciones Helper ---

def calcular_parametros_linea(x1, y1, x2, y2):
    """Calcula la pendiente (m) y la intersección Y (b) de una línea dados dos puntos."""
    if abs(x2 - x1) < 1e-6:  # Línea vertical
        return float('inf'), x1  # Pendiente infinita, y la intersección "b" sería el valor x
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def generar_puntos_linea(m, b, x_range):
    """Genera puntos (y) para graficar una línea dado un rango x."""
    y_vals = m * x_range + b
    return x_range, y_vals

def plot_linea_en_ejes(ax, m, b, p1x, p1y, p2x, p2y, color, estilo, etiqueta):
    """Dibuja una línea (incluyendo verticales) y sus puntos en los ejes de matplotlib."""
    if m == float('inf'): # Línea vertical
        ax.axvline(b, color=color, linestyle=estilo, lw=2, label=f'{etiqueta}: x = {b:.2f}')
    else:
        x_canvas = np.linspace(-10, 10, 400)
        y_canvas = m * x_canvas + b
        ax.plot(x_canvas, y_canvas, color=color, linestyle=estilo, lw=2, label=f'{etiqueta}: y = {m:.2f}x + {b:.2f}')
    # Dibuja los puntos de control
    ax.plot([p1x, p2x], [p1y, p2y], 'o', color=color, markersize=6)

def analizar_relacion(m1, b1, m2, b2, tol=1e-2):
    """Compara dos líneas y devuelve una cadena con su relación."""
    es_linea1_vertical = (m1 == float('inf'))
    es_linea2_vertical = (m2 == float('inf'))

    if es_linea1_vertical and es_linea2_vertical:
        return "Coincidentes (Verticales)" if abs(b1 - b2) < tol else "Paralelas (Verticales)"
    
    elif es_linea1_vertical or es_linea2_vertical:
        m_no_vertical = m2 if es_linea1_vertical else m1
        if abs(m_no_vertical) < tol:
            return "Perpendiculares (Vertical/Horizontal)"
        else:
            return "Secantes"
            
    else: # Ninguna es vertical
        if abs(m1 - m2) < tol:
            return "Coincidentes" if abs(b1 - b2) < tol else "Paralelas"
        elif abs(m1 * m2 + 1) < tol:
            return "Perpendiculares"
        else:
            try:
                x_intersect = (b2 - b1) / (m1 - m2)
                y_intersect = m1 * x_intersect + b1
                return f"Secantes en ({x_intersect:.2f}, {y_intersect:.2f})"
            except ZeroDivisionError:
                return "Paralelas" # Debería ser capturado arriba, pero por si acaso


# --- Controles de la Barra Lateral (usando expanders) ---
lineas_params = []

with st.sidebar.expander("🔵 Línea 1 (Azul)", expanded=True):
    col_p1_x, col_p1_y = st.columns(2)
    p1_x1 = col_p1_x.slider("P1_X", -10.0, 10.0, -5.0, 0.1, key="p1_x1")
    p1_y1 = col_p1_y.slider("P1_Y", -10.0, 10.0, -2.0, 0.1, key="p1_y1")
    col_p2_x, col_p2_y = st.columns(2)
    p2_x1 = col_p2_x.slider("P2_X", -10.0, 10.0, 5.0, 0.1, key="p2_x1")
    p2_y1 = col_p2_y.slider("P2_Y", -10.0, 10.0, 3.0, 0.1, key="p2_y1")
    lineas_params.append(((p1_x1, p1_y1), (p2_x1, p2_y1)))

with st.sidebar.expander("🔴 Línea 2 (Roja)"):
    col_p1_x, col_p1_y = st.columns(2)
    p1_x2 = col_p1_x.slider("P1_X", -10.0, 10.0, -5.0, 0.1, key="p1_x2")
    p1_y2 = col_p1_y.slider("P1_Y", -10.0, 10.0, 0.0, 0.1, key="p1_y2")
    col_p2_x, col_p2_y = st.columns(2)
    p2_x2 = col_p2_x.slider("P2_X", -10.0, 10.0, 5.0, 0.1, key="p2_x2")
    p2_y2 = col_p2_y.slider("P2_Y", -10.0, 10.0, -5.0, 0.1, key="p2_y2")
    lineas_params.append(((p1_x2, p1_y2), (p2_x2, p2_y2)))

with st.sidebar.expander("🟢 Línea 3 (Verde)"):
    col_p1_x, col_p1_y = st.columns(2)
    p1_x3 = col_p1_x.slider("P1_X", -10.0, 10.0, -3.0, 0.1, key="p1_x3")
    p1_y3 = col_p1_y.slider("P1_Y", -10.0, 10.0, -5.0, 0.1, key="p1_y3")
    col_p2_x, col_p2_y = st.columns(2)
    p2_x3 = col_p2_x.slider("P2_X", -10.0, 10.0, 3.0, 0.1, key="p2_x3")
    p2_y3 = col_p2_y.slider("P2_Y", -10.0, 10.0, 5.0, 0.1, key="p2_y3")
    lineas_params.append(((p1_x3, p1_y3), (p2_x3, p2_y3)))

with st.sidebar.expander("🟠 Línea 4 (Naranja)"):
    col_p1_x, col_p1_y = st.columns(2)
    p1_x4 = col_p1_x.slider("P1_X", -10.0, 10.0, -8.0, 0.1, key="p1_x4")
    p1_y4 = col_p1_y.slider("P1_Y", -10.0, 10.0, 8.0, 0.1, key="p1_y4")
    col_p2_x, col_p2_y = st.columns(2)
    p2_x4 = col_p2_x.slider("P2_X", -10.0, 10.0, 8.0, 0.1, key="p2_x4")
    p2_y4 = col_p2_y.slider("P2_Y", -10.0, 10.0, 8.0, 0.1, key="p2_y4")
    lineas_params.append(((p1_x4, p1_y4), (p2_x4, p2_y4)))

# --- LÓGICA PRINCIPAL Y GRÁFICOS ---
col_grafica, col_explicacion = st.columns([2, 1])

# Calcular los parámetros m y b para todas las líneas
params_mb = []
for (p1, p2) in lineas_params:
    m, b = calcular_parametros_linea(p1[0], p1[1], p2[0], p2[1])
    params_mb.append((m, b))

# --- Gráfica ---
with col_grafica:
    st.subheader("Gráfica de Líneas")
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Propiedades de las líneas
    colores = ['blue', 'red', 'green', 'orange']
    estilos = ['-', '--', ':', '-.']
    etiquetas = ['Línea 1', 'Línea 2', 'Línea 3', 'Línea 4']

    # Dibujar cada línea
    for i in range(4):
        m, b = params_mb[i]
        p1, p2 = lineas_params[i]
        plot_linea_en_ejes(ax, m, b, p1[0], p1[1], p2[0], p2[1], colores[i], estilos[i], etiquetas[i])

    # Configuración de los ejes y la cuadrícula
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.axhline(0, color='black', linewidth=0.5) # Eje X
    ax.axvline(0, color='black', linewidth=0.5) # Eje Y
    ax.grid(True, linestyle=':')
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_aspect('equal', adjustable='box') # Clave para ver perpendicularidad
    ax.legend()
    ax.set_title("Líneas en el Plano Cartesiano")
    
    st.pyplot(fig)


# --- Detección y Explicación de la Relación ---
with col_explicacion:
    st.subheader("📊 Análisis de Relaciones")
    st.write("Comparación de todos los pares de líneas:")

    emojis_color = ["🔵", "🔴", "🟢", "🟠"]
    
    # Iterar sobre todas las combinaciones únicas de 2 líneas
    # (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
    for (i, j) in combinations(range(4), 2):
        m_i, b_i = params_mb[i]
        m_j, b_j = params_mb[j]
        
        # Generar el título de la comparación
        st.markdown(f"---")
        st.markdown(f"**{etiquetas[i]} {emojis_color[i]} vs {etiquetas[j]} {emojis_color[j]}**")
        
        # Obtener el análisis
        relacion = analizar_relacion(m_i, b_i, m_j, b_j)
        
        # Mostrar el resultado con un formato bonito
        if "Perpendiculares" in relacion:
            st.success(f"📐 {relacion}")
        elif "Paralelas" in relacion:
            st.warning(f"↔️ {relacion}")
        elif "Coincidentes" in relacion:
            st.info(f"👯‍♀️ {relacion}")
        else: # Secantes
            st.write(f"✂️ {relacion}")