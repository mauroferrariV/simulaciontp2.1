import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from test import *
from utils import *

if len(sys.argv) > 1:
    if sys.argv[1] != "-n":
        print("Uso: Python randomGLC.py -n <Cantidad de numeros a generar>")
        sys.exit(1)
    
    if len(sys.argv) > 2 and sys.argv[2].strip():
        cantidad_a_generar = int(sys.argv[2])
    else:
        cantidad_a_generar = 1000
else:
    # Usar valores predeterminados si no se pasan argumentos
    cantidad_a_generar = 1000

def gcl(a, c, m, seed, n):
    """
    Genera n números usando el Generador Congruencial Lineal (GCL).

    X_{n+1} = (a * X_n + c) mod m
    """
    resultados = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        resultados.append(x)
    return resultados
  
a = 1
c = 332
m = 162222212399
seed = 1

# a = 1664525
# c = 1013904223
# m = 2**32
# seed = 1234

numeros = gcl(a, c, m, seed, cantidad_a_generar)
bits = numeros_a_bits(numeros, bits_por_numero=1)

frecuencia = test_frecuencia_bits(bits)
chi2_resultado = test_chi_cuadrado(numeros)
sumas = test_sumas_acumuladas(bits)
rachas = test_rachas(bits)

# 4. Mostrar resultados
print("Test de Frecuencia:", frecuencia)
print("Test Chi Cuadrado:", chi2_resultado)
print("Test Sumas Acumuladas:", sumas)
print("Test de Rachas:", rachas)

mostrar_mapa_de_bits(bits,"Mapa de Bits - Método GLC") 
