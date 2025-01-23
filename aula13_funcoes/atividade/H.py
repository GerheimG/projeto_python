# H) Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir 
# a média de altura  e peso de seus clientes. Faça um programa que pergunte
# a cada um dos clientes da academia seu código, nome, altura e peso. 
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média. 
# Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido.

import os


os.system('cls')


clientes_dict = {}

clientes_lista = []


def clientes(codigo,nome,altura,peso):
    return {'Código': codigo,'Nome': nome,'Altura': altura, 'Peso': peso}


while True:
    # Recebendo informações
    print('Para parar digite 0')
    codigo = int(input('Digite seu código: '))
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    pergunta = input('Deseja continuar? S para continuar ou 0 para sair: ')

    if pergunta == 'S':
        os.system('cls')  # Limpar a tela para o próximo cadastro
        continue
    if pergunta == '0':
        break

    # Colocando dentro da lista
    clientes_cadastro = clientes(codigo,nome,altura,peso)
    clientes_lista.append(clientes_cadastro)

def calcular_media_peso():
    somar_pesos = sum(clientes_dict['Peso'] for cliente in clientes_dict)
    media_peso = somar_pesos / len(clientes_lista)
    return media_peso

media_peso = calcular_media_peso()

print(clientes_lista)
print(media_peso)


# media_altura = somar_altura / len(clientes_dict)
# somar_altura = sum(clientes_dict['Altura'] for n in clientes_dict)