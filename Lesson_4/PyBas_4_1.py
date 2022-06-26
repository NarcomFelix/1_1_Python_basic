"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.
"""

# from sys import argv
# name, surname, payment_p_h, hours, bonus = argv
def pay():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    payment_p_h = int(input('Ставка в час: '))
    hours = int(input('Выработка в часах: '))
    bonus = int(input('Бонус: '))
    return print(f"{name} {surname}. Зароботная плата:", payment_p_h * hours + bonus)

pay()
