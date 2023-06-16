'''
Обмен столбцов

Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа
n и m — количество строк и столбцов в матрице, затем элементы матрицы
построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.
'''

n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

col_nums = input().split()
col_num1, col_num2 = int(col_nums[0]), int(col_nums[1])

for i in range(n):
    matrix[i][col_num1], matrix[i][col_num2] = matrix[i][col_num2], matrix[i][col_num1]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
