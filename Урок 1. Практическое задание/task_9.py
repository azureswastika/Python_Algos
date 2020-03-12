"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
while True:
    try:
        A = int(input())
        B = int(input())
        C = int(input())
        break
    except ValueError:
        print('Попробуйте еще раз')

if B < A < C or C < A < B:
    print(f'Среднее: {A}')
elif A < B < C or C < B < A:
    print(f'Среднее: {B}')
elif A < C < B or B < C < A:
    print(f'Среднее: {C}')
elif A == B == C:
    print('Числа равны')
