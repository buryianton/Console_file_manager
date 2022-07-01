try:
    age = int(input('Введите кол-во лет: '))
    print(f'Через 4 года тебе будет {age+4}')
except Exception as e:
    print('Вы ввели не число')
    print('Введите верное число')
    print(e)
#if - else
user_input = input('Введите кол-во лет: ')
if user_input.isdigit():
    age = int(user_input)
    print(f'Через 4 года тебе будет {age+4}')
else:
    #Этот блок срабатывает, если было исключение
    print('Вы ввели не число')
    print('Введите верное число')