# O método add em um conjunto (set) no Python é utilizado para adicionar um único elemento ao conjunto.

import os


os.system('cls')

# Criando um set
set = {1, 2, 3, 4, 5, 6, 7, 8}

set1 = {'1', '2', '3', '4', '5', '6', '7', '8'}


# Usando a função add
# A função add em um conjunto (set) adiciona um elemento ao conjunto. 
# Se o elemento já estiver presente, não faz nada; se não estiver, o adiciona. 
# O set não permite duplicatas, então cada elemento é único dentro dele.
set.add(9)
set1.add('9')

# Saída

# SE O SET FOR EM INTEIRO SAI EM ORDEM
print(set)

# SE O SET FOR EM FORMA DE STRINGS NÃO SAI EM ORDEM
print(set1)
