#ATIVIDADE B 

import os

os.system('cls')


numero1 = float(input('Insira um valor: '))
numero2 = float(input('Insira outro valor: '))
numero3 = float(input('Insira outro valor: '))
resposta = ''
resposta1 = ''


if numero1 > numero2 and numero1 > numero3:
    resposta = f'{numero1} é o maior número'
elif numero2 > numero1 and numero2 > numero3:
    resposta = f'{numero2} é o maior número'
elif numero3 > numero1 and numero3 > numero2:
    resposta = f'{numero3} é o maior número'
if numero1 < numero2 and numero1 < numero3:
    resposta1 = f'{numero1} é o menor número'
elif numero2 < numero1 and numero2 < numero3:
    resposta1 = f'{numero2} é o menor número'
elif numero3 < numero1 and numero3 < numero2:
    resposta1 = f'{numero3} é o menor número'
elif numero1 == numero2 == numero3:
    resposta = f'Todos os números são iguais'
else:
    print()

print(resposta, resposta1)