#Área de un triángulo#
#Escribe una función que devuelva el área de un triángulo dado su base y altura.

def check_number(message):
    number = input(message)
    while number:     
        try:
            number == float(number)
            return number
        except:
            print('Enter only numbers.')
            number = input(message)

base = check_number('Enter the base of the rectangle: ')
altitude = check_number('Enter the rectangle height: ')

area = base * altitude
print(f'The rectangle area is {area}')