# Adivinhe o número
# O programa escolhe um número aleatório entre 1 e 100 (use uma biblioteca como random).
# O usuário deve adivinhar o número, e o programa deve dar dicas ("maior" ou "menor") até que ele acerte.

import os
import random

os.system('cls')

numero_escolhido = int(random.randint(1, 100))


while (True):
    
    numero_advinhe = int(input('Advinhe o número de 1 a 100: '))
    
    if numero_escolhido == numero_advinhe:
        print('Você acertou o número')
        break

    elif numero_advinhe < numero_escolhido:
        print('Maior')
    
    elif numero_advinhe > numero_escolhido:
        print('Menor')

    

    

    
    