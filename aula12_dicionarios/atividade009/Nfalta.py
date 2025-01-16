import os


os.system('cls')

produtos = {}

for i in range(1,2):
    nome = input('Insira o nome do produto: ').lower()
    preco = float(input('Preço do produto: '))
    categoria = input('Categoria do produto: ')

    produtos[nome] = {'nome' : nome, 'preço' : preco, 'categoria' : categoria}



while True:
    pergun = input('Deseja alterar algo? S/N: ').upper()

    if pergun == 'S':
        item_alterado = input('Qual item deseja alterar? ')
        if item_alterado in produtos:
            subitem_alterado = input('Qual valor irá alterar? ')
            if subitem_alterado in produtos[item_alterado]:
                atualizar = input('Escreva a atualização: ')

                if subitem_alterado == 'preço':
                    atualizar = float(atualizar)

                produtos[item_alterado][subitem_alterado] = atualizar
