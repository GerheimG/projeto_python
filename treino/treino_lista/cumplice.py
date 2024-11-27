# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

import os


os.system('cls')

lista_resposta = []

print('=' * 70)
print('PERGUNTAS SOBRE UM CRIME\n RESPONDA APENAS COM SIM OU NÃO')
print('=' * 70)
for perg in range(1):
    resp1 = input('Telefonou para a vítima? ').lower().strip()
    print('-' * 70)
    resp2 = input('Esteve no local do crime? ').lower().strip()
    print('-' * 70)
    resp3 = input('Mora perto da vítima? ').lower().strip()
    print('-' * 70)
    resp4 = input('Devia para a vítima? ').lower().strip()
    print('-' * 70)
    resp5 = input('Já trabalhou com a vítima? ').lower().strip()
    print('-' * 70)
    lista_resposta.append(resp1)
    lista_resposta.append(resp2)
    lista_resposta.append(resp3)
    lista_resposta.append(resp4)
    lista_resposta.append(resp5)
    quantidade = lista_resposta.count('sim')
    
    if quantidade < 2:
        print('Você é inocente')
    elif quantidade == 2:
        print('Você é apenas suspeito')
    elif quantidade >= 3 and quantidade <= 4:
        print('Você é cúmplice')
    elif quantidade == 5:
        print('Você é o assassino')


