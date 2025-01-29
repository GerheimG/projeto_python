# H) Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir 
# a média de altura  e peso de seus clientes. Faça um programa que pergunte
# a cada um dos clientes da academia seu código, nome, altura e peso. 
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média. 
# Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido.

import os
from calculos.calcular_media_altura import calcular_media_altura
from calculos.calcular_media_peso import calcular_media_peso

os.system('cls')


lista_clientes = []


while True:
    # Pegando as informações
    print('Para parar digite 0')
    codigo = int(input('Digite o código: '))
    if codigo == 0:
        break
    nome = input('Digite o nome: ')
    altura = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))
    pergunta = input('Deseja continuar? S para '
            'continuar ou 0 para sair: ').upper()

    # Dicionario 
    registro = {}
    registro['Código'] = codigo
    registro['Nome'] = nome
    registro['Altura'] = altura
    registro['Peso'] = peso
    
    
    # Colocando o dicionario dentro da lista
    lista_clientes.append(registro)
    
    # Limpa a tela a cada cadastro
    os.system('cls')

    # Exibe todos os clientes cadastrados até o momento
    print('Clientes cadastrados até o momento:')
    for clientes in lista_clientes:
        print('Código:', clientes['Código'])
        print('Nome:', clientes['Nome'])
        print('Altura:', clientes['Altura'])
        print('Peso:', clientes['Peso'])
        print('=' * 60)
    
    # Caso a pessoa escolha sair
    if pergunta != 'S':
        break


# Calculando a média de peso após os cadastros
if lista_clientes:
    media_peso = calcular_media_peso(lista_clientes)
    print(f'A média de peso dos clientes é: {media_peso:.2f} kg')

# Calculando a média de peso após os cadastros
if lista_clientes:
    media_altura = calcular_media_altura(lista_clientes)
    print(f'A média de altura dos clientes é: {media_altura:.2f} m')