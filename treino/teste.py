import os  
from datetime import datetime  


os.system('cls')

# Classe base Produto
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço do produto
        self.categoria = categoria  # Categoria do produto
        self.estoque = []  # Lista para armazenar os produtos cadastrados


    # Método para aplicar desconto vou usar nas subclasses
    def aplicar_desconto(self):
        return self.preco  # Por padrão, não aplica nenhum desconto

    # Método para listar todos os produtos cadastrados
    def listar_produtos(self):
        print('Produtos Cadastrados ===')
        for produto in self.estoque:
            print(f"Nome: {produto.nome}")
            print(f"Categoria: {produto.categoria}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print("-" * 30)

    # Método para filtrar produtos por categoria
    def filtrar_por_categoria(self, categoria):
        
        produtos_filtrados = [produto for produto in self.estoque if produto.categoria.lower() == categoria.lower()]
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
            print(f"Produtos na categoria {categoria} ===")
            for produto in produtos_filtrados:
                print(f"Nome: {produto.nome}")
                print(f"Preço: R$ {produto.preco:.2f}")
                print("-" * 30)
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
        self.validade = datetime.strptime(validade, '%Y/%m/%d')  # Converte a data de validade para um objeto datetime
        self.aplicar_desconto()  # Aplica desconto automaticamente

    # Método que aplica desconto se o produto estiver próximo da validade
    def aplicar_desconto(self):
        dias_para_validade = (self.validade - datetime.now()).days  # Calcula quantos dias faltam para vencer
        if dias_para_validade < 40:  # Se o produto chegar perto do prazo da validade
            self.preco *= 0.85  # vai aplicar um desconto de 15%
        return dias_para_validade  # vai retornar os dias para validade

# Criando um produto aleatório para iniciar a lista de estoque
produto_geral = Produto("Banana", 50, "Alimento")

# Loop para cadastrar produtos no sistema
while True:
    print("\nCadastro de Produto")
    while True:
        nome = input("Nome do produto: ").capitalize().strip()  # Usuário coloca o nome do produto
        if nome == '':
            input('Preencha corretamente...')
            os.system('cls')
            continue
        else:
            break

    while True:
        preco = float(input("Preço (R$): "))  # Usuário coloca o preço
        if preco <= 0 or preco == '':
            input('Preencha corretamente...')
            os.system('cls')
            continue
        else:
            break


    categoria = input("Categoria (Eletrônico, Roupa, Alimento): ").strip().capitalize()  # Usuário escolhe a categoria

    # Vê qual é a categoria e cria um objeto dele
    if categoria == "Eletrônico":
        produto_geral.estoque.append(Eletronico(nome, preco))  # Adiciona o produto no estoque
    
    elif categoria == "Roupa":
        subcategoria = input("Coleção (Verão ou Outra): ").strip().capitalize()  # Pergunta se é coleção de verão ou outra
        produto_geral.estoque.append(Roupa(nome, preco, subcategoria))  # Adiciona a roupa no estoque

    elif categoria == "Alimento":
        validade = input("Data de validade (YYYY-MM-DD): ").strip()  # Usuário vai colocar a data de validade do alimento
        produto_geral.estoque.append(Alimento(nome, preco, validade))  # Adiciona o alimento no estoque

    else:
        print("Categoria inválida! Tente novamente.")  # Mensagem de erro se não for uma das categorias acima
        continue  # Volta para o início do loop

    print(f"Produto {nome} cadastrado com sucesso!\n")  # Mostra que cadastrou o produto

    # Pergunta se o usuário vai cadastrar mais produtos
    continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
    if continuar != 's':  # Se não quiser continuar, ele vai sair do loop
        break

# Lista todos os produtos cadastrados
produto_geral.listar_produtos()

# Pergunta pra saber se o usuáiro deseja filtrar os produtos por categoria
filtro = input("\nDeseja filtrar os produtos por categoria? (s/n): ").strip().lower()
if filtro == 's':
    categoria_filtro = input("Digite a categoria para filtrar (Eletrônico, Roupa, Alimento): ").strip().capitalize()
    produto_geral.filtrar_por_categoria(categoria_filtro)  # Filtra e mostra os produtos da categoria escolhida