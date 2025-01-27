import os


os.system('cls')

dicionario = {}


for i in range(1,5):
    chave = input(f'Insira a {i}ª chave: ')
    valor = input(f'Insira o {i}ª valor:')
    dicionario[chave] = valor


print(dicionario)