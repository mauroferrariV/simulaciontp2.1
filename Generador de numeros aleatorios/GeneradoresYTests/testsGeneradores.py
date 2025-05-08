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


def testPoker(numberList, n):
  
  # Verifico longitud de los digitos
  for i in numberList:
    if  len(str(i)) != 5:
      return(print("Test Fallido porque de alguno de los digitos es menor que 4 o mayor que 5"))
   
  # INICIO DEL TEST
  
  # Clasifico las "manos"  
  def clasificar_manos(numberList):
    clasificaciones = {
        "todos_diferentes": 0,
        "un_par": 0,
        "dos_pares": 0,
        "trio": 0,
        "full_house": 0,
        "poker": 0,
        "quintuples": 0
    }
    # Cuento las repeticiones usando la funcion Counter
    for numero in numberList:
        cuenta = Counter(numero)
        valores = sorted(cuenta.values(), reverse=True)
        
        if valores == [5]:
            clasificaciones["quintuples"] += 1
        elif valores == [4, 1]:
            clasificaciones["poker"] += 1
        elif valores == [3, 2]:
            clasificaciones["full_house"] += 1
        elif valores == [3, 1, 1]:
            clasificaciones["trio"] += 1
        elif valores == [2, 2, 1]:
            clasificaciones["dos_pares"] += 1
        elif valores == [2, 1, 1, 1]:
            clasificaciones["un_par"] += 1
        else:
            clasificaciones["todos_diferentes"] += 1
    
    return clasificaciones 

  # Genero los valores esperados de las "manos"
  esperados = {
    "todos_diferentes": n * 0.3024,   # Estos numeros representan las probabilidades de las manos
    "un_par": n * 0.504,
    "dos_pares": n * 0.108,
    "trio": n * 0.072,
    "full_house": n * 0.009,
    "poker": n * 0.0045,
    "quintuples": n * 0.0001
  }
  # Funcion chi-cuadrado interna del
  def calcular_chi_cuadrado(observados, esperados):
    chi2, p = chisquare(list(observados.values()), f_exp=list(esperados.values()))
    return chi2, p
  
  # Asigno la clasificación de las "manos" 
  observados = clasificar_manos(numberList)
  
  chi2, p = calcular_chi_cuadrado(observados, esperados)
  
  print("Chi-cuadrado:", chi2)
  print("P-valor:", p)
  
  if p < 0.05:
    print("El generador de números aleatorios no sigue una distribución uniforme. (Los numeros no parecen ser aleatorios.)")
  else:
    print("El generador de números aleatorios sigue una distribución uniforme. (Los numeros parecen ser aleatorios.)")



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
