import os


os.system('cls')

filmes = {}

for i in range(1,2):
    titulo = input('Insira o titulo da obra: ').lower()
    genero = input('Genero do filme: ')
    duracao = input('Duração do filme: ')
    classificacao = input('Classificação Indicativa: ')