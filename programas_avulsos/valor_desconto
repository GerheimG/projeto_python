#12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento
#pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
#Tabela de Código de Condições de Pagamento
#1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
#2 - À Vista no cartão de crédito, recebe 10% de desconto
#3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros


import os


os.system('cls')

valor = float(input('Insira o valor do produto: '))
formapagamento = input('Escolha entre pix, dinheiro  ou cartão de crédito e/ou parcelado 2 vezes: ')
resposta = ''

if formapagamento == 'pix':
    pixpag = valor * 0.15
    preco = valor - pixpag
    resposta = f'O valor será de: R${preco}'

elif formapagamento == 'dinheiro':
    dinpag = valor * 0.15
    preco2 = valor - dinpag
    resposta = f'O valor será de: R${preco2}'

elif formapagamento == 'cartão':
    cartpag = valor * 0.10
    preco3 = valor - cartpag
    resposta = f'O valor será de: R${preco3}'

else:
    formapagamento == 'parcelado'
    parcpag = valor / 2
    resposta = f'O valor será de duas parelas de R${parcpag}'


    
print(resposta)

