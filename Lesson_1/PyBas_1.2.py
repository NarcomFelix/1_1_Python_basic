"""
Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. 
"""


user_time = int(input("Введите время в секундах: "))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time - hours * 3600 - minutes * 60
if hours < 10:
    hours = str(0) + str(hours)
if minutes < 10:
    minutes = str(0) + str(minutes)
if seconds < 10:
    seconds = str(0) + str(seconds)

print(f'{hours}:{minutes}:{seconds}')

