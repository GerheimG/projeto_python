# union(set2) ou |: Retorna um novo set que é a união de dois sets.

import os


os.system('cls')

# Criando as sets
seta = {1, 2, 3, 4, 5, 6, 7, 8}
setb = {9, 10, 11, 12, 13, 14, 15, 16}


a = seta.union(setb)
# Usando a função union
# A função union em um conjunto (set) retorna um novo conjunto contendo
# todos os elementos de dois ou mais conjuntos, sem duplicatas. 
# Ou seja, ela combina os elementos de ambos os conjuntos, mas mantém apenas os elementos únicos.

# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}

# resultado = conjunto1.union(conjunto2)
# print(resultado)  // Saída: {1, 2, 3, 4, 5}

# Neste exemplo:
# A união dos conjuntos {1, 2, 3} e {3, 4, 5} resulta no conjunto {1, 2, 3, 4, 5}.
# O elemento 3 é repetido nos dois conjuntos, mas na união ele aparece apenas uma vez.



# Saída
print(a)