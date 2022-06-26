"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове
"""
user_str = input("Введите слова через пробел: ")

new_str = user_str.split()
exit_str = []
for el in new_str:
    if len(el) > 10:
        new_el = str(el)
        new_el = new_el[0:10]
        exit_str.append(new_el)
print(exit_str)

for el in enumerate(exit_str, 1):
    print(''.join(map(str, el)))