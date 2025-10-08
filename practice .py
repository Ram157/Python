def print_pack_report(n):
    if n<=1:
        print('Число <=1')
        return #
    while n!=1:
        if n%5==0 and n%3==0: print(n,'--Расфасуем по 3 или по 5')
        elif n%5==0 and n%3!=0: print(n, '--Расфасуем по 5')
        elif n%3==0:print(n,'--Расфасуем по 3')
        else: print(n,'Не заказываем')
        n-=1
print_pack_report(15)