# D) Crie uma função que receba uma temperatura 
# em fahrenheit e retorne o valor em graus célsius.

import os


os.system('cls')


# Definindo a função
def temperatura(fahrenheit):
    # Convertendo fahrenheit para celsius
    celsius = (fahrenheit - 32) / 9 * 5 
    return celsius

fahrenheit = int(input('Insira a temperatura em fahrenheit: '))

# Invocando a função
temp_celsius = temperatura(fahrenheit)

print(f'Aqui está a temperatura em célsius: {temp_celsius:.2f}')




