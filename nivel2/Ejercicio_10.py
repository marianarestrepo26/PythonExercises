#Palíndromo
#Escribe una función que determine si un texto es un palíndromo.

def palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
        return 'Es palindromo'
    else:
        return 'No es palindromo'

text = input('Ingresa una palabra: ')
print(palindrome(text))