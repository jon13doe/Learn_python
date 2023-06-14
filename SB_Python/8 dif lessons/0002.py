cd, l, ul, x = 1, 10, 0.1, int(input())
while l < x:
    l *= (1 + ul)
    cd += 1
print(cd)