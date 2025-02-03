import os


class Veiculo:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


# Solicitando entrada de dados do usuário
os.system('cls')
print('-'*60)
marca = input('Digite a marca do veiculo: ')
modelo = input('Digite o modelo do veiculo: ')
ano = input('Digite o ano do veiculo: ')
cor = input('Digite a cor do veiculo: ')


# Criando um objeto da classe Veiculo com os dados fornecidos pelo usuario
veiculo1 =  Veiculo(marca,modelo,ano,cor)

# Acessando e imprimindo atributos do objeto
print('-'*60)
print('\nInformações do Veiculo: ')
print('-'*60)
print(f'Nome: {veiculo1.marca}')
print(f'CPF: {veiculo1.modelo}')
print(f'Ano de nascimento: {veiculo1.ano}')
print(f'CEP: {veiculo1.cor}')

print('-'*60)