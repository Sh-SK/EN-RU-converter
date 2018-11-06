import os

print("Добро пожаловать в программу, которая изменяет название файлов в соответствии с заданным шаблоном!")
path = input("Введите путь к директории с файлами: ")
try:
    os.chdir(path)
    str1 = input("Что заменить в названии файла: ")
    str2 = input("Чем заменить: ")

    for filename in os.listdir(path):
        name = filename
        name = name.replace(str1, str2)
        os.rename(filename, name)
except Exception:
    print(err)





