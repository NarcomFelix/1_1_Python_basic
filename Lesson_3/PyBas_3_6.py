"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm' # все латинские буквы
    if not set(word).difference(latin_char): #из слова делаем множество и вычитаем латинские буквы, при остатке - ошибка
        return word.title()
    else:
        False

print(int_func(''))
