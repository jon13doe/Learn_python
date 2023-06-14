n = 6
# p = [0] * n
# for i in range(n):
#     p[i] = i ** 2

p = [x ** 2 for x in range(n)]

print(p)
#_________________________________________

print([a for a in range(7)])
print([a for a in "python"])
print([ord(a) for a in "python"])
t = ['True', 'False', 'True', 'False', 'True', 'False', 'True', 'False', 'True', 'False', 'True']
print([a for a in t])
print([len(a) for a in t])
print([1 for a in range(7)])
print([x % 4 for x in range(0, 7)])
print([a % 2 == 0 for a in range(11)])
print([0.5 * a - 2  for a in range(n)])

print([x for x in range(-7, 7) if x < 0])
a = [x for x in range(-10, 12) if x > 0 and x % 2 == 0 and x % 3 == 0]
print(a)

d = [0, 1, 2, 11, 13, 23]
print(['chet' if x % 2 == 0 else 'nechet' for x in d])
#_________________________________________

d_in = input("vvedi cherez probel ")
a = [int(x) for x in d_in.split()]
print(a)
