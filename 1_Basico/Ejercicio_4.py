#Mayoría de edad
#Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

def check_age(age = 0):
    while age:
        try: 
            age = int(age)
            if age >= 0:
                return age
            else:
                print('Error, the number entered is negative. Try again.')
                age = input('Enter your age: ')
        except:
            print('Error, you entered invalid data.')
            age = input('Enter your age: ')
            

age = check_age(input('Enter your age: '))

if age >= 18:
    print("You're of legal age.")
else:
    print("You're a minor.")