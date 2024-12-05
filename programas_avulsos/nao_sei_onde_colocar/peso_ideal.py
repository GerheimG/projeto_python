#calculando o peso ideal H ou M 
 

import os


os.system('cls')

genero = str(input('Coloque seu gênero: ')).capitalize()

if genero != 'Homem' and genero != 'Mulher':
      print('ERRO')
      exit()
else:
      pass

altura = float(input('Insira sua altura: '))
resposta = ''


if genero == 'Homem':
        pesoidealH = (72.7 * altura) - 58
        resposta = f'Seu peso ideal sendo {genero} é {pesoidealH:.2f}'

elif genero == 'Mulher':
    pesoidealM = (62.1 * altura) - 44.7
    resposta = f'Seu peso ideal sendo {genero} é {pesoidealM:.2f}'
        

print(resposta)