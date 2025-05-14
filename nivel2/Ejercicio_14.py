#Contar vocales
#Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

def count_vocals(word):
    voc = 0
    for vocal in word:
        if vocal in "aeiou":
            voc = voc + 1
    return f'{word} tiene {voc} vocales.'

print(count_vocals(input('Ingresa una palabra: ')))