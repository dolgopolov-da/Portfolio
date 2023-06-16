'''
Таблица умножения

На вход программе подаются два натуральных числа
n и m — количество строк и столбцов в матрице. Создайте матрицу mult размером
n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
'''

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    matrix.append([0] * m)

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

