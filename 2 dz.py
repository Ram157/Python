from random import *
from string import *
print('Введите длину пароля: ')
len=input()
lett = ''.join(choice(ascii_uppercase) for _ in range(3))
digit=''.join(choice(digits) for _ in range(3))
spec=''.join(choice(digits) for _ in range(2))
