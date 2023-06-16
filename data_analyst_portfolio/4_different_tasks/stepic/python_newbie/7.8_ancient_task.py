'''Старинная задача

Имеется 100 рублей. Сколько быков, коров и телят
можно купить на все эти деньги, если плата за быка – 10 рублей,
за корову – 5 рублей, за теленка – 0.5 рубля и надо купить
100 голов скота?

Примечание. Используйте вложенный цикл for.
'''

import math

max_value = int(100**0.5)
for bull in range(1, max_value):
    for cow in range(1, max_value):
        for calf in range(1, 170):
            if 10*bull + 5*cow + 0.5*calf == 100 and bull + cow + calf == 100:
                print('bull =', bull, 'cow =', cow, 'calf =', calf)