#Saludo personalizado
#Crea una función que reciba un nombre y muestre un saludo personalizado.

def personalized_greeting():
    while True:
        nombre = input("Ingrese su nombre: ").title()
        if nombre.isalpha():
            print(f"¡Hola, {nombre}!")
            break
        else:
            print("El nombre solo debe contener letras.")

personalized_greeting()