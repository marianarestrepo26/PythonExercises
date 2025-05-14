#Contar letras
#Escribe una función que cuente cuántas veces aparece una letra en una palabra.

def counter(word, letter):
    count = 0
    for let in word:
        if let == letter:
            count += 1
    return count

word = input('Enter a word: ')
letter = input('Enter a letter: ')
result = counter(word, letter)
print(f'The letter {letter} appears {result} times in the word {word}.')