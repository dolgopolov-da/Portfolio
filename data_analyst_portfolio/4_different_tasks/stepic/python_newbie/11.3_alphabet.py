'''Алфавит

Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
'''

lst = []

for i in range(26):
    lst.append(chr(i + 97) * (i + 1))
print(lst)
