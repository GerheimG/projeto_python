# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

import os
from datetime import datetime

os.system('cls')


class Nascimento:
    def __init__(self, ano_nascimento):
        self._ano_nascimento = ano_nascimento
        self._idade = self.calcular_idade(ano_nascimento)
    
    def get_ano_nascimento(self):
        return self._ano_nascimento
    
    def set_ano_nascimento(self, ano_nascimento):
        self._idade = self.calcular_idade(ano_nascimento)
    
    def calcular_idade(self, ano_nascimento):
        hoje = datetime.now()
        nascimento = datetime.strptime(ano_nascimento, '%d/%m/%Y')
        idade = hoje.year - nascimento.year
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1
        return idade
    
    def get_idade(self):
        return self._idade
    
    def exibir_info(self):
        print(f'Sua data de nascimento: {self._ano_nascimento}')
        print(f'Sua idade: {self._idade}')


ano_nascimento = input('Insira sua data de nascimento (dd/mm/yyyy): ')

nascimento1 = Nascimento(ano_nascimento)
nascimento1.exibir_info()
