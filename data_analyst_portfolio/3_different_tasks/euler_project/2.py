'''
Задача №2. Четные числа Фибоначчи.
Каждый следующий элемент ряда Фибоначчи получается
при сложении двух предыдущих. Начиная с 1 и 2,
первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
'''

numbers = [1, 2, 3]
finish_numbers = []
for i in range(29):
    next_num = numbers[len(numbers)-1] + numbers[len(numbers)-2]
    numbers.append(next_num)

for j in numbers:
    if j % 2 == 0:
        finish_numbers.append(j)

print(numbers)
print(finish_numbers)
print(sum(finish_numbers))
