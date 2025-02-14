# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

import os


os.system('cls')


class Tabela:
    def __init__(self,inteiro):
        self._inteiro = inteiro
    
    @property
    def inteiro(self):
        return self._inteiro
    
    @inteiro.setter
    def inteiro(self,inteiro):
        self._inteiro = inteiro
    
    def tabuada(self,):
        for i in range(1,11):
            print(self.inteiro * i, end=' | ')
            
    


inteiro = int(input('Valor: '))

valor1 = Tabela(inteiro)
valor1.tabuada()