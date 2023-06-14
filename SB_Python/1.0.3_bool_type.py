# Вводиться дійсне число. Потрібно визначити, що його ціла частина кратна 3. На екрані вивести True, якщо кратно 3 і False - у протилежному випадку. Задача здійснюється без використання умовного оператора.

a = float(input())
print(int(a) % 3 == 0)

#Вводиться вартість книги X карбованців (наприклад, X = 435,78) - позитивне дійсне число з точністю до сотів (два знака після зап'ятої). Потрібно визначити, чи дробове значення (число після зап'ятої) більше 50. На екрані вивести True, якщо більше і False - у протилежному випадку. Задача здійснюється без використання умовного оператора.

p = float(input())
print(p - int(p) > 0.50)

#Вводяться два цілих числа в один рядок через пропуск. Можна прочитати за допомогою команди:
#a, b = map(int, input().split())
#Визначити, чи можна перше число націло поділити на друге. На екран вивести True, якщо ділиться і False – інакше. Завдання виконується без використання умовного оператора.

a, b = map(int, input().split())
print(a % b == 0)

#Вводяться три цілі позитивні числа. Прочитати у змінні їх можна за допомогою команди:
#a, b, c = map(int, input().split())
#Необхідно визначити, чи можна їх інтерпретувати (сприймати) як довжини сторін трикутника. Сума довжин двох довільних сторін трикутника завжди має бути більшою за третю сторону. На екрані вивести True, якщо трикутник формується і False - інакше. Завдання виконується без використання умовного оператора.

a, b, c = map(int, input().split())
print(a < b + c and b < a + c and c < a + b)

#Вводиться дійсне число. Потрібно перевірити, що воно потрапляє або в діапазон [0; 2] або в діапазон [10; 20] (включно). На екран вивести True, якщо потрапляє і False – інакше. Завдання виконується без використання умовного оператора.

a = float(input())
print(0 <= a <= 2 or 10 <= a <= 20)