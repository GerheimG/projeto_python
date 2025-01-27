# C) Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas


# IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# INTROD.
print('=' * 70)
print('MÉDIA DAS NOTAS')
print('=' * 70)

# ENTRADA DE DADOS
nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))
nota3 = float(input('3° nota: '))
nota4 = float(input('4° nota: '))

# PROCESSAMENTO
media = (nota1 + nota2 + nota3 + nota4) / 4

#SAÍDA DE DADOS
print(f'A média das seguintes notas \n {nota1}, {nota2}, {nota3} e {nota4} será {media}')
print('=')