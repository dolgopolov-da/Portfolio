# объявление функции
def number_to_words(num):
    lst = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    if num in range(1, 11):
        for i in range(1, num + 1):
            if i == num:
                return lst[i]
    elif num == 11:
        return 'одиннадцать'
    elif num == 12:
        return 'двенадцать'
    elif num == 13:
        return 'тринадцать'
    elif num in range(14, 20):
        last_dig = num % 10
        str_last_dig = lst[last_dig]
        return str_last_dig[:len(str_last_dig) - 1] + 'надцать'
    elif num in range(20, 100):
        result = ''
        first_dig = num // 10
        last_dig = num % 10
        str_last_dig = lst[last_dig]
        if num in range(20, 40):
            for i in (2, 3):
                if first_dig == i:
                    result += lst[i] + 'дцать'
                    if last_dig != 0:
                        result += ' ' + str_last_dig
                        return result
                    else:
                        return result
        if num in range(40, 50):
            if first_dig == 4:
                result += 'сорок'
            if last_dig != 0:
                result += ' ' + str_last_dig
                return result
            else:
                return result
        if num in range(50, 90):
            for i in range(5, 9):
                if first_dig == i:
                    result += lst[i] + 'десят'
                    if last_dig != 0:
                        result += ' ' + str_last_dig
                        return result
                    else:
                        return result
        if num in range(90, 100):
            result += 'девяносто'
            if last_dig != 0:
                result += ' ' + str_last_dig
                return result
            else:
                return result



# считываем данные
n = 95

# вызываем функцию
print(number_to_words(n))