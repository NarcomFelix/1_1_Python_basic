"""
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().
"""

from PyBas_3_6 import int_func


def up(a):
    a = input("Введите слова через пробел: ").split() # получаем список из слов

    b = ''
    for el in a:
        res = int_func(el)
        b = b + str(res)
    return print(b)

up('')