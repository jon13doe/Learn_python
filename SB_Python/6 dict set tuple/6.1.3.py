a = 1, 2
print(a)
a = (1, 2, 3, 4)
print(a)
b = 1,
print(b)
x, y = (1, 2)
print(x, y)
a = (11, 12, 13, 14)
x, y, z, f = a
print(x, y, z, f)
print(a[0], len(a), a[0: 3])
a = ()
b = tuple()
c = (1, 2, 3)
d = a + b + c + (1,)
e = (0,) * 10
print(a, b, c, d, e)
a = tuple([1, 2, 3])
print(a)
a = tuple('hello')
print(a)
a = (True, 'vasya', [1, 2, 3], {'w': 1}, 9, 123)
a[2].append('ololo')
print(a, a.count(True), a.count(22), a.index('vasya'), a.index('vasya', 0, 2))
c = 9 in a
print(c)