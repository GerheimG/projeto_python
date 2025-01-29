# Desenvolva um programa que peça um número qualquer e calcule o dobro e o triplo desse número.
 # IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# INTROD.
print('=' * 70)
print('DOBRO E TRIPLO DE N(X)')
print('=' * 70)

# ENTRADA DE DADOS
numerox = float(input('Escolha qualquer valor: '))

# PROCESSAMENTO 
dobro = (numerox) * 2
triplo = (numerox) * 3

# SAÍDA DE DADOS 
(print(f'Com o {numerox} seu dobro será {dobro} e seu triplo será {triplo}'))
print('=')