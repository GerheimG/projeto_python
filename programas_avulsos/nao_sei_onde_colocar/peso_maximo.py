#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.

import os

os.system('cls')

peso = float(input('Quantos kilos de peixes? '))


peso >= 50
multa = (peso - 50)
valormulta = multa * 4

if peso > 50:
    print(f'O valor da sua multa será R${valormulta:.2f} reais')

else:
    print(f'Seu peixe está dentro do peso permitido')