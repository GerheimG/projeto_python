import os


os.system('cls')

filmes = {}


for i in range(1,2):
    titulo = input('Insira o titulo da obra: ').lower()
    genero = input('Genero do filme: ')
    duracao = int(input('Duração do filme(minutos): '))
    classificacao = (input('Classificação Indicativa: ')).lower()


    filmes[titulo] = {'titulo' : titulo, 'genero' : genero, 
            'duração' : duracao, 'classificação' : classificacao}



while True:
    pergunta = input('Deseja alterar algo?: ').upper()

    if pergunta == 'S':
        item_alterado = input('Digite o titulo do filme: ').lower()

        if item_alterado in filmes:
            subitem_alterado = input('Qual valor irá alterar: ').lower().strip()

            if subitem_alterado in filmes[item_alterado]:
                atualizar = input('Digite a alteração: ')

                if subitem_alterado == 'duração':
                    atualizar = int(atualizar)
                
                if subitem_alterado == 'classificacao':
                    atualizar = int(atualizar)

                filmes[item_alterado][subitem_alterado] = atualizar
                
        else:
            print('Esse item não esta disponivel')

        

    elif pergunta == 'N':
        livre = 0
        for keys, values in filmes.items():
            if values['classificação'] == 'livre':
                livre += 1
        
        muitas_horas = 0 
        for keys, values in filmes.items():
            if values['duração'] > 120:
                muitas_horas += 1
                
        print('Encerrando o programa..')
        print('=' * 70)
        print('Lista de filmes', filmes)
        print('=' * 70)
        print('Filmes com mais de 2 horas: ',muitas_horas )
        print('=' * 70)
        print('Filmes com a classificação livre: ', livre)
        print('=' * 70)
        ordem = sorted(filmes.values(), key= lambda titulo: titulo['titulo'])
        for titulo in ordem:
            print('Lista de filmes em ordem: ' ,titulo['titulo'])
        break