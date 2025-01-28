# Cria um contador que conta quantas vezes os elementos aparecem em um iterável.

from collections import Counter

# Exemplo com Counter
lst = ['a', 'b', 'c', 'a', 'b', 'a']
counter = Counter(lst)
print(counter)  # Saída: Counter({'a': 3, 'b': 2, 'c': 1})