'''
Задача №1.
Если выписать все натуральные числа меньше 10,
кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
'''

numbers = []
for i in range(0, 1000, 3):
    if i > 0:
        numbers.append(i)
for i in range(0, 1000, 5):
    if i > 0:
        numbers.append(i)

summ = sum(numbers)
print(numbers)
print(summ)