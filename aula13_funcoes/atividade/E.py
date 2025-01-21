# E) Crie uma função que receba
# a altura e o peso de uma pessoa. 
# Depois retorne o seu IMC.

import os


os.system('cls')


def calcular(altura, peso):
    # Calculando imc
    imc = peso / (altura ** 2)

    return imc

altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))


# Invocando a função
imc2 = calcular(altura, peso)

print(f'Seu IMC: {imc2:.2f}')