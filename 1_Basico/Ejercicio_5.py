#Conversor de temperatura
#Crea una función que convierta grados Celsius a Fahrenheit.

def check_temp():
    temp = input('Enter the temperature in Celcius: ')
    while temp:
        try:
            temp = float(temp)
            return temp
        except:
            print('Error, you entered invalid data.')
            temp = input('Enter the temperature in Celcius: ')

temp_C = check_temp()
temp_F = (temp_C * (9 / 5) + 32)

print(f'The temperature in Fahrenheit is: {temp_F}' )