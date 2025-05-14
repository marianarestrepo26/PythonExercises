#Factorial
#Crea una función que calcule el factorial de un número entero positivo.

def factorial(n = 0):
    while n:
        try: 
            n = int(n)
            if n > 0:
                factorial = 1
                i = 1
                while (i <= n):
                    factorial = factorial * i
                    i = i + 1
                return factorial
            else:
                print('Error, the number entered is negative. Try again.')
                n = input('Enter a number: ')
        except:
            print('Error, you entered invalid data.')
            n = input('Enter a number: ')

num =  input('Enter a number: ')      
number = factorial(num)

print (f'The factorial of {num} is {number}')