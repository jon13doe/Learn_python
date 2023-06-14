#Вкладені умови, множинний вибір

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a > b:
    if a > c:
        print("a - max")
    else:
        print("c - max")
else:
    if b > c:
        print("b - max")
    else:
        print("c - max")
        
#Задачі
# Є таке меню:
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# У програмі вводиться ціле число від 1 до 6. Потрібно вивести пункт меню, пов'язаний із цим числом. Реалізувати програму за допомогою операторів if-elif

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

m = list(map(str, m.split("\n")))
n = int(input())
if n == 1:
    print(m[0])
elif n == 2:
    print(m[1])
elif n == 3:
    print(m[2])
elif n == 4:
    print(m[3])
elif n == 5:
    print(m[4])
elif n == 6:
    print(m[5])
    
# Вводяться три цілих числа в один рядок через пропуск. Необхідно визначити найменше серед них та вивести його на екран. Реалізувати програму, використовуючи умовний оператор без використання функції min.
    
a, b, c = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

# Вводиться вес боксера-любителя (в кг, в виде вещественного числа). Відомо, що вес таків, що боксер може бути віднесений до однієї з весових категорій:
# 1) легкий вага – до 60 кг (включно);
# 2) перший напівсередній вага – до 64 кг (включно);
# 3) напівсередній вага – до 69 кг (включно);
# 4) остальные - понад 69 кг.
# Виведіть на екран номер категорії, в якому буде виступати боксер.

w = float(input())
if 0 <= w <= 60:
    print("1")
elif 60 <= w <= 64:
    print("2")
elif 64 <= w <= 69:
    print("3")
elif 69 < w:
    print("4")

# Запроваджується порядковий номер дня тижня (1, 2, ..., 7). Вивести на екран його назву (понеділок, вівторок, середа, четвер, п'ятниця, субота, неділя). Програму реалізувати за допомогою операторів if-elif.

d = "понедельник, вторник, среда, четверг, пятница, суббота, воскресенье".split(", ")
n = int(input())
if 0 < n <= 7:
    print(d[n - 1])
elif n <= 0:
    print('Вы уже переболели COVID-19')
else:
    print('У ВАС всё впереди...')

# Запроваджується порядковий номер місяця (1, 2, ..., 12). Вивести на екран кількість днів цього місяця. Прийняти, що рік не високосний. Реалізувати через умовний оператор, у якому слід використовувати трохи більше трьох гілок (блоків).
# PS Число днів у місяцях не високосного року, починаючи з січня: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    
d = "31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31".split(", ")
n = int(input())
if 0 < n <= 12:
    print(d[n - 1])
elif n <= 0:
    print('Вы уже переболели COVID-19')
else:
    print('У ВАС всё впереди...')

# Дата деякого дня характеризується двома натуральними числами: m (порядковий номер місяця) та n (число). За введеними m і n (в один рядок через пропуск) визначити:
# а) дату попереднього дня (прийняти, що m та n не характеризують 1 січня);
# б) дату наступного дня (прийняти, що m та n не характеризують 31 грудня).
# У задачі прийняти, що рік не є високосним. Вивести попередню дату та наступну дату (у форматі: mm.dd, де m – число місяця; d – номер дня) в один рядок через пробіл.
#PS Число днів у місяцях не високосного року, починаючи з січня: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    
m , d = map(int, input().split())
dm = "31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31".split(", ")
if 1 == d:
    print(f"{str(m - 1).rjust(2, '0')}.{str(dm[m - 2]).rjust(2, '0')} {str(m).rjust(2, '0')}.{str(d + 1).rjust(2, '0')}")
elif 1 < d < int(dm[m - 1]):
    print(f"{str(m).rjust(2, '0')}.{str(d - 1).rjust(2, '0')} {str(m).rjust(2, '0')}.{str(d + 1).rjust(2, '0')}")
elif int(dm[m - 1]) == d:
    print(f"{str(m).rjust(2, '0')}.{str(d - 1).rjust(2, '0')} {str(m + 1).rjust(2, '0')}.01")
    
# Вводиться ціле число k (1 <= k <= 365). Определить, яким днем ​​неділі (понеділок, вторник, середа, четвер, п'ятниця, субота або воскресенье) є к-й день не високого року, в якому 1 січня є понеділком.
    
d = "понедельник, вторник, среда, четверг, пятница, суббота, воскресенье".split(", ")
k = int(input())
if 0 < k <= 365:
    if k % 7 == 1 % 7:
        print(d[0])
    elif k % 7 == 2 % 7:
        print(d[1])
    elif k % 7 == 3 % 7:
        print(d[2])
    elif k % 7 == 4 % 7:
        print(d[3])
    elif k % 7 == 5 % 7:
        print(d[4])
    elif k % 7 == 6 % 7:
        print(d[5])
    elif k % 7 == 0:
        print(d[6])
elif k <= 0:
    print('Вы уже переболели COVID-19')
else:
    print('У ВАС всё впереди...')