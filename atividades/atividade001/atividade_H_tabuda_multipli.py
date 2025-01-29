# H)Implemente um programa que receba um número inteiro e imprima sua tabuada de multiplicação.

# IMPORTANDO BIBLIOTECA
import os

# LIMPANDO TERMINAL 
os.system('cls')

# INTROD.

print('=' * 70)
print('TABUADA DE MULTIPLICAÇÃO')
print('=' * 70)

# ENTRADA DE DADOS

num = int(input('Esolha qualquer valor inteiro: '))

# PROCESSAMENTO

vezes1 = num * 1
vezes2 = num * 2
vezes3 = num * 3 
vezes4 = num * 4
vezes5 = num * 5
vezes6 = num * 6
vezes7 = num * 7
vezes8 = num * 8
vezes9 = num * 9
resultado = vezes1, vezes2, vezes3, vezes4, vezes5, vezes6, vezes7, vezes8, vezes9

# SAÍDA DE DADOS 
print(f'A tabuada de {num} é igual a {resultado}')
print('=')