while True:
    print('Введите слово, которое загадываете(5 букв)')
    word=input()
    if len(word)!=5 or isalpha: continue
    print('Введите возможную букву')
    InWord=input()
    if 