"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint

N = [randint(1, 10) for i in range(randint(5, 10))]
X = max(N, key=lambda maxcount: N.count(maxcount))
print(f'{N}')
print(f'Чаще всего встречается: {X}')
