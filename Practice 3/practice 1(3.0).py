from random import randint

rand_int = randint(1, 100)
print('УГАДАЙ ЧИСЛО ОТ 1 ДО 100')
popitka = 0

while True:
    try:
        inp_int = int(input())
        popitka += 1
        if inp_int == rand_int:
            print('ВЫ УГАДАЛИ УРА')
            break
        elif inp_int > rand_int:
            print('ЗАДАННОЕ ЧИСЛО МЕНЬШЕ')
        else:
            print('ЗАДАННОЕ ЧИСЛО БОЛЬШЕ')
        if popitka >= 2:
            print(f'А ТАКЖЕ Остаток от 2 у заданного числа: {rand_int % 2}')
    except ValueError:
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue


