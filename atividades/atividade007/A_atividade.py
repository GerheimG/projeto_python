# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

import os


os.system('cls')


print('-' * 70)
print('Para sair digite "0" ou "s"')
print('-' * 70)

lista_notas = []
soma = 0

while True:
    notas = input('Insira as notas: ')

    if notas == 's' or notas == '0':
        break

    else:
        numero = int(notas)
        soma += numero
        lista_notas.append(notas)
        continue

lista_inversa = lista_notas[::-1]
copia = lista_notas.copy()
copia.sort(reverse=True)
dividir = len(lista_notas)
media = soma / dividir

print('-' * 70)
print('Quantidade de notas:\n', len(lista_notas))
print('-' * 70)
print('Lista recebida:\n', lista_notas)
print('-' * 70)
print('Lista ordem inversa:')

for i in range(len(lista_inversa)):
    print(lista_inversa[i])
print('-' * 70)
print('Soma das notas:\n', soma)
print('-' * 70)
print(f'Média das notas:\n{media:.2f}')
print('-' * 70)

