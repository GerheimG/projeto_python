# ATIVIDADE C 

import os

os.system('cls')

velocidade = float(input('Insira sua velocidade: '))
limite = 60
resposta = ''


if velocidade <= limite:
    resposta = f'Você estava dentro do limite de {limite} km/h!'
else:
    resposta = f'Você excedeu o limite permitido de {limite} km/h!!'

print(resposta)