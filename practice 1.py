rulow = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ruup  = rulow.upper()
enlow = 'abcdefghijklmnopqrstuvwxyz'
enup  = enlow.upper()
def shift_text(text, shift):
    res = []
    for ch in text:
        if ch in rulow:
            i = rulow.index(ch)
            res.append(rulow[(i + shift) % len(rulow)])
        elif ch in ruup:
            i = ruup.index(ch)
            res.append(ruup[(i + shift) % len(ruup)])
        elif ch in enlow:
            i = enlow.index(ch)
            res.append(enlow[(i + shift) % len(enlow)])
        elif ch in enup:
            i = enup.index(ch)
            res.append(enup[(i + shift) % len(enup)])
        else:
            res.append(ch) 
    return ''.join(res)
while True:
        print('Отправьте 0 — ШИФРОВАТЬ, 1 — ДЕШИФРОВАТЬ, 2 — ВЫХОД')
        choice = input().strip()
        if choice not in ('0', '1', '2'):
            print('Введите либо 0, либо 1, либо 2')
            continue
        if choice == '2':
            break
        while True:
            print('Введите число, на которое хотите сдвинуть символы:')
            s = input().strip()
            try:
                shift = int(s)
                break
            except :
                print('Ошибка: нужно целое число.')
        print('Введите СИМВОЛЫ:')
        text = input()
        if choice == '1':
            shift = -shift
        print(shift_text(text, shift))

