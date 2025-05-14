#Saludo personalizado
#Crea una función que reciba un nombre y muestre un saludo personalizado.

def personalized_greeting():
    name = input('Enter your name: ').title()
    while name:
        if name.isalpha():
            print(f'¡Hello, {name}!')
            break
        else:
            print('Error, can only contain letters.')
            name = input('Enter your name: ').title()

personalized_greeting()