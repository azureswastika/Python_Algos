"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

while True:
    try:
        A = int(input('Сторона а\n'))
        break
    except ValueError:
        print('Попробуйте еще раз')
while True:
    try:
        B = int(input('Сторона b\n'))
        break
    except ValueError:
        print('Попробуйте еще раз')
while True:
    try:
        C = int(input('Сторона c\n'))
        break
    except ValueError:
        print('Попробуйте еще раз')

if A > B + C or B > A + C or C > A + B:
    print('Треугольника не существует')
elif A != B and A != C and C != B:
    print('Треугольник разносторонний')
elif A == B == C:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')
