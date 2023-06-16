'''Игра "Угадайка"'''

import random

def is_valid(text, n):
    for i in range(len(text)):
        if not text[i].isdigit():
            return False
    if not int(text) in range(1, n):
        return False
    else:
        return True


def main():
    while True:
        n = input('Введите максимальный предел загадываемого числа (целое число больше 1): ')
        is_n_digit = True
        for i in range(len(n)):
            if not n[i].isdigit():
                print('Нужно ввести целое число больше 1.')
                is_n_digit = False
                break
        if not is_n_digit:
            continue
        else:
            if int(n) > 1 and float(n) == int(n):
                n = int(n)
                break
            else:
                print('Нужно ввести целое число больше 1.')

    guess_number = random.randint(1, n)
    print('Добро пожаловать в числовую угадайку')

    game = True
    count = 0

    while game:
        count += 1
        txt = input(f'Введите число от 1 до {n}: ')
        if not is_valid(txt, n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            user_number = int(txt)

        if user_number < guess_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > guess_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            game = False
    else:
        print(f'Количество попыток: {count}')

    while True:
        again = input('Хотите сыграть ещё раз? ("д" - да, "н" - нет): ')
        if again == "н":
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif again == "д":
            main()
            break
        else:
            print('Нужно ввести: "д" - да или "н" - нет, другие ответы не принимаются :)')


main()