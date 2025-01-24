#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

import os

os.system('cls')

# Entrada de dados
num1 = int(input('Insira um valor: '))
num2 = int(input('Insira um valor: '))
num3 = int(input('Insira um valor: '))

# Verificando se todos são iguais
if num1 == num2 == num3:
    print('Todos são iguais')
else:
    # Ordenando os números de forma crescente e depois imprimindo em ordem decrescente
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    print(", ".join(map(str, numeros)))
