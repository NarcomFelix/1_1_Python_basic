"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке
"""

with open('text_2.txt', 'r') as r_obj:
    n = 1
    for line in r_obj:
        list_1 = line.split(' ')
        print('Кол-во слов с строке', n, ':', len(list_1))
        n += 1
