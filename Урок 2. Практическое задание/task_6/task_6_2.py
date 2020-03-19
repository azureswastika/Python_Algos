"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import randint

def recursive_ex(rand_numb, attempts):
    """Вызов рекурсии"""
    if attempts != 0:
        try:
            user_val = int(input('Введите значение\n'))
            if user_val > rand_numb:
                print('Ваше число больше загаданного')
                recursive_ex(rand_numb, attempts - 1)
            elif user_val < rand_numb:
                print('Ваше число меньше загаданного')
                recursive_ex(rand_numb, attempts - 1)
            else:
                print(f'Выугадали! Загаданное число - {rand_numb}')
        except ValueError:
            print('Неправильный значение')
            recursive_ex(rand_numb, 10)
    else:
        print(f'Вы не угадали, загаданное число - {rand_numb}')

recursive_ex(randint(0, 100), 10)
