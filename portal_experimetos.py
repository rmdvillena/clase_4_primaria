import streamlit as st
import plotly.graph_objects as go

# --- Configuración de la página ---
st.set_page_config(page_title="Laboratorio Atmosférico Total", page_icon="🧑‍🔬", layout="centered")

# --- Estado de la sesión para guardar los valores de los gases ---
# Se inicia con la composición real de la Tierra
if 'gas_values' not in st.session_state:
    st.session_state.gas_values = {
        "n2": 78.1,
        "o2": 20.9,
        "ar": 0.9,
        "co2": 0.1
    }

# --- Título ---
st.title("🧪 Laboratorio Atmosférico: Control Total")
st.write("""
¡Bienvenido al panel de control avanzado! Ahora tienes el poder de ajustar la proporción de **todos los gases principales** de la atmósfera. Observa cómo un pequeño cambio en un gas obliga a los otros a ajustarse.
""")

st.markdown("---")

# --- Panel de Control ---
st.header("🕹️ Panel de Control Atmosférico")

# Guardar los valores anteriores para saber cuál ha cambiado
old_values = st.session_state.gas_values.copy()

# --- Sliders para cada gas ---
n2_level = st.slider("Nitrógeno (N₂) [%]", 0.0, 100.0, st.session_state.gas_values["n2"], 0.1)
o2_level = st.slider("Oxígeno (O₂) [%]", 0.0, 100.0, st.session_state.gas_values["o2"], 0.1)
ar_level = st.slider("Argón (Ar) [%]", 0.0, 100.0, st.session_state.gas_values["ar"], 0.1)
co2_level = st.slider("CO₂ y Otros Gases [%]", 0.0, 100.0, st.session_state.gas_values["co2"], 0.1)

# Diccionario con los nuevos valores
new_values = {"n2": n2_level, "o2": o2_level, "ar": ar_level, "co2": co2_level}

# --- Lógica de ajuste automático para mantener el 100% ---
changed_gas = None
for gas, value in new_values.items():
    if abs(value - old_values[gas]) > 0.01: # Comparación con tolerancia para flotantes
        changed_gas = gas
        break

if changed_gas:
    current_total = sum(new_values.values())
    diff = 100.0 - current_total
    
    other_gases_total = sum(value for gas, value in old_values.items() if gas != changed_gas)
    
    for gas, value in new_values.items():
        if gas != changed_gas:
            if other_gases_total > 0:
                proportion = old_values[gas] / other_gases_total
                new_values[gas] += diff * proportion
            if new_values[gas] < 0:
                new_values[gas] = 0

    final_total = sum(new_values.values())
    if final_total > 0:
        for gas in new_values:
            new_values[gas] = (new_values[gas] / final_total) * 100
    
    st.session_state.gas_values = new_values
    # --- CORRECCIÓN IMPORTANTE AQUÍ ---
    # Se reemplaza st.experimental_rerun() por st.rerun()
    st.rerun()


# --- El "Frasco de Gases" Visual ---
st.subheader("Composición del Aire Resultante")

labels = ['Nitrógeno (N₂)', 'Oxígeno (O₂)', 'Argón (Ar)', 'CO₂ y Otros']
values = list(st.session_state.gas_values.values())
colors = ['#636EFA', '#00CC96', '#AB63FA', '#EF553B']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, textinfo='label+percent', sort=False)])
fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)), textfont_size=14)
fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=400)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Panel de Diagnóstico Mejorado ---
st.header("🌎 Diagnóstico del Planeta")

o2 = st.session_state.gas_values["o2"]
co2 = st.session_state.gas_values["co2"]

# El orden de las condiciones es importante para dar el diagnóstico más crítico primero
if co2 > 5:
    st.error("""
    ### ❌ Diagnóstico: Atmósfera TÓXICA e INHABITABLE
    **Causa:** Efecto Invernadero Extremo por exceso de CO₂.
    **Análisis:** ¡Esta atmósfera es **letal**! El aire es irrespirable y el planeta se ha sobrecalentado a niveles de un horno. La vida es **imposible** en estas condiciones, similar a Venus.
    """)
elif o2 < 16:
    st.error("""
    ### ❌ Diagnóstico: Atmósfera IRRESPIRABLE
    **Causa:** Falta crítica de Oxígeno (Hipoxia severa).
    **Análisis:** ¡No hay suficiente oxígeno para respirar! Los animales se asfixiarían en cuestión de minutos. Esta atmósfera **no es apta para la vida** animal.
    """)
elif o2 > 35:
    st.warning("""
    ### ⚠️ Diagnóstico: Atmósfera PELIGROSAMENTE INFLAMABLE
    **Causa:** Exceso de Oxígeno (Hiperoxia).
    **Análisis:** Aunque parezca bueno, demasiado oxígeno es tóxico a largo plazo y convierte el ambiente en un polvorín. Una sola chispa podría causar incendios gigantescos e incontrolables. **Es una mezcla muy inestable.**
    """)
elif (18 <= o2 <= 23) and (co2 <= 1):
    st.success("""
    ### ✅ Diagnóstico: Atmósfera ÓPTIMA para la Vida
    **Análisis:** ¡Equilibrio perfecto! Esta es la receta de un planeta sano y vibrante. El oxígeno es ideal para la vida animal, el CO₂ mantiene una temperatura agradable y el nitrógeno actúa como un gas estabilizador.
    """)
else:
    st.info("""
    ### 🌀 Diagnóstico: Atmósfera INESTABLE o DEGRADADA
    **Análisis:** Esta mezcla se desvía del equilibrio ideal. Puede que la vida sobreviva con dificultad, pero las condiciones no son buenas. El clima podría ser errático o el aire de mala calidad, causando estrés en plantas y animales. **No es una atmósfera saludable a largo plazo.**
    """)