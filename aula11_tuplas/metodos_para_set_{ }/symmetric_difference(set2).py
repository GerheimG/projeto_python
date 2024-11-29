# symmetric_difference(set2) ou ^: Retorna um novo set com elementos que estão em um dos sets, mas não em ambos.

import os


os.system('cls')

# Criando um set
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
setb = {9, 10, 11, 12, 13, 14, 15, 16}


a = seta.symmetric_difference(setb)
# Usando a função symmetric difference
# A função symmetric_difference em um conjunto (set) retorna um novo conjunto contendo 
# os elementos que estão em um conjunto ou no outro, mas não em ambos. 
# Em outras palavras, ela calcula a diferença simétrica entre dois conjuntos, ou seja,
#  os elementos exclusivos de cada conjunto (sem considerar os elementos comuns).

# conjunto1 = {1, 2, 3, 4}
# conjunto2 = {3, 4, 5, 6}

# resultado = conjunto1.symmetric_difference(conjunto2)
# print(resultado) // Saída: {1, 2, 5, 6}

# Neste exemplo:

# Os elementos 1 e 2 estão em conjunto1, mas não em conjunto2.
# Os elementos 5 e 6 estão em conjunto2, mas não em conjunto1.
# Os elementos 3 e 4 são comuns aos dois conjuntos e não aparecem no resultado.



# Saída
print(a)