# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista

import os


os.system('cls')

lista = ['Guilherme', 'Laura', 'Bruno', 'João', 'Lucão', 'Claudyney']

print(lista)
if 'Pedro' not in lista:
    print('Pedro não está presente na lista')
else:
    print('Pedro está presente na lista')