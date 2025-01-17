import os

from datetime import datetime

os.system('cls')

viagens = {}

for i in range(1,2):
    destino = input('Insira o destino: ').lower().strip()
    duracao = input('Insira a duração: ').lower().strip()
    data = input('Insira a data: ')
    vaga = int(input('Quantas vagas disponiveis: '))


    data = datetime.strptime(data,'%d/%m/%Y')


    viagens[destino] = {'duração' : duracao, 'data' : data, 'vaga' : vaga}

while True:
    pergunt = input('Deseja alterar algo: s/n').lower().strip()

    if pergunt == 's':
        item_alterar = input('Destino que deseja alterar: ').lower().strip()

        if item_alterar in viagens:
            subitem_alterar = input('Qual valor irá alterar: '
                                    '\n(data,vaga)')
            if subitem_alterar in viagens[item_alterar]:
                atualizar = input('Digite a alteração: ')

                if subitem_alterar == 'data':
                    atualizar = datetime.strptime(atualizar, '%d/%m/%Y')
                
                if subitem_alterar == 'vaga':
                    atualizar = int(atualizar)

                    viagens[item_alterar][subitem_alterar] = atualizar



    else:
        print('fechando')
        break

data_limite = '1/6/2025'
data_limite = datetime.strptime(data_limite, ('%d/%m/%Y'))

data_longa = 0
menos_vagas = 0
for keys, values in viagens.items():
    if values['vaga'] < 10:
        menos_vagas += 1
    if values['data'] >= data_limite:
        data_longa += 1

ordem_viagem = dict(sorted(viagens.items(), key= lambda x: x[0]))

for keys, values in ordem_viagem.items():
    print(f'O destino: {destino.capitalize()}')
    print('A data: ',values['data'].strftime('%d/%m/%Y'))
    print('Duração:', values['duração'])
    print('Vagas:' ,values['vaga'])
    print(f'Menos que 10 vagas: {menos_vagas} ')
    print('Viagens com data distante de 1/6/2025: ', data_longa)
    print('Viagens ordenadas por data\n:', ordem_viagem)
    print('-' * 70)



