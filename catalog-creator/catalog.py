import os

print("Добро пожаловать в программу Catalog creator!\nОна создает каталог из названий файлов в папке.")
path = input("Введите путь к директории с файлами: ")
try:
    os.chdir(path)
    # file = open("catalog.txt", "w")
    for i, filename in enumerate(os.listdir(path)):
        name = filename
        name = name.rstrip('.pdf')
        with open("catalog.txt", "a") as file:
            file.write(name + '\n')
    # file.close()
    print("Обработано {} файлов".format(i + 1))
except Exception as err:
    print(err)
