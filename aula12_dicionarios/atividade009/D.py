import os

os.system('cls')


dicionario_vinho = {}

for vinhos in range(1, 2):
    numero = input('Insira o número do vinho: ')
    tipo = input('Tipo do vinho: ')
    teor = float(input('Insira o teor alcoólico: '))
    safra = int(input('Insira a safra: '))

    if safra > 2015:
         contagems = 0

         contagems =+ 1

    if teor > 12:
        contagemt = 0
        
        contagemt =+ 1

    dicionario_vinho[numero] = {'tipo' : tipo, 'teor' : teor, 'safra' : safra}

print(dicionario_vinho)

while True:
    alteracao = input('Vai alterar algo? S/N')
    if alteracao == 's':
        item_alterado = input('Digite o número do vinho: ')
            
        if item_alterado in dicionario_vinho:
            subitem_alterado = input('Digite o que quer alterar: ').strip().lower()

            if subitem_alterado in dicionario_vinho[item_alterado]:
                atualizacao = input('Digite a alteração: ')

                if subitem_alterado == 'teor alcoolico':
                        atualizacao = float(atualizacao)
                if subitem_alterado == 'safra':
                        atualizacao = int(atualizacao)
                        
                dicionario_vinho[item_alterado][subitem_alterado] = atualizacao
                print(dicionario_vinho)


            else:
                print('Esse item não esta disponivel')

    elif alteracao == 'n':
        break

print('=' * 70)
print('Dicionário', dicionario_vinho)
print('=' * 70)
print('Vinhos com teor acima de 12:', contagemt)
print('=' * 70)
print('Vinhos da safra de 2015 pra cima:', contagems)
print('=' * 70) 