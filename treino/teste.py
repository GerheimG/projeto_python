estoque = []
produtos = {}
import os
while True:
    print('-' * 60)
    pergunta = input('Cadastrar produto? (S/N): ').upper().strip()
    os.system('cls')
    if pergunta == 'S':
        while True:
            codigo = int(input('Insira o código do produto: '))
            if any(produtos['Código'] == codigo for produtos in estoque):
                print('Código indisponivel.')
                input('Pressione enter...')
                os.system('cls')
                continue
            break
        while True:
            nome = input('Insira o nome do produto: ').capitalize().strip()
            if any(produtos['Nome'] == nome for produtos in estoque):
                print('Nome indisponivel.')
                input('Pressione enter...')
                continue
            break
        categoria = input('Insira a categoria do produto: ')
        while True:
            try:
                preco = float(input('Insira o preço do produto: '))
                if preco < 0:
                    print('O preço deve ser um valor positivo.Tente novamente.')
                    continue
                break
            except ValueError:
                print('Valor inválido para preço.Tente novamente.')
        
        while True:
            try:
                quantidade = int(input('Insira a quantidade de produtos: '))
                if quantidade < 0:
                    print('Quantidade não pode ser um valor negativo.'
                        'Tente novamente')
                    continue
                break
            except ValueError:
                print('A quantidade deve ser um valor psotivo.Tente novamente.')
                
    
        produtos= {
            'Código': codigo,
            'Nome': nome,
            'Categoria': categoria,
            'Preço': preco,
            'Quantidade': quantidade
            }

        estoque.append(produtos)

        print("="*50)
        print("     *** Produto Cadastrado com sucesso ***")
        print("="*50)

        
    elif pergunta == 'N':
        print('Fechando.')
        break

for item in estoque:
    print(f'Código: {item["Código"]} | Nome: {item["Nome"]} '
        f'| Categoria: {item["Categoria"]} | Preço: {item["Preço"]} '
        f'| Quantidade: {item["Quantidade"]}')
    print('=' * 65)