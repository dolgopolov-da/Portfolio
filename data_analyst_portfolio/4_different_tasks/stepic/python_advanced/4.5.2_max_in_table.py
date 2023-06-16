'''
Максимум в таблице

На вход программе подаются два натуральных числа n и m — количество
строк и столбцов в матрице, затем n строк по m
целых чисел в каждой, отделенных символом пробела.

Напишите программу, которая находит индексы (строку и столбец)
первого вхождения максимального элемента.
'''

n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)

maximum = matrix[0][0]
for i in range(n):
    if maximum < max(matrix[i]):
        maximum = max(matrix[i])

done = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == maximum:
            print(i, j)
            done = True
            break
    if done:
        break
