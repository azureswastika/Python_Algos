"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

try:
    N = int(input())
    X = 0
    for i in range(1, N + 1):
        X += i
    Y = N * (N + 1) // 2
    print(X)
    print(Y)
except ValueError:
    print('Ошибка')
