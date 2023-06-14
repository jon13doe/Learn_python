i, lst, n = 1, [], int(input())
if n < 100:
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            lst.append(i)
        i += 1
    print(*lst)
else: print("слишком большое значение n")