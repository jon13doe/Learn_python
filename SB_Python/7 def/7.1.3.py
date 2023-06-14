import time


def getNod_long(a, b):
    '''Рахуємо нод натуральніх чисел а і б
    за алгоритмом Евкліда
    :param a - перше натуральне число
    :param b - друге натуральне число
    :return - нод
    '''
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def getNod_fast(a, b):
    '''Рахуємо нод натуральніх чисел а і б
    за швидким алгоритмом Евкліда
    :param a - перше натуральне число
    :param b - друге натуральне число
    :return - нод
    '''
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def testNod(funk):
    #   test 1
    a = 28
    b = 35
    res = funk(a, b)
    if res == 7:
        print('test 1 - ok')
    else:
        print('test 1 - fail')

    #   test 2
    a = 100
    b = 1
    res = funk(a, b)
    if res == 1:
        print('test 2 - ok')
    else:
        print('test 2 - fail')

    #   test 3
    a = 2
    b = 100000000
    st = time.time()
    res = funk(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('test 3 - ok')
    else:
        print('test 3 - fail')


testNod(getNod_long)
testNod(getNod_fast)
res = getNod_long(18, 24)
print(res)
help(getNod_long)
