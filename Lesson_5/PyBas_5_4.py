"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""
my_dict = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре"}

with open('text_4_1.txt', 'r', encoding="utf-8") as r_obj:
    with open('text_4_2.txt', 'w') as w_obj:
        for line in r_obj:
            list_r = line.split(' ')
            list_w = list_r
            a = int(list_r[2])
            b = my_dict.get(a)
            list_w.insert(0, b)
            list_w.pop(1)
            line_new = (' '.join(list_w))
            w_obj.writelines(line_new)