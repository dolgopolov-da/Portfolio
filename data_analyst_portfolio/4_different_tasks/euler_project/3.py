'''
Задача №3. Наибольший простой делитель.
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

import math

n = 600851475143

def factorization(n):
    simple_numbers = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            simple_numbers.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        simple_numbers.append(n)
    return simple_numbers


Answer = factorization(n)
print(math.prod(Answer))
print(Answer)
print('Ответ на поставленный в задаче вопрос:', Answer[len(Answer)-1])

