import streamlit as st
import pydeck as pdk
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from urllib.request import urlopen

# --- Configuración de la página ---
st.set_page_config(page_title="Laboratorio de Tsunamis 🌊", page_icon="🔬", layout="wide")

# --- Función para crear el gráfico de altura ---
def crear_grafico_altura(altura_ola_metros):
    """Crea un gráfico visual de la altura de la ola comparada con una casa."""
    fig, ax = plt.subplots(figsize=(4, 6))

    # Definir la altura máxima del gráfico y las referencias
    max_altura_grafico = max(30, altura_ola_metros + 5)
    altura_casa = 7  # metros (aprox 2 pisos)
    altura_arbol = 12 # metros
    altura_persona = 1.8 # metros

    # Dibujar la ola como un gran rectángulo azul
    ax.add_patch(plt.Rectangle((0, 0), 1, altura_ola_metros, color='#0077be', alpha=0.7))
    ax.text(0.5, altura_ola_metros / 2, f"{altura_ola_metros:.1f}\nmetros",
            color="white", ha='center', va='center', fontsize=16, weight='bold')

    # Añadir imágenes de referencia para la escala
    try:
        # Cargar imágenes desde URLs
        url_casa = "https://i.imgur.com/s65EEaB.png"
        url_arbol = "https://i.imgur.com/fomRk7V.png"
        url_persona = "https://i.imgur.com/k6n2m9M.png"
        
        img_casa = plt.imread(urlopen(url_casa))
        img_arbol = plt.imread(urlopen(url_arbol))
        img_persona = plt.imread(urlopen(url_persona))

        # Añadir las imágenes al gráfico
        ax.add_artist(AnnotationBbox(OffsetImage(img_casa, zoom=0.15), (0.5, altura_casa / 2), frameon=False))
        ax.add_artist(AnnotationBbox(OffsetImage(img_arbol, zoom=0.1), (0.75, altura_arbol / 2), frameon=False))
        ax.add_artist(AnnotationBbox(OffsetImage(img_persona, zoom=0.03), (0.25, altura_persona / 2), frameon=False))
    except Exception as e:
        # Si las imágenes no cargan, poner texto
        ax.text(0.5, altura_casa / 2, "CASA\n(7m)", ha='center', va='center', fontsize=10)
        st.warning("No se pudieron cargar las imágenes de referencia.")

    # Limpiar y configurar el gráfico
    ax.set_ylim(0, max_altura_grafico)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_yticks(np.arange(0, max_altura_grafico, 5))
    ax.set_ylabel("Altura (metros)")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    return fig

# --- Datos de ubicaciones predefinidas ---
LOCATIONS = {
    "Fosa de Japón (2011)": {"lat": 38.3, "lon": 142.4},
    "Costa de Chile (1960)": {"lat": -38.29, "lon": -73.05},
    "Fosa de las Marianas": {"lat": 11.35, "lon": 142.2},
    "Cerca de Hawái": {"lat": 21.3, "lon": -157.8},
    "Modo Experto (Personalizado)": {"lat": 20.0, "lon": 150.0}
}

# --- Inicialización del estado de la sesión ---
if 'epicentro' not in st.session_state:
    st.session_state.epicentro = LOCATIONS["Fosa de Japón (2011)"]

# --- Título ---
st.title("🌊 Laboratorio de Tsunamis: ¡Tú Tienes el Control Total!")
st.write("Controla la ubicación, fuerza y profundidad de un maremoto. Al final, verás un gráfico que te mostrará qué tan alta sería la ola al llegar a la costa.")
st.markdown("---")

# --- División en dos columnas ---
col1, col2 = st.columns([1, 1.5])

# --- Columna 1: Controles ---
with col1:
    st.header("👇 PASO 1: La CAUSA")
    st.image("https://i.imgur.com/gC3gD1P.png", caption="El terremoto submarino (maremoto) empuja el agua.")
    st.markdown("---")

    st.header("📍 PASO 2: Elige el Epicentro")
    selected_location_name = st.selectbox("Elige una zona de epicentro:", list(LOCATIONS.keys()))
    
    if selected_location_name == "Modo Experto (Personalizado)":
        lat = st.number_input("Latitud:", -90.0, 90.0, st.session_state.epicentro['lat'], format="%.2f")
        lon = st.number_input("Longitud:", -180.0, 180.0, st.session_state.epicentro['lon'], format="%.2f")
        st.session_state.epicentro = {"lat": lat, "lon": lon}
    else:
        st.session_state.epicentro = LOCATIONS[selected_location_name]
    st.markdown("---")
    
    st.header("🕹️ PASO 3: Elige los Parámetros")
    magnitud = st.slider("Magnitud del Maremoto (fuerza):", 7.0, 9.5, 8.5, 0.1)
    profundidad = st.slider("Profundidad del Maremoto (km bajo el lecho marino):", 10, 300, 30, 5)

    impacto = magnitud * (1 - (profundidad / 350))
    st.subheader("Nivel de Amenaza del Tsunami:")
    # ... (código de diagnóstico de amenaza)
    # Placeholder para el gráfico de altura
    placeholder_grafico = st.empty()


# --- Columna 2: Mapa y simulación ---
with col2:
    st.header("👉 PASO 4: Observa el EFECTO")
    
    start_simulation = st.button("🌊 ¡Iniciar Simulación del Tsunami!")

    epicentro_lat = st.session_state.epicentro['lat']
    epicentro_lon = st.session_state.epicentro['lon']
    
    # ... (código del mapa y la simulación)
    # El código de la simulación del mapa no necesita cambios
    cities_df = pd.DataFrame({'name': ['Tokio', 'Honolulu', 'Lima', 'Sídney'], 'lat': [35.68, 21.31, -12.04, -33.86], 'lon': [139.76, -157.85, -77.04, 151.20], 'color': [[0, 0, 255, 200]] * 4})
    map_placeholder = st.empty()
    initial_view_state = pdk.ViewState(latitude=epicentro_lat, longitude=epicentro_lon, zoom=2, pitch=45)

    def draw_map(epicenter_data, wave_data, cities_data):
        # ... (código de la función draw_map sin cambios)
        epicenter_layer = pdk.Layer("ScatterplotLayer", data=epicenter_data, get_position="[lon, lat]", get_color="[255, 0, 0, 255]", get_radius=25000)
        wave_layer = pdk.Layer("ScatterplotLayer", data=wave_data, get_position="[lon, lat]", get_fill_color="color", get_radius="radius", get_line_color="line_color", get_line_width=20000)
        cities_layer = pdk.Layer("ScatterplotLayer", data=cities_data, get_position="[lon, lat]", get_fill_color="color", get_radius=80000, pickable=True)
        r = pdk.Deck(layers=[wave_layer, epicenter_layer, cities_layer], initial_view_state=initial_view_state, map_provider='carto', map_style='light', tooltip={"html": "<b>{name}</b>"})
        map_placeholder.pydeck_chart(r)

    if start_simulation:
        if impacto < 5.5: impacto_real = 0
        else: impacto_real = impacto

        max_reach_km = 1000 + (impacto_real - 5.0) * 1500
        if max_reach_km < 0: max_reach_km = 0
        wave_steps = 50
        
        for i in range(wave_steps + 1):
            # ... (código del bucle de simulación sin cambios)
            current_radius_km = (i / wave_steps) * max_reach_km
            intensity_ratio = max(0, 1 - (current_radius_km / max_reach_km))
            wave_alpha = int(120 * intensity_ratio)
            line_alpha = int(200 * intensity_ratio)
            wave_color = [0, 150, 255, wave_alpha]
            line_color = [0, 100, 255, line_alpha]
            wave_df = pd.DataFrame([{'lat': epicentro_lat, 'lon': epicentro_lon, 'radius': current_radius_km * 1000, 'color': wave_color, 'line_color': line_color}])
            cities_step_df = cities_df.copy()
            for index, city in cities_step_df.iterrows():
                dist_lat = np.radians(city.lat - epicentro_lat); dist_lon = np.radians(city.lon - epicentro_lon)
                a = np.sin(dist_lat/2)**2 + np.cos(np.radians(epicentro_lat)) * np.cos(np.radians(city.lat)) * np.sin(dist_lon/2)**2
                c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)); distance_km = 6371 * c
                if distance_km < current_radius_km:
                    cities_step_df.at[index, 'color'] = [255, 0, 0, 200]
            draw_map(pd.DataFrame([{'lat': epicentro_lat, 'lon': epicentro_lon}]), wave_df, cities_step_df)
            time.sleep(0.05)

        st.success(f"🎉 ¡Simulación completada!")
        
        # --- CÁLCULO Y VISUALIZACIÓN DEL GRÁFICO DE ALTURA ---
        with placeholder_grafico.container():
            st.subheader("Impacto en la Costa")
            # Fórmula para calcular la altura de la ola al llegar a la costa
            altura_costa = (impacto - 5.0) * 4.0
            if altura_costa < 1:
                st.write("La ola es demasiado pequeña para causar daños en la costa.")
            else:
                st.write(f"La ola llegaría a la costa con una altura máxima de **{altura_costa:.1f} metros**.")
                fig = crear_grafico_altura(altura_costa)
                st.pyplot(fig)
    else:
        initial_wave_df = pd.DataFrame([{'lat': epicentro_lat, 'lon': epicentro_lon, 'radius': 0, 'color': [0,0,0,0], 'line_color': [0,0,0,0]}])
        draw_map(pd.DataFrame([{'lat': epicentro_lat, 'lon': epicentro_lon}]), initial_wave_df, cities_df)