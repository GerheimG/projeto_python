import os


os.system('cls')

produtos = {}

for i in range(1,2):
    nome = input('Insira o nome do produto: ').lower()
    preco = input('Preço do produto: ')
    categoria = input('Categoria do produto: ')