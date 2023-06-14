def send_mail(from_name, ob):
    text = f"uv. vasys wtf {from_name}, {ob}"
    print(text)


# alt+ctr+l
send_mail('dunduk', 'kozel')


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res


a = get_sqrt(49)
print(a)


def get_max2(a, b):
    return a if a > b else b


def get_max3(a, b, c):
    return get_max2(x, get_max2(y, z))


x, y = 5, 7
print(get_max2(x, y))
x, y, z = -1, 4, 22
print(get_max2(x, get_max2(y, z)))
print(get_max3(x, y, z))


def even(x):
    return x % 2 == 0


for i in range(12):
    if even(i):
        print(i)
