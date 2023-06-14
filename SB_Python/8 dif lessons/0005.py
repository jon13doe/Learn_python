# Вводится строка. Необходимо найти все индексы фрагмента
# "ра" во введенной строке. Вывести в строку через пробелы
# найденные индексы. Если этот фрагмент ни разу не будет
# найден, то вывести значение -1.
s = str(input())
n = []
if s.count('ра') == 0:
    print('-1')
else:
    for i in range(len(s) - 1):
        if s[i] == 'р' and s[i + 1] == 'а':
            n += [i]
    print(*n)
#водится строка с номером телефона. Ожидается формат ввода:
#+7(xxx)xxx-xx-xx
#где x - это цифра. Размер введенных символов считается верным
# (то есть, не может быть, чтобы отсутствовала какая-либо цифра
# или была лишняя). Необходимо проверить, что введенная строка
# соответствует этому формату. Вывести ДА, если соответствует и
# НЕТ - в противном случае.

#1
n = str(input())
s = '+7(XXX)XXX-XX-XX'
ss = []
sx = []
for i in range(len(s)):
    if s[i] != 'X':
        ss += [i]
    else:
        sx += [i]
if len(n) != len(s):
    print('НЕТ')
else:
    for i, pin in enumerate(sx):
        if n[pin].isdigit() != True:
            print("НЕТ")
            break
        for i, pis in enumerate(ss):
            if n[pis] != s[pis]:
                print('НЕТ')
                break
    else:
        print('ДА')

#2

n = input()
if len(n) == 16:
    a = n[0] + n[2] + n[6]+ n[10] +n[13]
    b = n[3] + n[4] + n[5] + n[7] + n[8] + n[9] + n[11] + n[12] + n[14] + n[15]
    if a == "+()--" and n[1] == "7" and b.isdigit():
        print("ДА")
    else:
        print("НЕТ")
else:
    print("НЕТ")

#3
s = input()
t = ''.join([c for c in s if c.isdigit()])
print('ДА' if f'+7({t[1:4]}){t[4:7]}-{t[7:9]}-{t[9:]}' == s else 'НЕТ')
#4
lst = list(input())
for i, j in enumerate(lst):
    if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and i != 1:
        lst[i] = 'x'
print("ДА" if ''.join(lst) == '+7(xxx)xxx-xx-xx' else "НЕТ")

# В виде строки записано арифметическое выражение, например:
# "10 + 25 - 12" или "10 + 25 - 12 + 20 - 1 + 3" и т. д.
# То есть, количество действий может быть разным.
# Необходимо выполнить вычисление и результат отобразить на
# экране. Полагается, что в качестве арифметических операций
# здесь используется только сложение (+) и вычитание (-),
# а в качестве операндов - целые неотрицательные числа.
# Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

#1
p = input()
p = p.replace(' ','')
p = p.replace('+',' ')
p = p.replace('-',' -')
p = list(map(int, p.split()))
print(sum(p))
#2
text = input().replace(' ', '').replace('-', '+-').split('+')
print(sum(map(int, text)))
#3
print(eval(input()))

#Вводится список в виде целых чисел в одну строку через пробел.
# Необходимо сначала сформировать список на основе введенной
# строки, а затем, каждое значение этого списка изменить, возведя
# в квадрат. Отобразить результат на экране в виде строки полученных
# чисел, записанных через пробел. Программу следует реализовать с
# использованием функции enumerate.

l = list(map(int, input().split()))
for i, z in enumerate(l):
    l[i] = z * z
print(*l)

# Вводится список в виде целых чисел в одну строку через пробел.
# Сначала нужно сформировать список из введенной строки.
# Затем, каждый элемент этого списка продублировать один раз.
# Результат отобразить на экране в виде строки полученных чисел,
# записанных через пробел.

l = list(map(int, input().split()))
ln = []
for i in range(len(l)):
    ln.append(l[i])
    ln.append(l[i])
print(*ln)

# Вводится список в виде вещественных чисел в одну
# строку через пробел. С помощью цикла for необходимо
# найти наименьшее значение в этом списке. Полученный
# результат вывести на экран.  Реализовать программу
# без использования функции min, max и сортировки.

l = list(map(float, input().split()))
min = l[0]
for i in range(1, len(l)):
    if l[i] < min:
        min = l[i]
print(min)

# Вводится список в виде вещественных чисел в одну строку
# через пробел. Сначала нужно сформировать список из
# введенной строки. Затем, все отрицательные значения
# в этом списке заменить на -1.0. Результат вывести
# на экран в виде строки чисел через пробел.
# Программу следует реализовать с использованием функции enumerate.

n = list(map(float, input().split()))
for i in range(len(n)):
    if n[i] < 0:
        n[i] = -1.0
print(*n)