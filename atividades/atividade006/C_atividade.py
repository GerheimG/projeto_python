# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

import os 


os.system('cls')


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
multi = []

primeiro_intervalo = lista_numeros[0:9]
segundo_intervalo = lista_numeros[7:13]
pares = lista_numeros[1:15:2]
impares = lista_numeros[0:15:2]
for i in lista_numeros:
    if (i % 2 == 0) or (i % 3 == 0) or (i % 4 == 0):
        multi.append(i)
lista_reversa = lista_numeros[::-1]
intervalo_produtos1 = lista_numeros[4:6]
intervalo_produtos2 = lista_numeros[10:12]

produto = [
    a * b
    for a in intervalo_produtos1
    for b in intervalo_produtos2
]

print('=' * 60)
print('O intervalo de 1 até 9:\n', primeiro_intervalo)
print('-' * 60)
print('O intervalo de 8 até 13:\n', segundo_intervalo)
print('-' * 60)
print('Os números pares:\n', pares)
print('-' * 60)
print('Os números ímpares:\n', impares)
print('-' * 60)
print('Os múltiplos de 2, 3 e 4:\n', multi)
print('-' * 60)
print('Lista reversa:\n', lista_reversa)
print('-' * 60)
print('O produto dos intervalos 5-6 por 11-12:\n',produto)
print('=' * 60)