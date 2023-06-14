def get_V(a, b, c, verbose=True):
    if verbose == True:
        print(f'a = {a}, b = {b}, c = {c}')
    return a * b * c


res1 = get_V(2, 3, 4)
res2 = get_V(c=4, a=2, b=3, verbose=False)
res3 = get_V(2, c=4, b=3, verbose=False)
print(res1, res2, res3, sep='\n')


def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1, s2 = s1.lower(), s2.lower()
    if trim:
        s1, s2 = s1.strip(), s2.strip()

    return s1 == s2


print(cmp_str('Python ', ' Python'))
print(cmp_str('Python ', ' Python', trim=False))
print(cmp_str('Python ', ' PYTHON'))
print(cmp_str('Python ', ' PYTHON', reg=True))


def add_value(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)

    return lst


l = add_value(1)
l = add_value(2)
print(l)
