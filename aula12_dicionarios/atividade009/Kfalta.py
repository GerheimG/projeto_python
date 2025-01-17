import os

from datetime import datetime

os.system('cls')

tarefa = dict()

for i in range(1,2):
    nome = input('Digite o nome da tarefa: ').lower()
    expira = input('Digite o vencimento da tarefa: ')
    prioridade = input('Digite a prioridade: ').lower()

    tarefa[nome] = {'nome' : nome, 'expira' : expira,
                'prioridade' : prioridade}

while True:
    pergun = input('Deseja alterar algo? S/N: ').lower()

    if pergun == 's':
        item_alterado = input('Oque deseja alterar? ')
        
        if item_alterado in tarefa:
            subitem_alterado = input('Qual valor irá alterar' 
                                    '\n(nome,expira,prioridade): ')

            if subitem_alterado in tarefa[item_alterado]:
                atualizar = input('Digite a alteração: ')

                tarefa[item_alterado][subitem_alterado] = atualizar

        
        else:
            print('Item não encontrado.')
            break


prioridade_alta = 0
for keys, values in tarefa:
    if values['prioridade'] == 'alta':
        prioridade_alta += 1