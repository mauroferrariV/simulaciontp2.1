import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from test import *
from utils import *

def mid_square(seed, n, digits=4):
    """
    Genera n números pseudoaleatorios usando el método de los cuadrados medios.
    
    Parámetros:
    - seed: semilla inicial (entero).
    - n: cantidad de números a generar.
    - digits: cantidad de dígitos deseados en la semilla y en la salida.

    Retorna:
    - Una lista de números generados.
    """
    results = []
    current = seed

    for _ in range(n):
        square = str(current ** 2).zfill(2 * digits)
        mid = len(square) // 2
        current = int(square[mid - digits // 2 : mid + digits // 2])
        results.append(current)
    
    return results

if len(sys.argv) > 1:
    if sys.argv[1] != "-n":
        print("Uso: Python randomMidSquare.py -n <Cantidad de numeros a generar>")
        sys.exit(1)
    
    if len(sys.argv) > 2 and sys.argv[2].strip():
        cantidad_a_generar = int(sys.argv[2])
    else:
        cantidad_a_generar = 1000000
else:
    # Usar valores predeterminados si no se pasan argumentos
    cantidad_a_generar = 1000000

numeros = mid_square(seed=5731, n=cantidad_a_generar, digits=4)
bits = numeros_a_bits(numeros, bits_por_numero=16)

frecuencia = test_frecuencia_bits(bits)
chi2_resultado = test_chi_cuadrado(numeros)
sumas = test_sumas_acumuladas(bits)
rachas = test_rachas(bits)

# 4. Mostrar resultados
print("Test de Frecuencia:", frecuencia)
print("Test Chi Cuadrado:", chi2_resultado)
print("Test Sumas Acumuladas:", sumas)
print("Test de Rachas:", rachas)


mostrar_mapa_de_bits(bits,"Mapa de Bits - Método de los Cuadrados Medios") 