'''
Обмен диагоналей

Дана квадратная матрица чисел. Напишите программу,
которая меняет местами элементы, стоящие на главной и побочной диагонали,
при этом каждый элемент должен остаться в том же столбце (то есть в каждом
столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
'''

n = int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n - j - 1][j] = matrix[n - j - 1][j], matrix[i][j]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
