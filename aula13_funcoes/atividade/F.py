# F) Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade 
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo 
# chave e valor utilizando como base essas duas listas. 
# Depois, seu programa deverá imprimir esse dicionário 
# utilizando uma estrutura de repetição for.

import os


os.system('cls')

def receber_dicionario(lista_1, lista_2):
    dicionario = {}
    for keys, valeus in zip(lista_1, lista_2):
        dicionario[keys] = valeus 

    return dicionario

lista_1 = ['nome', 'peso', 'idade']
lista_2 = ['john', 40, 18]

dicionario = receber_dicionario(lista_1, lista_2)

for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')