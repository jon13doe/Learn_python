n = int(input("vvedi n - celoe <100: "))
if n < 1 or n > 100:
    print("n ne v diapazone 1 - 100")
else:
    p = 1
    for i in range(1, n + 1):
        p *= i
    print(f"faktorial {n}! = {p}")