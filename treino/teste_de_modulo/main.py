# Crie um sistema de cadastro de produtos para uma loja, onde cada tipo de produto tem regras de desconto específicas.
# A classe base Produto deve conter os atributos nome, preco e categoria, e um método aplicar_desconto(), 
# que será sobrescrito nas subclasses. A classe Eletronico aplica 10% de desconto,
# a classe Roupa aplica 20% para coleção de verão e 5% para outras coleções, 
# e a classe Alimento aplica 15% de desconto se o produto estiver perto da data de validade (simulada). 
# O sistema deve permitir o cadastro de múltiplos produtos, armazená-los em uma lista, e usar um laço for para aplicar os 
# descontos e exibir os dados de cada produto. Também deve ser possível filtrar os produtos por categoria. 
# O objetivo é praticar o uso de listas, loops, condicionais e herança.

from classes import Produto

if __name__ == '__main__':
    produto = Produto