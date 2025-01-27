# Retorna todas as combinações possíveis de um iterável com um determinado tamanho.

import itertools

# Exemplo com itertools.combinations
itens = [1, 2, 3]
combinacoes = itertools.combinations(itens, 2)
print(list(combinacoes))  # Saída: [(1, 2), (1, 3), (2, 3)]