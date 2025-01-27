import os


os.system('cls')


dicionario = {'Martelo' : 'Usado para martelar',
            'Fita de medir' : 'Usado para medir',
            'Linha': 'Usado para marcação',
            'Colher': 'Usado para aplicar cimento',
            'Cinta': 'Ferramenta de ajuste'
            }

while True:
    print('1 - Alterar valor da ferramenta')
    print('2 - Mostrar Dicionário')
    print('3 - Sair')

    resposta = input('Escolha: ')

    if resposta == '1':
        print('Dicionário atual', dicionario)
        chave = input('Escolha uma das ferramentas: ')
        if chave in dicionario:
            del dicionario[chave]
            valor = input('Insira a nova descrição: ')
            dicionario[chave] = valor
            print('Dicionário modificado', dicionario)
            
    

    elif resposta == '2':
        print('Dicionário', dicionario)
        
        quantidade = len(dicionario)
        ordem = sorted(dicionario.items())

        print('-')
        print(f'Existem {quantidade} ferramentas')
        print('-')
        print('Dicionário em Ordem: ')
        print(ordem)
        print('-')

        espaco = 0
        for elemento in dicionario:
            if ' ' in elemento:
                espaco += 1
        print(f'Existem {espaco} ferramentas com mais de uma palavra')
        print()
    elif resposta == '3':
        break
    

