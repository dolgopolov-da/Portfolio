'''Шифр Цезаря'''

import random

# строка латинских символов
en_dict_lower = 'abcdefghijklmnopqrstuvwxyz'
en_dict_upper = ''.join([en_dict_lower[i].upper() for i in range(len(en_dict_lower))])

# строка кириллических символов
ru_dict_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_dict_upper = ''.join([ru_dict_lower[i].upper() for i in range(len(ru_dict_lower))])

# строки нешифруемых символов
digits = '0123456789'
punctuation = ',.;:!#$%&*+-=?@^_ '

def what_to_do():
    """Определяет направления (шифрование/дешифрование)"""
    while True:
        what_to_do = input('Выберите направление ("1" или "ш" - шифрование, "2" или "д" - дешифрование): ')
        if what_to_do not in ('1', 'ш', '2', 'д'):
            print('Неверный ввод')
        else:
            return what_to_do


def lang_selection(dict1_low, dict1_up, dict2_low, dict2_up):
    """Выбор языка шифруемого сообщения"""
    while True:
        lang_selection = input('Укажите язык шифруемого сообщения: "ru"/"1" или "en"/"2": ')
        if lang_selection == 'ru' or lang_selection == '1':
            return dict1_low, dict1_up
        elif lang_selection == 'en' or lang_selection == '2':
            return dict2_low, dict2_up
        else:
            print('Неверный ввод')


def encrypt_text(text, dict_low, dict_up):
    """Запрашивает шаг сдвига и выполняет шифрование введенного текста"""
    rot_n = int(input('Введите шаг сдвига для шифрования: '))
    print(f'Используемое преобразование в шифре Цезаря: ROT_{rot_n}')
    encrypted_dict_low = ''
    encrypted_dict_up = ''
    encrypted_text = ''

    for i in range(len(dict_low)):
        encrypted_dict_low += dict_low[(i + rot_n) % len(dict_low)]
    for i in range(len(dict_up)):
        encrypted_dict_up += dict_up[(i + rot_n) % len(dict_up)]

    for i in range(len(text)):
        if text[i] in dict_low:
            encrypted_text += encrypted_dict_low[dict_low.find(text[i])]
        elif text[i] in dict_up:
            encrypted_text += encrypted_dict_up[dict_up.find(text[i])]
        elif text[i] in digits:
            encrypted_text += text[i]
        elif text[i] in punctuation:
            encrypted_text += text[i]

    return encrypted_text


def decrypt_text(text, dict_low, dict_up):
    """Запрашивает шаг сдвига и выполняет дешифрование введенного текста"""
    rot_n = int(input('Введите шаг сдвига для дешифровки: '))
    print(f'Используемое преобразование в шифре Цезаря: ROT_{rot_n}')
    decrypted_dict_low = ''
    decrypted_dict_up = ''
    decrypted_text = ''

    for i in range(len(dict_low)):
        decrypted_dict_low += dict_low[(i - rot_n) % len(dict_low)]
    for i in range(len(dict_up)):
        decrypted_dict_up += dict_up[(i - rot_n) % len(dict_up)]

    for i in range(len(text)):
        if text[i] in dict_low:
            decrypted_text += decrypted_dict_low[dict_low.find(text[i])]
        elif text[i] in dict_up:
            decrypted_text += decrypted_dict_up[dict_up.find(text[i])]
        elif text[i] in digits:
            decrypted_text += text[i]
        elif text[i] in punctuation:
            decrypted_text += text[i]

    return decrypted_text


def main():
    # выбор направления (шифрование или дешифрование)
    direction = what_to_do()

    # выбор языка шифруемого/дешифруемого сообщения
    dict_lower, dict_upper = lang_selection(ru_dict_lower, ru_dict_upper, en_dict_lower, en_dict_upper)

    # ввод и проверка шифруемого/дешифруемого сообщения
    is_message_valid = False
    while not is_message_valid:
        message = input('Введите шифруемое/дешифруемое сообщение: ')
        for i in range(len(message)):
            if message[i] not in dict_lower + dict_upper + digits + punctuation:
                print('В введенном сообщении обнаружен символ из другого языка.')
                while True:
                    print('Выберите действие:', '1 - ввести сообщение', '2 - изменить выбор языка', sep='\n')
                    reselect = input()
                    if reselect == '1':
                        break
                    elif reselect == '2':
                        dict_lower, dict_upper = lang_selection(ru_dict_lower, ru_dict_upper,
                                                                en_dict_lower, en_dict_upper)
                        break
                    else:
                        print('Неверный ввод')
            else:
                is_message_valid = True
                break


    # шифрование/дешифрование сообщения
    if direction in ('1', 'ш'):
        final_message = encrypt_text(message, dict_lower, dict_upper)
        print(f'Введенное сообщение: "{message}"')
        print(f'Зашифрованное сообщение: "{final_message}"')
    else:
        final_message = decrypt_text(message, dict_lower, dict_upper)
        print(f'Введенное сообщение: "{message}"')
        print(f'Дешифрованное сообщение: "{final_message}"')


main()