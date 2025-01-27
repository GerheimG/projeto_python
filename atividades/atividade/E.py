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

if imc2 < 18.5:
    print(f'Seu imc {imc2:.2f}, Você está abaixo do peso')
elif imc2 > 18.6 and imc2 < 24.9:
    print(f'Seu imc {imc2:.2f}, Você está no peso ideal')
elif imc2 > 25.0 and imc2 < 29.9:
    print(f'Seu imc {imc2:.2f}, Você está levemente acima do peso')
elif imc2 > 30.0 and imc2 < 34.9:
    print(f'Seu imc {imc2:.2f}, Obesidade grau I')
elif imc2 > 35.0 and imc2 < 39.9:
    print(f'Seu imc {imc2:.2f}, Obesidade grau II (severa)')
else:
    imc2 >= 40
    print(f'Seu imc {imc2:.2f}, Obesidade grau III (mórbida)')
