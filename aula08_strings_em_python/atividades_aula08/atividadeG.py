# G) Faça um programa que receba um número inteiro e mostre na tela:
# A quantidade de unidades, a quantidade de dezenas, a quantidade 
# de centenas e a quantidade de milhares.


import os


os.system('cls')

numero = int(input('Insira um número: '))

if numero > 9999 or numero < 0:
    print('NÚMERO INVÁLIDO')
    exit()
else:
    
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = (numero % 10) // 1


print(f'Milhar {milhar}, centena {centena}, \
dezena {dezena}, unidade {unidade}')