'''
Кодировка в байты
'''

some_str = 'hello'
print(type(some_str))

some_byte = b'hello'
print(some_byte)
print(type(some_byte))

for char in some_byte:
    print(char)

print(ord('E'))

some_utf_8_str = 'тут русские символы'

#кодирование - поличились байты
some_utf_8_bites = some_utf_8_str.encode('utf-8')

print(some_utf_8_bites)

#декодирование из байт в строку
some_utf_8_str = some_utf_8_bites.decode('utf-8')

print(some_utf_8_str)

with open('code.txt', 'w', encoding='utf-8') as f:
    f.write('For text in english language we use ascii')

with open('code_ascii.txt', 'w', encoding='ascii') as f:
    f.write('For text in english language we use ascii')