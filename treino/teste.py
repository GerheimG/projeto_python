import os
from datetime import datetime

os.system('cls')

class Produto:
    def __init__(self,nome,preco,categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.lista = []
        self.dicionario = {
            'Nome' : nome,
            'Preço' : preco,
            'Categoria' : categoria
        }
        self.lista.append(self.dicionario)
        print(self.lista)
    
    def aplicar_desconto(self):
        pass


class Eletronico(Produto):
    def __init__(self, nome, preco, categoria):
        super().__init__(nome, preco, categoria)
        self.desconto = 10
    
    def aplicar_desconto(self):
        return self.preco - (self.preco * self.desconto / 100)

class Roupa(Produto):
    def __init__(self, nome, preco, categoria):
        super().__init__(nome, preco, categoria)
        self.desconto_verao = 20
        self.desconto = 5
    
    def aplicar_desconto(self):
        if self.categoria in self.dicionario['Categoria'] == 'verao':
            return self.preco - (self.preco * self.desconto_verao / 100)
        else:
            return self.preco - (self.preco * self.desconto / 100)

class Alimento(Produto):
    def __init__(self, nome, preco, categoria):
        super().__init__(nome, preco, categoria)
        self.desconto = 15
    
    def aplicar_desconto(self):
        return self.preco - (self.preco * self.desconto / 100)





# # Teste
# produto = Eletronico("TV", 1000, "Eletrônicos")
# print('Nome:', produto.nome)
# print("Preço original:", produto.preco)
# print("Preço com desconto:", produto.aplicar_desconto())

# produto1 = Roupa('Blusa', 500, 'Roupa')
# print('Nome:', produto1.nome)
# print("Preço original:", produto1.preco)
# print("Preço com desconto:", produto1.aplicar_desconto())

# produto2 = Alimento('Banana', 40, 'Alimento')
# print('Nome:', produto2.nome)
# print("Preço original:", produto2.preco)
# print("Preço com desconto:", produto2.aplicar_desconto())

nome = input('nome:')
preco = float(input('preco:'))
categoria = input('categoria:')


produto3 = Roupa(nome,preco,categoria)
print('Nome:', produto3.nome)
print("Preço original:", produto3.preco)
print("Preço com desconto:", produto3.aplicar_desconto())