import os

os.system('cls')

dados = {'nome': 'john', 'idade': '40' , 'peso': '80', 'altura': '1.70'}


while True:
    print('MENU DE OPÇÕES')
    print('1 - Listar chaves e valores')
    print('2 - Alterar um valor')
    print('3 - Excluir item específico')
    print('4 - Exibir apenas nome e altura')
    print('5 - Sair')

    resposta = input('Escolha: ')

    if resposta == '1':
        for keys, values in dados.items():
            print(f'{keys}: {values}')
    
    elif resposta == '2':

        while True:
            valor_novo = input('Digite o valor a alterar: ').strip().lower()
            if valor_novo in dados:
                mudando = input('Digite o novo valor: ')

                dados[valor_novo] = mudando

                break
        
        print(dados)
    
    elif resposta == '3':

        while True:
            valor_excluir = input('Digite o valor para excluir: ').strip().lower()
            del dados[valor_excluir]
            print(dados)

            break
    
    elif resposta == '4':
        print('Nome:', dados['nome'])
        print('Altura:', dados['altura'])

    elif resposta == '5':
        print('Saindo.')
        break