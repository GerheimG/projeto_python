# Atividade H

import os

os.system('cls')

a = int(input('Insira o valor: '))
b = int(input('Insira outro valor: '))
c = int(input('Insira outro valor: '))

delta = (b ** 2) - (4 * a * c)
x1 = (-b + delta ** 0.5)  / 2*a
x2 = (-b - delta ** 0.5)  / 2*a


print(f'As raízes da equação são {x1:.2f}, {x2:.2f}')