# Crie um programa que converta uma medida em metros para centímetros e milímetros.

# IMPORTANDO BIBLIOTECA

import os

# LIMPANDO TERMINAL

os.system('cls')

# INTROD.

print('=' * 70)
print('CONVERTENDO VALORES')
print('=' * 70)

# ENTRADA DE DADOS 

medidax = float(input('Insira a medida em metros \n que deseja converter: '))

# PROCESSAMENTO
cent = medidax * 100
milim = medidax * 1000

# SAÍDA DE DADOS 
print(f'Convertendo {medidax} metro(s) para centímetros será {cent} e \n para milímetros será {milim}')
print('=')