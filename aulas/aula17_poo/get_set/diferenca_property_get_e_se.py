import os


os.system('cls')


# class MinhaClasse:
#     def __init__(self, valor):
#         self._atributo = valor
    
#     def get_atributo(self):
#         return self._atributo
    
#     def set_atributo(self, valor):
#         self._atributo = valor

# obj = MinhaClasse(10)
# # O atributo trabalha como função
# obj.set_atributo(20)
# # Saída como função
# print(obj.get_atributo())


class MinhaClasse:
    def __init__(self, valor):
        self._atributo = valor
    
    @property
    def atributo(self):
        return self._atributo
    
    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor

obj = MinhaClasse(10)
# O atributo trabalha como função
obj.atributo = 20
# Saída como função
print(obj.atributo)
        