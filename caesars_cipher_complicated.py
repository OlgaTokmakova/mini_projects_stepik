# ШИФР ЦЕЗАРЯ УСЛОЖНЕННЫЙ (без заданного шага)

text = input('Введите Ваш текст: ').split()


def caesar(text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code_text = ''
    for i in range(len(text)):
        count = 0
        for j in text[i]:
            if j.isalpha():
                count += 1
        for j in text[i]:
            if j.isalpha():
                if j == j.lower():
                    place = eng_lower_alphabet.index(j)
                    code_text += eng_lower_alphabet[(place + int(count)) % 26]
                if j == j.upper():
                    place = eng_upper_alphabet.index(j)
                    code_text += eng_upper_alphabet[(place + int(count)) % 26]
            else:
                code_text += j
        code_text += ' '
    print(code_text)


caesar(text)