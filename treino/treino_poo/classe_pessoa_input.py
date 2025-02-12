import os


os.system('cls')


class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade += 1
    
    def engordar(self):
        self.peso += 10
    
    def emagrecer(self):
        self.peso -= 7
    
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05
    
    def exibir_info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')

nome = input('Nome: ')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

print('\nInformações depois de 1 ano:')



pessoa1 = Pessoa(nome,idade,peso,altura)
pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()
pessoa1.exibir_info()