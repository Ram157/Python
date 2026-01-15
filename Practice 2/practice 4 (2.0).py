from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits

while True:
    chars = ''
    print('Введите длину пароля: ')
    try:
        length = int(input())
    except ValueError:
        print('ВВОДИ ЦЕЛОЕ ЧИСЛО')
        continue
    print('Вводите 1 ЕСЛИ НУЖЕН, 0 ЕСЛИ НЕ НУЖЕН')
    print('Должен ли быть верхний регистр?')
    while True:
        try:
            if int(input()) == 1:
                chars += ascii_uppercase
            break
        except ValueError:
            print('НУЖЕН ЛИБО 0  ЛИБО 1')
    print('Должен ли быть нижний регистр?')
    while True:
        try:
            if int(input()) == 1:
                chars += ascii_lowercase
            break
        except ValueError:
            print('НУЖЕН ЛИБО 0  ЛИБО 1')
    print('Должны ли быть цифры?')
    while True:
        try:
            if int(input()) == 1:
                chars += digits
            break
        except ValueError:
            print('НУЖЕН ЛИБО 0  ЛИБО 1')
    print('Должны ли быть спец символы?')
    while True:
        try:
            if int(input()) == 1:
                chars += '!@#$%^&*()'
            break
        except ValueError:
            print('НУЖЕН ЛИБО 0  ЛИБО 1')
    password = list(''.join(choice(chars) for _ in range(length)))
    shuffle(password)
    password = ''.join(password)
    print(password)
    print('ЕСЛИ ХОТИТЕ ЕЩЕ ОДИН ПАРОЛЬ--1 '
          'ЕСЛИ ХОТИТЕ ВЫЙТИ--ЛЮБОЙ ДРУГОЙ СИМВОЛ')
    if input() == '1':
        continue
    else:
        break
