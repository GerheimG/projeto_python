# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

import os

os.system('cls')

class Numero:
    def __init__(self,inteiro):
        self._inteiro = inteiro
    
    def get_inteiro(self):
        return self._inteiro
    
    def set_inteiro(self,inteiro):
        self._inteiro = inteiro
    
    def sucessor_inteiro(self):
        sucessor = self._inteiro + 1
        return sucessor
    
    def antecessor_inteiro(self):
        antecessor = self._inteiro - 1
        return antecessor
    
    def exibir_info(self):
        print(f'Número: {self.get_inteiro()}')
        print(f'Sucessor: {self.sucessor_inteiro()}')
        print(f'Antecessor: {self.antecessor_inteiro()}')

inteiro = int(input('Digite um valor inteiro: '))

valor1 = Numero(inteiro)
valor1.exibir_info()

