# Cria uma nova função com alguns dos argumentos já fixados.

from functools import partial

# Exemplo com partial
def somar(a, b):
    return a + b

soma_10 = partial(somar, 10)
print(soma_10(5))  # Saída: 15 (10 + 5)
