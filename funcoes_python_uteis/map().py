# Aplica uma função a todos os itens de um iterável (como uma lista ou tupla).

# Exemplo com map
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Saída: [1, 4, 9, 16]