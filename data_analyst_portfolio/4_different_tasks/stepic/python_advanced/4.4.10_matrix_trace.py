'''
След матрицы

Следом квадратной матрицы называется сумма элементов главной диагонали.
Напишите программу, которая выводит след заданной квадратной матрицы.
'''

n = int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

amount = 0
for i in range(n):
    amount += matrix[i][i]

print(amount)



