from classes import Produto
from classes import Eletronico
from classes import Alimento
from classes import Roupa
from datetime import datetime
import os
import time


# Criando um produto aleatório para iniciar a lista de estoque
produto_geral = Produto("Banana", 50, "Alimento")

# Loop para cadastrar produtos no sistema
while True:
    print("\n=== Cadastro de Produto ===")
    print('—'*30)
    while True:
        
        nome = input("Nome do produto: ").capitalize().strip()  # Usuário coloca o nome do produto
        if nome == '':
            input('Preencha corretamente...')
            os.system('cls')
            continue
        else:
            break

    while True:
        print('—'*30)
        preco = float(input("Preço (R$): "))  # Usuário coloca o preço
        if preco <= 0 or preco == '':
            input('Preencha corretamente...')
            os.system('cls')
            continue
        else:
            break

    print('—'*30)
    categoria = input("Categoria (Eletrônico, Roupa, Alimento): ").strip().capitalize()  # Usuário escolhe a categoria

    # Vê qual é a categoria e cria um objeto dele
    if categoria == "Eletrônico":
        produto_geral.estoque.append(Eletronico(nome, preco))  # Adiciona o produto no estoque
    
    elif categoria == "Roupa":
        print('—'*30)
        subcategoria = input("Coleção (Verão ou Outra): ").strip().capitalize()  # Pergunta se é coleção de verão ou outra
        produto_geral.estoque.append(Roupa(nome, preco, subcategoria))  # Adiciona a roupa no estoque

    elif categoria == "Alimento":
        while True:
            try:
                validade = input("Data de validade (YYYY-MM-DD): ").strip()  # Usuário vai colocar a data de validade do alimento
                validade = datetime.strptime(validade, '%Y/%m/%d')
                break
            except ValueError:
                print('Insira uma data válida no formato YYYY/MM/DD...')
                continue
        produto_geral.estoque.append(Alimento(nome, preco, validade))  # Adiciona o alimento no estoque

    else:
        print("Categoria inválida! Tente novamente.")  # Mensagem de erro se não for uma das categorias acima
        continue  # Volta para o início do loop

    print('—'*30)
    print(f"=== Produto {nome} cadastrado com sucesso! ===\n")  # Mostra que cadastrou o produto

    # Pergunta se o usuário vai cadastrar mais produtos
    continuar = input("=== Deseja cadastrar outro produto? (s/n): ").strip().lower()
    print('   \\\Limpando terminal//')
    time.sleep(2)
    os.system('cls')
    if continuar != 's':  # Se não quiser continuar, ele vai sair do loop
        print('   \\\Limpando terminal//')
        time.sleep(2)
        os.system('cls')
        break

# Lista todos os produtos cadastrados
produto_geral.listar_produtos()

# Pergunta pra saber se o usuáiro deseja filtrar os produtos por categoria
filtro = input("\n=== Deseja filtrar os produtos por categoria? (s/n): ").strip().lower()
print('   \\\Limpando terminal//')
time.sleep(2)
os.system('cls')

if filtro == 's':
    categoria_filtro = input("=== Digite a categoria para filtrar (Eletrônico, Roupa, Alimento): ").strip().capitalize()
    time.sleep(1)
    os.system('cls')
    produto_geral.filtrar_por_categoria(categoria_filtro)  # Filtra e mostra os produtos da categoria escolhida