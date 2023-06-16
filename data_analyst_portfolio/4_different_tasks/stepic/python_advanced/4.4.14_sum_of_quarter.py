'''
Суммы четвертей

Квадратная матрица разбивается на четыре четверти,
ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.

Напишите программу, которая вычисляет сумму элементов:
верхней четверти; правой четверти; нижней четверти; левой четверти.
'''

n = int(input())
matrix = []
sum_up = 0
sum_down = 0
sum_left = 0
sum_right = 0

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i > j and i < n - j - 1:
            sum_left += matrix[i][j]
        elif i < j and i > n - j - 1:
            sum_right += matrix[i][j]
        elif i < j and i < n - j - 1:
            sum_up += matrix[i][j]
        elif i > j and i > n - j - 1:
            sum_down += matrix[i][j]

print('Верхняя четверть:', sum_up)
print('Правая четверть:', sum_right)
print('Нижняя четверть:', sum_down)
print('Левая четверть:', sum_left)

