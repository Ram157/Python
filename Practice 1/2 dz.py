from random import *
from string import *
print('Введите длину пароля: ')
spec_symbols='!@#$%^&*()'
len=int(input())
passs = ''.join(choice(ascii_uppercase+digits+spec_symbols) for _ in range(len))
passs=list(passs)
shuffle(passs)
passs=''.join(passs)
print(passs)