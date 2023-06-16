'''
Максимальный в области 1

Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
'''

n = int(input())
matrix = []
shaded_area = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i >= j:
            shaded_area.append(matrix[i][j])

print(max(shaded_area))



