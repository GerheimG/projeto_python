# Faça um programa que receba um valor e mostre sua raiz quadrada.
# Para raízes que não são exatas, arredonde para cima ou para baixo. 
# Faça a validação para números negativos,
# avisando ao usuário que o resultado será um número complexo.

import os
import math

os.system('cls')

numero = float(input('Insira um valor pra mostrar sua raiz: '))


if numero < 0:
    print('O resultado será um número complexo')
    exit()
else:
    raizQuadrada = math.sqrt(numero)
    arredondar_pra_cima = math.ceil(raizQuadrada)


print(f'A raiz de {numero} é: {arredondar_pra_cima}')
