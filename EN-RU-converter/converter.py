dict_ENRU = {"~": "Ё", "`": "ё",
             "q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з", "[": "х", "]": "ъ", "{": "Х", "}": "Ъ",
             "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д", ";": "ж", ":": "Ж", "'": "э", '"': "Э",
             "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь", ",": "б", "<": "Б", ".": "ю", ">": "Ю", "/": ".", "?": ","}
tuple_const = (" ", "!", "%", "*", "(", ")", "-", "_", "=", "+", '\\')
str = input("Введите строку, которую надо исправить: ")
str = str.lower()
result = []

for i, char in enumerate(str):
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
res_str = ''.join(result)
# res_str = res_str.capitalize()
output = "Строка в неправильной раскладке: {}\nИсправленная строка: {}".format(str, res_str)
print(output)
