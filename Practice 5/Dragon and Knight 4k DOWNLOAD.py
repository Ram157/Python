from random import randint

class Creature:
    def __init__(self, hp, power, name):
        self._hp = hp
        self._power = power
        self._name = name

    def info(self):
        print(f'NAME: {self._name} || POWER: {self._power} || HP: {self._hp}')

    def get_hp(self):
        return self._hp

    def set_hp(self, value):
        self._hp = max(0, value)

    def get_power(self):
        return self._power

    def set_power(self, value):
        self._power = value

    def get_name(self):
        return self._name


class Dragon(Creature):
    def fireBall(self, enemy):
        damage = randint(2, 4)
        print(f'{self.get_name()} пускает огненный шар! Урон: {damage}')
        enemy.set_hp(enemy.get_hp() - damage)

    def atackKogti(self, enemy):
        damage = randint(1, 2)
        print(f'{self.get_name()} атакует когтями! Урон: {damage}')
        enemy.set_hp(enemy.get_hp() - damage)

    def heal(self):
        heal_value = randint(1, 2)
        print(f'{self.get_name()} восстанавливает {heal_value} HP!')
        self.set_hp(self.get_hp() + heal_value)


class Player(Creature):
    def meditation(self):
        print(f'{self.get_name()} медитирует и восстанавливает 1 HP.')
        self.set_hp(self.get_hp() + 1)

    def atack(self, enemy):
        damage = randint(self.get_power(), self.get_power() * 2)
        print(f'{self.get_name()} атакует мечом! Урон: {damage}')
        enemy.set_hp(enemy.get_hp() - damage)

    def bowAtack(self, enemy):
        damage = randint(1, 2)
        print(f'{self.get_name()} стреляет из лука! Урон: {damage}')
        enemy.set_hp(enemy.get_hp() - damage)

    def trening(self):
        print(f'{self.get_name()} тренируется и увеличивает силу на 1.')
        self.set_power(self.get_power() + 1)


print('СОЗДАНИЕ ПЕРСОНАЖА\nВВЕДИТЕ ИМЯ ПЕРСОНАЖА:')
nick = input('> ')
player1 = Player(5, 2, nick)
dragon1 = Dragon(20, 2, 'Вадим')

choice = None
time = 0

while choice != '3' and time < 6:
    print('\nВАШИ ХАРАКТЕРИСТИКИ:')
    player1.info()
    print('\n1 — Медитация\n2 — Тренировка\n3 — В путь')
    choice = input('> ')
    if choice == '1':
        player1.meditation()
    elif choice == '2':
        player1.trening()
    elif choice == '3':
        break
    else:
        print('Некорректный выбор.')
        continue
    time += 1
if time >= 6:
    print('\nВы слишком долго готовились и упустили дракона. Приключение закончилось.')
else:
    print('\nВы отправились в путь...И НАТКНУЛИСЬ НА ДРАКОНА!')
    while dragon1.get_hp() > 0 and player1.get_hp() > 0:
        print('Характеристики дракона:')
        dragon1.info()
        print('Ваши характеристики:')
        player1.info()
        print('Ваши действия:\n1 — Атака мечом\n2 — Атака из лука\n3 — Медитация')
        attack_choice = input('> ')
        if attack_choice == '1':
            player1.atack(dragon1)
        elif attack_choice == '2':
            player1.bowAtack(dragon1)
        elif attack_choice == '3':
            player1.meditation()
        else:
            print('Вы замешкались...')
            continue
        if dragon1.get_hp() > 0:
            move = randint(1, 4)
            if move == 1:
                dragon1.fireBall(player1)
            elif move == 2:
                dragon1.atackKogti(player1)
            else:
                dragon1.heal()
        time += 1
    if player1.get_hp() > 0 and dragon1.get_hp() <= 0:
        print('Вы победили! Дракон повержен, слава герою!')
    elif player1.get_hp() <= 0 and dragon1.get_hp() > 0:
        print('Вы проиграли... Дракон победил.')
    else:
        print('Вы и дракон поняли, что бой бессмысленен, и решили заключить мир.')
