#Mayor de una lista
#Crea una función que reciba una lista de números y devuelva el mayor.

def major(list):
    major = list[0]
    for number in list[1:]:
        if number > major:
            major = number
    return major


number = [7, 8, 13, 20, 1, 0]
result = major(number)
print(result)