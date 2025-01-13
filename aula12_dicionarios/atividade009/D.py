import os

os.system('cls')


dicionario_vinho = {}

for vinhos in range(1, 2):
    numero = input('Insira o número do vinho: ')
    tipo = input('Tipo do vinho: ')
    teor = float(input('Insira o teor alcoólico: '))
    safra = int(input('Insira a safra: '))

    dicionario_vinho[numero] = {'tipo' : tipo, 'teor' : teor, 'safra' : safra}

print(dicionario_vinho)

while True:
    alteracao = input('Vai alterar algo? S/N')
    
    if alteracao == 'S':
       item_alterado = input('Digite o número do vinho: ')
       
       if item_alterado in dicionario_vinho:
           subitem_alterado = input('Digite o que quer alterar: ').strip().lower()

           if subitem_alterado in dicionario_vinho[item_alterado]:
               atualizacao = input('Digite a alteração: ')

               if subitem_alterado == 'teor':
                atualizacao = float(atualizacao)
    
