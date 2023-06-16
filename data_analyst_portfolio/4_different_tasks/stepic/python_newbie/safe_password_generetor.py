'''Генератор безопасных паролей'''

import random

def is_include_digits():
    while True:
        include_digits = input('Включать в пароль цифры? ("д" - да/"н" - нет)\n')
        if include_digits in ('д', 'да'):
            return True
        elif include_digits in ('н', 'нет'):
            return False
        else:
            print('Недопустимый ответ.')


def is_include_uppercase_letters():
    while True:
        include_uppercase_letters = input('Включать в пароль прописные (верхний регистр) '
                                      'буквы? ("д" - да/"н" - нет)\n')
        if include_uppercase_letters in ('д', 'да'):
            return True
        elif include_uppercase_letters in ('н', 'нет'):
            return False
        else:
            print('Недопустимый ответ.')


def is_include_lowercase_letters():
    while True:
        include_lowercase_letters = input('Включать в пароль строчные (нижний регистр) буквы? '
                                      '("д" - да/"н" - нет)\n')
        if include_lowercase_letters in ('д', 'да'):
            return True
        elif include_lowercase_letters in ('н', 'нет'):
            return False
        else:
            print('Недопустимый ответ.')


def is_include_punctuation():
    while True:
        include_punctuation = input('Включать в пароль символы? ("д" - да/"н" - нет)\n')
        if include_punctuation in ('д', 'да'):
            return True
        elif include_punctuation in ('н', 'нет'):
            return False
        else:
            print('Недопустимый ответ.')


def is_exclude_bad_symbols():
    while True:
        exclude_bad_symbols = input('Исключать из пароля неоднозначные символы? '
                                '("д" - да/"н" - нет)\n')
        if exclude_bad_symbols in ('д', 'да'):
            return True
        elif exclude_bad_symbols in ('н', 'нет'):
            return False
        else:
            print('Недопустимый ответ.')


def generate_password(password_amount, password_len, char_list):
    # заполнение итоговой переменной chars
    password_list = []

    for i in range(int(password_amount)):
        chars = ''
        for j in range(int(password_len)):
            random_char = random.choice(char_list[random.randrange(0, len(char_list))])
            chars += random_char
        password_list.append(chars)

    print('Пароли сгенерированы: ')
    print(*password_list, sep='\n')


def main():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    bad_symbols = 'il1Lo0O'

    chars = ''
    char_list = []
    count = 0
    password_amount = input('Количество паролей для генерации: ')
    password_len = input('Введите длину пароля: ')

    # составление итогового списка допустимых символов
    while True:
        if is_exclude_bad_symbols() == True:
            if is_include_digits() == True:
                count += 1
                digit_list = [digits[i] for i in range(len(digits)) if digits[i] not in bad_symbols]
                char_list.append(digit_list)
            if is_include_lowercase_letters() == True:
                count += 1
                lowercase_letters_list = [lowercase_letters[i] for i in range(len(lowercase_letters))
                                          if lowercase_letters[i] not in bad_symbols]
                char_list.append(lowercase_letters_list)
            if is_include_uppercase_letters() == True:
                count += 1
                uppercase_letters_list = [uppercase_letters[i] for i in range(len(uppercase_letters))
                                          if uppercase_letters[i] not in bad_symbols]
                char_list.append(uppercase_letters_list)
            if is_include_punctuation() == True:
                count += 1
                punctuation_list = [punctuation[i] for i in range(len(punctuation))
                                          if punctuation[i] not in bad_symbols]
                char_list.append(punctuation_list)
        else:
            if is_include_digits() == True:
                count += 1
                digit_list = [digits[i] for i in range(len(digits))]
                char_list.append(digit_list)
            if is_include_lowercase_letters() == True:
                count += 1
                lowercase_letters_list = [lowercase_letters[i] for i in range(len(lowercase_letters))]
                char_list.append(lowercase_letters_list)
            if is_include_uppercase_letters() == True:
                count += 1
                uppercase_letters_list = [uppercase_letters[i] for i in range(len(uppercase_letters))]
                char_list.append(uppercase_letters_list)
            if is_include_punctuation() == True:
                count += 1
                punctuation_list = [punctuation[i] for i in range(len(punctuation))]
                char_list.append(punctuation_list)
        if count == 0:
            print('Не выбрано ни одного типа знаков для пароля.')
            continue
        else:
            break

    generate_password(password_amount, password_len, char_list)


main()