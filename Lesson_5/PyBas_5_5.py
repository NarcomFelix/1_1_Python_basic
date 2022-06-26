"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
a = 1
with open('text_5.txt', 'w') as w_obj:
    while a != 'q':
        a = input('Введите число, для выхода нажмите q: ')
        if a != 'q':
            w_obj.write(a)
            w_obj.write(' ')
        else:
            break

with open('text_5.txt', 'r') as r_obj:
    for line in r_obj:
        line = line.split(' ')
        summa = 0
        for el in range(len(line)):
            summa = summa + int(el)
print(summa)
