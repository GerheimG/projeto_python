import os

os.system('cls')

# Limite para os números
valor = int(input("Limite: "))

# Loop para verificar números primos até o valor informado
for numero in range(2, valor + 1):
    soma = 0
    for numero_primo in range(2, numero):
        if numero % numero_primo == 0:
            soma += 1
            break  # Se houver um divisor, o número não é primo, podemos parar
    if soma == 0:  # Nenhum divisor encontrado, o número é primo
        print(numero, ",", end=" ")
