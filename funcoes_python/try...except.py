# Essencial para tratar erros durante a execução do código.

# Exemplo de tratamento de exceção
try:
    x = 1 / 0  # Gera um erro de divisão por zero
except ZeroDivisionError:
    print("Não é possível dividir por zero!")  # Saída: Não é possível dividir por zero!