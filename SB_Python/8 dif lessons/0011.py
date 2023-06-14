# Вводится строка из русских букв и символов пробела.
# Необходимо ее закодировать азбукой Морзе, где каждой
# букве ставится в соответствие код из точки и тире.
# После каждой закодированной буквы должен стоять пробел
# (символ окончания кода буквы). После последнего кода
# пробела быть не должно (в конце строки).

d = {' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--',
     'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
     'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--',
     'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...',
     'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
     'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
     'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}
print(*[d.get(a) for a in input().upper()])


# Имеется закодированная строка с помощью азбуки Морзе.
# Коды разделены между собой пробелом. Необходимо ее
# раскодировать, используя азбуку Морзе из предыдущего
# занятия. Полученное сообщение (строку) вывести на экран.

d = {' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--',
     'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
     'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--',
     'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...',
     'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
     'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
     'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}
e = {value: key for key, value in d.items()}
print(*[e.get(a).lower() for a in input().split()], sep='')

# Вводится список целых чисел в одну строчку через пробел.
# С помощью словаря выделите только уникальные (не повторяющиеся)
# введенные значения и, затем, сформируйте список из уникальных чисел.
# Выведите его на экран в виде набора чисел, записанных через пробел.

#1
lst = list(map(int, input().split()))
a = {}
a = a.fromkeys(lst)
c = [c for c in a.keys()]
print(*c)
#2
print(*dict.fromkeys(input().split()))

# Вводятся данные в формате:
#
# <день рождения 1> имя_1
# <день рождения 2> имя_2
# ...
# <день рождения N> имя_N
#
# Дни рождений и имена могут повторяться.
# На их основе сформировать словарь и вывести его в формате (см. пример ниже):
#
# день рождения 1: имя1, ..., имяN1
# день рождения 2: имя1, ..., имяN2
# ...
# день рождения M: имя1, ..., имяNM

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

d = {}
for i in lst_in:
    key, value = i.split()
    d[key] = (d[key] if key in d else []) + [value]
for key, value in d.items():
    print(key, ': ', ', '.join(value), sep='')

# 2
d = {}

for line in map(str.strip, sys.stdin.readlines()):
    key, value = line.split()
    d.setdefault(key, []).append(value)

for key in d:
    print(f'{key}: {", ".join(d[key])}')


# Имеется словарь с наименованиями предметов и их весом (в граммах):
#
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

# Сергей собирается в поход и готов взвалить на свои хрупкие плечи
# максимальный вес в N кг (вводится с клавиатуры). Он решил класть
# в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые,
# затем, все более легкие) так, чтобы их суммарный вес не превысил
# значения N кг. Все предметы даны в единственном экземпляре.
# Выведите список предметов (в строчку через пробел), которые
# берет с собой Сергей в порядке убывания их веса.

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
sorted_values = sorted(things.values())
sorted_values.reverse()
thingss = {}
for i in sorted_values:
    for k in things.keys():
        if things[k] == i:
            thingss[k] = things[k]
            break
print(thingss)
s = []
w = int(input()) * 1000
for t, iw in thingss.items():
    if w >= iw:
        w -= iw
        s.append(t)
print(*s)