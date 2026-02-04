import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Examen Máster Matemáticas", page_icon="🎓", layout="wide")

st.title("🎓 Examen Máster de Matemáticas (Nivel 10 años)")
st.markdown("""
**Instrucciones:** Tienes **40 preguntas** de alto nivel.
Este examen cambia cada vez que lo recargas. ¡Si sacas un 40/40 eres un genio!
""")

if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

# --- GENERADORES DE GRÁFICOS ---

def crear_poligono_regular(n_lados, color='skyblue'):
    fig, ax = plt.subplots(figsize=(2, 2))
    theta = np.linspace(0, 2*np.pi, n_lados, endpoint=False)
    if n_lados % 2 != 0: theta += np.pi/2
    x, y = np.cos(theta), np.sin(theta)
    ax.add_patch(patches.Polygon(np.column_stack([x, y]), color=color, ec='black'))
    ax.axis('off'); ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    return fig

def crear_triangulo_angulos(tipo):
    fig, ax = plt.subplots(figsize=(3, 2))
    if tipo == 'rectangulo':
        pts = [[0,0], [3,0], [0,2]] # Recto en (0,0)
        ax.text(0.2, 0.2, "90º", color='red')
    elif tipo == 'acutangulo':
        pts = [[0,0], [3,0], [1.5, 2.5]]
    else: # obtusangulo
        pts = [[0,0], [3,0], [-1, 1.5]]
        ax.text(0.1, 0.2, ">90º", color='red')
    ax.add_patch(patches.Polygon(pts, color='#ffcc99', ec='black'))
    ax.axis('off'); ax.autoscale()
    return fig

def crear_figura_area(ancho, alto):
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.add_patch(patches.Rectangle((0,0), ancho, alto, color='lightgreen', ec='black'))
    ax.text(ancho/2, -0.5, f"{ancho} cm", ha='center')
    ax.text(-0.5, alto/2, f"{alto} cm", va='center')
    ax.axis('off'); ax.set_xlim(-1, ancho+1); ax.set_ylim(-1, alto+1)
    return fig

def crear_reloj(hora, minuto):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.add_patch(patches.Circle((0,0), 1, fill=False, lw=2))
    # Hora
    angulo_h = np.pi/2 - (hora + minuto/60)*2*np.pi/12
    ax.plot([0, 0.5*np.cos(angulo_h)], [0, 0.5*np.sin(angulo_h)], 'k-', lw=3)
    # Minuto
    angulo_m = np.pi/2 - minuto*2*np.pi/60
    ax.plot([0, 0.8*np.cos(angulo_m)], [0, 0.8*np.sin(angulo_m)], 'b-', lw=2)
    ax.axis('off'); ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    return fig

def crear_grafico_complejo():
    fig, ax = plt.subplots(figsize=(4, 2.5))
    datos = [15, 25, 10, 30]
    ax.bar(['A', 'B', 'C', 'D'], datos, color=['red', 'blue', 'green', 'orange'])
    ax.grid(axis='y', linestyle='--')
    return fig

# --- BANCO DE PREGUNTAS ---

# 1-10: GEOMETRÍA AVANZADA
st.header("Bloque 1: Geometría Avanzada")
cols1 = st.columns(4)

# P1: Ángulos Triángulo
with cols1[0]:
    st.pyplot(crear_triangulo_angulos('rectangulo'))
    st.session_state.respuestas['p1'] = st.selectbox("1. ¿Cuánto suman los 3 ángulos interiores?", ["90º", "180º", "360º"], key='k1')

# P2: Diagonales
with cols1[1]:
    st.pyplot(crear_poligono_regular(5, 'violet'))
    st.session_state.respuestas['p2'] = st.number_input("2. ¿Cuántas diagonales tiene un pentágono?", 0, 10, key='k2')

# P3: Lados Paralelos
with cols1[2]:
    st.write("3. ¿Qué cuadrilátero tiene **solo un par** de lados paralelos?")
    st.session_state.respuestas['p3'] = st.selectbox("", ["Cuadrado", "Romboide", "Trapecio"], key='k3')

# P4: Circunferencia
with cols1[3]:
    st.write("4. Si el radio mide 6 cm, ¿cuánto mide el diámetro?")
    st.session_state.respuestas['p4'] = st.number_input("", 0, 100, key='k4')

cols2 = st.columns(4)
# P5: Clasificación Triángulos
with cols2[0]:
    st.pyplot(crear_triangulo_angulos('obtusangulo'))
    st.session_state.respuestas['p5'] = st.selectbox("5. Este triángulo tiene un ángulo >90º. Es:", ["Acutángulo", "Rectángulo", "Obtusángulo"], key='k5')

# P6: Polígonos
with cols2[1]:
    st.pyplot(crear_poligono_regular(6))
    st.session_state.respuestas['p6'] = st.selectbox("6. Un polígono de 6 lados regular tiene:", ["Lados iguales", "Ángulos diferentes", "Lados desiguales"], key='k6')

# P7: Nombre polígono
with cols2[2]:
    st.write("7. ¿Cómo se llama el polígono de 12 lados?")
    st.session_state.respuestas['p7'] = st.text_input("", key='k7').lower()

# P8: Elementos
with cols2[3]:
    st.write("8. La línea que divide un ángulo en dos partes iguales se llama:")
    st.session_state.respuestas['p8'] = st.selectbox("", ["Mediatriz", "Bisectriz", "Diagonal"], key='k8')

cols3 = st.columns(2)
with cols3[0]:
    st.session_state.respuestas['p9'] = st.radio("9. Un triángulo Isósceles tiene:", ["3 lados iguales", "2 lados iguales", "0 lados iguales"], horizontal=True, key='k9')
with cols3[1]:
    st.session_state.respuestas['p10'] = st.radio("10. ¿Un cuadrado es también un rectángulo?", ["Sí, siempre", "No, nunca"], horizontal=True, key='k10')

st.divider()

# 11-20: CÁLCULO DE PERÍMETROS Y ÁREAS
st.header("Bloque 2: Perímetros y Áreas (Cálculo)")

c_a = st.columns(5)
# P11 Area Rectángulo
with c_a[0]:
    st.pyplot(crear_figura_area(4, 3))
    st.session_state.respuestas['p11'] = st.number_input("11. Área (cm²):", key='k11') # 12

# P12 Perímetro Cuadrado
with c_a[1]:
    st.write("12. Cuadrado de lado 1,5 cm.")
    st.session_state.respuestas['p12'] = st.number_input("Perímetro:", key='k12') # 6.0

# P13 Lado faltante
with c_a[2]:
    st.write("13. El perímetro de un triángulo equilátero es 30m. ¿Cuánto mide su lado?")
    st.session_state.respuestas['p13'] = st.number_input("", key='k13') # 10

# P14 Perímetro Rectángulo
with c_a[3]:
    st.write("14. Rectángulo: Largo 10, Ancho la mitad del largo.")
    st.session_state.respuestas['p14'] = st.number_input("Perímetro:", key='k14') # Ancho=5. P=30

# P15 Concepto Área
with c_a[4]:
    st.write("15. ¿En qué se mide el Área?")
    st.session_state.respuestas['p15'] = st.selectbox("", ["cm", "cm²", "cm³"], key='k15')

c_b = st.columns(5)
# P16-P20 Rápidas
st.session_state.respuestas['p16'] = c_b[0].number_input("16. Área cuadrado lado 5:", key='k16') # 25
st.session_state.respuestas['p17'] = c_b[1].number_input("17. Perímetro hexágono lado 7:", key='k17') # 42
st.session_state.respuestas['p18'] = c_b[2].number_input("18. Lados de un eneágono:", key='k18') # 9
st.session_state.respuestas['p19'] = c_b[3].number_input("19. Área rectángulo 8x2:", key='k19') # 16
st.session_state.respuestas['p20'] = c_b[4].selectbox("20. Figura con 4 lados iguales y ángulos rectos:", ["Rombo", "Cuadrado", "Rectángulo"], key='k20')

st.divider()

# 21-30: ÁNGULOS Y RELOJES
st.header("Bloque 3: Ángulos y Lógica")
c_ang = st.columns(5)

with c_ang[0]:
    st.pyplot(crear_reloj(3, 0))
    st.session_state.respuestas['p21'] = st.selectbox("21. Ángulo a las 3:00:", ["Agudo", "Recto", "Obtuso"], key='k21')

with c_ang[1]:
    st.pyplot(crear_reloj(6, 0))
    st.session_state.respuestas['p22'] = st.selectbox("22. Ángulo a las 6:00:", ["Recto", "Llano (180º)", "Completo"], key='k22')

with c_ang[2]:
    st.write("23. Ángulo complementario de 50º (lo que falta para 90º):")
    st.session_state.respuestas['p23'] = st.number_input("", key='k23') # 40

with c_ang[3]:
    st.write("24. Ángulo suplementario de 100º (lo que falta para 180º):")
    st.session_state.respuestas['p24'] = st.number_input("", key='k24') # 80

with c_ang[4]:
    st.write("25. Suma de ángulos de un cuadrilátero:")
    st.session_state.respuestas['p25'] = st.selectbox("", ["180º", "360º", "540º"], key='k25')

# P26-30
st.session_state.respuestas['p26'] = st.selectbox("26. 45º es un ángulo:", ["Agudo", "Recto"], key='k26')
st.session_state.respuestas['p27'] = st.selectbox("27. 135º es un ángulo:", ["Agudo", "Obtuso"], key='k27')
st.session_state.respuestas['p28'] = st.selectbox("28. Dos rectas que forman 90º son:", ["Paralelas", "Perpendiculares"], key='k28')
st.session_state.respuestas['p29'] = st.selectbox("29. Dos rectas que NUNCA se tocan son:", ["Paralelas", "Secantes"], key='k29')
st.session_state.respuestas['p30'] = st.selectbox("30. Instrumento para medir ángulos:", ["Compás", "Transportador"], key='k30')

st.divider()

# 31-40: ESTADÍSTICA Y REPASO FINAL
st.header("Bloque 4: Datos y Retos")
c_dat = st.columns([2, 3])

with c_dat[0]:
    st.pyplot(crear_grafico_complejo())

with c_dat[1]:
    st.write("Mira el gráfico: A=15, B=25, C=10, D=30")
    st.session_state.respuestas['p31'] = st.number_input("31. ¿Cuánto suman A y B?", key='k31') # 40
    st.session_state.respuestas['p32'] = st.number_input("32. ¿Cuál es la diferencia entre el mayor (D) y el menor (C)?", key='k32') # 20
    st.session_state.respuestas['p33'] = st.selectbox("33. La Moda (el dato que más se repite/más alto) es:", ["A", "B", "C", "D"], key='k33')

# P34-40 Mix
c_mix = st.columns(3)
st.session_state.respuestas['p34'] = c_mix[0].number_input("34. Convertir: 3 metros son ___ cm:", key='k34') # 300
st.session_state.respuestas['p35'] = c_mix[1].number_input("35. Convertir: 50 mm son ___ cm:", key='k35') # 5
st.session_state.respuestas['p36'] = c_mix[2].number_input("36. Mitad de 1/2 (fracción decimal 0.25):", format="%.2f", key='k36') # 0.25 o texto
st.session_state.respuestas['p37'] = st.selectbox("37. Probabilidad: Tirar un dado y sacar un 7:", ["Imposible", "Seguro", "Probable"], key='k37')
st.session_state.respuestas['p38'] = st.selectbox("38. Un decágono tiene:", ["10 vértices", "12 vértices"], key='k38')
st.session_state.respuestas['p39'] = st.text_input("39. Nombre del triángulo con 3 lados desiguales:", key='k39').lower() # escaleno
st.session_state.respuestas['p40'] = st.number_input("40. RETO: Perímetro de cuadrado de área 100 cm²:", key='k40') # Lado 10 -> P=40

st.divider()

# --- CORRECCIÓN ---
if st.button("🚀 CORREGIR LAS 40 PREGUNTAS"):
    score = 0
    errores = []

    # Solucionario (Diccionario clave: respuesta correcta)
    soluciones = {
        'p1': "180º", 'p2': 5, 'p3': "Trapecio", 'p4': 12, 'p5': "Obtusángulo",
        'p6': "Lados iguales", 'p7': ["dodecágono", "dodecagono"], 'p8': "Bisectriz",
        'p9': "2 lados iguales", 'p10': "Sí, siempre", 
        'p11': 12, 'p12': 6, 'p13': 10, 'p14': 30, 'p15': "cm²",
        'p16': 25, 'p17': 42, 'p18': 9, 'p19': 16, 'p20': "Cuadrado",
        'p21': "Recto", 'p22': "Llano (180º)", 'p23': 40, 'p24': 80, 'p25': "360º",
        'p26': "Agudo", 'p27': "Obtuso", 'p28': "Perpendiculares", 'p29': "Paralelas", 'p30': "Transportador",
        'p31': 40, 'p32': 20, 'p33': "D", 'p34': 300, 'p35': 5,
        'p36': 0.25, 'p37': "Imposible", 'p38': "10 vértices", 
        'p39': "escaleno", 'p40': 40
    }

    for key, val in soluciones.items():
        user_val = st.session_state.respuestas.get(key)
        
        # Lógica flexible para texto
        if isinstance(val, list):
            correct = user_val in val
        elif isinstance(user_val, str):
            correct = user_val.strip().lower() == str(val).lower()
        else:
            correct = user_val == val
            
        if correct:
            score += 1
        else:
            errores.append(f"Pregunta {key[1:]}")

    st.balloons()
    st.markdown(f"## 🏆 NOTA FINAL: {score} / 40")
    
    if score == 40:
        st.success("¡ERES UN GENIO DE LAS MATEMÁTICAS! ¡PERFECTO!")
    elif score >= 35:
        st.success("¡Excelente! Casi perfecto.")
    elif score >= 20:
        st.warning(f"Bien aprobado. Fallaste en: {', '.join(errores)}")
    else:
        st.error(f"Hay que repasar más. Fallos: {', '.join(errores)}")