import os


os.system('cls')

viagem = {}

for i in range(1,2):
    destino = input('Insira o destino: ').lower()
    data_Partida = input('Data de partida: ')
    duracao = int(input('Duração da viagem: '))
    vagas_dispon = int(input('Vagas disponiveis: '))

    viagem[destino] = {'Data' : data_Partida, 'Duração' : duracao,
                    'Vagas Disponiveis' : vagas_dispon}

