import sys
import time
from testsGeneradores import *
import matplotlib.pyplot as plt

if sys.argv[1]!="-s" or sys.argv[3]!="-n":
  print("Uso: Python randomMidSquare.py -s <Seed (semilla)> -n <Cantidad de Numeros>")
  print("Para semilla vacia, ingrese como argumento de la semilla " " (comillas dobles con 1 espacio)")
  sys.exit(1)

if sys.argv[2] == " ":
    seed = int(time.time())
else:
  seed = int(sys.argv[2])

n=int(sys.argv[4])

def mid_squares(seed,n):
  numberList = []
  seedList = []
  x0=seed
  for i in range(n):
    if i != 0:
      if x0 == seed:
        return
    numberList.append(x0**2)
    newSeed=str(int(x0)**2).zfill(8)
    if len(newSeed) > 4:
      inicioCorte= (len(newSeed) - 4) // 2
    x0 = int((newSeed)[inicioCorte:inicioCorte + 4])
    seedList.append(x0)
  return numberList, seedList

numberList,seedList=mid_squares(seed,n)
print("")
print("--Numeros Generados--")
print(numberList)
print("")
print("--Semillas Generadas--")
print(seedList)
print("")
print("--Test de Frecuencia de Digitos--")
testFrecuencia(numberList)
print("")
print("--Test Chi Cuadrado--")
testChiCuadrado(numberList, n)
print("")
print("--Test Poker--")
testPoker(numberList, n)
print("")
print("--Test Rachas--")
testRachas(numberList, n)
print("")


listCantNums = [i for i in range(n)]

plt.scatter(listCantNums, numberList, s=10, c="black")
plt.xlabel('Numero X Generado')
plt.ylabel('Valor del Numero X')
plt.title('Diagrama de Dispersión')
plt.show()