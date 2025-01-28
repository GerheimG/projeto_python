# A) Crie uma função que receba uma lista de números. 
# Depois retorne duas listas com os números pares, 
# os números ímpares, a quantidade de números pares 
# e a quantidade de números ímpares.

import os


os.system('cls')



def listar_numero(numero):
    
    lista_par = []
    lista_impar = []
    # Descobrir quais são pares ou ímpares
    for n in lista:
        if n % 2 == 0:
            lista_par.append(n)
        else:
            lista_impar.append(n)
        # Contando os pares e ímpares
        quantidade_par = len(lista_par)
        quantidade_impar = len(lista_impar)
    
    return lista_par, lista_impar, quantidade_par, quantidade_impar

# Definindo a lista de número
lista = (1,2,3,4,5,6,7,8,9,10)

# Chamando a função
lista_par, lista_impar, quantidade_par, quantidade_impar = listar_numero(lista)

# Saída
print('Lista de números pares', lista_par)
print('Quantidade de pares:', quantidade_par)
print('Lista de números ímpares', lista_impar)
print('Quantidade de ímpares:', quantidade_impar)




