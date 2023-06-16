txt = '7-123-456-c-7890'

if '-' not in txt:
    print('NO')
else:
    lst = txt.split('-')
    if len(lst) == 3 and len(lst[0]) == 3 and len(lst[1]) == 3 and len(lst[2]) == 4:
        is_digit = True
        for el in lst:
            for ch in el:
                if ch.isdigit() == False:
                    is_digit = False
        if is_digit:
            print('YES')
        else:
            print('NO')
    elif len(lst) == 4 and lst[0] == '7' and len(lst[1]) == 3 and len(lst[2]) == 3 and len(lst[3]) == 4:
        is_digit = True
        for el in lst:
            for ch in el:
                if ch.isdigit() == False:
                    is_digit = False
        if is_digit:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')