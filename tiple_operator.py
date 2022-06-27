'''
Тернарный оператор
if - else, не должно быть elif
'''
import random

numbers = []

for i in range(30):
    numbers.append(random.randint(0,100))

print(numbers)

#проверить есть ли 13 в списке
if 13 in numbers:
    print('13 в нашем списке')
else:
    print('Нет 13 в нашем списке')

#запись в одну строку + меняется порядок выражений
#если условие верно <условие> если условие не верно
print('13 в нашем списке') if 13 in numbers else print('Нет 13 в нашем списке')

# когда есть какая-то переменная
result = None
if 4 in numbers:
    result = 'Есть 4'
else:
    result = 'Нет 4'

print('Результат выражения: ', result)

result = 'Есть 4' if 4 in numbers else 'Нет 4'
print('Результат выражения: ', result)

print('13 в нашем списке' if 13 in numbers else '13 нет в нашем списке')

