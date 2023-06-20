'''12 месяцев

Решите уравнение в натуральных числах
28n+30k+31m=365

Примечание. Используйте вложенный цикл for. В первую
очередь запишите решение с наименьшим значением n.
'''

import math

max_value = math.ceil(365**0.5)
for n in range(1, max_value):
    for k in range(1, max_value):
        for m in range(1, max_value):
            if 28*n + 30*k + 31*m == 365:
                print('n =', n, 'k =', k, 'm =', m)