from random import randint 
class Creature():
    def __init__(self,hp, power, name) -> None:
        self.power = power
        self.name = name
        self.hp = hp
    def info(self):
        print(f'NAME: {self.name} || POWER: {self.power}, || HP: {self.hp}')
class Dragon(Creature):
    def fireBall(enemy):
        enemy.hp -= 2
    def atackKogti(enemy):
        enemy.hp-=1
class Player(Creature):
    def meditation(self)->None:
        self.hp += 1
    def atack(self,enemy):
        enemy.hp -= self.power*2
    def bowAtack(self, enemy):
        enemy.hp -= 1
    def trening(self) -> None:
        self.power += 1

print('СОЗДАНИЕ ПЕРСОНАЖА \n ВВЕДИТЕ ИМЯ ПЕРСОНАЖА')
nick = input()
player1 = Player(1, 1, nick)
dragon1 = Dragon(3, 1, 'Vadim')
chouse=None
time=0
while chouse != '3' or time == 6:
    player1.info()
    print('МЕДИТАЦИЯ--1\nТРЕНИРОВКА--2\nВ ПУТЬ--3')
    chouse = input()
    if chouse == '1': player1.meditation()
    elif chouse =='2': player1.trening()
    else: break
    time+=1
if time >= 6:
    print('ВЫ СЛИШКОМ МНОГО ТРЕНИРОВАЛИСЬ ИЛИ ЖЕ МЕДИТИРОВАЛИ, ЧТО УПУСТИЛИ ДРАКОНА, ВАШЕ ПУТЕШЕСТВИЕ КОНЧИЛОСЬ')
else: 
 while dragon1.hp > 0 and player1.hp > 0: 
    print(f'ВЫ НАТКНУЛИСЬ НА ДРАКОНА!!! ЕГО ХАРАКТЕРИСТИКИ: ')
    dragon1.info()
    print(f'ВАШИ ХАРАКТЕРИСТИКИ: {player1.info()}')
    print('ВАШИ ДЕЙСТВИЯ??\n1--АТАКА МЕЧОМ\n2--АТАКА ЛУКОМ')
    chouseAtack = input()
    if chouseAtack == '1': player1.atack(dragon1)
    if chouseAtack == '2': player1.bowAtack(dragon1)
    time += 1
    if time % 3 == 0:dragon1.fireBall(player1)
    else:dragon1.atackKogti(player1)
if player1.hp>0:print('ВЫ ПОБЕДИЛИ УРА')
else:print("RIPPPPPPP")
