# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

import os

os.system('cls')

class Numero:
    def __init__(self,inteiro):
        self._inteiro = inteiro
    
    def get_inteiro(self):
        return self._inteiro
    
    def set_inteiro(self,inteiro):
        self._inteiro = inteiro
    
    def dobrar(self):
        dobro = self._inteiro * 2
        return dobro
    
    def triplicar(self):
        triplo = self._inteiro * 3
        return triplo

    def exibir_info(self):
        print(f'Número: {self.get_inteiro()}')
        print(f'Dobro: {self.dobrar()}')
        print(f'Triplo: {self.triplicar()}')

inteiro = float(input('Insira um valor: '))

valor1 = Numero(inteiro)
valor1.exibir_info()