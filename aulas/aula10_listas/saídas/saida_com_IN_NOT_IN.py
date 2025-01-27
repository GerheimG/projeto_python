import os


os.system('cls')

print('-' * 60)
print('SAÍDA COM IN E NOT IN')
print('-' * 60)

# Exemplo com in 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (3 in lista_numeros):
    print(lista_numeros)
    posicao = lista_numeros.index(3)
    print(f'O número 3 está na posição {posicao}')
else:
    print('O elemento não consta na listagem')

print()

# Exemplo com not in
lista_nomes = ['John', 'Jane', 'Carol']

if ('Maira' not in lista_nomes):
    # Antes
    print(lista_nomes)

    # Não está na lista, acrescentar 
    lista_nomes.append('Maria')
    
    print('\nO nome Maria foi acrescentado')
    print(lista_nomes)

print()
print('-' * 60)
print('Fim do Programa!')
print('-' * 60)
