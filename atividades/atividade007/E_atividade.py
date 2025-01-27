# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.

import os


os.system('cls')

lista = []
lista_impar = []
lista_par = []

for n in range(1,8):
    numeros = int(input(f'Insira o {n}ª valor: '))
    lista.append(numeros)
    if numeros % 2 == 0:
        lista_par.append(numeros)
    if numeros % 2 != 0:
        lista_impar.append(numeros)

print('Números fornecidos:', lista)
print('Números ímpares:', lista_impar)
print('Números pares:', lista_par)