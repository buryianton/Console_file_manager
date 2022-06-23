import os
import json

FILE_NAME_ORDERS = 'bank_orders.json'
FILE_NAME_MONEY = 'bank_money.txt'

orders = []  # сумма каждой покупки
money = []   # кол-во денег на счете в формате, выгруженном из документа
account = 0  # кол-во денег на счете в видео переменной int
history = {} # история покупок


if os.path.exists(FILE_NAME_MONEY):
    with open('bank_money.txt', 'r') as f:
        for figures in f:
            money.append(figures.replace('\n',''))
            for figures in money:
                account += int(figures)

if os.path.exists(FILE_NAME_ORDERS):
    with open('bank_orders.json', 'r') as f:
        history = json.load(f)

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. вывести баланс')
    print('5. выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        money_put = int(input("Введите сумму: "))
        account += money_put
        print('На счету ', account, 'р.')

    elif choice == '2':
        order = int(input('Введите сумму покупки: '))
        orders.append(order)
        if account < order:
            print('Не хватает средств на счете')
        elif account > order:
            account -= order
        purchase = input('Введите назначение покупки: ')
        history[purchase] = order

    elif choice == '3':
        print(history)

    elif choice == '4':
        print('Ваш баланс: ', account, 'р.\n')

    elif choice == '5':
        with open(FILE_NAME_MONEY, 'w') as f:
            f.write(f'{account}\n')
        with open(FILE_NAME_ORDERS, 'w') as f:
            json.dump(history, f)
        break
    else:
        print('Неверный пункт меню')