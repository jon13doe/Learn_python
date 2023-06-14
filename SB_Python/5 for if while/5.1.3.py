s = 0
d = 1
while d != 0:
    d = int(input("d = "))
    if d % 2 == 0:
        continue
    s +=d
    print(s)