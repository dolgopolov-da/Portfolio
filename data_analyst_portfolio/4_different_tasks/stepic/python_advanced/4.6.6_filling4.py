'''
Заполнение 4

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
и заполняет её в соответствии с образцом.

'''

n = int(input())
matrix = []

for i in range(n):
    row = [0] * n
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i == (n - j - 1) or i == j:
            matrix[i][j] = 1
        elif i < j and i < (n - j - 1) or i > j and i > (n - j - 1):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
