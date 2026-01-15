from random import choice
from string import ascii_uppercase, digits

print('Введите длину пароля: ')
length = int(input())
spec_symbols = '!@#$%^&*()'
passw = ''.join(
    choice(ascii_uppercase + digits + spec_symbols)
    for _ in range(length)
)
print(passw)