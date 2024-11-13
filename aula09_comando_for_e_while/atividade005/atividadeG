# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

inicio = int(input('Insira um valor para iniciar: '))
fim = int(input('Insira um valor para terminar:'))


# Iteração no intervalo 0 a 100
for numero in range(inicio, fim):

    # Se menor que 2, o loop salta
    if numero < 2:
        continue

    # Validação do número primo
    primo = True # Assume que o número é primo
    for divisor in range(2, int(numero ** 0.5) + 1): # Iteração para divisores entre 2 e ²v numero + 1 (raiz quadrada)
        if numero % divisor == 0: # Se resto da divisão for 0
            primo = False # Primo recebe falso
            break # Encerra o ciclo, pois achou um divisor

    if primo: # Se no final, mantiver primo
        print(f'{numero}') # Imprimir o numero do 1º loop

