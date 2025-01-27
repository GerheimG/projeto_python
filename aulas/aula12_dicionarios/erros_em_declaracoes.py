import os


os.system('cls')

print('-' * 50)
print('ESTRUTURA DE DADOS: DICIONÁRIO ') # dict => {}
print('-' * 50)

# Índices iguais: só irá exibir um item
dicionario1 = {'nome' : 'John' , 'nome' : 'Jane'}

# Posso ter uma tupla como índice e uma lista como valor
dicionario2 = {(1, 2) : [1, 2]}

# Mas não posso ter uma lista como índice e uma tupla como valor
dicionario3 = {[1, 2] : (1, 2)}

# Saída
print('-' * 50)
print(dicionario1)
print(dicionario2)

print()