'''Простые числа

На вход программе подается два натуральных числа a и b
(a<b). Напишите программу, которая находит все простые числа от
a до b включительно.
'''

def is_simple(a=1, b=10):
    a = int(input('Enter start value: '))
    b = int(input('Enter end value: '))

    for i in range(a, b + 1):
        if i < 2:
            continue
        is_simple = True
        splitter = 2
        while is_simple and splitter ** 2 <= i:
            if i % splitter == 0:
                is_simple = False
                break
            splitter += 1

        if is_simple:
            print('Simple number finded:', i)

is_simple()

