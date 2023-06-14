d = [1, 5, -7, 9, -8, 0, 8]
flFind = True
i = 0
while i < len(d):
    print(i)
    flFind = d[i] % 2 == 0
    if flFind:
        break
    i += 1
print(flFind, d[i])