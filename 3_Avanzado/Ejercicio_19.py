#Generador de contraseñas
#Crea una función que genere una contraseña aleatoria de una longitud dada.

import random
import string

def generate_password(length):
    while length:
        try:
            length = int(length)
            if length >= 6:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(length))
                return password
            else:
                print('Minimum length must be 6 characters.')
                length = input('Enter the password length: ')
        except: 
            print('Error, you entered invalid data.')
            length = input('Enter the password length: ')
            
           

length = input('Enter the password length: ')
print(generate_password(length))