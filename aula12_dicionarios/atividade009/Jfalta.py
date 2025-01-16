import os


os.system('cls')

evento = {}

for i in range(1,2):
    nome = input('Insira o nome do evento: ').lower()
    nome_part = input('Nome participante: ')
    email = input('Email participante: ')
    data = input('Insira a data: ')
    localizacao =input('Preço do produto: ')

    evento[nome]