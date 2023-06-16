'''Аве, Цезарь 🌶️
На вход программе подается строка текста на английском языке,
в которой нужно зашифровать все слова. Каждое слово строки следует
зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.
'''

import random

txt = 'To be, or not to be, that is the question'

# строка латинских символов
dict_lower = 'abcdefghijklmnopqrstuvwxyz'
dict_upper = ''.join([dict_lower[i].upper() for i in range(len(dict_lower))])

lst = []
encrypted_txt = ''

start_pos = 0
end_pos = 0
for i in range(len(txt)):
    if txt[i].isalpha():
        if i < len(txt) - 1:
            continue
        else:
            end_pos = i + 1
            lst.append(txt[start_pos:end_pos])
    else:
        end_pos = i
        lst.append(txt[start_pos:end_pos])
        start_pos = i
        if i < len(txt) - 1 and txt[i + 1].isalpha():
            lst.append(txt[i])
            start_pos, end_pos = i + 1, i + 1
        elif i == len(txt) - 1:
            lst.append(txt[i])

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] in dict_lower:
            encrypted_txt += dict_lower[(dict_lower.find(lst[i][j]) + len(lst[i])) % len(dict_lower)]
        elif lst[i][j] in dict_upper:
            encrypted_txt += dict_upper[(dict_upper.find(lst[i][j]) + len(lst[i])) % len(dict_upper)]
        else:
            encrypted_txt += lst[i][j]
print(lst)
print(encrypted_txt)


