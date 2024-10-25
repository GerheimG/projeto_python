# J) Elabore um programa que peça as dimensões de um retângulo e calcule seu perímetro.

# IMPORTANDO BIBLIOTECA

import os 

# LIMPANDO TERMINAL

os.system('cls')

#INTROD.

print('=' * 70)
print('CÁLCULO DE UM RETÂNGULO')
print('=' * 70)

# ENTRADA DE DADOS

base = float(input('Insira o valor da base: '))
altura = float(input('Insira o valor da altura: '))

# PROCESSAMENTO

perimetro = 2 * (base + altura)

# SAÍDA DE DADOS 

print(f'Um retângulo com uma base de valor {base} e altura de valor {altura} \n terá um perímetro de {perimetro}')
