'''
Магический квадрат 🌶️

Магическим квадратом порядка n называется квадратная таблица размера n×n,
составленная из всех чисел 1,2,3,…,n**2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой.
Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
'''

n = int(input())
matrix = []
digit_list = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

is_quad_magic = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] in range(1, n**2 + 1) and matrix[i][j] not in digit_list:
            digit_list.append(matrix[i][j])
if len(digit_list) != n ** 2:
    is_quad_magic = False

if not is_quad_magic:
    print('NO')
else:
    row_sum = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != row_sum:
            is_quad_magic = False

    if not is_quad_magic:
        print('NO')
    else:
        for j in range(n):
            col_sum = 0
            for i in range(n):
                col_sum += matrix[i][j]
            if col_sum != row_sum:
                is_quad_magic = False
                break

        if not is_quad_magic:
            print('NO')
        else:
            main_diag_sum = 0
            second_diag_sum = 0
            for i in range(n):
                main_diag_sum += matrix[i][i]
            for i in range(n):
                second_diag_sum += matrix[i][n - i - 1]
            if main_diag_sum != row_sum or second_diag_sum != row_sum:
                is_quad_magic = False
                print('NO')
            else:
                print('YES')
