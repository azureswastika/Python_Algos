"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""

import hashlib

def find_substring(string):
    hash_list = set()
    substring_list = []
    for i in range(len(string) + 1):
        for x in range(i + 1, len(string) + 1):
            hash_list.add(hashlib.sha1(string[i:x].encode('utf-8')).hexdigest())
            substring_list.append(string[i:x])
    
    hash_list.remove(hashlib.sha1(string.encode('utf-8')).hexdigest())
    substring_list.remove(string)
    substring_list = list(set(substring_list))
    print(f'Количество подстрок в строке "{string}" = {len(hash_list)}')
    print(f'Подстроки: \n' +'\n'.join(substring_list))


STRING = input('Строка: ')
find_substring(STRING)