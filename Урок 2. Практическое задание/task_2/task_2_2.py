"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursive_ex(n_val, even, odd):
    """Вызов рекурсии"""
    if n_val > 0:
        if n_val % 2 == 0:
            recursive_ex(n_val // 10, even + 1, odd)
        else:
            recursive_ex(n_val // 10, even, odd + 1)
    else:
        print(f'Четных - {even}, нечетных - {odd}')

try:
    N = int(input())
    recursive_ex(N, 0, 0)
except ValueError:
    print('Попробуйте еще раз')
