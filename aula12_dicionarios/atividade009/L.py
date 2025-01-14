import os


os.system('cls')

filmes = {}

for i in range(1,3):
    titulo = input('Insira o titulo da obra: ').lower()
    genero = input('Genero do filme: ')
    duracao = int(input('Duração do filme(minutos): '))
    classificacao = int(input('Classificação Indicativa: '))


    filmes[titulo] = {'titulo' : titulo, 'genero' : genero, 
            'duração' : duracao, 'Classificação indicativa' : classificacao}




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
                print(filmes)
        else:
            print('Esse item não esta disponivel')

    elif pergun == 'N':
        break

print(filme_longo)