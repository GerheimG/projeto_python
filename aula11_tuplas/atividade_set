# Trabalho sobre a estrutura de dados de SET
# Senac Minas / Juiz de Fora 
# Aluno: Guilherme Gerheim
# Turma: 0392
# Ano: 2024

# Catalogo de jogo

import os


os.system('cls')


catalogo = set([
    "The Legend of Zelda: Breath of the Wild",
    "The Witcher 3: Wild Hunt",
    "Call of Duty: Modern Warfare II",
    "FIFA 24 (EA Sports FC)",
    "The Sims 4",
    "Resident Evil 4 Remake",
    "Hollow Knight",
    "Grand Theft Auto V"
])
catalogo2 = set([
    "God of War (2018)",
    "The Witcher 3: Wild Hunt",  # Repetido
    "Counter-Strike 2",
    "FIFA 24 (EA Sports FC)",    # Repetido
    "Cities: Skylines 2",
    "Resident Evil 4 Remake",    # Repetido
    "Celeste",
    "Grand Theft Auto V"         # Repetido
])

print('-' * 50)
print('APERTA S PARA SAIR')
print('-' * 50)

print('=' * 50)
print('Catalogo da primeira loja')
print(catalogo)
print('=' * 50)
print('Catalogo da segunda loja')
print(catalogo2)
print('=' * 50)
while True:
    jogos = input('Coloque mais jogos na primeira loja: ')
    print('-' * 50)
    if jogos == 's':
        print('Saindo')
        print('-' * 50)
        break       
    catalogo.add(jogos)


while True:
    jogos = input('Insira mais jogos na sua outra loja: ')
    print('-' * 50)
    if jogos == 's':
        print('Saindo')
        print('-' * 50)
        break       
    catalogo2.add(jogos)

print('Catalogo loja 1:', catalogo)
print()
print('Catalogo loja 2:', catalogo2)
print()

while True:
    print('-' * 50)
    entra = input('Quer remover algum jogo da primeira loja?(s/n)').lower().strip()
    print('-' * 50)
    if entra == 's':
        remover = input('Insira o nome do jogo: ')
        catalogo.discard(remover)
        break
    else:
        entra == 'n'
        break

while True:
    print('-' * 50)
    entra = input('Quer remover algum jogo da segunda loja?(s/n)').lower().strip()
    print('-' * 50)
    if entra == 's':
        remover = input('Insira o nome do jogo: ')
        catalogo2.discard(remover)
        break
    else:
        entra == 'n'
        break
print('-' * 50)
print('Catalogo loja 1 depois da remoção:', catalogo)
print('-' * 50)
print()
print('-' * 50)
print('Catalogo loja 2 depois da remoção:', catalogo2)
print('-' * 50)
print()

print('-' * 50)
igual = catalogo.intersection(catalogo2)
print('Aqui está os jogos presentes em ambas as lojas:', igual)
print('-' * 50)
print()

print('-' * 50)
uniao = catalogo.union(catalogo2)
print('Aqui está o catalogo das lojas juntas:', uniao)
print('-' * 50)

while True:
    limpar = input('Deseja limpar a primeira loja? (s/n)')
    if limpar == 's':
        catalogo.clear()
        print('-' * 50)
        print('Aqui está a loja depois da limpeza:', catalogo)
        print('-' * 50)
        break
    else:
        limpar == 'n'
        print(catalogo)
        break

while True:
    limpar = input('Deseja limpar a segunda loja? (s/n)')
    if limpar == 's':
        catalogo2.clear()
        print('-' * 50)
        print('Aqui está a loja depois da limpeza:', catalogo2)
        print('-' * 50)
        break
    else:
        limpar == 'n'
        print(catalogo2)
        break