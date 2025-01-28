# I) Faça um programa que receba o nome completo de uma pessoa e, em seguida, mostre o primeiro e o último nome.


import os

os.system('cls')

nome_completo = input('Coloque seu nome: ').capitalize()

lista = nome_completo.split()
primeiro = lista[0:1]
ultimo = lista[-1:]
nome = ' '.join(primeiro + ultimo)

print(nome)
