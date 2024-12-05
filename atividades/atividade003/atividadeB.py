#Faça um programa que receba 2 valores, faça a divisão entre eles. 
#Se a divisão não for inteira, o programa deverá arredondar o resultado para cima e para baixo. 
#Faça a validação para divisão por 0.

import os
import math

os.system('cls')

dividendo = int(input('Insira o dividendo: '))
divisor = int(input('Insira o divisor valor: '))

if divisor == 0:
    print('Divisão por zero não é permitida!!')
    exit()
else:
    divisao = dividendo / divisor


arredondar_pra_cima = math.ceil(divisao)
arredondar_pra_baixo = math.floor(divisao)

print(f'O resultado é: {arredondar_pra_cima or arredondar_pra_baixo}')