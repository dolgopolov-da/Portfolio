'''Сумма факториалов

Дано натуральное число n. Напишите программу,
которая выводит значение суммы 1!+2!+3!+…+n!.
'''
import math

n = int(input())
total = 0
factorial_i = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        factorial_i *= j
    total += factorial_i
    factorial_i = 1

print(total)


