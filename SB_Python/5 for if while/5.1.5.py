d = [5, 4, 2, 1]
for i in range(len(d)):
    d[i] = str(i + 2 * i)
print(*d)