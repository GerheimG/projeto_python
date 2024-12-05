# ATIVIDADE D

import os

os.system('cls')

salario = float(input('Insira seu salário atual: '))
resposta = ''


if salario <= 0:
    print('Valor inválido!!')

elif salario > 1500:
    novo = salario * 1.05
    
    resposta = f'Seu novo salário será {novo}'


elif salario < 1000:
    novo = salario * 1.10
    resposta = f'Seu novo salário será {novo}'

else:
    resposta = f'Seu salário se manterá o mesmo'


print(resposta)
    