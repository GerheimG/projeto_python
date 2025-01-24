# B) Crie uma função que cadastre o nome de um aluno(a),
# a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados
# utilizando uma estrutura de repetição for.

import os


os.system('cls')


alunos_lista = []

def aluno():
    dicionario = {}
    
    # Recebendo os dados do aluno
    nome = input('Insira o nome do aluno: ')
    matricula = int(input('Insira o número de matrícula: '))
    data = input('Insira a data de nascimento (dd/mm/yy):  ')

    dicionario['Nome'] = nome
    dicionario['Matricula'] = matricula
    dicionario['Data'] = data

    alunos_lista.append(dicionario)

    return dicionario

cadastro = aluno()

for i in alunos_lista:
    print('Nome:',i['Nome'])
    print('Matricula:',i['Matricula'])
    print('Data:',i['Data'])