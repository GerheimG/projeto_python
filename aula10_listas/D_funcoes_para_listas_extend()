import os 


os.system('cls')

# Inicializa a lsita vazia
lista_numeros = [100, 200]

# Solicita o usuário a inserir números separados por espaço
entrada = input('Digite números separados por espaços: ')

# Divide a string de etreda em uma lista de strings
numeros = entrada.split()

# Cria uma lista para armazenar os pares
pares = []

# Itera sobre os números inseridos 
for numero in numeros:
    # Converte a string para inteiro
    numero_aux = int(numero)
    # Verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par a lista pares
        pares.append(numero_aux)

print('-' * 60)
print(f'Lista gerada: {pares}')
print('-' * 60)

# Usa extend() para adicionar todos os números pares à lista principal 
lista_numeros.extend(pares)

# Exibe a tela resultante
print(f'Números pares adicionados à lista: {lista_numeros}')