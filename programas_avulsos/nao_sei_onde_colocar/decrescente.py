#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

import os


os.system('cls')

num1 = int(input('Insira um valor: '))
num2 = int(input('Insira um valor: '))
num3 = int(input('Insira um valor: '))

if num1 > num2 and num1 > num3 and num2 > num3:
    print(f'{num1}, {num2}, {num3}')

elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f'{num1}, {num3}, {num2}')

elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f'{num2}, {num1}, {num3}')

elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f'{num2}, {num3}, {num1}')

elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f'{num3}, {num2}, {num1}')
elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f'{num3}, {num1}, {num2}')
else:
    print(f'Todos são iguais')