# Une múltiplos iteráveis em um único iterável.

import itertools

# Exemplo com itertools.chain
listas = [1, 2, 3], [4, 5, 6]
resultado = list(itertools.chain(*listas))
print(resultado)  # Saída: [1, 2, 3, 4, 5, 6]
