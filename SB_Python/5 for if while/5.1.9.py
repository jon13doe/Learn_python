# Форматирование. Замена 2х пробелов на 1
t = ["Ніч на    землю наступила.",
     "Небо  зорями укрила.",
     "Зорі спати не    схотіли,",
     "І на   землю полетіли."]
for i, line in enumerate(t):
    while line.count('  '):
        line = line.replace('  ', ' ')
    t[i] = line
print(t)

# Создание списка по M N переменным и замена в них значений
M, N = list(map(int, input("vvedi  m i n ").split()))
z = []
for i in range(M):
    z.append([0] * N)
print(z)
for i in range(M):
    for j in range(N):
        z[i][j] = 1
print(z)

# смена мместами строк и столбцов
m = [[1, 2, 3, 4], [5, 6, 7, 8], [-1, -2, -3, -4], [-5, -6, -7, -8]]
print(m)
for i in range(len(m)):
    for j in range(i + 1, len(m)):
      m[i][j], m[j][i] = m [j][i], m[i][j]
for r in m:
    for x in r:
        print(x, end="\t")
    print()