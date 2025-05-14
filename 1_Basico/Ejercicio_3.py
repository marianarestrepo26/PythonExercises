#Número par o impar
#Crea una función que determine si un número es par o impar.

def check_number():
    number = input('Enter an intenger number: ')
    while number:
        try:
            number = int(number)
            return number
        except:
            print('Error, you entered invalid data.')
            number = input('Enter an intenger number: ')

number = check_number()
if number % 2 == 0:
    print('Is pair.')
else:
    print('Is odd.')