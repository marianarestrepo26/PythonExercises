#Composición de funciones
#Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.


def name():
    n = input('Enter your name: ')
    return valide_name(n)

def valide_name(n):
    while n:
        if n.isalpha():
            return n
        else:
            print('Error, name is not valide.')
            n = input('Enter your name: ')
            
print(name())