'''
Симметричная матрица

Напишите программу, которая проверяет симметричность
квадратной матрицы относительно главной диагонали
'''

n = int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

simmetrical = True
for i in range(n):
    for j in range(n):
        if i != j:
            if matrix[i][j] != matrix[j][i]:
                simmetrical = False
                break
    if not simmetrical:
        print('NO')
        break

if simmetrical:
    print('YES')
