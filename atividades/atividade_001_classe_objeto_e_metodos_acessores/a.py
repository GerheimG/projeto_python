# Faça um programa que peça 3 valores, depois calcule e imprima  a soma e a multiplicação desses valores. 

import os


os.system('cls')


class Calculo:
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c
    
    def set_a(self,a):
        self._a = a
    
    def set_b(self,b):
        self._b = b
    
    def set_c(self,c):
        self._c = c
    
    def calcular_soma(self):
        soma = self._a + self._b + self._c
        return soma
    
    def calcular_produto(self):
        produto = self._a * self._b * self._c
        return produto
    
    def exibir_info(self):
        print(f'Aqui estão os valores: {self._a}, {self._b} e {self._c}')
        print(f'Aqui está a soma: {self.calcular_soma()}')
        print(f'Aqui está a multiplicação: {self.calcular_produto()}')


a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

calculo1 = Calculo(a,b,c)
calculo1.exibir_info()

