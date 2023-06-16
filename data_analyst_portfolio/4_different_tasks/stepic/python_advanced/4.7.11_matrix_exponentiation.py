'''
Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в m-ую степень.
'''
import copy

#заполняем матрицу числами
n = int(input())
matrix = []
for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)
#степень
m = int(input())

#матрица-множитель
matrix_copy = copy.deepcopy(matrix)

#меняем местами строки матрицы-множителя со столбцами (чтобы проще умножать)
matrix_rotate = []
for j in range(n):
    lst = []
    for i in range(n):
        lst.append(matrix[i][j])
    matrix_rotate.append(lst)

#заполняем итоговую матрицу нулями
result_matrix = [[0] * n for _ in range(n)]

#заполняем матрицу значениями сумм произведений элементов матрицы и матрицы-множителя
for step in range(m - 1):
    if step > 0:
        matrix = copy.deepcopy(result_matrix)
        result_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix[i][k] * matrix_rotate[j][k]

#выводим итоговую матрицу
for i in range(n):
    for j in range(m):
        print(str(result_matrix[i][j]).ljust(3), end=' ')
    print()