# IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# A) Desenvolva um programa que solicite três valores ao usuário. Em seguida, calcule e exiba a soma e a multiplicação desses valores.

# ENTRADA DE DADOS
print('=' * 70)
print('TRÊS VALORES')
print('=' * 70)
print('')
valor1 = float(input('Insira o 1° valor: '))
valor2 = float(input('Insira o 2° valor: '))
valor3 = float(input('Insira o 3° valor: '))
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

# SAÍDA DE DADOS
soma = print(f'Aqui está a soma dos valores: {soma}')
multiplicacao = print(f'Aqui está a multiplicação desses valores: {multiplicacao}')
print('=')