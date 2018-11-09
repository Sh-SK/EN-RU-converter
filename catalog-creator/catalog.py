import os

print("Добро пожаловать в программу Catalog creator!\nОна создает каталог из названий файлов в папке.")
path = input("Введите путь к директории с файлами: ")
try:
    os.chdir(path)
    # file = open("catalog.txt", "w")
    for i, filename in enumerate(os.listdir(path)):
        name = filename
        name = name.rstrip('.pdf')
        name = name.split(' - ')
        author = name[0]
        author = author.strip()
        title = name[1].split('(')[0].strip()
        year = name[1].split('(')[1].rstrip(')')
        with open("catalog.txt", "a") as file:
            file.write(author + '|' + title + '|' + year + '\n')
    # file.close()
    print("Обработано {} файлов".format(i + 1))
except Exception as err:
    print(err)

# отделение авторов от названия и названия от года
# создание класса Книга
# создание CSV-файла
# косяк когда в названии есть -
