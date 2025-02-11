import os


os.system('cls')


class Carro:
    def __init__(self, marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro('honda', 'civic', '2024')

print(f'Marca: {carro1.marca}')
print(f'Modelo: {carro1.modelo}')
print(f'Ano: {carro1.ano}')



