# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

import os


os.system('cls')


class Retangulo:
    def __init__(self,base,altura):
        self._base = base
        self._altura = altura
        
    def get_base(self):
        return self._base
    
    def get_altura(self):
        return self._altura
    
    def set_base(self,base):
        self._base = base
    
    def set_altura(self,altura):
        self._altura = altura
    
    def calcular_perimetro(self):
        perimetro = 2 * (self._base + self._altura)
        return perimetro
    
    
    
    def exibir_info(self):
        print(f'Base do retângulo: {self.get_base()}')
        print(f'Altura do retângulo: {self.get_altura()}')
        print(f'Perimetro do retângulo: {self.calcular_perimetro()}')



base = float(input('Insira o valor da base: '))
altura = float(input('Insira o valor da altura: '))

retangulo1 = Retangulo(base,altura)
retangulo1.exibir_info()

