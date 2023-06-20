'''
Заполнение спиралью 😈😈

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
заполнив её "спиралью" в соответствии с образцом.
'''

size = '6 10'.split()
n = int(size[0])
m = int(size[1])
matrix = []

for i in range(n):
    matrix.append([0] * m)

count = 1
i = 0
j = 0
directions = ['right', 'down', 'left', 'up']
current_direction = 'right'
for _ in range(n * m):
    if current_direction == 'right':
        matrix[i][j] = count
        count += 1
        if j != m - 1:
            if matrix[i][j + 1] == 0:
                j += 1
            else:
                current_direction = 'down'
                i += 1
        else:
            current_direction = 'down'
            i += 1
    elif current_direction == 'down':
        matrix[i][j] = count
        count += 1
        if i != n - 1:
            if matrix[i + 1][j] == 0:
                i += 1
            else:
                current_direction = 'left'
                j -= 1
        else:
            current_direction = 'left'
            j -= 1
    elif current_direction == 'left':
        matrix[i][j] = count
        count += 1
        if j != 0:
            if matrix[i][j - 1] == 0:
                j -= 1
            else:
                current_direction = 'up'
                i -= 1
        else:
            current_direction = 'up'
            i -= 1
    elif current_direction == 'up':
        matrix[i][j] = count
        count += 1
        if i > 0:
            if matrix[i - 1][j] == 0:
                i -= 1
            else:
                current_direction = 'right'
                j += 1
        else:
            current_direction = 'right'
            j += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
