import sys
import time
from testsGeneradores import *
import matplotlib.pyplot as plt
import random

if sys.argv[1]!="-s" or sys.argv[3]!="-n":
  print("Uso: Python randomPython.py -s <Seed (semilla)> -n <Cantidad de Numeros>")
  print("Para semilla vacia, ingrese como argumento de la semilla " " (comillas dobles con 1 espacio)")
  sys.exit(1)

if sys.argv[2] == " ":
    seed = int(time.time())
else:
  seed = int(sys.argv[2])

n=int(sys.argv[4])

def pyRand(seed,n):
  numberList = []
  x0=seed
  random.seed(seed)
  
  for i in range(n):
    numberList.append(random.randint(1,n))
    
  return numberList

numberList=pyRand(seed,n)
print("")
print("--Numeros Generados--")
print(numberList)
print("")
print("--Test de Frecuencia de Digitos--")
testFrecuencia(numberList)
print("")
print("--Test Chi Cuadrado--")
testChiCuadrado(numberList, n)
print("")
print("--Test Rachas--")
testRachas(numberList, n)
print("")
print("--Test Suma Acumulada--")
testSumasAcumuladas(numberList)
print("")


listCantNums = [i for i in range(n)]

plt.scatter(listCantNums, numberList, s=10,  c="black")
plt.xlabel('Numero X Generado')
plt.ylabel('Valor del Numero X')
plt.title('Diagrama de Dispersión')
plt.show()