'''
Упаковка дубликатов 🌶️

На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности одинаковых
символов заданной строки в подсписки.
'''

txt = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()
lst = []
sublst = []

for i in range(len(txt)):
    if i == 0:
        sublst.append(txt[i])
        continue
    if txt[i] == txt[i - 1]:
        sublst.append(txt[i])
        if i != len(txt) - 1:
            continue
        else:
            lst.append(sublst)
    else:
        lst.append(sublst)
        sublst = []
        sublst.append(txt[i])
        if i != len(txt) - 1:
            continue
        else:
            lst.append(sublst)


print(lst)