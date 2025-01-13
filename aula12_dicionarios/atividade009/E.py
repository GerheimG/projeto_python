import os

os.system('cls')


dicionario_alunos = {}

for alunos in range(1, 2):
    nome = input('Nome do aluno: ')
    datanasci = int(input('Data de nascimento: '))
    matricula = int(input('Número de matrícula: '))

    dicionario_alunos[matricula] = {'nome' : nome, 'nascimento' : datanasci}

while True:
    resposta = input('Deseja alterar algo? S/N')

    if resposta == 'S':
        item_alterado = input('Digite o nome do aluno: ')

        if item_alterado in dicionario_alunos:
            subitem_alterar = input('Digite o que quer alterar: ').strip().lower()

            if subitem_alterar in dicionario_alunos[item_alterado]:
                atualizar = input('Digite a alteração: ')

                if subitem_alterar == 'nascimento':
                    atualizar = int(atualizar)