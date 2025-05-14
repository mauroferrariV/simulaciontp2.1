from collections import Counter
import numpy as np
from scipy.stats import chi2

def test_frecuencia_bits(bits):
    conteo = Counter(bits)
    total = len(bits)
    frecuencia_0 = conteo['0'] / total
    frecuencia_1 = conteo['1'] / total
    diferencia = abs(frecuencia_0 - frecuencia_1)

    resultado = "Pasa" if diferencia <= 0.05 else "No pasa"

    return {
        "frecuencia_0": frecuencia_0,
        "frecuencia_1": frecuencia_1,
        "diferencia": diferencia,
        "resultado": resultado
    }
    
def test_chi_cuadrado(numeros, bins=10):
    observados, _ = np.histogram(numeros, bins=bins)
    esperado = len(numeros) / bins
    chi2_valor = np.sum((observados - esperado)**2 / esperado)
    p_valor = 1 - chi2.cdf(chi2_valor, df=bins - 1)

    resultado = "Pasa" if p_valor > 0.05 else "No pasa"

    return {
        "chi2_valor": chi2_valor,
        "p_valor": p_valor,
        "resultado": resultado
    }
    
def test_sumas_acumuladas(bits):
    secuencia = np.array([1 if b == '1' else -1 for b in bits])
    suma_acumulada = np.cumsum(secuencia)
    max_desvio = np.max(np.abs(suma_acumulada))

    n = len(bits)
    esperado = np.sqrt(n) / 2
    desviacion = np.sqrt(n) / np.sqrt(12)
    z = (max_desvio - esperado) / desviacion

    if abs(z) < 1.96:
        resultado = 'Pasa'
    else:
        resultado = 'No pasa'

    return {
        'max_desvio': int(max_desvio),
        'umbral': round(esperado + 1.96 * desviacion, 2),
        'z_score': round(z, 4),
        'resultado': resultado
    }
    
def test_rachas(bits):
    rachas = 1
    for i in range(1, len(bits)):
        if bits[i] != bits[i - 1]:
            rachas += 1

    n0 = bits.count('0')
    n1 = bits.count('1')
    n = len(bits)

    if n0 == 0 or n1 == 0:
        return {"resultado": "No aplica (todos los bits son iguales)"}

    media = 1 + (2 * n0 * n1) / n
    varianza = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n**2 * (n - 1))
    z = (rachas - media) / np.sqrt(varianza)

    resultado = "Pasa" if abs(z) < 1.96 else "No pasa"

    return {
        "rachas": rachas,
        "media_esperada": media,
        "z_score": z,
        "resultado": resultado
    }