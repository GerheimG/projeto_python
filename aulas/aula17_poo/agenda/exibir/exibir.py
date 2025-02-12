import os
from exibir.agenda import listar_compromissos


def exibir_agenda(agenda):
    os.system('cls')
    # Exibi todos os compromissos agendados ou apenas os compromissos
    # de uma data especifica

    # parâmetro agenda: Dicionário que armazena os compromissos.

    print('\nExibindo Compromissos Agendados')
    opcao = input('Todos os compromissos ou por data? (t/d): ').lower()

    if opcao == 't':
        # Lista todos os compromissos
        listar_compromissos(agenda)
    elif opcao == 'd':
        # Lista compromissos de uma data específica
        data = input(
            'Digite a data dos compromissos(formato dd/mm/aaaa): '
        )
        listar_compromissos(agenda, data)
    else:
        print('\nOpção inválida! "t" para todos ou "d" para data')