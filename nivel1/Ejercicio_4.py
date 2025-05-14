#Mayoría de edad
#Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

def check_age(age = 0):
    while True:
        age = input("Ingresa tu edad: ")
        if age.isdigit():
            return int(age)
        elif age.startswith("-"):
            print("El número ingresado es negativo, por favor ingresa una edad válida")
        else:
            print("El dato ingresado no es válido.")

age = check_age()

if age >= 18:
    print('Eres mayor de edad.')
else:
    print('Eres menor de edad.')