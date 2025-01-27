# difference(set2) ou -: Retorna um novo set com os elementos do primeiro set que não estão no segundo set.

import os


os.system('cls')

# Criando os sets
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setb = {9, 10, 11, 12, 13, 14, 15, 16}

# Usando a função difference
# A função difference em um conjunto (set) retorna um novo conjunto contendo 
# os elementos que estão presentes no conjunto original, mas não estão em outro(s) conjunto(s) fornecido(s). 
# Em outras palavras, ela calcula a diferença entre o conjunto original e os outros conjuntos passados como argumento.
# conjunto1 = {1, 2, 3, 4}
# conjunto2 = {3, 4, 5, 6}
# resultado = conjunto1.difference(conjunto2)
# print(resultado)  # Saída: {1, 2}

a = seta.difference(setb)

# Saída
print(a)