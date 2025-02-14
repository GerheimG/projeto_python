# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

import os


os.system('cls')


class Calculo:
    def __init__(self,a,b):
        self._a = a
        self._b = b
    
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def set_a(self,a):
        self._a = a
    
    def set_b(self,b):
        self._b = b
    
    
    def dividir(self):
        resultado = self._a / self._b
        return resultado
    
    def exibir(self):
        print(f'Os valores: {self._a} e {self._b}')
        print(f'Resultado da divisão: {self.dividir():.4f}')

a = float(input('Insira um valor: '))
while True:
    b = float(input('Insira outro valor: '))
    if b == 0:
        print('Não pode ser 0')
        continue
    else:
        break

numero1= Calculo(a,b)
numero1.exibir()