#B) Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os

os.system('cls')

nome = input('Insira o nome: ')
nomenovo = nome.replace('Silva', 'Oliveira')

print(f'Noma antigo: {nome}\n Nome novo: {nomenovo}')