#Eliminar duplicados
#Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

def remove_duplication(dup):
    return list(set(dup))

dup = [0, 4, 5, 6, 1, 1, 0, 0, 6, 2, 7, 7, 9, 7]
print(remove_duplication(dup))