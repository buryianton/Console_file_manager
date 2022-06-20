'''
программа для сохранения покупок
'''
import os

FILE_NAME = 'orders.txt'

orders = []
if os.path.exists(FILE_NAME):
    with open('orders.txt', 'r') as f:
        for order in f:
            orders.append(order.replace('\n', ''))

while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choice = input('Введите номер:')
    if choice == '1':
        name = input('Введите названия: ')
        orders.append(name)
    elif choice == '2':
        for order in orders:
            print(order)
    elif choice == '3':
        with open(FILE_NAME, 'w') as f:
            for order in orders:
                f.write(f'{order}\n')
        break
    else:
        print('Неправильно введены данные')
