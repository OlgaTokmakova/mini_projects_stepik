# ПАРОЛИ
from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cnt_pw = int(input('Укажите количество паролей для генерации: '))
len_pw = int(input('Укажите длину одного пароля: '))


while True:
    dig_on = input('Включать ли цифры 0123456789? (y/n) ')
    if dig_on == 'y':
        chars += digits
        break
    if dig_on == 'n':
        break
    if dig_on not in ('y', 'n'):
        print('Введите "y" или "n" ')
        continue

while True:
    ABC_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
    if ABC_on == 'y':
        chars += uppercase_letters
        break
    if ABC_on == 'n':
        break
    if ABC_on not in ('y', 'n'):
        print('Введите "y" или "n" ')
        continue

while True:
    abc_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
    if abc_on == 'y':
        chars += lowercase_letters
        break
    if abc_on == 'n':
        break
    if abc_on not in ('y', 'n'):
        print('Введите "y" или "n" ')
        continue

while True:
    ch_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
    if ch_on == 'y':
        chars += punctuation
        break
    elif ch_on == 'n':
        break
    if ch_on not in ('y', 'n'):
        print('Введите "y" или "n" ')
        continue

while True:
    exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
    if exc_on == 'y':
        chars = chars.replace('i', '')
        chars = chars.replace('l', '')
        chars = chars.replace('1', '')
        chars = chars.replace('L', '')
        chars = chars.replace('o', '')
        chars = chars.replace('O', '')
        chars = chars.replace('0', '')
        break
    if exc_on == 'n':
        break
    if exc_on not in ('y', 'n'):
        print('Введите "y" или "n" ')
        continue



def generate_password(length, chars):
    psw = ''
    for i in range(length):
        psw += choice(chars)
    return psw


for i in range(cnt_pw):
    print(generate_password(len_pw, chars))
