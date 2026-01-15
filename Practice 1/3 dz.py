print('Введите строку')
text = input().lower()
char_simv = []
for char in set(text):
    char_simv.append((text.count(char), char))
char_simv.sort(key=lambda x: -x[0])
for count, char in char_simv[:3]:
    print(f"Символ '{char}' встречается {count} раз")
