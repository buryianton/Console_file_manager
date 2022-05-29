def bank_account():
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