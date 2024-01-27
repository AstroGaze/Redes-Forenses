from Crypto.Util import number
import random


#Ejercicio 1
#Obtener un numero aleatorio
print("Ejercicio 1- obtener un numero de 256 bits usando la funcion random", random.getrandbits(256),'\n')

#Ejercicio 2
#Obtener un numero primo

i = 0
while(True):
    i = i + 1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la iteracion: ", i, " se econtro el primo: ", j, "\n")
        break