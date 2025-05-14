#Invertir texto
#Crea una función que invierta una cadena de texto.

def reverse_text(text):
    while text:
        if text.isalpha():
            return text[::-1]
        else:
            print('Error, you entered invalid data.')
            text = input('Enter a word: ')

print(reverse_text(input('Enter a word: ')))