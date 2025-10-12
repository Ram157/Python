print('Введите строку')
s=input().lower()
s2=set(s)
l=[]
c=0
for x in s2:
    l+=[(s.count(x),x)]
l.sort(key=lambda y:-y[0])
for count, char in l[:3]:
    print(f"Символ '{char}' встречается {count} раз")
