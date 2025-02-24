class ClassePai: #Super Classe
    # Método Construtor
    def __init__(self,a ,b):
        self.a = a
        self.b = b
    
    # Método que vai ser sobrecarregado
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b')
        resultado = self.a * self.b
        print(f'Este cálculo está sendo realizado')
        print(f'pelo Método da Classe Pai')
        print(f'O resultado da multiplicação de {self.a} e {self.b} = {resultado}')


class ClasseFilha(ClassePai): # Classe derivada
    # Método Construtor
    def __init__(self, a, b):
        super().__init__(a, b) # Chama o construtor da classe pai
        # Não é necessário redefinr a variável self.a e self.b,
        # pois já foram inicializados pelo construtor da classe pai
    
    # Sobrecarga de método
    def metodo_classe(self):
        # Primeiro, exeuta o método da classe pai
        super().metodo_classe()
        # Depois, executa o método da classe filha
        resultado = self.a + self.b
        print(f'O resultado da soma na Classe Filha é: {resultado}')


# Programa Principal
teste = ClasseFilha(1,2)
teste.metodo_classe()