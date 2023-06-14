#print() funk
a = 7
print(a) # вивід значення заданної змінної

var_a = "hello"
print(var_a) # вивід значення заданної змінної

var_a = "World"
print(var_a) # вивід значення заданної змінної

a, b = 7/8, "hello" # варіан послідовного завдання значень змінних
a, b = b, a
print(a, b)

print(id(a), id(b)) # вивід id змінних
print(type(a), type(b)) # вивід типу змінних

#Базові математичні дії
a = 1 + 2.5
b = 3 - 1 / 2
c = 2 * 7
d = 8 / 4
e = 7 // 4 #Ціла частка від двлення
f = 2 % 3 #Десяткова частка від двлення
g = 3 ** 3 #Возведення числа у ступінь
print(a, b, c, d, e, f, g)

# abs(), min(), max(), pow(), round(), модуль MATH

import math

a = 1.004
b = -4.50000324
c = 7.13
d = 2
e = 3

print(abs(a), abs(b), abs(c))  # модуль числа

print("max", max(a, b, c))  # максимальне значення

print("min", min(a, b, c))  # мінімальне значення

print(d ** e, pow(d, e))  # ступінь числа

print("0.5-", round(0.5), "1.5-", round(1.5), "10.5-", round(10.5), "15.5-", round(15.5),
      a, "-", round(a, 2), b, "-", round(b, 6), c, "-", round(c, -1)) # скорочення числа
      
print(math.e, math.ceil(b), math.floor(b), math.ceil(c), math.floor(c)) # округлення до ближчого верхньго/нижнього значення

print(math.factorial(2), math.factorial(e)) # факторіал числа

print(math.trunc(a), math.trunc(b), math.trunc(c)) # округлення до цілого в сторону 0

print(int(a), int(b), int(c))

print("pi-", math.pi, "e-", math.e) # виведення констант пи та е