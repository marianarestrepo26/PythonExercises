#Simular dado
#Crea una función que simule el lanzamiento de un dado de 6 caras.

import random

def throw_dice():
    return random.randint(1, 6)

dice = throw_dice()
print(f'Your number is {dice}')