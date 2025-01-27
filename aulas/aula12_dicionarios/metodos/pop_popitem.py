import os

os.system('cls')

# Criação do dicionário vazio
meu_dicionario = {}

while True:
    print('-' * 70)
    # Exibição do menu de opções
    print('\n Menu de Opções')
    print('1. Adicionar um par chaver_valor')
    print('2. Remover item usando pop()')
    print('3. Remover o último item usando popitem()')
    print('4. Mostrar dicionário atual')
    print('5. Sair')
    print('-' * 70)

    # Solicitação da escolha do usuário 
    opcao = input('Escolha uma opção (1, 5): ')
    if opcao == '1':
        # Adicionar um par chave-valor ao dicionário
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado')
    
    elif opcao == '2':
        # Remover um item especifico usando pop()
        if meu_dicionario:
            chave = input('Digite a chave do item que deseja remover: ')
            valor_removido = meu_dicionario.pop(chave, 'Chave não encontrada')
            print(f'Item removido: {chave}: {valor_removido}')
        else:
            print('O dicionário está vazio. Adicione itens primeiro.')
    
    elif opcao == '3':
        # Remover o ultimo item usando popitem()
        if meu_dicionario:
            chave, valor = meu_dicionario.popitem()
            print(f'Último item removido: {chave}: {valor}')
        else:
            print('O dicionário está vazio. Adicione itens primeiro.')
    
    elif opcao == '4':
        # Mostrar o dicionário atual 
        if meu_dicionario:
            print('Dicionário atual:', meu_dicionario)
        else:
            print('O dicionário está vazio')
    
    elif opcao == '5':
        print('Saindo do programa.')
        break

    else:
        print('Opção inválida. Tente novamente.')

