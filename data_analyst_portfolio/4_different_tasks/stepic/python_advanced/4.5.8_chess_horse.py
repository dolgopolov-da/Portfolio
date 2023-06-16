'''
Ходы коня

На шахматной доске 8×8 стоит конь. Напишите программу,
которая отмечает положение коня на доске и все клетки,
которые бьет конь. Клетку, где стоит конь, отметьте
английской буквой N, клетки, которые бьет конь, отметьте
символами *, остальные клетки заполните точками.
'''

n = 8
alpha_coord = 'abcdefgh'
digit_coord = '87654321'
matrix = []

for i in range(n):
    matrix.append(['.'] * n)

horse_coord = list(input())
row = digit_coord.find(horse_coord[1])
column = alpha_coord.find(horse_coord[0])

matrix[row][column] = 'N'

for i in range(n):
    for j in range(n):
        if i in (row - 2, row + 2) and j in (column - 1, column + 1):
            matrix[i][j] = '*'
        elif i in (row - 1, row + 1) and j in (column - 2, column + 2):
            matrix[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
