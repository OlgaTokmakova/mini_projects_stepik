# Угадайка

from random import randint

print('Добро пожаловать в числовую угадайку!')


def is_valid(s, gran):
    if s.isdigit() and 1 <= int(s) <= gran:
        return True
    else:
        return False


def question():
    while True:
        answer = input().lower().strip()
        if answer not in ("да", "нет"):
            print("Введите 'да' или 'нет'")
            continue
        if answer == 'да':
            game()
        if answer == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


def game():
    gran = int(input('Введите предел диапазона чисел '))
    num = randint(1, gran)
    count = 0
    while True:
        number = input('Введите Ваше число ')
        if is_valid(number, gran):
            number = int(number)
        if number < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            continue
        if number > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            continue
        if number == num:
            count += 1
            print('Вы угадали, поздравляем!', 'Количество Ваших попыток', count)
            print("Хотите сыграть еще разок?) Да/Нет")
            break


game()
question()
