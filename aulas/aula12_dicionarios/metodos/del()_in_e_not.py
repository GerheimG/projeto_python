import os


agenda = {
    'Jojo': '991962-3030',
    'Dio': '991962-5050',
    'Jolyne': '991962-6060',
    'Lisa Lisa': '991962-7070',
    'Speedwagon': '991962-8080',
    'Zeppeli': '991962-9090',
    'Suzie Q': '991962-0000'
}

while True:
    os.system('cls')

    print('-' * 70)
    print('\nAgenda de Contatos:')
    for nome, telefone in agenda.items():
        print(f'{nome}: {telefone}')
    print('-' * 70)

    # Primeiro teste: verificar se 'Jojo' está no dicionário
    if 'Jojo' in agenda:
        print('Primeiro teste: verificando se Jojo está no Dicionário')
        print('VERDADEIRO! Jojo está no Dicionário')
    else:
        print('FALSO! Jojo não está no Dicionário')

    print()

    # Segundo teste: verificar se 'John' não está no dicionário 
    if 'John' not in agenda:
        print('Segundo teste: verificando se Jojo não está no Dicionário')
        print('VERDADEIRO! Jojo não está no Dicionário')
    else:
        print('FALSO! Jojo está no Dicionário')

    print('-' * 70)
    print()

    # Exibição do menu de opções
    print('\n Menu de Opções')
    print('1. Adicionar um contato')
    print('2. Remover um contato')
    print('3. Verificar um contato específico')
    print('4. Mostrar agenda')
    print('5. Sair')
    print('-' * 70)

    opcao = input('Escolha uma opção (1-5): ')

    if opcao == '1':
        # Adicionar um contato 
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print(f'Contato {nome}: {telefone} adicionado')
    
    elif opcao == '2':
        # Remover um contato
        nome = input('Digite o nome do contato que deseja remover: ')
        if nome in agenda:
            del agenda[nome]
            print(f'Contato {nome} removido ')
        else:
            print(f'Contato {nome} não encontrado na agenda')

    elif opcao == '3':
        # Verificar contato específico
        nome = input('Digite o nome do contato que deseja verificar: ')
        if nome in agenda:
            print(f'Contato encontrado - {nome}: {agenda[nome]}')
        else:
            print(f'Contato {nome} não encontrado na agenda.')
    
    elif opcao == '4':
        # Mostrar agenda atual
        print('\nAgenda de Contatos')
        print(agenda)

    elif opcao == '5':
        print('Saindo do programa')
        break

    else:
        print('Opção inválida. Tente novamente.')

    # Pausa para o usuário ver as mensagens antes de limpar a tela
    input('\nPressione Enter para continuar...')