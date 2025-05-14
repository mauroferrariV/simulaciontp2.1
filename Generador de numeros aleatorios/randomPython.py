import sys
import time
from test import *
from utils import *
import matplotlib.pyplot as plt
import random
import math

if len(sys.argv) > 1:
    if sys.argv[1] != "-n":
        print("Uso: Python randomPython.py -n <Cantidad de numeros a generar>")
        sys.exit(1)
    
    if len(sys.argv) > 2 and sys.argv[2].strip():
        cantidad_a_generar = int(sys.argv[2])
    else:
        cantidad_a_generar = 1000
else:
    # Usar valores predeterminados si no se pasan argumentos
    cantidad_a_generar = 1000

def generar_random_bits(n, bits_por_numero=32):
    numeros = [int(random.random() * (2**bits_por_numero)) for _ in range(n)]
    bits = numeros_a_bits(numeros, bits_por_numero)
    return numeros, bits

[numeros, bits] = generar_random_bits(cantidad_a_generar)


frecuencia = test_frecuencia_bits(bits)
chi2_resultado = test_chi_cuadrado(numeros)
sumas = test_sumas_acumuladas(bits)
rachas = test_rachas(bits)

# 4. Mostrar resultados
print("Test de Frecuencia:", frecuencia)
print("Test Chi Cuadrado:", chi2_resultado)
print("Test Sumas Acumuladas:", sumas)
print("Test de Rachas:", rachas)

mostrar_mapa_de_bits(bits,"Mapa de Bits - Método Python") 
