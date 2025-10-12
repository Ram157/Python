from random import randint
WinCounterBot = WinCounterPlayer = 0
while WinCounterBot != 3 and WinCounterPlayer != 3:
    print('КАМЕНЬ---1\n'
          'НОЖНИЦЫ---2\n'
           'БУМАГА---3\n')
    ChoicePlayer = input()
    if all(ChoicePlayer != x for x in ('123')): continue
    ChoiceBot = str(randint(1,3))
    if ChoiceBot == ChoicePlayer:
        print('НИЧЬЯ')
        continue 
    else:
        if ((ChoicePlayer == '3' and ChoiceBot == '1' ) 
            or (ChoicePlayer == '2' and ChoiceBot == '3')
           or (ChoicePlayer == '1' and ChoiceBot == '2')):
                print('ТЫ ВЫИГРАЛ РАУНД УРА')
                WinCounterPlayer += 1
        else:
             print('Ты проиграл раунд(((')
             WinCounterBot += 1
if WinCounterBot == 3: print('Вы проиграли игру(')
else: print('ВЫ ВЫИГРАЛИ ИГРУ, УРА')          
  
        
