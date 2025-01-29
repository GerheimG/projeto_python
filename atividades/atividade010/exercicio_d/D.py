# D) Crie uma função que receba uma temperatura 
# em fahrenheit e retorne o valor em graus célsius.

import os
from temperatura.calculo_temperatura import temperatura

os.system('cls')


fahrenheit = int(input('Insira a temperatura em fahrenheit: '))

# Invocando a função
temp_celsius = temperatura(fahrenheit)

print(f'Aqui está a temperatura em célsius: {temp_celsius:.2f}')




