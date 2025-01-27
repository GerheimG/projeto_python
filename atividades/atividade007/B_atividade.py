# Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.

import os
import random


os.system('cls')



lista = []

for num in range(1,50):
    numeros = random.randint(1,100)
    lista.append(numeros)

lista1 = lista[0:10]
lista2 = lista[10:20]
lista3 = lista[20:30]
lista4 = lista[30:40]
lista5 = lista[40:50]


print('Lista original', lista)
print('Primeira lista:', lista1)
print('Segunda lista:', lista2)
print('Terceira lista:', lista3)
print('Quarta lista:', lista4)
print('Quinta lista:', lista5)