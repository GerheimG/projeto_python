import os
from exibir.agenda import adicionar_compromisso


def cadastrar_compromisso(agenda):
    os.system('cls')
    # Permite ao usuário cadastrar um compromisso na agenda
    # parâmetro agenda: Dicionário que armazena os compromissos
    print('\nCadastro de Compromisso')
    data = input('Digite a data do compromisso (formato dd/mm/aaaa): ')
    descricao = input('Digite a descrição do compromisso: ')

    # Adiciona o compromisso à agenda
    adicionar_compromisso(agenda,data, descricao)

    print(f'\nCompromisso agendado para {data}: {descricao}')