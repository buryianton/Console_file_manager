import os
import shutil
import sys
from decorators import add_separators

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
        all = os.listdir()
        print(all)
        print('\n')


        try:
            answer = input('Сохранить содержимое рабочей директории в файл? Введите да или нет:\n')
            if answer == 'да':
                folders = []
                files = []
                for i in all:
                    if os.path.isdir(i) == True:
                        folders.append(i)
                    elif os.path.isfile(i) == True:
                        files.append(i)

                with open('listdir.txt', 'w') as f:
                    f.write(f'files: ')
                    for i in files:
                        f.write(f'{i}, ')
                    f.seek(f.tell()-2, 0)
                    f.write('\n')
                    f.write(f'dirs: ')
                    for r in folders:
                        f.write(f'{r}, ')
                    f.seek(f.tell()-2, 0)
                print('Содержимое сохранено в файле listdir.txt')

            elif answer == 'нет':
                pass
            elif answer != 'да' and answer != 'нет':
                print('Здесь можно ввести только "да" или "нет"')
        except:
            print('Введите либо да, либо нет')


    if choice == '5':
        all = os.listdir()
        print('В данной директории есть следующие папки: ')
        [print('Папка ', i) for i in all if os.path.isdir(i) == True]
        count = 0
        total = [1 for i in all if os.path.isdir(i) == True]
        print('В директории ', sum(total), ' папок')
        #for i in all:
        #    if os.path.isdir(i) == True:
        #        print("Папка ", i)
        print('\n')

    if choice == '6':
        all = os.listdir()
        print('В данной директории есть следующие файлы: ')
        [print('Файл', i) for i in all if os.path.isfile(i) == True]
        count = 0
        total = [1 for i in all if os.path.isfile(i) == True]
        print('В директории ', sum(total), ' файлов')
        #for i in all:
        #    if os.path.isfile(i) == True:
        #        print('Файл ', i)
        print('\n')

    if choice == '7':
        print('Операционная система: ')
        print(sys.platform)
        print('\n')

    if choice == '8':
        print('ФИО создателя программы: Бурый Антон Сергеевич')

    if choice == '9':
        @add_separators
        def Pushkin():
            try:
                year = int(input('Введите год рождения А.С.Пушкина:'))
                while year != 1799:
                    print("Не верно")
                    year = int(input('Введите год рождения А.С.Пушкина:'))
                if year == 1799:
                    Pushkin_birthday()
            except:
                print('Здесь можно ввести только число')


        @add_separators
        def Pushkin_birthday():
            try:
                day = int(input('Введите день рождения Пушкин?'))
                while day != 6:
                    print("Не верно")
                    day = int(input('В какой день июня родился Пушкин? '))
                if day == 6:
                    print('Верно')
            except:
                print('Здесь можно ввести только число')

        Pushkin()

    if choice == '10':
        import bank

    if choice == '12':
        break