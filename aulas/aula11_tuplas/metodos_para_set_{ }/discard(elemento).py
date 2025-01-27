# Remove um elemento do set se ele estiver presente. Não faz nada se o elemento não estiver presente.

import os


os.system('cls')

# Criando a set
set = {1, 2, 3, 4, 5, 6, 7, 8}


set.discard(4)
# Usando a função discard
# A função discard em um conjunto (set) remove um elemento específico do conjunto, se ele estiver presente. 
# Se o elemento não estiver no conjunto, a função não faz nada e não gera erro.
# Diferente de remove, que gera um erro se o elemento não for encontrado, 
# o discard simplesmente ignora a operação nesse caso.

# conjunto = {1, 2, 3, 4}
# //Removendo um elemento que existe
# conjunto.discard(3)
# print(conjunto)  # Saída: {1, 2, 4}
# // Tentando remover um elemento que não existe
# conjunto.discard(5)
# print(conjunto)  // Saída: {1, 2, 4} (sem alteração)



# Saída
print(set)
