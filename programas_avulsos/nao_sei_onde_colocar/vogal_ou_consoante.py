import os

os.system('cls')

letra = (input('Insira uma letra: '))
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'


if letra == a or letra == e or letra == i or letra == o or letra == u:
    print(f'A letra é uma vogal!')
elif letra == a or e or i or o or u:
    print(f'A letra é uma consoante!')
