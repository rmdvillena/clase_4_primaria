import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración
st.set_page_config(page_title="El Mapa del Tesoro (Economía)", page_icon="🗺️")

st.title("🗺️ Encuentra el Tesoro del Mercado")
st.markdown("""
¡Mira el gráfico de abajo!
* **Línea Roja (Demanda):** Son los niños. Si es barato, hay muchos. Si es caro, hay pocos.
* **Línea Azul (Oferta):** Eres tú (la fábrica). Si pagan mucho, quieres fabricar más.
* **TU MISIÓN:** Mueve el precio para encontrar el **"Punto Mágico"** donde las líneas se cruzan.
""")

# --- CONTROL DEL JUGADOR ---
st.sidebar.header("🎛️ Tu Control")
precio_actual = st.sidebar.slider("¿Qué precio pones?", 10, 100, 30, 5)

# --- MATEMÁTICAS DETRÁS DE LAS LÍNEAS ---
# Generamos una lista de precios del 0 al 110 para dibujar las líneas completas
rango_precios = list(range(0, 110, 5))

# 1. Curva de Demanda (Niños): Baja cuando sube el precio
# Formula: 200 niños menos 2 por cada dólar
datos_demanda = [max(0, 200 - (2 * p)) for p in rango_precios]

# 2. Curva de Oferta (Fábrica): Sube cuando sube el precio
# Formula: Fabricas 2 consolas por cada dólar que cuesta
datos_oferta = [2 * p for p in rango_precios]

# --- CÁLCULOS DEL JUGADOR ---
cantidad_demanda_actual = max(0, 200 - (2 * precio_actual))
cantidad_oferta_actual = 2 * precio_actual

# --- CREAR EL GRÁFICO DE LÍNEAS (PLOTLY) ---
fig = go.Figure()

# Línea Roja (Demanda)
fig.add_trace(go.Scatter(
    x=rango_precios, 
    y=datos_demanda,
    mode='lines',
    name='Niños (Compradores)',
    line=dict(color='red', width=4)
))

# Línea Azul (Oferta)
fig.add_trace(go.Scatter(
    x=rango_precios, 
    y=datos_oferta,
    mode='lines',
    name='Tu Tienda (Vendedor)',
    line=dict(color='blue', width=4)
))

# El Punto del Jugador (Tu situación actual)
fig.add_trace(go.Scatter(
    x=[precio_actual],
    y=[cantidad_oferta_actual],
    mode='markers+text',
    name='TU ESTÁS AQUÍ',
    marker=dict(color='green', size=20, symbol='star'),
    text=["TÚ"],
    textposition="top center"
))

# Configuración visual del gráfico
fig.update_layout(
    title="El Cruce de Oferta y Demanda",
    xaxis_title="Precio ($)",
    yaxis_title="Cantidad de Consolas",
    height=500,
    hovermode="x unified"
)

# Añadir una nota visual donde se cruzan (Equilibrio en Precio 50)
fig.add_annotation(
    x=50, y=100,
    text="¡PUNTO DE EQUILIBRIO!",
    showarrow=True,
    arrowhead=1,
    ax=0, ay=-40
)

st.plotly_chart(fig, use_container_width=True)

# --- EXPLICACIÓN DE LO QUE VE EL NIÑO ---
st.write("---")
col1, col2, col3 = st.columns(3)

col1.metric("Precio que pusiste", f"${precio_actual}")
col2.metric("Niños que quieren comprar", f"{cantidad_demanda_actual}")
col3.metric("Consolas que tú ofreces", f"{cantidad_oferta_actual}")

st.write("---")

# Lógica del resultado
if precio_actual == 50:
    st.balloons()
    st.success("🏆 **¡GANASTE! ¡ENCONTRASTE EL EQUILIBRIO!**")
    st.write("Mira el gráfico: Tu estrella verde está justo en la X donde se cruzan las líneas.")
    st.write("Vendes exactamente lo que la gente quiere. ¡Nadie se queda triste y no te sobra nada!")

elif precio_actual < 50:
    st.warning("📉 **Precio muy bajo**")
    st.write(f"Mira la **línea roja** está muy alta (muchos niños quieren comprar: {cantidad_demanda_actual}).")
    st.write(f"Pero tu **línea azul** está baja (fabricas poco porque es barato: {cantidad_oferta_actual}).")
    st.write("👉 **¡Sube el precio!** Tienes filas de gente esperando.")

else:
    st.error("📈 **Precio muy alto**")
    st.write(f"Mira la **línea azul** está muy alta (te emocionaste fabricando: {cantidad_oferta_actual}).")
    st.write(f"Pero la **línea roja** está por los suelos (nadie quiere pagar tanto: {cantidad_demanda_actual}).")
    st.write("👉 **¡Baja el precio!** Te vas a comer las consolas con patatas.")