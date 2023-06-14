a = [x ** 1 for x in range(1, 5)]
aa = {x ** 1 for x in range(1, 5)}
aaa = {x: x ** 1 for x in range(1, 5)}
print(a, aa, aaa, sep='\n')
d = [1, 2, '2', -1, '5', 4]
a = {int(x) for x in d}
print(a)
m = {'beznad': 1, 'neud': '2', 'udov': '3', 'horos': 4, 'otl': 5}
a = {key.upper(): int(value) for key, value in m.items()}
print(a)
a = {int(x) for x in d if int(x) > 0}
print(a)
a = {int(value): key for key, value in m.items() if 2 <= int(value) <= 5}
print(a)