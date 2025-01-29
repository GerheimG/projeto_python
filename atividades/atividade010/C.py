# C) Crie uma função que verifica se uma aluno(a)
# está cadastrado ou não em um dicionário. 
# Se estiver cadastrado, imprima o nome desse aluno e o 
# resto dos seus dados. O dicionário deverá conter nome, 
# matrícula e a data de nascimento do aluno.

import os


os.system('cls')

alunos_dict = {}

alunos_lista = []

def aluno():
    # Recebendo os dados do aluno
    nome = input('Insira o nome do aluno: ').capitalize().strip()
    matricula = int(input('Insira o número de matrícula: '))
    data = input('Insira a data de nascimento: ')

    # Colocando dentro da lista
    alunos_dict = {'Nome': nome, 'Matricula': matricula, 'Data': data}
    alunos_lista.append(alunos_dict)
    print(alunos_lista)
    return nome, matricula, data



def verificar_aluno():
    pergunta = input('Qual aluno irá verificar? ').capitalize().strip()
    
    # Verificando se o aluno está na lista
    for aluno in alunos_lista:
        if aluno['Nome'] == pergunta:
            print('Nome: ', aluno['Nome'])
            print('Matrícula: ', aluno['Matricula'])
            print('Data de Nascimento: ', aluno['Data'])
            break
    else:
        print('Aluno não está cadastrado.')

resultado = aluno()
verificar_aluno()