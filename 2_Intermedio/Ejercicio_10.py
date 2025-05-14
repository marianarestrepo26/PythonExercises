#Palíndromo
#Escribe una función que determine si un texto es un palíndromo.

def palindrome(text):
    text = text.lower().replace(" ", "")
    while text:
        if text.isalpha():
            if text == text[::-1]:
                return 'Is palindrome'
            else:
                return 'Is not a palindrome'
        else:
            print('Error, you entered invalid data.')
            text = input('Enter a word: ')

print(palindrome(input('Enter a word: ')))