#Suma de dos números
#Escribe una función que reciba dos números y devuelva su suma.

def check_number():
    number = input('Enter a number: ')
    while number:
        try:
            number = float(number)
            return number
        except:
            print('Error, you entered invalid data.')
            number = input('Enter a number: ')

n1 = check_number()
n2 = check_number()
sum = n1 + n2
print(f'The sum of {n1} and {n2} is {sum}')