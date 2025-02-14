# Faça um programa que converta metros em centímetros e milímetros.

import os


os.system('cls')


class Converter:
    def __init__(self,valor):
        self._valor = valor
    
    def get_valor(self):
        return self._valor
    
    def set_valor(self,valor):
        self._valor = valor

    def converter_centimetro(self):
        centimetro = self._valor * 100
        return centimetro
    
    def converter_milimetro(self):
        milimetro = self._valor * 1000
        return milimetro
    
    def exibir_info(self):
        print(f'Valor em metro: {self.get_valor()}')
        print(f'Valor em centímetros: {self.converter_centimetro()}')
        print(f'Valor em milímetros: {self.converter_milimetro()}')

valor = float(input('Insira o valor em metros: '))

valor1 = Converter(valor)
valor1.exibir_info()