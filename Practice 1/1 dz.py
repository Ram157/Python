number = int(input('Введите ваше число: '))
chet = 'четное' if number % 2 == 0 else 'нечетное'
if 10 < number < 50:
    diapason = 'принадлежит диапазону (10, 50)'
else:
    diapason = 'не принадлежит диапазону (10, 50)'
print(f'Число {chet}, {diapason}.')