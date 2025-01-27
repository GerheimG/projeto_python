# Faça um programa que sorteia os números da Mega Sena e da Lotofácil


import os
import random


os.system('cls')


lista_mega = []
lista_loto = []

for num in range(1, 7):
    numeros_mega = random.randint(1,60)
    lista_mega.append(numeros_mega)

for num in range(1, 15):
    numeros_loto = random.randint(1,25)
    lista_loto.append(numeros_loto)

print('Aqui estão os números sorteados da Mega Sena', lista_mega)
print('Aqui estão os números sorteados da LotoFácil', lista_loto)