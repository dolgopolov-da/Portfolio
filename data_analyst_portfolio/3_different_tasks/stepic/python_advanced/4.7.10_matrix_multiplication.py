'''
Умножение матриц 🌶️

Напишите программу, которая перемножает две матрицы.
'''

#первая матрица
size1 = input().split()
n1 = int(size1[0])
m1 = int(size1[1])
matrix1 = []
for i in range(n1):
    row = [int(num) for num in input().split()]
    matrix1.append(row)

input()

#вторая матрица
size2 = input().split()
n2 = int(size2[0])
m2 = int(size2[1])
matrix2 = []
for i in range(n2):
    row = [int(num) for num in input().split()]
    matrix2.append(row)

#меняем местами строки матрицы2 со столбцами (чтобы длина вложенных списков равнялась матрице1)
matrix2_rotate = []
for j in range(m2):
    lst = []
    for i in range(n2):
        lst.append(matrix2[i][j])
    matrix2_rotate.append(lst)

#задаем размеры матрицы3 исходя из размеров матриц 1 и 2, заполняем матрицу3 нулями
n3, m3 = n1, m2
matrix3 = [[0] * m3 for _ in range(n3)]

#заполняем матрицу3 значениями сумм произведений элементов матрицы1 и измененной матрицы2
for i in range(len(matrix1)):
    for j in range(len(matrix2_rotate)):
        for k in range(len(matrix1[i])):
            matrix3[i][j] += matrix1[i][k] * matrix2_rotate[j][k]

#выводим матрицу3
for i in range(n3):
    for j in range(m3):
        print(str(matrix3[i][j]).ljust(3), end=' ')
    print()
