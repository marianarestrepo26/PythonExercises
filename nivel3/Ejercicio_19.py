#Generador de contraseñas
#Crea una función que genere una contraseña aleatoria de una longitud dada.

import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("La longitud mínima debe ser de 6 caracteres")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password())