'''
Заполнение 2

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
и заполняет её в соответствии с образцом.
'''

size = input().split()
n = int(size[0])
m = int(size[1])
matrix = []

for i in range(n):
    matrix.append([0] * m)


for i in range(n):
    for j in range(m):
        if j == 0:
            matrix[i][j] = i + 1
        else:
            matrix[i][j] = matrix[i][j - 1] + n

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
