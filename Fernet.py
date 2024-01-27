#Cifrado Fernet

#Importamos Fernet
from cryptography.fernet import Fernet

#Generamos la clave
clave = Fernet.generate_key()

#Creamos la instancia de Fernet
f = Fernet(clave)

#Encriptamos el mensaje
token = f.encrypt(b'Mensaje Secreto')

#Mensaje Cifrado
print(token)

#Descifrar
des = f.decrypt(token)

print(des)