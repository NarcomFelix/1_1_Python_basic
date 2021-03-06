"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

my_dict_1 = {}
my_dict_2 = {}
with open('text_7.txt', 'r', encoding="utf-8") as r_obj:
    summ = 0
    n = 0
    for line in r_obj:

        a = line.replace('\n', '')
        my_list = a.split(' ')
        income = int(my_list[2]) - int(my_list[3])

        if income > 0:
            summ = summ + income
            n += 1
        my_dict_1.update({my_list[0]: income})
    average_income = summ/n
    my_dict_2.update({"average_profit": average_income})
    exit_list =[my_dict_1, my_dict_2]
    print(exit_list)
with open('my_file.json', 'w') as write_f:
    json.dump(exit_list, write_f)