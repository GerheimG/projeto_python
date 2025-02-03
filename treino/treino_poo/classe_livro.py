import os 


os.system('cls')

class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

        


print('-'*60)
titulo = input('Titulo: ')
autor = input('Autor: ')
ano_publicacao = int(input('Ano: '))
print('-'*60)

livro1 = Livro(titulo,autor,ano_publicacao)


print('-'*60)
print(f'Titulo do livro: {livro1.titulo}')
print(f'Autor do livro: {livro1.autor}')
print(f'Ano de publicação: {livro1.ano_publicacao}')