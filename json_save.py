import json
import xml
import yaml

# Объект - сохраняем в строку
# строка -> объект

#xml
#json
#yaml

person = {
    'name': 'Max',
    'age': 10,
    'phone': ['8911', '73833'],
    '1': 'test'
}
print('Начальный объект')
print(person)
print(type(person))

result = json.dumps(person)

print('В формате json')
print(result)
print(type(result))

person_recovery = json.loads(result)

print('Восстановленный объект')
print(person_recovery)
print(type(person_recovery))

print(person == person_recovery)

#сохраняем в файл
with open('person.json','w') as f:
    json.dump(person, f)

with open('person.json', 'r') as f:
    result = json.load(f)
    print(result)

# сохраняем в файл
with open('person.yaml', 'w') as f:
    yaml.dump(person, f)

with open('person.yaml', 'r') as f:
    result = yaml.load(f)
    print(result)
