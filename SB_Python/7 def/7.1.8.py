s = lambda a, b: a + b
print(s(1, 2))

a = [1, 2, lambda: print("lambda"), s, 3, 333]
print(a[0], a[2], a[2](), a[3], a[3](1, 1))

lst = [5, 3, 8, -11, 0, -2]


def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


r = get_filter(lst)
print(r)

r = get_filter(lst, lambda x: x % 2 == 0 and x != 0)
print(r)