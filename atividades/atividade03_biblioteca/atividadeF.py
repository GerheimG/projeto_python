#Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import os
import random

os.system('cls')

numero_aleatorio = int(random.uniform(1, 10))

print('Computador está pensando em um número...')
numero = int(input('Tente acertar o número, está entre 1 a 10..: '))

if numero == numero_aleatorio:
    print('Você acertou!!!')
else:
    print(f'Você errou!!! ele pensou no {numero_aleatorio:.0f}')
