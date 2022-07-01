"""
Пишем в файл название вызываемых функций
"""
def save_call_to_file(func):
    def inner(*args, **kwargs):
        #пишем название функции в файл
        function_name = func.__name__
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'{function_name}\n')

        result = func(*args, **kwargs)
        return result

    return inner

@save_call_to_file
def hello():
    pass

@save_call_to_file
def other():
    #что-то сделать перед базовой функцией
    pass

@save_call_to_file
def go():
    pass

hello()
other()
go()
go()
hello()
other()