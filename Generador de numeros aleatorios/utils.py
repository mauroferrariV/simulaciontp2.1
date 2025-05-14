import sys
import matplotlib.pyplot as plt
import numpy as np
import math

def mostrar_mapa_de_bits(bits, titulo = "Mapa de Bits"):
    total_bits = len(bits)
    ancho = int(math.sqrt(total_bits))
    alto = total_bits // ancho
    largo = ancho * alto
    bits = bits[:largo]  # recortamos el sobrante para que sea divisible
    
    array = np.array([int(b) for b in bits]).reshape((alto, ancho))

    plt.imshow(array, cmap="binary", interpolation="nearest")
    plt.title(titulo)
    plt.axis('off')
    plt.show()
    
def numeros_a_bits(numeros, bits_por_numero=16):
    bits = ""
    for num in numeros:
        binario = bin(num)[2:].zfill(bits_por_numero)
        bits += binario
    return bits