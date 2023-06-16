'''
Задача №10. Сложение простых чисел.
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
'''

from math import sqrt


def sum_simple_numbers(min_number: int, max_number: int):  # excluding this number
    simple_num = []
    x = min_number
    y = 0

    for x in range(min_number, max_number):
        for i in simple_num:
            if i > int((sqrt(x) + 1)):
                simple_num.append(x)
                break
            if x % i == 0:
                break
        else:
            simple_num.append(x)

    print("Сумма простых чисел от {0} до {1} (не включая {1}): ".format(min_number, max_number), sum(simple_num))


sum_simple_numbers(2, 2000000)
