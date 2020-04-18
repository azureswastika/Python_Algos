"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursive_ex(max_numb, min_numb, need_numb, counter):
    """Вызов рекурсии"""
    if max_numb != 0:
        try:
            user_val = int(input(f'Число {min_numb}: '))
            counter = recursive_calc(need_numb, user_val, counter)
            recursive_ex(max_numb - 1, min_numb + 1, need_numb, counter)
        except ValueError:
            print('Попробуйте еще раз')
            recursive_ex(max_numb, min_numb, need_numb, counter)
    else:
        print(f'Было введено {counter} цифр "{need_numb}"')

def recursive_calc(need_numb, user_val, counter):
    """Вызов рекурсии"""
    if user_val > 0:
        if user_val % 10 == need_numb:
            return recursive_calc(need_numb, user_val // 10, counter + 1)
        return recursive_calc(need_numb, user_val // 10, counter)
    return counter


try:
    N = int(input('Сколько будет чисел?\n'))
    X = int(input('Какую цифру считать?\n'))
    recursive_ex(N, 1, X, 0)
except ValueError:
    print('Попробуйте еще раз')
