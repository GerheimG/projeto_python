import os 

os.system('cls')

produtos_dict = {}

for l in range(1,2):
    nome = input('Insira o nome do produto: ').lower()
    quantidade = int(input('Insira a quantidade: '))
    preco = float(input('Preço do produto: '))

    produtos_dict[nome] = {'quantidade' : quantidade, 'preço' : preco}