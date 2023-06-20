'''
Больше среднего

Напишите программу, которая выводит количество элементов квадратной
матрицы в каждой строке, больших среднего арифметического элементов данной строки.
'''

from statistics import mean

n = int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for i in range(n):
    count = 0
    row_average = mean(matrix[i])
    for j in range(n):
        if matrix[i][j] > row_average:
            count += 1
    print(count)



