#  Leia a idade de 20 pessoas e exiba quantas pessoas são maiores de idade. 

import os


os.system('cls')

soma = 0

for i in range(1,21):
    idade = int(input(f'Contagem de maior de idade {i}ª: '))

    if idade < 18:
        print('Você é menor de idade')
        continue
    
    else:
        print('Você é maior de idade')