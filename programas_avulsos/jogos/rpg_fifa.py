import os
import random

os.system('cls')



escolhas = ['meio', 'direita', 'esquerda', 'ângulo', 'canto direito', 'canto esquerdo']

goleiro = random.choice(escolhas)
outro_jogador = random.choice(escolhas)


pergunta = input('Você quer bater o pênalti? ').lower().strip()

if pergunta != 'sim' and pergunta != 'não':
    print('opção invalida')
    exit()
else:
    pass

if pergunta == 'sim':
    pass

elif pergunta == 'não':
    print('Outro jogador irá bater')
    input('pressione enter')
    print('Ele está indo para a cobrança')
    input('pressione enter')
    print('Ele caminha lentamente em direção a bola e....')
    input('pressione enter')

    if outro_jogador == goleiro:
        print(f'Ele bateu no {outro_jogador} e o goleiro pulou no {goleiro}')
        print('O goleiro pega o pênalti e garante a vitória do time')
        print('FINAL DA PARTIDA')
        exit()

    else:
        print(f'Ele bateu no {outro_jogador} e o goleiro pulou no {goleiro}')
        print('O outro jogador ganha todo o crédito da partida e seu time sai vitorioso')
        print('FINAL DA PARTIDA')
        exit()

    
chute = input('Onde você irá chutar(meio,direita,esquerda,ângulo,canto direito ou esquerdo)? ').lower().strip()

if chute not in escolhas:
    print('Opção inválida')
    exit()
else:
    pass

if chute == goleiro:
    print(f'Você chutou no {chute} e o goleiro pulou no {goleiro}')
    print('VOCÊ ERROU')

elif chute != goleiro:
    print(f'Você chutou no {chute} e o goleiro pulou no {goleiro}')
    print('Você marcou o gol!!!')


