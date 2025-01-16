import os


os.system('cls')

viagem = {}

for i in range(1,2):
    destino = input('Insira o destino: ').lower()
    data_Partida = input('Data de partida: ')
    duracao = (input('Duração da viagem: '))
    vagas_dispon = int(input('Vagas disponiveis: '))

    viagem[destino] = {'destino' : destino, 'data' : data_Partida,
                'duração' : duracao,'vagas disponiveis' : vagas_dispon}
    
menos_que_dez = 0

for keys, values in viagem.items():
    if values['vagas disponiveis'] <= 10:
        menos_que_dez += 1





