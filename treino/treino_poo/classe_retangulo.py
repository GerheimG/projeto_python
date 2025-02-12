import os


os.system('cls')


class Retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        area = self.largura * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return perimetro
    
    def verificar_quadrado(self):
        if self.altura == self.largura:
            return 'Sim' 
        return 'Não'
        
    
    def exibir_info(self):
        print(f'Área: {self.calcular_area()}')
        print(f'Perímetro: {self.calcular_perimetro()}')
        print(f'É um quadrado: {self.verificar_quadrado()}')

retangulo1 = Retangulo(90,10)
retangulo1.calcular_area()
retangulo1.calcular_perimetro()
retangulo1.verificar_quadrado()
retangulo1.exibir_info()