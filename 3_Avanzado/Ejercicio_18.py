#Suma de elementos únicos
#Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.

def elements_sum(list):
    return sum([el for el in list if list.count(el) == 1 ])

list = [1, 8, 2, 6, 5, 4]

print(elements_sum(list))