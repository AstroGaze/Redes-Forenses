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
    j = random.getrandbits(1536)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la iteracion: ", i, " se econtro el primo: ", j, "\n")
        break

#Ejercicio 3
#Obtener inverso multiplicativo
def inversoMultiplicativo(x, y):
    print("Ejercicio 3 - El inverso multiplicativo del numero x : ", "\n", x, "\n", "y el numero y: ", "\n", y, "\n", "es: ", "\n", number.inverse(x, y), "\n")

a = random.getrandbits(1024)
b = random.getrandbits(1024)

inversoMultiplicativo(a, b)

#Ejercicio 4
#Potencia de un numero 2^(e) mod p, donde "e" es un numero de 256 bits y "p" es un numero primo de 1024 bits
a = 2
b = random.getrandbits(256)
c = j

def potencia(x,y,z):
    print("Ejercicio 4 - la potencia de x a la y mod z es: ", "\n", pow(x,y,z))

potencia(a,b,c)
