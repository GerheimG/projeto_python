import os


os.system('cls')

dicionario = {}

for i in range(1,4):
    chave = input(f'Insira a {i}ª cor: ')
    valor = input(f'Insira o {i}ª valor: ')
    dicionario[chave] = valor


while True:
    print('1- Adicionar cor e valor')
    print('2- Trocar valor')
    print('3- Mostrar em ordem alfabética')
    resposta = input('Escolha: ')
    
    if resposta == '1':

        novas_cores = input('Digite os novos pares chave-valor'\
                        'no formato: chave1:valor1 , chave2:valor2: ')

        lista_cores = novas_cores.split(',')
        novas = {}
        for cor in lista_cores:
            chave , valor = cor.split(':')
            novas[chave] = valor
            dicionario.update(novas)
    
    elif resposta == '2':

        print(dicionario)
        print()
        alterar = input('Qual chave deseja alterar: ')
        if alterar in dicionario:
            del dicionario[alterar]
            novo_valor = input('Insira o novo valor: ')
            dicionario[alterar] = novo_valor
            print(dicionario)

    elif resposta == '3':
        conta = 0
        ordem = sorted(dicionario)
        print('Dicionário em ordem', ordem)
        # lista = list(dicionario)
        alfa = 'abcdefghijklmnopqrstuvwxyz'

        for char in alfa:
            num =  0
            for palavra in ordem:
                if char in palavra[0]:
                    num += 1
            if num == 0:
                continue
            else:
                print(f'{num} cor(es) começam com a letra {char}')