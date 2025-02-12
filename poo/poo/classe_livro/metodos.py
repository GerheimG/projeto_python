import os

class Livro:

    def __init__(self,titulo,autor,ano_publicacao,numero_pag):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_pag = numero_pag
    
    def cadastrar_livro(self):
        titulo = input('Título: ')
        autor = input('Autor: ')
        while True:
            try:
                ano = int(input('Ano: '))
            except ValueError:
                print('Insira um ano válido.')
                input('pressione enter.')
                os.system('cls')
                continue
            break
        while True:
            try:
                numero_pag = int(input('Páginas: '))
            except ValueError:
                print('Insira um valor válido.')
                input('pressione enter.')
                os.system('cls')
                continue
            break
        novo_livro = Livro(titulo,autor,ano,numero_pag)
        return novo_livro

    def exibir_info(self):
        print('-'*60)
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano: {self.ano_publicacao}')
        print(f'Páginas: {self.numero_pag}')


livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 234)
livro2 = Livro('1984', 'George Orwell', 1949, 532)
livro3 = Livro('Dom Casmurro', 'Machado de Assis', 1899, 342)
novo_livro = livro1.cadastrar_livro()
