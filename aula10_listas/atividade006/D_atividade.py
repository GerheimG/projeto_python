# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os


os.system('cls')

lista = []
soma = 0

for n in range(1, 5):
    notas = int(input(f'Insira a {n}ª nota: '))
    lista.append(notas)
    soma += notas
    media = soma / n

print('Aqui está as notas:', lista)
print('Aqui está a média das notas:', media)