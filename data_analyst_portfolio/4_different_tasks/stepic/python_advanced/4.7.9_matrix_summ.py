'''
Сложение матриц

Напишите программу для вычисления суммы двух матриц.
'''

size = input().split()
n = int(size[0])
m = int(size[1])
matrix1 = []
matrix2 = []
matrix3 = [[0] * m for _ in range(n)]

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix1.append(row)

input()

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix2.append(row)

for i in range(n):
    for j in range(m):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

for i in range(n):
    for j in range(m):
        print(str(matrix3[i][j]).ljust(3), end=' ')
    print()
