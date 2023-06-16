'''
Зеркальное отображение

Дана квадратная матрица чисел. Напишите программу,
которая зеркально отображает её элементы относительно
горизонтальной оси симметрии.
'''

n = int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
