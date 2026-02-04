import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

# --- 1. FUNCIONES LÓGICAS (Inglés Estándar) ---
def time_to_english(hour, minute):
    numbers = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 20: "twenty", 25: "twenty-five"
    }
    
    # Ajustar la hora actual y la siguiente
    display_hour = hour % 12
    if display_hour == 0: display_hour = 12
    
    next_hour = (hour + 1) % 12
    if next_hour == 0: next_hour = 12

    # Lógica exacta para intervalos de 5 minutos
    if minute == 0:
        return f"It's {numbers[display_hour]} o'clock"
    elif minute == 15:
        return f"It's quarter past {numbers[display_hour]}"
    elif minute == 30:
        return f"It's half past {numbers[display_hour]}"
    elif minute == 45:
        return f"It's quarter to {numbers[next_hour]}"
    
    elif minute < 30:
        # Para 5, 10, 20, 25 past
        return f"It's {numbers[minute]} past {numbers[display_hour]}"
    
    else:
        # Para 25, 20, 10, 5 to
        minutes_to = 60 - minute
        return f"It's {numbers[minutes_to]} to {numbers[next_hour]}"

def draw_clock(hour, minute):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Esfera
    circle = plt.Circle((0, 0), 1.05, color='#2c3e50', fill=False, linewidth=4)
    ax.add_artist(circle)
    
    # Números
    for i in range(1, 13):
        angle_rad = math.radians(90 - i * 30)
        ax.text(0.85 * math.cos(angle_rad), 0.85 * math.sin(angle_rad), 
                str(i), ha='center', va='center', fontsize=16, fontweight='bold', color='#34495e')

    # Marcas de minutos
    for i in range(60):
        angle_rad = math.radians(90 - i * 6)
        lw = 2 if i % 5 == 0 else 0.5
        ax.plot([0.95 * math.cos(angle_rad), 1.0 * math.cos(angle_rad)], 
                [0.95 * math.sin(angle_rad), 1.0 * math.sin(angle_rad)], color='black', linewidth=lw)

    # Manecillas
    minute_angle = 90 - (minute * 6)
    # La hora avanza proporcionalmente a los minutos
    hour_angle = 90 - (hour * 30) - (minute * 0.5)
    
    # Dibujar Hora
    ax.plot([0, 0.5 * math.cos(math.radians(hour_angle))], 
            [0, 0.5 * math.sin(math.radians(hour_angle))], 
            color='#e74c3c', linewidth=6, solid_capstyle='round')
    
    # Dibujar Minuto
    ax.plot([0, 0.8 * math.cos(math.radians(minute_angle))], 
            [0, 0.8 * math.sin(math.radians(minute_angle))], 
            color='#2980b9', linewidth=4, solid_capstyle='round')
    
    ax.plot([0], [0], marker='o', markersize=8, color='black')
    return fig

# --- 2. INTERFAZ ---
st.set_page_config(page_title="Clock Quiz", layout="centered")

# Estado Inicial
if 'quiz_hour' not in st.session_state:
    st.session_state.quiz_hour = 3
if 'quiz_minute' not in st.session_state:
    st.session_state.quiz_minute = 0

st.title("🇬🇧 What time is it?")

col_btn, col_empty = st.columns([1, 2])
with col_btn:
    # --- CAMBIO PRINCIPAL AQUÍ ---
    # range(0, 60, 5) genera: 0, 5, 10, 15, 20, 25, 30... 55
    if st.button("🎲 Nueva Hora (x5)", type="primary"):
        st.session_state.quiz_hour = np.random.randint(1, 13)
        st.session_state.quiz_minute = np.random.choice(range(0, 60, 5)) 
        st.rerun()

# Mostrar Reloj
col_fig_L, col_fig_C, col_fig_R = st.columns([1, 2, 1])
with col_fig_C:
    fig = draw_clock(st.session_state.quiz_hour, st.session_state.quiz_minute)
    st.pyplot(fig, use_container_width=True)

st.write("---")

# Respuesta
st.subheader("Tu turno:")
user_guess = st.text_input("Escribe la hora en inglés:", placeholder="Ej: It's quarter past...")

with st.expander("👁️ Ver Solución"):
    correct_text = time_to_english(st.session_state.quiz_hour, st.session_state.quiz_minute)
    digital_time = f"{st.session_state.quiz_hour:02d}:{st.session_state.quiz_minute:02d}"
    
    st.markdown(f"### 👉 {correct_text}")
    st.caption(f"(Digital: {digital_time})")
    
    if user_guess:
        # Normalizamos quitando espacios extra y mayúsculas para comparar mejor
        if user_guess.lower().strip() == correct_text.lower().strip():
            st.success("¡Perfecto! 🎉")
        else:
            st.info(f"Comprueba tu respuesta con la solución de arriba.")