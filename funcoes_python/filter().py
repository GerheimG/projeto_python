# Filtra elementos de um iterável com base em uma condição.

# Exemplo com filter
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Saída: [2, 4]