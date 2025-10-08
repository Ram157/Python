from random import randint
RandInt=randint(1, 100)
print('УГАДАЙ ЧИСЛО ОТ 1 ДО 100')
while True:
    try: 
        s = int(input())
        if s != RandInt:
            print(['ЗАДАННОЕ ЧИСЛО МЕНЬШЕ' if s > RandInt  else 'ЗАДАННОЕ ЧИСЛО БОЛЬШЕ' ])
            break
        else: 
            print('ВЫ УГАДАЛИ УРА')
            break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
while True:
    try: 
        s = int(input())
        if s != RandInt:
         print(['ЗАДАННОЕ ЧИСЛО МЕНЬШЕ' if s > RandInt else 'ЗАДАННОЕ ЧИСЛО БОЛЬШЕ' ],
               ' А ТАКЖЕ Остаток от 2 у заданного числа:',s%2)
        else: 
            print('ВЫ УГАДАЛИ УРА')
        break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
while True:
    try: 
        s = int(input())
        print(['ЗАДАННОЕ ЧИСЛО МЕНЬШЕ' if s > RandInt else 'ЗАДАННОЕ ЧИСЛО БОЛЬШЕ' ])
        break
    except: 
        print('ТЫ ВВЕЛ НЕ ЧИСЛО ВВЕДИ ЗАНОВО')
        continue
while True:
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

