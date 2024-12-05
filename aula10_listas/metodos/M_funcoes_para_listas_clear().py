import os 


os.system('cls')

# Solicita o usuário a inserir números seperados por espaços 
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista  de strings em uma lista de inteiros 
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para decidir se deseja limpar a lista 
escolha = input('Deseja limpar a lista/ (s/n): ').strip().lower()


# Exibe a lista fornecida para referência 
print(f'Lista fornecida: {numeros}')

# Verifica a escolha do usuário e limpa se a resposta for 's'
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa:', numeros)
else:
    print('A lista não foi limpa.') 
