"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
"""

my_list = []
n = int(input("Сколько будет элеметов в списке: "))
a = 1
while a <= n:
    my_list.append(input("Введите значение: "))
    a += 1
print(f'Начальный список:', my_list)

if len(my_list) == 0 or len(my_list) == 1:
    print(f'Cписок не изменён:', my_list)
else:
    if len(my_list) % 2 == 0:
        for i in range(0, len(my_list), 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        # print(f'Изменённый список Ч:', my_list)
    else:
        for i in range(0, len(my_list) - 1, 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        # print(f'Изменённый список НЧ:', my_list)

print(f'Изменённый список:', my_list)