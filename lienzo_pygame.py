import pygame
import sys
import math
from itertools import combinations

# --- Funciones de Análisis (las mismas de antes) ---

def calcular_parametros_linea(x1, y1, x2, y2):
    """Calcula la pendiente (m) y la intersección Y (b) de una línea."""
    # Evitar división por cero si los puntos son idénticos
    if x2 == x1 and y2 == y1:
        return None, None # No es una línea
    
    if abs(x2 - x1) < 1e-6:  # Línea vertical
        return float('inf'), x1  # Pendiente infinita, b es el valor x
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def analizar_relacion(linea1, linea2, tol=1e-2):
    """Compara dos líneas y devuelve una cadena con su relación."""
    m1, b1 = linea1['params']
    m2, b2 = linea2['params']
    
    # Si alguna línea no es válida
    if m1 is None or m2 is None:
        return "Una línea no es válida"

    es_linea1_vertical = (m1 == float('inf'))
    es_linea2_vertical = (m2 == float('inf'))

    if es_linea1_vertical and es_linea2_vertical:
        return "Coincidentes (Verticales)" if abs(b1 - b2) < tol else "Paralelas (Verticales)"
    
    elif es_linea1_vertical or es_linea2_vertical:
        m_no_vertical = m2 if es_linea1_vertical else m1
        return "Perpendiculares (V/H)" if abs(m_no_vertical) < tol else "Secantes"
            
    else: # Ninguna es vertical
        if abs(m1 - m2) < tol:
            return "Coincidentes" if abs(b1 - b2) < tol else "Paralelas"
        elif abs(m1 * m2 + 1) < tol:
            return "Perpendiculares"
        else:
            return "Secantes"

def analizar_todas_las_lineas(lista_lineas):
    """Imprime el análisis de todos los pares de líneas en la consola."""
    print("\n--- 📊 ANÁLISIS DE LÍNEAS ---")
    if len(lista_lineas) < 2:
        print("Necesitas al menos 2 líneas para comparar.")
        return

    # Iterar sobre todas las combinaciones únicas de 2 líneas
    for (linea_i, linea_j) in combinations(lista_lineas, 2):
        relacion = analizar_relacion(linea_i, linea_j)
        print(f"  * {linea_i['nombre']} vs {linea_j['nombre']}: {relacion}")
    print("----------------------------\n")

# --- Configuración de Pygame ---
pygame.init()
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Lienzo para Pintar Líneas - Haz clic para dibujar")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
COLORES_LINEA = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 165, 0), (128, 0, 128)]

# Almacenamiento
lineas_dibujadas = [] # Lista para guardar los datos de las líneas
punto_inicio = None
contador_lineas = 0

# --- Bucle Principal del Juego ---
ejecutando = True
while ejecutando:
    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if punto_inicio is None:
                # Primer clic: Inicia la línea
                punto_inicio = evento.pos
            else:
                # Segundo clic: Termina la línea
                punto_fin = evento.pos
                
                # Calcular parámetros m y b
                m, b = calcular_parametros_linea(punto_inicio[0], punto_inicio[1], punto_fin[0], punto_fin[1])
                
                # Guardar la línea
                if m is not None:
                    contador_lineas += 1
                    nueva_linea = {
                        "nombre": f"Línea {contador_lineas}",
                        "puntos": (punto_inicio, punto_fin),
                        "params": (m, b),
                        "color": COLORES_LINEA[(contador_lineas - 1) % len(COLORES_LINEA)]
                    }
                    lineas_dibujadas.append(nueva_linea)
                    print(f"¡Línea {contador_lineas} añadida! ({punto_inicio} -> {punto_fin})")
                    
                    # Analizar todas las líneas
                    analizar_todas_las_lineas(lineas_dibujadas)
                
                # Reiniciar para la próxima línea
                punto_inicio = None

    # --- Lógica de Dibujo ---
    PANTALLA.fill(BLANCO) # Fondo blanco
    
    # Dibujar todas las líneas guardadas
    for linea in lineas_dibujadas:
        pygame.draw.line(PANTALLA, linea["color"], linea["puntos"][0], linea["puntos"][1], 3)
    
    # Dibujar el punto de inicio si existe
    if punto_inicio is not None:
        pygame.draw.circle(PANTALLA, NEGRO, punto_inicio, 5)
        # Opcional: dibujar línea hasta el cursor actual
        pygame.draw.line(PANTALLA, GRIS, punto_inicio, pygame.mouse.get_pos(), 1)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()