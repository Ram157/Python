accounts = {}
def create_account(name):
    accounts[name] = 0
    print(f"Счёт '{name}' создан. Баланс: 0")

def deposit(name, amount):
    accounts[name] += amount
    print(f"На счёт '{name}' зачислено {amount}. Баланс: {accounts[name]}")

def withdraw(name, amount):
    if accounts[name] >= amount:
        accounts[name] -= amount
        print(f"Со счёта '{name}' снято {amount}. Баланс: {accounts[name]}")
    else:
        print("Недостаточно средств")

def transfer(from_acc, to_acc, amount):
    if accounts[from_acc] >= amount:
        accounts[from_acc] -= amount
        accounts[to_acc] += amount
        print(f"Перевод {amount} со счёта '{from_acc}' на '{to_acc}' выполнен")
    else:
        print("Недостаточно средств")

def balance(name):
    print(f"Баланс счёта '{name}': {accounts[name]}")
while True:
    command = input("Введите команду (create, deposit, withdraw, transfer, balance, exit): ")
    if command == "create":
        name = input("Введите имя счёта: ")
        create_account(name)
    elif command == "deposit":
        name = input("Введите имя счёта: ")
        amount = float(input("Введите сумму для зачисления: "))
        deposit(name, amount)
    elif command == "withdraw":
        name = input("Введите имя счёта: ")
        amount = float(input("Введите сумму для снятия: "))
        withdraw(name, amount)
    elif command == "transfer":
        from_acc = input("Введите имя отправителя: ")
        to_acc = input("Введите имя получателя: ")
        amount = float(input("Введите сумму: "))
        transfer(from_acc, to_acc, amount)
    elif command == "balance":
        name = input("Введите имя счёта: ")
        balance(name)
    elif command == "exit":
        break
    else:
        print("Неизвестная команда")