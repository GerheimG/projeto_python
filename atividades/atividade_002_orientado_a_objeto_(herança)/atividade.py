# Crie um sistema de cadastro de produtos para uma loja, onde cada tipo de produto tem regras de desconto específicas.
# A classe base Produto deve conter os atributos nome, preco e categoria, e um método aplicar_desconto(), 
# que será sobrescrito nas subclasses. A classe Eletronico aplica 10% de desconto,
# a classe Roupa aplica 20% para coleção de verão e 5% para outras coleções, 
# e a classe Alimento aplica 15% de desconto se o produto estiver perto da data de validade (simulada). 
# O sistema deve permitir o cadastro de múltiplos produtos, armazená-los em uma lista, e usar um laço for para aplicar os 
# descontos e exibir os dados de cada produto. Também deve ser possível filtrar os produtos por categoria. 
# O objetivo é praticar o uso de listas, loops, condicionais e herança.






#Nao funciona





import os
from datetime import datetime

os.system('cls')

class Produto:
    def __init__(self,nome,preco,categoria):
        self._nome = nome
        self._preco = preco
        self._categoria = categoria
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def categoria(self):
        return self._categoria
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @preco.setter
    def preco(self,preco):
        self._preco = preco
    
    @categoria.setter
    def categoria(self,categoria):
        self._categoria = categoria
    

    def aplicar_desconto(self):
        pass

class Eletronico(Produto):
    def __init__(self):
        if self.categoria == 'Eletronico':
            return self.preco * 0.10

class Roupa(Produto):
    def __init__(self):
        if self.categoria == 'Roupa':
            colecao = input('Insira a coleção (Verão ou outras): ')
            if colecao == 'Verao':
                return self.preco * 0.20
            else:
                return self.preco * 0.05

class Alimento(Produto):
    def __init__(self):
        data_limite = datetime.date(2030, 10, 20)
        if self.categoria == 'Alimento':
            validade = input('Insira a validade (aaaa/mm/dd) ')
            datetime.strptime(validade, '%Y/%m/%d')
            if validade > data_limite:
                return self.preco * 0.15
            else:
                pass
            
            

while True:
    produtos = {}
    estoque = []
    print('-' * 60)
    pergunta = input('Cadastrar produto? (S/N): ').upper().strip()
    os.system('cls')
    if pergunta == 'S':
        while True:
            nome = input('Insira o nome do produto: ').capitalize().strip()
            if any(produtos['Nome'] == nome for produtos in estoque):
                print('Nome indisponivel.')
                input('Pressione enter...')
                continue
            break
        
        while True:
            try:
                preco = float(input('Insira o preço do produto: '))
                if preco < 0:
                    print('O preço deve ser um valor positivo.Tente novamente.')
                    continue
                break
            except ValueError:
                print('Valor inválido para preço.Tente novamente.')
        
        categoria = input('Insira a categoria do produto: ')

        produtos= {
            'Nome': nome,
            'Preço': preco,
            'Categoria': categoria
            }

        estoque.append(produtos)

        print("="*50)
        print("     *** Produto Cadastrado com sucesso ***")
        print("="*50)

        
    elif pergunta == 'N':
        print('Fechando.')
        break

for item in estoque:
            print(f'Nome: {item["Nome"]} '
                f'| Categoria: {item["Categoria"]} | Preço: {item["Preço"]} '
                )
            print('=' * 65)

cadastro = Produto(nome,preco,categoria)