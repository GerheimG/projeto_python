import os


os.system('cls')

grupo1 = []
grupo2 = []


for i in range(1, 6):
    nomes = input(f'{i}º nome: ')
    grupo1.append(nomes)

for c in range(1, 6):
    nomes = input(f'{c}ª nome: ')
    grupo2.append(nomes)

grupo1.extend(grupo2)

print(grupo1)

