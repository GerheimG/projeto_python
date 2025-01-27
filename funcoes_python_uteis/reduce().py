# Aplica uma função cumulativa aos itens de um iterável, de modo que o resultado final seja um único valor

from functools import reduce

# Exemplo com reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Saída: 24 (1 * 2 * 3 * 4)

