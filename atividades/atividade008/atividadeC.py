# C) Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

nome = 'João da Silva'

if 'Oliveira' in nome:
    print(f'Oliveira está presente no nome: {nome}')
else:
    print(f'Oliveira não está presente no nome: {nome}')