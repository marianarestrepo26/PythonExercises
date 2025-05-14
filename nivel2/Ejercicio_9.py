#Filtrar pares
#Crea una función que reciba una lista de números y devuelva solo los pares.

def filter_pairs(list):
    return[n for n in list if n % 2 == 0]

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_pairs(list))