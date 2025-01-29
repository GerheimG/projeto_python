# B) Crie uma função que cadastre o nome de um aluno(a),
# a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados
# utilizando uma estrutura de repetição for.

import os

os.system('cls')


from dados.inserir_dados import aluno
from dados.exibir_dados import exibir



dicionario = {}

resultado = aluno()
exibir_aluno = exibir(dicionario)

print(resultado)

