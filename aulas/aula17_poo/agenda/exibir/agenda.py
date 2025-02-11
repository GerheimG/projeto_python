def adicionar_compromisso(agenda,data,descricao):
    # Adiciona um compromisso ao dicionário de compromissos.
    # Se a data já existe, adiciona o compromisso à
    # lista de compromissos dessa data

    #parâmetro agenda: Dicionário que armazena os compromissos.
    #parâmetro data: Data do compromisso.
    #parâmetro descrição: Descrição do compromisso.

    if data not in agenda:
        # Se não houver compromissos na data,
        # cria uma lista para armazená-los
        agenda[data] = []
    
    # Adiciona o compromisso na data específica
    agenda[data].append(descricao)

def listar_compromissos(agenda,data=None):
    # Exibe todos os compromissos de uma data específica ou
    # de todas as datas.

    #parãmetro agenda: Dicionário que armazena os compromissos
    #parâmetro data: Data dos compromissos a serem listados
    # (se for None, lista todos).
    if data:
        if data in agenda:
            print(f'\nCompromisso para {data}: ')
            for compromisso in agenda[data]:
                print(f'- {compromisso}')
        else:
            print(f'\nNenhum compromisso encontrado para a data {data}')
    else:
        if not agenda:
            print(f'\nNenhum compromisso agendado.')
        else:
            for data, compromissos in agenda.items():
                print(f'\nCompromissos para {data}:')
                for compromisso in compromissos:
                    print(f'- {compromisso}')