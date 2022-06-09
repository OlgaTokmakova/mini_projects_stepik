# ШИФР ЦЕЗАРЯ

quest1 = input('Выберете шифровать или дешифровать? шифр/дешифр ').lower()
while quest1 != 'шифр' and quest1 != 'дешифр':
    quest1 = input('Нужно выбрать "шифр" или "дешифр" ')

quest2 = input('Выберете язык алфавита. рус/en ').lower()
while quest2 != 'рус' and quest2 != 'en':
    quest2 = input('Нужно выбрать "рус" или "en" ')

quest3 = input('Задайте шаг сдвига ')
while not quest3.isdigit():
    quest3 = input('Введите цифру. ')

text = input('Введите Ваш текст: ')


def caesar(code, lang, step, text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    code_text = ''
    for i in range(len(text)):
        if lang == 'рус':
            alf = 32
            lower_alf = rus_lower_alphabet
            upper_alf = rus_upper_alphabet
        if lang == 'en':
            alf = 26
            lower_alf = eng_lower_alphabet
            upper_alf = eng_upper_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = lower_alf.index(text[i])
            if text[i] == text[i].upper():
                place = upper_alf.index(text[i])

            if code == 'дешифр':
                index = (place - int(step)) % alf
            if code == 'шифр':
                index = (place + int(step)) % alf

            if text[i] == text[i].lower():
                print(lower_alf[index], end='')
            if text[i] == text[i].upper():
                print(upper_alf[index], end='')
        else:
            print(text[i], end='')


caesar(quest1, quest2, quest3, text)
