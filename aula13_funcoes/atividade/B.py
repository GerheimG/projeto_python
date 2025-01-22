# B) Crie uma função que cadastre o nome de um aluno(a),
# a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados
# utilizando uma estrutura de repetição for.

import os


os.system('cls')

def aluno(nome,matricula,data):
    return nome, matricula, data

# Recebendo os dados do aluno
nome = input('Insira o nome do aluno: ')
matricula = int(input('Insira o número de matrícula: '))
data = input('Insira a data de nascimento: ')

# Chamando a função para cadastrar o aluno
cadastro = aluno(nome, matricula, data)

# Saída com FOR
for i in cadastro:
    print(i)