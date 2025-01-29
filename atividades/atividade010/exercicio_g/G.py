# G) Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11.
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto :
# 4. Divisão : 5. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. 
# Em seguida, você criará funções que retornem
# os resultados das operações, imprimindo os resultados na tela.

import os
from matematica_basica import somar, subtrair, multiplicar, dividir
from matematica_basica import divisao_inteira, resto_divisao

os.system('cls')



while True:
    a = float(input('Escolha o valor A, maior que 0 e menor que 11: '))
    if a < 0 or a > 11:
        print('Escolha um valor válido ')
        input('Pressione enter...')
        os.system('cls')
        continue
    b = float(input('Escolha o valor B, maior que 0 e menor que 11: '))
    if b < 0 or b > 11:
        print('Escolha um valor válido ')
        input('Pressione enter...')
        os.system('cls')
        continue

    else:
        os.system('cls')
        break

print(f'Valores escolhidos {a} e {b}')
print('=' * 60)
print('1 - Soma')
print('2 - Subtração')
print('3 - Produto')
print('4 - Divisão')
print('5 - Divisão Inteira')
print('6 - Resto da divisão')
opcao = int(input('Escolha 1 ao 6: '))

if opcao == 1:
    print(f'A soma de {a} e {b} é: {somar.somar(a,b):.2f} ')

elif opcao == 2:
    print(f'A subtração de {a} e {b} é: {subtrair.subtrair(a,b):.2f} ')

elif opcao == 3:
    print(f'O produto de {a} e {b} é: {multiplicar.multiplicar(a,b):.2f} ')

elif opcao == 4:
    print(f'A divisão de {a} e {b} é: {dividir.dividir(a,b):.2f} ')

elif opcao == 5:
    print(f'A divisão inteira de {a} e {b} é: {divisao_inteira.divisao_inteira(a,b):.2f} ')

elif opcao == 6:
    print(f'O resto da divisão de {a} e {b} é: {resto_divisao.resto_divisao(a,b):.2f} ')