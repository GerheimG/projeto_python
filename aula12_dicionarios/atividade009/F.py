import os

os.system('cls')

dados = {'nome': 'john', 'idade': '40' , 'peso': '80', 'altura': '1.70'}

for keys, values in dados.items():
    print(f'{keys}: {values}')



del dados['peso']

print('=' * 70)

for keys, values in dados.items():
    print(f'{keys}: {values}')
