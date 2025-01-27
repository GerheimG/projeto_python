#importando as bibliotecas

import os

# Podemos importar so as funções que queremos utilizar
from datetime import datetime
from datetime import date

# Limpando terminal
os.system('cls')

#Declarando uma variavel para data
data = datetime.now()

#declarando uma variavel data formatada
data_formatada = data.strftime('%d/%m/%Y')

#declarando uma variavel data e hora formatada
data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')
print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatada: {data_hora_formatada}')

#recebendo o ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# Imprimindo a data atual e o nascimento
print('='*50)
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........:{nascimento}')
#imprimindo só o ano
print(f'Ano atual............:{data_atual.year}')
#imprindo só a idade
print(f'Sua idade é..........:{idade} anos')