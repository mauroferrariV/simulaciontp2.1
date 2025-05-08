import numpy as np
import math
from collections import Counter
from scipy.stats import chisquare

def testFrecuencia(numberList):
  totaldig = 0
  digitFrec=[0]*10
  for i in range(len(numberList)):
    for x in str(numberList[i]):
      digitFrec[int(x)]= digitFrec[int(x)] + 1
      totaldig += 1
  
  for y in range(len(digitFrec)):
    digitFrec[y]=digitFrec[y]/totaldig
  frecEsp = [1/10]*10
  chi2_stat, p_value = chisquare(digitFrec, frecEsp)

  # Mostrar los resultados
  print(f"Chi-cuadrado: {chi2_stat}")
  print(f"P-valor: {p_value}")

  if p_value < 0.05:
      print("El generador de números aleatorios no sigue una distribución uniforme. (Los numeros no parecen ser aleatorios.)")
  else:
      print("El generador de números aleatorios sigue una distribución uniforme. (Los numeros parecen ser aleatorios.)")

def testChiCuadrado(numberList, n):

  n_intervals = 10
  observed_frequencies, bin_edges = np.histogram(numberList, bins=n_intervals)

  expected_frequencies = np.full(n_intervals, n / n_intervals)

  chi2, p = chisquare(observed_frequencies, expected_frequencies)
  
  print(f"Chi-cuadrado: {chi2}")
  print(f"Valor p: {p}")

  # Interpretación del valor p
  if p > 0.05:
    print("El generador de números aleatorios sigue una distribución uniforme. (Los numeros parecen ser aleatorios.)")
  else:
    print("El generador de números aleatorios no sigue una distribución uniforme. (Los numeros no parecen ser aleatorios.)")


def testSumasAcumuladas(numberList):
    """
    Test de Sumas Acumuladas para evaluar la aleatoriedad de un generador de números.
    """
    n = len(numberList)
    
    # Calcular la suma acumulada centrada
    suma_acumulada = np.cumsum(numberList - np.mean(numberList))

    # Encontrar el valor máximo y mínimo de la suma acumulada
    max_suma = np.max(suma_acumulada)
    min_suma = np.min(suma_acumulada)

    # Calcular el estadístico Vn
    vn = max(abs(max_suma), abs(min_suma))

    # Calcular el valor esperado y la desviación estándar
    valor_esperado = math.sqrt(n) / 2
    desviacion_estandar = math.sqrt(n) / math.sqrt(12)

    # Calcular el estadístico Z
    z = (vn - valor_esperado) / desviacion_estandar

    # Evaluar el resultado del test
    if abs(z) < 1.96:  # Nivel de significancia del 5%
        print("El test de sumas acumuladas no rechaza la hipótesis de aleatoriedad.")
    else:
        print("El test de sumas acumuladas rechaza la hipótesis de aleatoriedad.")


def testRachas(numberList, n):
  def contar_rachas(numeros):
    rachas = 1  # Empezamos con una racha inicial
    for i in range(1, len(numeros)):
        if (numeros[i] > numeros[i - 1] and numeros[i - 1] <= numeros[i - 2]) or \
           (numeros[i] < numeros[i - 1] and numeros[i - 1] >= numeros[i - 2]):
            rachas += 1
    return rachas

# Calcular el estadístico Z para la prueba de rachas
  def calcular_estadistico_z(rachas, n):
      media = (2 * n - 1) / 3
      varianza = (16 * n - 29) / 90
      z = (rachas - media) / math.sqrt(varianza)
      return z

  rachas = contar_rachas(numberList)
  z = calcular_estadistico_z(rachas, n)

  print(f"Número de rachas: {rachas}")
  print(f"Estadístico Z: {z}")

  z_critico = 1.96  # Valor crítico para un nivel de significancia del 5% (p = 0.05)
  if abs(z) < z_critico:
      print("El generador de números aleatorios sigue una distribución uniforme. (Los numeros parecen ser aleatorios.)")
  else:
      print("El generador de números aleatorios no sigue una distribución uniforme. (Los numeros no parecen ser aleatorios.)")
