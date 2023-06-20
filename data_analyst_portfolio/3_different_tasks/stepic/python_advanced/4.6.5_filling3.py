'''
Заполнение 2

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
и заполняет её в соответствии с образцом: : разместить единицы
на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.

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

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
