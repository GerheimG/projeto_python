# Combina dois ou mais iteráveis em um único iterável de tuplas.

# Exemplo com zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Saída: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]