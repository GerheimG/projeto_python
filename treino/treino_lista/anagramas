# Dada uma lista de palavras, crie uma função que agrupe as palavras que são anagramas (ou seja, as palavras que têm os mesmos caracteres, mas em uma ordem diferente).

import os


os.system('cls')

lista = []
anagramas = []


print('-' * 50)
print('PRESSIONE "S" PARA SAIR')
print('-' * 50)

while True:
    palavras = input('Insira uma palavra: ')
    inverso = palavras[::-1]
    if palavras == 's':
        print('Saindo...')
        break
    if palavras == inverso:
        anagramas.append(palavras)
    else:
        lista.append(palavras)
        continue

print('Palavras que não são anagramas:', lista)
print('Palavras que são anagramas:', anagramas)