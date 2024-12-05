# B) Crie um programa que pergunte o ano de nascimento do usuário e calcule sua idade atual.

# IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# importando blibioteca de tempo 
import datetime

# ENTRADA DE DADOS
print('=' * 70)
print('CÁLCULO DA IDADE ATUAL')
print('=' * 70)
print('')
nome = str(input('Qual seu nome?: '))
nascimento = int(input('Qual o ano de seu nascimento?: '))

# PROCESSAMENTO
ano_atual = datetime.datetime.now().year
idadeatual = int(ano_atual) - int(nascimento)

# SAÍDA DE DADOS
print(f'Olá {nome} você tem ou irá fazer {idadeatual} anos!!')
print('=')