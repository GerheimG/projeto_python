# C) Crie uma função que verifica se uma aluno(a)
# está cadastrado ou não em um dicionário. 
# Se estiver cadastrado, imprima o nome desse aluno e o 
# resto dos seus dados. O dicionário deverá conter nome, 
# matrícula e a data de nascimento do aluno.

import os


os.system('cls')

alunos_dict = {}

alunos_lista = []

def aluno(nome,matricula,data):
    return {'Nome': nome, 'Matricula': matricula, 'Data': data}

for n in range(2):
    # Recebendo os dados do aluno
    nome = input('Insira o nome do aluno: ').capitalize().strip()
    matricula = int(input('Insira o número de matrícula: '))
    data = input('Insira a data de nascimento: ')


    aluno_cadastro = aluno(nome,matricula,data)
    alunos_lista.append(aluno_cadastro)

print(alunos_lista)

cadastro = aluno(nome,matricula,data)

pergunta = input('Qual aluno irá verificar: ').capitalize().strip()
for n in alunos_lista:
    if n['Nome'].capitalize() == pergunta.capitalize():
        print('Nome: ',n['Nome'])
        print('Matricula: ',n['Matricula'])
        print('Data: ',n['Data'])
        break
else:
    print('Aluno não está cadastrado')