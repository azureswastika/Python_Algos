"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursive_ex(n_val, rec_count, num, summ):
    """Вызов рекурсии"""
    if n_val > 0:
        summ += num
        num /= -2
        recursive_ex(n_val - 1, rec_count + 1, num, summ)
    else:
        print(f'Количество элементов - {rec_count}, их сумма - {summ}')

try:
    N = int(input())
    recursive_ex(N, 0, 1, 0)
except ValueError:
    print('Попробуйте еще раз')
