"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""
from random import random

while True:
    try:
        M1 = int(input())
        M2 = int(input())
        break
    except ValueError:
        print('Попробуйте еще раз')
N = int(random() * (M2 - M1 + 1)) + M1
print(N)

while True:
    try:
        M1 = float(input())
        M2 = float(input())
        break
    except ValueError:
        print('Попробуйте еще раз')
N = random() * (M2 - M1 +1) + M1
print(round(N, 3))

while True:
    try:
        M1 = ord(input())
        M2 = ord(input())
        break
    except ValueError:
        print('Попробуйте еще раз')
N = int(random() * (M2 - M1 + 1)) + M1
print(chr(N))
