# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.


import os

os.system('cls')


while (True):
    usuario = 'Fidelim'
    senha = 'batataalada'

    login_usuario = input('Insira seu usuário: ')
    login_senha = input('Insira sua senha: ')

    if login_usuario != usuario and login_senha != senha:
        print('Login ou senha incorreto')
        continue
    
    else:
        print(f'Bem vindo {usuario}')
        break