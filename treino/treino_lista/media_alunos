# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

import os


os.system('cls')

lista_notas = []
lista_nomes = []
lista_mediamaior7 = []
soma = 0


for al in range(1,11):
    nome = input(f'Nome do {al}ª aluno: ')
    for note in range(1,5):
        nota = float(input(f'Insira a {note}º nota do aluno {nome}: '))
        soma += nota
        media = soma / 4
for i in range(1, 5):
    mediareal = media / 4
    if mediareal > 7:
        lista_mediamaior7.append(mediareal)
media7 = len(lista_mediamaior7)

print('Alunos acima da média 7:', media7)
                       


        