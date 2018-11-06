import os
print("Добро пожаловать в программу, которая изменяет название файла в соответствии с заданным шаблоном!")
# path = input("Введите путь к директории с файлами: ")  # E:\ZennoPoster\Projects\xakep_archieve\test  Enter path to folder:
path = r"E:\ZennoPoster\Projects\xakep_archieve\test"
str1 = input("Что заменить в названии файла: ")  # xa-
str2 = input("Чем заменить: ")  # xakep #

# os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает файл или директорию из src в dst.

for filename in os.listdir(path):
    os.chdir(path)
    name = filename
    name = name.replace(str1, str2)
    os.rename(filename, name)
