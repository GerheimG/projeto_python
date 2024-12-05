#Faça um programa que receba um ângulo qualquer. 
#Em seguida, calcule o seno, cosseno e tangente do ângulo,
#limitando a saída a 2 casas decimais.

import os
import math

os.system('cls')

angulo = float(input('Insira um valor: '))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')