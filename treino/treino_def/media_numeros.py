# Função que calcula a média de uma lista de números.

import os
from functools import reduce

os.system('cls')

lista = []


def receber_numeros():
    while True:
        print(f'Lista de números\n', lista)
        print('Digite 0 para sair')
        numero = int(input('Insira o numero: '))
        lista.append(numero)
        os.system('cls')
        if numero == 0:
            break
    return lista

def calcular_media():
    somar = reduce(lambda x, y: x + y, lista)
    quantidade = len(lista) - 1
    media = somar / quantidade
    print(media)
    return media



receber_numeros()
calcular_media()