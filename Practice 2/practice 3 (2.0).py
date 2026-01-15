from math import inf


def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    sum_roman = 0
    last_int = inf
    for char in s:
        if last_int < roman[char]:
            sum_roman = sum_roman - (last_int * 2) + roman[char]
            last_int = roman[char]
        else:
            last_int = roman[char]
            sum_roman += roman[char]
    return sum_roman


def int_to_roman(n):
    if n <= 0:
        return ''
    data = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = []
    for value, symbol in data:
        if n == 0:
            break
        k = n // value
        if k:
            res.append(symbol * k)
            n -= value * k
    return ''.join(res)


roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
result = [
    (roman_num, roman_to_int(roman_num))
    for roman_num in roman_tests
]
print(result)

