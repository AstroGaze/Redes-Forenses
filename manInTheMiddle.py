from Crypto.Util import number
import random

g = 2

primo = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

numberAlice = random.getrandbits(256)
numberBob = random.getrandbits(256)
numberEve = random.getrandbits(256)

def potencia(x,y,z):
    return pow(x,y,z)

A = potencia(g,numberAlice,primo)
B = potencia(g,numberBob,primo)
E = potencia(g,numberEve, primo)

print("Alice: ",  A)
print("Bob: ",  B)
print("Eve : ", E)

s1 = potencia(E,numberAlice,primo)
s2 = potencia(A, numberEve, primo)
s3 = potencia(E, numberBob, primo)
s4 = potencia(B, numberEve,primo)



print("S1: ", s1)
print("S2: ", s2)
print("S3 ", s3)
print("S4: ", s4)