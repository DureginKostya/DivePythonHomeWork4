'''Задание 2:
Напишите функцию, принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте его
строковое представление.
reverse_kwargs(rev=True, acc="YES", stroka=4) -> 
{True: "rev", "YES": 'acc', 4: "stroka"}
'''

def reverse_kwargs(**kwargs) -> dict[any, any]:
    '''Получение словаря, в котором ключ - переданный аргумент,
    а значение - имя аргумента'''
    dict_revers_kwargs = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            value = str(value)
        dict_revers_kwargs[value] = key
    return dict_revers_kwargs


print(reverse_kwargs(rev=True, acc="YES", stroka=4, list=[1, 5, 6]))
