# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

import os


os.system('cls')


class Notas:
    def __init__(self,nota1,nota2,nota3,nota4):
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
        self._nota4 = nota4
    
    def get_nota1(self):
        return self._nota1
    
    def get_nota2(self):
        return self._nota2
    
    def get_nota3(self):
        return self._nota3

    def get_nota4(self):
        return self._nota4
    
    def set_nota1(self,nota1):
        self._nota1 = nota1
    
    def set_nota2(self,nota2):
        self._nota2 = nota2
    
    def set_nota3(self,nota3):
        self._nota3 = nota3
    
    def set_nota4(self,nota4):
        self._nota4 = nota4
    
    def calcular_media(self):
        numeros = self._nota1 + self._nota2 + self._nota3 + self._nota4
        media = numeros / 4
        return media
        
    
    def exibir_info(self):
        print(f'Notas: {self.get_nota1()},{self.get_nota2()},{self.get_nota3()},{self.get_nota4()}')
        print(f'Média das notas: {self.calcular_media()}')
    
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))

valor = Notas(nota1,nota2,nota3,nota4)
valor.exibir_info()