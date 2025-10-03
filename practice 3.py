from random import *
from string import *
print('Введите длину пароля: ')
try:len=int(input())
except ValueError:
 print('ВВОДИ ЧИСЛО')
 len=int(input())
print('Вводите 1 ЕСЛИ НУЖЕН, 0 ЕСЛИ НЕ НУЖЕН')
print('Должен ли быть верхний регистр?')
verhreg=int(input())

verhreg=int(input())
print('Должен ли быть верхний регистр?')
spec_symbols='!@#$%^&*()'

passs = ''.join(choice(ascii_uppercase+digits+spec_symbols) for _ in range(len))
passs=list(passs)
shuffle(passs)
passs=''.join(passs)
print(passs)