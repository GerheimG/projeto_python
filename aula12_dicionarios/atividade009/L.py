import os


os.system('cls')

filmes = {}
muitas_horas = 0 

for i in range(1,2):
    titulo = input('Insira o titulo da obra: ').lower()
    genero = input('Genero do filme: ')
    duracao = int(input('Duração do filme(minutos): '))
    classificacao = (input('Classificação Indicativa: ')).lower()

    if duracao > 120:
        muitas_horas += 1

    filmes[titulo] = {'titulo' : titulo, 'genero' : genero, 
            'duração' : duracao, 'Classificação indicativa' : classificacao}

livre = 0
for keys, values in filmes.items():
    if values['Classificação indicativa'] == 'livre':
        livre += 1

while True:
    pergun = input('Deseja alterar algo?: ').upper()

    if pergun == 'S':
        item_alterado = input('Digite o titulo do filme: ').lower()

        if item_alterado in filmes:
            subitem_alterado = input('Qual valor irá alterar: ').lower().strip()

            if subitem_alterado in filmes[item_alterado]:
                atualizar = input('Digite a alteração: ')

                if subitem_alterado == 'duracao':
                    atualizar = int(atualizar)
                
                if subitem_alterado == 'classificacao':
                    atualizar = int(atualizar)

                filmes[item_alterado][subitem_alterado] = atualizar
                
        else:
            print('Esse item não esta disponivel')

    elif pergun == 'N':
        print('Encerrando o programa..')
        print('=' * 70)
        print('Lista de filmes', filmes)
        print('=' * 70)
        print('Livros com mais de 2 horas: ',muitas_horas )
        print('=' * 70)
        print('Livros com a classificação livre: ', livre)
        print('=' * 70)
        ordem = sorted(filmes.values(), key= lambda x: (x['titulo']))
        for titulo in ordem:
            print('Lista de filmes em ordem: ' ,titulo['titulo'])
        break