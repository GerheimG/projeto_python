# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

import os


os.system('cls')


class Retangulo:
    def __init__(self,base,altura):
        self._base = base
        self._altura = altura
    
    @property
    def base(self):
        return self._base
    
    @property
    def altura(self):
        return self._altura
    
    @base.setter
    def base(self,base):
        self._base = base
    
    @altura.setter
    def altura(self,altura):
        self._altura = altura
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro
    
    def exibir_info(self):
        print(f'Base do retângulo: {self.base}')
        print(f'Altura do retângulo: {self.altura}')
        print(f'Perimetro do retângulo: {self.calcular_perimetro()}')



base = float(input('Insira o valor da base: '))
altura = float(input('Insira o valor da altura: '))

retangulo1 = Retangulo(base,altura)
retangulo1.exibir_info()

