'''Сумма факториалов

Дано натуральное число n. Напишите программу,
которая выводит значение суммы 1!+2!+3!+…+n!.
'''
import math

n = int(input())
total = 0

for i in range(1, n + 1):
    total += math.factorial(i)

print(total)


