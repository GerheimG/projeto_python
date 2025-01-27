#Faça um programa para sortear um número de 1 a 20.

import os 
import random

os.system('cls')

aleatorio_inteiro = random.randint(1, 20)

print(f'O número sorteado foi: {aleatorio_inteiro}')