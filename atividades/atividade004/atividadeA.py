# ATIVIDADE A 
import os

os.system('cls')

numero = int(input('Insira um número inteiro: '))
resposta = ''
if numero % 2 == 0:
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'

print('=' * 70)
print(resposta)
