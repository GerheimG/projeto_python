import os

os.system('cls')

# Criação do dicionário vazio
meu_dicionario = {}


# Loop principal do programa
while True:
    print('-' * 70)
    # Exibição do menu de opções
    print('\n Menu de Opções')
    print('1. Adicionar um par chave-valor')
    print('2. Mostra o dicionário')
    print('3. Sair')
    print('-' * 70)

    # Solicitação da escolha do usuário 
    opcao = input('Escolha uma opção (1, 3): ')

    if opcao == '1':
        # Criação de um dicionário usando fromkeys()
        chaves = input('Digite as chaves separadas por vírgula: ')
        valor_padrao = input('Digite o valor padrão para as chaves: ')

        if not chaves or not valor_padrao:
            print('Erro: Chaves ou valor padrão não podem ser vazios.')
        else:
            meu_dicionario = dict.fromkeys(chaves, valor_padrao)
            print('Dicionário criado', meu_dicionario)
    
    elif opcao == '2':
        # Verifica se o dicionário foi criado antes de tentar acessá-lo
        if meu_dicionario:
            print('Chaves disponíveis:', ', '.join(meu_dicionario.keys()))
            chave = input('Digite a chave que deseja buscar: ')
            valor = meu_dicionario.get(chave, 'Chave não encontrada')
            print('-' * 70)
            print(f"'Valor para a chave {chave}': {valor}")
        else:
            print('-' * 70)
            print('Erro! Crie um dicionário primeiro.')
    
    elif opcao == '3':
        print('Saindo do programa.')
        break

    else:
        print('Opção inválida. Tente novamente!')    