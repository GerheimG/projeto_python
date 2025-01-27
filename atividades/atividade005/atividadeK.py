# Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.


import os


os.system('cls')

para = print('APERTE "s" para parar')

while True:
    frase = input('Insira uma frase ou nome: ').lower().strip()

    invertida = frase[::-1]
    
    if frase == 's':
        break


    if frase == invertida:
        print('É um palíndromo')
        
    else:
        print('Não é um palíndromo') 