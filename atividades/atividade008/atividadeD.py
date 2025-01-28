# D) Faça um programa que leia uma frase e depois exiba na tela:
# A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na 
# frase e quantas letras tem a 2ª palavra na frase.

import os


os.system('cls')

frase = 'Eu programo em Python'

minuscula = frase.lower()
maiscula = frase.upper()
quantidade_caracter = len(frase)
frase2 = 'programo'
quantidade = len(frase2)
invertida = frase[::-1]

print(minuscula)
print(maiscula)
print(f'A frase toda tem: {quantidade_caracter} caracteres')
print(f'A segunda palavra tem: {quantidade} caracteres')
print(f'Invertida: {invertida}')
