from datetime import datetime, date

DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные': [
        {'amount': 0.5, 'expiration_date': date(2023, 7, 15)},
        {'amount': 2, 'expiration_date': date(2023, 8, 1)},
    ],
    'Пельмени Бульмени': [
        {'amount': 0.8, 'expiration_date': date(2025, 10, 13)}
    ],
    'Вода': [
        {'amount': 1.5, 'expiration_date': None}
    ],
}


def parse_date(date_str: str) -> date:
    parsed_date = None
    if date_str:
        parsed_date = datetime.strptime(date_str, DATE_FORMAT).date()
    return parsed_date


def add(title, amount, expiration_date):
    info = {'amount': amount, 'expiration_date': expiration_date}
    if title not in goods:
        goods[title] = []
    goods[title].append(info)


def add_by_note(s):
    parts = s.strip().split()
    last_part = parts[-1]
    possible_date = parse_date(last_part)
    
    if possible_date is not None:
        #Формат название количество дата
        quantity_str = parts[-2]
        name_parts = parts[:-2]
        name = ' '.join(name_parts)
        expiration_date_value = possible_date
    else:
        #Формат название количество
        quantity_str = parts[-1]
        name_parts = parts[:-1]
        name = ' '.join(name_parts)
        expiration_date_value = None
    
    quantity = float(quantity_str)
    add(title=name, amount=quantity, expiration_date=expiration_date_value)
    return name, quantity, expiration_date_value


def find(s):
    s = s.lower()
    matching_products = {}
    for name, partii in goods.items():
        if s in name.lower():
            matching_products[name] = partii
    
    return matching_products


def amount(s) -> float:
    found_items = find(s)
    total_weight = 0.0
    
    for name, partii in found_items.items():
        for part in partii:
            total_weight += part['amount']
    
    return total_weight


def put_food_in_refrigerator():
    print('Что будем ложить? ')
    print('Напиши в формате: {НАЗВАНИЕ} {КОЛ_ВО} {ГОД-МЕСЯЦ-ДЕНЬ (опционально)}')
    inp = input()
    name, product_amount, _ = add_by_note(inp)
    print(f'Ты успешно добавил {name} в кол-ве {product_amount} кг')
    menu()


def find_food_in_refrigerator():
    print('Что хочешь найти? ')
    search = input('Ввод: ')
    found_products = find(search)
    total_weight = amount(search)

    if len(found_products) == 0:
        print('К сожалению, я ничего не нашел(((')
        menu()
        return

    print('Нашел!')
    print("-" * 50)

    for name, partii_list in found_products.items():
        print(f' {name}:')
        part_number = 0
        for part in partii_list:
            part_number += 1
            part_amount = part['amount']
            part_date = part['expiration_date']
            
            if part_date is not None:
                print(f'- Партия {part_number}: {part_amount} кг, срок годности: {part_date}')
            else:
                print(f'- Партия {part_number}: {part_amount} кг')
    
    print("-" * 50)
    print(f'Всего: {total_weight} кг')
    menu()

def menu(): 
    while True:
        print(f'На данный момент холодильник забит {amount('')} кг еды!')
        print('Возможные операции:')
        print('1. Положить продукты в холодильник')
        print('2. Найти продукты в холодильнике')
        user_choice = input('Какое действие Вы хотите сделать? Напишите ТОЛЬКО цифру: ')

        if user_choice == '1':
            put_food_in_refrigerator()
            break
        elif user_choice == '2':
            find_food_in_refrigerator()
            break
        else:
            menu()
            break

menu()
