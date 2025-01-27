# Retorna um objeto iterável que contém tuplas com o índice e o valor de cada item em um iterável.

# Exemplo com enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Saída:
# 0: apple
# 1: banana
# 2: cherry