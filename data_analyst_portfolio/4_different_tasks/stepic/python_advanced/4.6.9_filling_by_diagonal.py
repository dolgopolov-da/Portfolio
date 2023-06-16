'''
Заполнение диагоналями 🌶️

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
заполнив её "диагоналями" в соответствии с образцом.
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
        if i == 0 and j == 0:
            matrix[i][j] += count
        elif i == 0:
            matrix[i][j] = matrix[i][j - 1] + count
            if count < n:
                count += 1
        else:
            if m == 1:
                matrix[i][j] = matrix[i - 1][j] + 1
            elif j < m - 1:
                matrix[i][j] = matrix[i - 1][j + 1] + 1
            else:
                if m > n - i:
                    matrix[i][j] = matrix[i][j - 1] + n - i
                else:
                    matrix[i][j] = matrix[i][j - 1] + m - 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
