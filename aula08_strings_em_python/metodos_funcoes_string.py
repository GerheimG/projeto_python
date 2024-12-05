import os 


os.system('cls')

print('-'*70)
print('Funções String')
print('-'*70)

frase1 = 'Olá Mundo!'
quantidade_de_caracteres = len(frase1) # conta os caracteres
print(f'A frase {frase1} \ncontém {quantidade_de_caracteres} caracteres')
print('=' * 70)

minusculas = frase1.lower()  # frase em minusculo
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('=' * 70)

capitalizada = frase1.capitalize() # frase capitaçizada
print(f'Frase original: {frase1}')
print(f'Frase nova: {capitalizada}')
print('=' * 70)

frase2 = '     Olá, Mundo       '
sem_espacos = frase2.strip() # retirar os espaços antes e depois
print(f'Frase original: {frase2}')
print(f'Frase nova: {sem_espacos}')
print('=' * 70)

substituicao = frase1.replace('Mundo', 'Python')  # troca palavra
print(f'Frase original: {frase1}')
print(f'Frase nova: {substituicao}')
print('=' * 70)

lista = frase1.split(',') #separa as palavras de uma str em uma lista
print(f'Frase original: {frase1}')
print(f'Frase nova: {lista}')
print('=' * 70)

lista = ['Olá', 'mundo']
juncao = '-'.join(lista) # transformou uma lista em uma string com separador
print(f'Frase original: {lista}')
print(f'Frase nova: {juncao}')
print('=' * 70)