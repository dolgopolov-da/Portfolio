# объявление функции
def is_password_good(password):
    result = True
    if len(password) < 8:
        result = False
        return result
    is_upper = False
    is_lower = False
    is_digit = False
    for i in range(len(password)):
        if password[i].isalpha():
            if password[i] == password[i].upper():
                is_upper = True
            elif password[i] == password[i].lower():
                is_lower = True
        elif password[i].isdigit():
            is_digit = True
    if is_upper != True or is_lower != True or is_digit != True:
        result = False
        return result
    else:
        return result


# считываем данные
txt = 'aaaaaaA@'

# вызываем функцию
print(is_password_good(txt))