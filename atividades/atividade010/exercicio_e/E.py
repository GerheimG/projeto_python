# E) Crie uma função que receba
# a altura e o peso de uma pessoa. 
# Depois retorne o seu IMC.

import os
from calculo.indice import calcular

os.system('cls')




altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))


# Invocando a função
imc = calcular(altura, peso)

print(f'Aqui está seu imc: {imc:.2f}')
