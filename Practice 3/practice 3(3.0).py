from random import randint

win_counter_bot = 0
win_counter_player = 0

while win_counter_bot != 3 and win_counter_player != 3:
    print('КАМЕНЬ---1\n'
          'НОЖНИЦЫ---2\n'
          'БУМАГА---3\n')
    choice_player = input()
    if choice_player not in ('1', '2', '3'):
        continue
    choice_bot = str(randint(1, 3))
    if choice_bot == choice_player:
        print('НИЧЬЯ')
        continue
    else:
        if ((choice_player == '3' and choice_bot == '1') or
            (choice_player == '2' and choice_bot == '3') or
            (choice_player == '1' and choice_bot == '2')):
                print('ТЫ ВЫИГРАЛ РАУНД УРА')
                win_counter_player += 1
        else:
            print('Ты проиграл раунд(((')
            win_counter_bot += 1
    print(f'ХОД ПРОТИВНИКА БЫЛ -- {choice_bot}')
if win_counter_bot == 3:
    print('Вы проиграли игру(')
else:
    print('ВЫ ВЫИГРАЛИ ИГРУ, УРА')
