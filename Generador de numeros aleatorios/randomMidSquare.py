import sys
import time
from testsGeneradores import *
import matplotlib.pyplot as plt

if sys.argv[1]!="-s":
  print("Uso: Python randomMidSquare.py -s <Seed (semilla)>")
  print("Para semilla vacia, ingrese como argumento de la semilla " " (comillas dobles con 1 espacio)")
  sys.exit(1)

if sys.argv[2] == " ":
    seed = int(time.time())
else:
  seed = int(sys.argv[2])


def mid_squares(seed):
  seed_number = seed
  number = seed_number
  already_seen = set()
  counter = 0

  while number not in already_seen:
      counter += 1
      already_seen.add(number)
      number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
      print(f"#{counter}: {number}")

  print(f"Arranco con {seed_number} y"
        f" se repitio {counter} iteraciones"
        f" con {number} resultado final.")
  
  return already_seen

numberList = mid_squares(seed)




print("")
print("--Numeros/Semillas Generados--")
print(list(numberList))
print("")
print("--Test de Frecuencia de Digitos--")
testFrecuencia(list(numberList))
print("")
print("--Test Chi Cuadrado--")
testChiCuadrado(list(numberList), len(list(numberList)))
print("")
print("--Test Rachas--")
testRachas(list(numberList), len(list(numberList)))
print("")
print("--Test Suma Acumulada--")
testSumasAcumuladas(list(numberList))
print("")


listCantNums = [i for i in range(len( list(numberList)))]


print("Tamaño de numberList:", len(list(numberList)), len(listCantNums))

plt.scatter(listCantNums, list(numberList), s=10, c="black")
plt.xlabel('Numero X Generado')
plt.ylabel('Valor del Numero X')
plt.title('Diagrama de Dispersión')
plt.show()