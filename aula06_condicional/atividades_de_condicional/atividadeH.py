# Atividade H

import os

os.system('cls')

a = int(1)
b = int(-6)
c = int(5)

delta = (b ** 2) - (4 * a * c)
bhaskara1 = (-b + delta ** 0.5)  / 2*a
bhaskara2 = (-b - delta ** 0.5)  / 2*a


print(f'As raízes da equação são {bhaskara1, bhaskara2}')