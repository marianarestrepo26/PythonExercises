#FizzBuzz
#Crea una función que reciba un número y devuelva 'Fizz', 'Buzz' o 'FizzBuzz' según las reglas del juego.

number= input('Enter a intenger number: ')

def fizzbuzz(number = 0):
    while number:
        try:
            n = int(number)
            if n % 15 == 0:
                print('FizzBuzz')
            elif n % 3 == 0:
                print('Fizz')
            elif n % 5 == 0:
                print('Buzz')
            else:
                print('The number is not a multiple of 3, 5 y 15.')
        except:
            print('Error, you entered invalid data.')

print(fizzbuzz(number))