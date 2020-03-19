"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursive_ex(n_val, min_val, x_val):
    """Вызов рекурсии"""
    if n_val < min_val:
        print(n_val * (n_val + 1) // 2)
        print(x_val)
    else:
        recursive_ex(n_val, min_val + 1, x_val + min_val)

try:
    N = int(input())
    recursive_ex(N, 1, 0)
except ValueError:
    print('Ошибка')
