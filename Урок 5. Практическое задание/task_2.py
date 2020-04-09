"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque
from itertools import islice

FIRST_NUM = deque(list(input('Введите первое число в шестнадцатеричной системе счисления: ')))
SECOND_NUM = deque(list(input('Введите второе число в шестнадцатеричной системе счисления: ')))

LIST_OF_NUMBERS = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(FIRST_NUM) > len(SECOND_NUM):
    FIRST_NUM, SECOND_NUM = SECOND_NUM, FIRST_NUM

SECOND_NUM.reverse()
D = deque(list())

J = -1
K = 0
for i in SECOND_NUM:
    one = LIST_OF_NUMBERS.index(i)
    two = LIST_OF_NUMBERS.index(FIRST_NUM[J])
    D.append(LIST_OF_NUMBERS[(one + two + K) % 16])
    if(one + two) >= 15:
        K = 1
    else:
        K = 0
    J -= 1
    if J == -len(FIRST_NUM)-1:
        break

DIFFERENT = len(SECOND_NUM) - len(FIRST_NUM)
SECOND_NUM.reverse()
SLICE_DIFF = list(islice(SECOND_NUM, 0, DIFFERENT))
if DIFFERENT:
    for i in SLICE_DIFF:
        D.append(LIST_OF_NUMBERS[(LIST_OF_NUMBERS.index(i) + K) % 16])
        if LIST_OF_NUMBERS.index(i) + 1 >= 15:
            K = 1
        else:
            K = 0

if K == 1:
    D.append('1')

D.reverse()
print(list(D))

class Numb:
    def __init__(self, num):
        self.number = list(num)

    def __str__(self):
        return self.number.__str__()

    def __add__(self, other):
        tmp_1 = int(''.join(self.number), 16)
        tmp_2 = int(''.join(other.number), 16)
        return Numb(f'{tmp_1 + tmp_2:X}')

    def __mul__(self, other):
        tmp_1 = int(''.join(self.number), 16)
        tmp_2 = int(''.join(other.number), 16)
        return Numb(f'{tmp_1 * tmp_2:X}')


print(Numb('1e2') + Numb('1c4f'))
print(Numb('1e2') * Numb('1c4f'))