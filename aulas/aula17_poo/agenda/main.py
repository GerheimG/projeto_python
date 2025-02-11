import os
from exibir.cadastro import cadastrar_compromisso
from exibir import exibir_agenda

def main():
    os.system('cls')
    # Agenda será um dicionário onde a chave é a data e o
    # valor é uma linha de compromissos.
    agenda = {}

    while True:
        print(f'\nAgenda de Compromissos')
        print('-'*60)
        print('1. Cadastrar compromisso')
        print('2. Exibir compromissos')
        print('3. Sair')

        opcao = input('Escolha uma opção (1/2/3): ')

        if opcao == '1':
            # Cadastrar compromisso
            cadastrar_compromisso(agenda)
        elif opcao == '2':
            exibir_agenda(agenda)
        elif opcao == '3':
            # Sair do programa
            print('\nSaidno da agenda...')
            break
        else:
            print('\nOpção inválida! Por favor, escolha 1, 2, 3.')

# Garante que a função main() só será executada se o arquivo
# for executado diretamente

if __name__ == '__main__':
    main()