from random import randint
RandInt=randint(1, 100)
print('УГАДАЙ ЧИСЛО ОТ 1 ДО 100')
while True:
    try: 
        InpInt = int(input())
        print(['ЗАДАННОЕ ЧИСЛО МЕНЬШЕ' if InpInt > RandInt  else 'ЗАДАННОЕ ЧИСЛО БОЛЬШЕ' ])
        break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
while True and RandInt != InpInt:
    try: 
        InpInt = int(input())
        if InpInt != RandInt:
         print(['ЗАДАННОЕ ЧИСЛО МЕНЬШЕ' if InpInt > RandInt else 'ЗАДАННОЕ ЧИСЛО БОЛЬШЕ' ],
               ' А ТАКЖЕ Остаток от 2 у заданного числа:',InpInt%2)
        else: 
            print('ВЫ УГАДАЛИ УРА')
        break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
while True and RandInt != InpInt:
    try: 
        InpInt = int(input())
        print('ЗАДАННЫМ ЧИСЛОМ БЫЛО',RandInt)
        break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
while True and RandInt != InpInt:
    try: 
        s = int(input())
        if s != RandInt:
            print('ЗАДАННОЕ ЧИСЛО',RandInt) 
        else: 
            print('ВЫ УГАДАЛИ УРА')
        break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
if RandInt == InpInt:print('ТЫ УГАДАЛ, УРА')


