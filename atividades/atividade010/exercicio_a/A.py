# A) Crie uma função que receba uma lista de números. 
# Depois retorne duas listas com os números pares, 
# os números ímpares, a quantidade de números pares 
# e a quantidade de números ímpares.

import os
from contar.contagem import listar_numero

os.system('cls')




lista_par, lista_impar, quantidade_par, quantidade_impar = listar_numero()




# Saída
print('Lista de números pares', lista_par)
print('Quantidade de pares:', quantidade_par)
print('Lista de números ímpares', lista_impar)
print('Quantidade de ímpares:', quantidade_impar)




