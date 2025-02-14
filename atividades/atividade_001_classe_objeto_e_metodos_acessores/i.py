# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

import os


os.system('cls')


class Dolar:
    def __init__(self,dolares):
        self._dolares = dolares
    

    @property
    def dolar(self):
        return self._dolares
    
    @dolar.setter
    def dolar(self,dolares):
        self._dolares = dolares
    
    def cotacao_dolar(self):
        valor_dolar = self._dolares / 5.72
        return valor_dolar

    def exibir_info(self):
        print(f'O valor em reais: {self.dolar}')
        print(f'Em dólar: {self.cotacao_dolar():.2f}')

dolares = float(input('Insira o calor em reais: '))

valor1 = Dolar(dolares)
valor1.exibir_info()