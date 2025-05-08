import time
import sys
from testsGeneradores import *
import matplotlib.pyplot as plt

if sys.argv[1]!="-s" or sys.argv[3]!="-a" or sys.argv[5]!="-c" or sys.argv[7]!="-m" or sys.argv[9]!="-n":
  print("Uso: Python randomGLC.py -s <Seed (semilla)> -a <Parametro A> -c <Parametro C> -m <Parametro M> -n <Cantidad de Numeros>")
  print("Para semilla vacia, ingrese como argumento de la semilla " " (comillas dobles con 1 espacio)")
  sys.exit(1)

if sys.argv[2] == " ":
    seed = int(time.time())
else:
  seed = int(sys.argv[2])

a=int(sys.argv[4])
c=int(sys.argv[6])
m=int(eval(sys.argv[8]))
n=int(sys.argv[10])

def generadorGCL(a,c,m,seed,n):
  numberList=[]
  x0=seed
  for i in range(n):
    if i != 0:
      if x0 == seed:
        return
    if (m>0) and (a > 0) and (a < m) and (c >= 0) and (c < m) and (seed >= 0) and (seed < m):
      seed = (a * seed + c) % m
      numberList.append(seed)
  return (numberList)


# MAIN
numberList=generadorGCL(a,c,m,seed,n)
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

plt.scatter(listCantNums, numberList,s=10, c="black")
plt.xlabel('Numero X Generado')
plt.ylabel('Valor del Numero X')
plt.title('Diagrama de Dispersión')
plt.show()