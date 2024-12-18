# bibliotecas
import os

# biblioteca para pegar data e hora do sistema
import datetime

#limpando terminal 
os.system('cls')


print('=' * 70)
print('Entradas de dados em Python')
print('=' * 70)

# entrada
nome = (input('Qual seu nome?: '))
peso = (input('Entre com seu peso: '))
altura = (input('Coloque sua altura: '))
nomedamae = (input('Nome da sua mãe: '))
nomedopai = (input('Nome do pai: '))
nascimentodopai = (input('Ano de nascimento do pai: '))
nascimentodamae = (input('Ano de nascimento da mãe: '))

# entrada com casting
nascimento = int(input('Ano do seu nascimento: '))
idadedamae = int(input('Qual a idade da sua mãe?: '))
idadedopai = int(input('Qual a idade do seu pai?: '))
sexualidade = str(input('Qual sua sexualidade?: '))
comidafavorita = str(input('Qual sua comida favorita?: '))
timefavorito = str(input('Qual seu time favorito?: '))
cep = int(input('Entre com seu CEP:'))
bairro = str(input('Qual seu bairro?: '))
rua = str(input('Nome da Rua: '))
numero = int(input('Entre com o número: '))
diferancapem = int(idadedopai) - int(idadedamae)
# pegando ano atual 
ano_atual = datetime.datetime.now().year
idade= int(ano_atual) - nascimento
idadedoapai = int(ano_atual) - int(nascimentodopai)
idadedamae = int(ano_atual) - int(nascimentodamae)

#saída
print('=' * 70)
print('SAÍDA DE DADOS')
print('=' * 70)
print('Nome...............: ', nome)
print('Nascimento.........: ', nascimento)
print('Peso...............: ', peso)
print('Altura.............: ', altura)


# saída interpolada
print('=' * 70)
print(f'CEP..................: {cep}')
print(f'Bairro...............: {bairro}')
print(f'Rua..................: {rua}')
print(f'Número...............: {numero}')
print('=' * 70)
print(f'Olá {nome}, você tem {idade} anos!')
print(f'Sua mãe se chama {nomedamae} e seu pai se chama {nomedopai}')
print(f'A idade de {nomedopai} é {idadedoapai} e da {nomedamae} é {idadedamae}')
print(f'A idade de sua mâe é {idadedamae} e a de seu pai é {idadedopai}')
print(f'{nomedopai} e {nomedamae} tem {diferancapem} anos de diferença')
print(f'Sua sexualidae.......: {sexualidade}')
print(f'Seu time do coração é {timefavorito} e você ama {comidafavorita}')
print('=' * 70)
print('')
