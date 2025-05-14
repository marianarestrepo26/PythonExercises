#Contar letras
#Escribe una función que cuente cuántas veces aparece una letra en una palabra.

def counter(word, letter):
    count = 0
    for let in word:
        if let == letter:
            count += 1
    return count

word = input('Ingresa una palabra: ')
letter = input('Ingresa una letra: ')
result = counter(word, letter)
print(f'La letra {letter} aparece {result} veces en la palabra {word}.')