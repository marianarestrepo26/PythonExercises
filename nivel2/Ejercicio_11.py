#Factorial
#Crea una función que calcule el factorial de un número entero positivo.

number = int(input("Introduzca un número: "))

factorial = 1
i = 1
while (i <= number):
    factorial = factorial * i
    i = i + 1
print ("El factorial de " + str(number) + " es " + str(factorial))