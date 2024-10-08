import random
import math
import time


# Función para calcular la distancia euclidiana entre dos puntos
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# Función que encuentra la menor distancia en un grupo pequeño de puntos (fuerza bruta)
def distancia_minima_fuerza_bruta(puntos):
    min_distancia = float('inf')
    par = None
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia(puntos[i], puntos[j])
            if dist < min_distancia:
                min_distancia = dist
                par = (puntos[i], puntos[j])
    return par, min_distancia


# Función que encuentra el par más cercano usando "divide y vencerás"
def distancia_minima(puntos):
    n = len(puntos)

    # Si hay pocos puntos, usar fuerza bruta
    if n <= 3:
        return distancia_minima_fuerza_bruta(puntos)

    # Dividir los puntos en dos mitades
    mitad = n // 2
    izquierda = puntos[:mitad]
    derecha = puntos[mitad:]

    # Hallar las distancias mínimas en ambas mitades
    par_izq, min_izq = distancia_minima(izquierda)
    par_der, min_der = distancia_minima(derecha)

    # Tomar el menor de las dos distancias
    if min_izq < min_der:
        d_min = min_izq
        par_min = par_izq
    else:
        d_min = min_der
        par_min = par_der

    # Considerar puntos cercanos a la línea divisoria
    puntos_en_franja = [p for p in puntos if abs(p[0] - puntos[mitad][0]) < d_min]

    # Ordenar puntos en la franja por la coordenada y
    puntos_en_franja.sort(key=lambda p: p[1])

    # Buscar la menor distancia entre los puntos en la franja
    n_franja = len(puntos_en_franja)
    for i in range(n_franja):
        for j in range(i + 1, min(i + 7, n_franja)):
            dist = distancia(puntos_en_franja[i], puntos_en_franja[j])
            if dist < d_min:
                d_min = dist
                par_min = (puntos_en_franja[i], puntos_en_franja[j])

    return par_min, d_min


# Función para generar puntos aleatorios
def generar_puntos(n):
    return [(random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(n)]


# Función para medir tiempo de ejecución
def medir_tiempo(n):
    puntos = generar_puntos(n)
    puntos.sort()  # Ordenamos los puntos por la coordenada x
    inicio = time.time()
    par, distancia_min = distancia_minima(puntos)
    fin = time.time()
    print(
        f"n = {n}, Tiempo de ejecución: {fin - inicio:.6f} segundos, Par más cercano: {par}, Distancia: {distancia_min:.6f}")


# Ejecutar el programa para diferentes tamaños de n
for n in [10, 100, 1000, 10000, 100000]:
    medir_tiempo(n)
