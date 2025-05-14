#Validar contraseña segura
#Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).

def verify_password(password):

    while not 6 <= len(password):
            print('Error, your password must contain more than 6 characters')
            password = input('Enter a password: ')

    numbers = 0
    capitals = 0
    lower = 0
    symbols = 0

    for caracter in password:
        if caracter.isspace():
            return False
        elif caracter.isdigit():
            numbers += 1
        elif caracter.isupper():
            capitals += 1
        elif caracter.islower():
            lower += 1
        else:
            symbols += 1

    return numbers >= 1 and capitals !=0 and lower >= 1 and symbols >= 1

print(verify_password(input('Enter a password: ')))