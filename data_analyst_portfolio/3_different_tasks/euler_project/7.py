'''
Задача №7. 10001-е простое число.
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?
'''
from math import sqrt

simple_num = []

x_min = 2
x_max = 200000
x = x_min
y = 0

for x in range(x_min, x_max + 1):
    for i in simple_num:
        if i > int((sqrt(x) + 1)):
            simple_num.append(x)
            break
        if x % i == 0:
            break
    else:
        simple_num.append(x)


print("10001-е простое число: ", simple_num[10000])
print(len(simple_num))
