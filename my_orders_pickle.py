'''
программа для сохранения покупок
название + цена
'''
import os
import pickle

FILE_NAME = 'orders_pickle.data'

orders = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        orders = pickle.load(f)

while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choice = input('Введите номер:')
    if choice == '1':
        name = input('Введите названия: ')
        cost = int(input('Введите цену: '))
        order = (name, cost)
        orders.append(order)
    elif choice == '2':
        for order in orders:
            print(order)
    elif choice == '3':
        with open(FILE_NAME, 'wb') as f:
            pickle.dump(orders, f)
        break
    else:
        print('Неправильно введены данные')
