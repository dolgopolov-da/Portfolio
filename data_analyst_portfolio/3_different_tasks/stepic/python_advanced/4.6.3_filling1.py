'''
Заполнение 1

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
и заполняет её числами от 1 до n⋅m в соответствии с образцом.
'''

size = input().split()
n = int(size[0])
m = int(size[1])
matrix = []

for i in range(n):
    matrix.append([0] * m)

count = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] += count
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
