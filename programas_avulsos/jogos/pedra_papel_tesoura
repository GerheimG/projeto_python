# JOKENPO CONTRA A MAQUINA


# IMPORTANDO AS BIBLIOTECAS
import os
import random

# LIMPANDO O TERMINAL
os.system('cls')

# CRIANDO UMA LISTA
escolhas = ['pedra', 'papel', 'tesoura']

# ENTRADA DE DADOS
sua_escolha = input('Escolha entre pedra, papel ou tesoura: ').lower().strip()

# LIMITAR AS ESCOLHAS DO USUÁRIO
if sua_escolha not in escolhas:
    print('Escolha uma opção válida')
    exit()

else:
    pass

# FAZENDO A MÁQUINA ESCOLHER UMA OPÇÃO

escolha_maquina = random.choice(escolhas)


# DECLARANDO AS CONDICIONIAS 
if sua_escolha == 'papel' and escolha_maquina == 'pedra':
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, você ganhou')

elif sua_escolha == 'papel' and escolha_maquina == 'tesoura':
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, você perdeu')

elif sua_escolha == 'pedra' and escolha_maquina == 'papel':
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, você perdeu')

elif sua_escolha == 'pedra' and escolha_maquina == 'tesoura':
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, você ganhou')

elif sua_escolha == 'tesoura' and escolha_maquina == 'pedra':
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, você perdeu')

elif sua_escolha == 'tesoura' and escolha_maquina == 'papel':
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, você ganhou')

else:
    sua_escolha == escolha_maquina
    print(f'Você escolheu {sua_escolha} e a máquina {escolha_maquina}, então empate!')
