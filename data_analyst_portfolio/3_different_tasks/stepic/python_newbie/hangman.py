'''Игра "Виселица" (Hangman)
'''

import random, words_list

# заполняем список возможных слов из файла words_list.py
words = random.sample(words_list.words, 50)
ru_dict = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def get_word(list):
    '''Возвращает случайное слово из списка в верхнем регистре'''
    word = random.choice(list).upper()
    return word


def display_hangman(tries):
    '''Функция получения текущего состояния'''
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = word[0] + '_' * (len(word) - 2) + word[len(word) - 1]
    lst_word_completion = list(word_completion)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        attempt = input('Введите букву кириллицы или слово: ').upper()
        if attempt in guessed_letters or attempt in guessed_words:
            print('Вы это уже пробовали, попытка не засчитана.')
        elif attempt not in ru_dict:
            print('Неверный ввод. Ожидается буква кириллицы или слово целиком, попытка не засчитана.')
        elif attempt == word:
            guessed = True
        elif attempt in word:
            guessed_letters.append(attempt)
            for i in range(len(word)):
                if word[i] == attempt:
                    lst_word_completion[i] = word[i]
            word_completion = ''.join(lst_word_completion)
            if word_completion == word:
                guessed = True
            print(word_completion)
        elif attempt not in word and len(attempt) == len(word):
            tries -= 1
            guessed_words.append(attempt)
            print(display_hangman(tries))
        elif attempt not in word and len(attempt) == 1:
            tries -= 1
            guessed_words.append(attempt)
            print(display_hangman(tries))
    else:
        if guessed:
            print('Поздравляем, вы угадали слово! Вы победили!')
        elif tries == 0:
            print(f'Загаданное слово: {word}.')
            print('К сожалению, вы проиграли.')


while True:
    word = get_word(words)
    play(word)
    again = input('Хотите сыграть еще? ("д" - да, "н" - нет)\n')
    if again == 'д':
        continue
    else:
        print('До свидания, возращайтесь!')
        break

