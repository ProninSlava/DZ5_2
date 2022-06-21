from datetime import datetime
import os


def debug_decorator(old_function):

    def new_function(*args,**kwargs):
        if not os.path.isdir('info'):
            os.mkdir('info')
        with open("info/file_nfo.txt", 'a', encoding='UTF-8') as f:
            f.write(f'Функция "{old_function.__name__}" была вызвана.' + '\n')
            f.write(f'Дата и время вызова: {datetime.now()}'+ '\n')
            f.write(f'Аргументы: {args}' + '\n')
            result = old_function(*args, **kwargs)
            f.write(f'Возвращаемое значение: {result}' + '\n')

    return new_function

