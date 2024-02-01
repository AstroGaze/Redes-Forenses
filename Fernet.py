#Cifrado Fernet

#Importamos Fernet
from cryptography.fernet import Fernet

#Generamos la clave
clave = Fernet.generate_key()

#Creamos la instancia de Fernet
f = Fernet(clave)

#Encriptamos el mensaje
token = f.encrypt(b'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente dolores laudantium dignissimos? Voluptatem officiis libero ipsa temporibus porro cupiditate numquam, ratione cum reiciendis sed illo vel maiores ipsam aperiam iste!')

#Mensaje Cifrado
print(token)

#Descifrar
des = f.decrypt(token)

print(des)