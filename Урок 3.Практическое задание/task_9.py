"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import randint

try:
    COUNT_OF_STRINGS = int(input('Задайте количество строк в матрице: '))
    COUNT_OF_COLUMN = int(input('Задайте количество столбцов в матрице: '))
    MATRIX = []
    for i in range(COUNT_OF_COLUMN):
        LIST = []
        for x in range(COUNT_OF_STRINGS):
            LIST.append(randint(1, 100))
        MATRIX.append(LIST)
    NUM = []
    for i in MATRIX:
        for x in i:
            print(f'{x}', end=' ')
        print()
        NUM.append(min(i))
    print(f'{NUM} минимальные значения по столбцам')
    print(f'Максимальное среди них = {max(NUM)}')
except ValueError:
    print('Попробуйте еще раз')
