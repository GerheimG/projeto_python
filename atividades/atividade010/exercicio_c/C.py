# C) Crie uma função que verifica se uma aluno(a)
# está cadastrado ou não em um dicionário. 
# Se estiver cadastrado, imprima o nome desse aluno e o 
# resto dos seus dados. O dicionário deverá conter nome, 
# matrícula e a data de nascimento do aluno.

import os
from receber_dados.dados import aluno
from receber_dados.verificar_alunos import verificar_aluno

os.system('cls')

alunos_lista = []

resultado = aluno()
aluno = verificar_aluno(resultado)