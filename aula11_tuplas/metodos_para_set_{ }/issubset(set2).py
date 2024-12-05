# Verifica se o set é um subconjunto de outro set.

import os


os.system('cls')

# Criando as setas
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setb = {1, 2, 3, 4, 5}


a = setb.issubset(seta)
# Usando a função issubset
# A função issubset em um conjunto (set) verifica se todos os elementos
#  do conjunto atual estão presentes em outro conjunto. Em outras palavras, 
# ela retorna True se o conjunto atual for um subconjunto do conjunto fornecido,
# ou seja, se o conjunto atual tiver todos os seus elementos dentro do outro conjunto. 
# Caso contrário, retorna False.

# conjunto1 = {1, 2, 3}
# conjunto2 = {1, 2, 3, 4, 5}
# resultado = conjunto1.issubset(conjunto2)
# print(resultado)  // Saída: True

# Neste exemplo, conjunto1 é um subconjunto de conjunto2, porque todos os elementos de conjunto1 estão presentes em conjunto2.
# Se conjunto1 tivesse um elemento que não está em conjunto2, o resultado seria False.

# Exemplo de False:

# conjunto1 = {1, 2, 6}
# conjunto2 = {1, 2, 3, 4, 5}
# resultado = conjunto1.issubset(conjunto2)
# print(resultado) // Saída: False

# Neste caso, 6 não está em conjunto2, então conjunto1 não é um subconjunto de conjunto2.


# Saída
print(a)