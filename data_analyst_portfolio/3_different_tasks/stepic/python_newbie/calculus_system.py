'''Test
'''


def calc_10_to_16(number):
    digits = '0123456789ABCDEFG'

    lst = []
    while number > 16:
        lst.append(number % 16)
        number //= 16
    else:
        lst.append(number)

    lst = lst[::-1]
    for i in range(len(lst)):
        lst[i] = digits[lst[i]]

    result = ''.join(lst)
    print(result)


def calc_10_to_2(number):
    lst = []
    while number >= 2:
        lst.append(str(number % 2))
        number //= 2
    else:
        lst.append(str(number))

    lst = lst[::-1]
    result = ''.join(lst)
    print(result)



calc_10_to_16(1000)
calc_10_to_2(513)
print(bin(513))
print(hex(1000))



