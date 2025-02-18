# Sobrecarga de Métodos 

class ClassePai: #Super Classe
    # Método construtor
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    # Para sobrecarregar
    # Vai ser usada para soma 2 números
    def metodo_classe(self,a ,b):
        pass


class ClasseFilha(ClassePai): # Classe Derivada
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Sobrecarga de Método
    def metodo_classe(self):
        return self.a + self.b


# Programa principal
teste = ClasseFilha(1,2)
teste.metodo_classe()
print(teste.metodo_classe())
        