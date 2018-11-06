import os
print("Добро пожаловать в программу, которая изменяет название файлов в соответствии с заданным шаблоном!")
path = input("Введите путь к директории с файлами: ")  # E:\Dev\ZennoPoster\Projects\xakep_archieve\test
# paths = paths.split("\\")
# path = os.path.join(paths)

str1 = input("Что заменить в названии файла: ")
str2 = input("Чем заменить: ")

for filename in os.listdir(path):
    os.chdir(path)
    name = filename
    name = name.replace(str1, str2)
    try:
        os.rename(filename, name)
    except(OSError):
        print("Ошибка в имени файла.")
