# Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os


os.system('cls')

inicio = int(input('Insira um valor para iniciar: '))
fim = int(input('Insira um valor para terminar: '))

for i in range(inicio, fim + 1):

    if i == 17:
        continue
    
    elif i == 23:
        continue
    
    elif i == 38:
        continue

    print(i)
        

    