'''
Сереализация - сохранение объекта в виде байт
Десереализация - восстановление объекта
'''
import pickle

big_object = {
    'items': [
        '1',
        (2,3),
        ['some', 'else'],
        {'op': 'ap'}
    ]
}

#сереализация
result = pickle.dumps(big_object)

print(result)
print(type(result))
#десереализация
big_object_recovery = pickle.loads(result)

print(big_object_recovery)
print(type(big_object_recovery))

print(big_object == big_object_recovery)

#dump
with open('big_obj.data', 'wb') as f:
    pickle.dump(big_object, f)

#load
with open('big_obj.data', 'rb') as f:
    big_object_recovery = pickle.load(f)

print(big_object_recovery)