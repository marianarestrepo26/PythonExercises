#Área de un triángulo#
#Escribe una función que devuelva el área de un triángulo dado su base y altura.

def check_number(mensaje):
    while True:
        number = input(mensaje)
        if number.replace('.', '', 1).isdigit():
            return float(number)
        else:
            print("Ingresa solo números.")

base = check_number("Ingresa la base del rectángulo: ")
altitude = check_number("Ingresa la altura del rectángulo: ")

area = base * altitude
print("El área del rectángulo es:", area)