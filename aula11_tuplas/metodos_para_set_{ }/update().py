import os

os.system('cls')

# Criando um conjunto inicial
conjunto = {1, 2, 3}
print("Conjunto inicial:", conjunto)

# Usando o método update com uma lista
# Adiciona elementos da lista [3, 4, 5] ao conjunto.
# Note que o elemento '3' já está no conjunto, então não será duplicado.
conjunto.update([3, 4, 5])
print("Após update com uma lista:", conjunto)  # Saída: {1, 2, 3, 4, 5}

# Usando o método update com um conjunto
# Adiciona os elementos do conjunto {5, 6, 7}.
# O elemento '5' já está presente, então só '6' e '7' serão adicionados.
conjunto.update({5, 6, 7})
print("Após update com outro conjunto:", conjunto)  # Saída: {1, 2, 3, 4, 5, 6, 7}

# Usando o método update com uma tupla
# Adiciona os elementos da tupla (7, 8, 9).
# O elemento '7' já está presente, então só '8' e '9' serão adicionados.
conjunto.update((7, 8, 9))
print("Após update com uma tupla:", conjunto)  # Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Usando o método update com múltiplos iteráveis
# Adiciona elementos de múltiplos iteráveis (conjunto, lista e tupla).
conjunto.update({10, 11}, [12, 13], (14, 15))
print("Após update com múltiplos iteráveis:", conjunto)
# Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# Comparação entre add e update:
# Usando add para adicionar um único elemento
conjunto.add(16)
print("Após add de um único elemento (16):", conjunto)  # Saída: {1, 2, ..., 16}

# Usando update para adicionar múltiplos elementos
conjunto.update([17, 18])
print("Após update com múltiplos elementos (17 e 18):", conjunto)  # Saída: {1, 2, ..., 16, 17, 18}
