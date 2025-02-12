import os


os.system('cls')


class Calculadora:
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def somar(self):
        soma = self.valor1 + self.valor2
        return soma
    
    def subtrair(self):
        subtracao = self.valor1 - self.valor2
        return subtracao
    
    def exibir_resultado(self):
        print(f'Resultado da soma: {self.somar()}')
        print(f'Resultado da subtração: {self.subtrair()}')

valores1 = Calculadora(12,5)
valores1.exibir_resultado()