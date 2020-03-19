"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursive_ex(numb_count, max_sum, max_val):
    """Вызов рекурсии"""
    if numb_count > 0:
        try:
            user_numb = int(input('Введите очередное число: '))
            user_sum = recursive_calc(user_numb, 0)
            if user_sum > max_sum:
                recursive_ex(numb_count - 1, max_sum=user_sum, max_val=user_numb)
        except ValueError:
            print('Попробуйте еще раз')
            recursive_ex(numb_count, max_sum, max_val)
    else:
        print(f'Наибольшее число по сумме цифр: {max_val}, сумма его цифр: {max_sum}')

def recursive_calc(user_val, user_sum):
    """Вызов рекурсии"""
    if user_val > 0:
        return recursive_calc(user_val // 10, user_sum + user_val % 10)
    return user_sum

try:
    N = int(input('Введите количество чисел: '))
    recursive_ex(N, 0, 0)
except ValueError:
    print('Попробуйте еще раз')
