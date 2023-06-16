'''
Поворот матрицы

Напишите программу, которая поворачивает квадратную матрицу чисел
на 90∘ по часовой стрелке.
'''

n = int(input())
matrix = []
rotate_matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for i in range(n):
    rotate_matrix.append([0] * n)

for i in range(n):
    for j in range(n):
        rotate_matrix[j][n - i - 1] = matrix[i][j]

for i in range(n):
    for j in range(n):
        print(rotate_matrix[i][j], end=' ')
    print()
