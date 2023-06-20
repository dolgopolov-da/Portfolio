'''
Шахматная доска

На вход программе подаются два натуральных числа n и m.
Напишите программу для создания матрицы размером n×m,
заполнив её символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка. Выведите полученную
матрицу на экран, разделяя элементы пробелами.
'''

size = input().split()
n = int(size[0])
m = int(size[1])
matrix = []

for i in range(n):
    matrix.append(['.'] * m)

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
