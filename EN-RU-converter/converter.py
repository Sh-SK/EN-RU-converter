#! python3
# converter.py - Программа для исправления текста набранного в неправильной (неверной) раскладке.
# Использование: python converter.py <текст в неверной раскладке> – Исправляет введенный текст

import sys

dict_ENRU = {"~": "Ё", "`": "ё",
             "q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з", "[": "х", "]": "ъ", "{": "Х", "}": "Ъ",
             "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д", ";": "ж", ":": "Ж", "'": "э", '"': "Э",
             "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь", ",": "б", "<": "Б", ".": "ю", ">": "Ю", "/": ".", "?": ","}
tuple_const = (" ", "!", "%", "*", "(", ")", "-", "_", "=", "+", '\\')


def convert(text):
    text = text.lower()
    result = []

    for i, char in enumerate(text):
        if (char in dict_ENRU) == True:
            ch = dict_ENRU.get(char)
            result.append(ch)
        elif (chr(48) <= char <= chr(57)):
            result.append(char)
        elif (char in tuple_const):
            result.append(char)
        else:
            print("Error. Символ не найден в словаре.")
            break
    res_text = ''.join(result)
    # res_text = res_text.capitalize()
    return res_text

if len(sys.argv) < 2:
    myString = input("Введите строку, которую надо исправить: ")
    resString = convert(myString)
    output = "Строка в неправильной раскладке: {}\nИсправленная строка: {}".format(myString, resString)
    print(output)

if len(sys.argv) >= 2:
    myList = sys.argv[1:]
    myString = ' '.join(myList)
    resString = convert(myString)
    print(resString)
