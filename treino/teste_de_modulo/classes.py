import os  
from datetime import datetime  
import time

os.system('cls')

# Classe base Produto
class Produto:
    def __init__(self, nome, preco, categoria):
        self._nome = nome  # Nome do produto
        self._preco = preco  # Preço do produto
        self._categoria = categoria  # Categoria do produto
        self.estoque = []  # Lista para armazenar os produtos cadastrados
    
    # Getter e setter para o atributo 'nome'
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # Getter e setter para o atributo 'preco'
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    # Getter e setter para o atributo 'categoria'
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria


    # Método para aplicar desconto vou usar nas subclasses
    def aplicar_desconto(self):
        return self.preco  # Por padrão, não aplica nenhum desconto

    # Método para listar todos os produtos cadastrados
    def listar_produtos(self):
        print('=== Produtos Cadastrados ===')
        for produto in self.estoque:
            print(f"Nome: {produto.nome}")
            print(f"Categoria: {produto.categoria}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print("—" * 30)

    # Método para filtrar produtos por categoria
    def filtrar_por_categoria(self, categoria):
        
        produtos_filtrados = [produto for produto in self.estoque if \
            produto.categoria.lower() == categoria.lower()]
        """
        Cria uma lista apenas com os produtos do estoque que pertencem a categoria que o usuário escolheu.

        Ela percorre todos os produtos que estão na lista 'self.estoque' e pega aqueles que a 
        categoria seja igual a categoria que o usuário escolheu.

        self.estoque: é a lista de objetos da classe Produto, cada um com uma 'categoria'.
        categoria: string com o nome da categoria fornecida pelo usuário para filtrar os produtos.

        Ela traz uma lista de objetos 'produto' que possuem a categoria correspondente à categoria 
        escolhida pelo usuário.

        Se 'self.estoque' contém produtos das categorias "Eletrônico", "Roupa", e "Alimento",
        e 'categoria' for "eletrônico", a lista vai ter apenas os produtos dessa categoria.
        """
        
        if produtos_filtrados:
            print(f"=== Produtos na categoria {categoria} ===")
            for produto in produtos_filtrados:
                print(f"Nome: {produto.nome}")
                print(f"Preço: R$ {produto.preco:.2f}")
                print("—" * 30)
        else:
            print(f"Nenhum produto encontrado na categoria {categoria}.")

# Classe Eletronico que herda de Produto
class Eletronico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, 'Eletrônico')  # Chama o construtor da classe Produto
        self.aplicar_desconto()  # Aplica o desconto automaticamente ao criar um eletrônico
    
    # Método que aplica um desconto de 10%
    def aplicar_desconto(self):
        self.preco *= 0.90  # Preço reduzido em 10%

# Classe Roupa que herda de Produto
class Roupa(Produto):
    def __init__(self, nome, preco, subcategoria):
        super().__init__(nome, preco, 'Roupa')  # Define a categoria como 'Roupa'
        self.subcategoria = subcategoria  # Subcategoria para roupas (tipo: Verão, Inverno ou outra.)
        self.aplicar_desconto()  # Aplica desconto automaticamente
    
    # Método que aplica desconto dependendo da coleção
    def aplicar_desconto(self):
        if self.subcategoria.lower() == 'verão':  # Se for da coleção verão, ele vaai descontar 20% do preço
            self.preco *= 0.80  # 20% de desconto
        else:
            self.preco *= 0.95  # 5% de desconto aqui porque é de outra coleção

# Classe Alimento que herda de Produto
class Alimento(Produto):
    def __init__(self, nome, preco, validade):
        super().__init__(nome, preco, 'Alimento')  # Define a categoria como 'Alimento'
        self.validade = validade # A validade ja foi formatada na entrada de dados
        self.aplicar_desconto()  # Aplica desconto automaticamente

    # Método que aplica desconto se o produto estiver próximo da validade
    def aplicar_desconto(self):
        dias_para_validade = (self.validade - datetime.now()).days  # Calcula quantos dias faltam para vencer
        if dias_para_validade < 40:  # Se o produto chegar perto do prazo da validade
            self.preco *= 0.85  # vai aplicar um desconto de 15%
        return dias_para_validade  # vai retornar os dias para validade
