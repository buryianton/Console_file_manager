import os
import shutil
import sys

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. просмотр только папок')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        folder = input('Введите название папки: ')
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"Папка с названием {folder} создана")
            print('\n')
        elif os.path.exists(folder):
            print('Папка с таким названием уже существует')
            print('\n')

    if choice == '2':
        folder = input('Введите название папки, которую хотите удалить: ')
        if os.path.exists(folder):
            os.rmdir(folder)
            print(f"Папка с названием {folder} удалена")
            print("\n")
        elif not os.path.exists(folder):
            print(f'Папки с названием {folder} не существует')
            print('\n')

    if choice == '3':
        folder = input('Введите название файла или папки, которую хотите скопировать: ')
        new_name = input('Введите новое название: ')
        if os.path.exists(folder):
            shutil.copy(folder, new_name)
            print(f'Копия {folder} создана')
        if not os.path.exists(folder):
            print(f'Папки или файла с название {folder} не существует')

    if choice == '4':
        print('Содержимое директории:')
        print(os.listdir())
        print('\n')

    if choice == '5':
        all = os.listdir()
        print('В данной директории есть следующие папки: ')
        for i in all:
            if os.path.isdir(i) == True:
                print("Папка ", i)
        print('\n')

    if choice == '6':
        all = os.listdir()
        print('В данной директории есть следующие файлы: ')
        for i in all:
            if os.path.isfile(i) == True:
                print('Файл ', i)
        print('\n')

    if choice == '7':
        print('Операционная система: ')
        print(sys.platform)
        print('\n')

    if choice == '8':
        print('ФИО создателя программы: Бурый Антон Сергеевич')

    if choice == '9':
        def Pushkin():
            year = input('Ввведите год рождения А.С.Пушкина:')
            while year != '1799':
                print("Не верно")
                year = input('Ввведите год рождения А.С.Пушкина:')
            if year == '1799':
                Pushkin_birthday()

        def Pushkin_birthday():
            day = input('Ввведите день рождения Пушкин?')
            while day != '6':
                print("Не верно")
                day = input('В какой день июня родился Пушкин?')
            print('Верно')
        Pushkin()

    if choice == '10':
        while True:
            print('1. пополнение счета')
            print('2. покупка')
            print('3. история покупок')
            print('4. выход')

            choice = input('Выберите пункт меню: ')

            if choice == '1':
                money = int(input("Введите сумму: "))
                account += money
                print('На счету ', account, 'р.')
            elif choice == '2':
                money = int(input('Введите сумму покупки: '))
                amount.append(money)
                if money < account:
                    print('Не хватает средств на счете')
                elif money > account:
                    account -= money
                purchase = input('Введите назначение покупки: ')
                history.append(purchase)

            elif choice == '3':
                for i in range(len(history)):
                    print(history[i], ' - ', amount[i])

            elif choice == '4':
                break
            else:
                print('Неверный пункт меню')
