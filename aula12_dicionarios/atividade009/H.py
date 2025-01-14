import os

os.system('cls')

livros_dic = {}

for l in range(1,2):
    titulo = input('Insira o titulo do livro: ').lower()
    autor = input('Insira o nome do autor: ').lower()
    ano_publi = int(input('Insira o ano de publicação: '))
    num_pag = int(input('Insira o número de páginas: '))

    livros_dic[titulo] = {'autor' : autor, 'ano': ano_publi,
                        'páginas': num_pag}
    
while True:
    pergun = input('Deseja alterar algo? S/N: ').upper()

    if pergun == 'S':
        item_alterado = input('Qual o titulo: ')

        if item_alterado in livros_dic:
            subitem_alterar = input('Digite oque quer alterar: ').lower().strip()

            if subitem_alterar in livros_dic[item_alterado]:
                atualizar = input('Digite a alteração: ')
            
            print(livros_dic)


