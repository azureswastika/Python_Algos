"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

try:
    N = int(input('Введите количество чисел: '))
    MAX_SUM = 0
    MAX_VAL = 0
    while N != 0:
        N -= 1
        USER_NUMB = int(input('Введите очередное число: '))
        USER_SUM = 0
        R = USER_NUMB
        while R > 0:
            USER_SUM += R % 10
            R //= 10
        if USER_SUM > MAX_SUM:
            MAX_SUM = USER_SUM
            MAX_VAL = USER_NUMB
    print(f'Наибольшее число по сумме цифр: {MAX_VAL}, сумма его цифр: {MAX_SUM}')

except ValueError:
    print('Попробуйте еще раз')
