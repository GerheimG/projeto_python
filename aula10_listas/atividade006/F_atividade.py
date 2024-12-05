# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os


os.system('cls')

lista_nomes = []

for n in range(1, 6):
    nomes = input(f'Insira o {n}ª nome: ')
    lista_nomes.append(nomes)

for indice, name in enumerate(lista_nomes, start= 1):
      
    print(f'Índice: {indice} = Nome: {name}')


