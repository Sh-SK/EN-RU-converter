import os, csv

print("Добро пожаловать в программу Catalog creator!\nОна создает каталог из названий файлов в папке.\n")
path = input("Введите путь к директории с файлами: ")
try:
    os.chdir(path)
    for i, filename in enumerate(os.listdir(path)):
        book = []
        name = filename
        name = name.rstrip('.pdf')
        name = name.split(' - ')
        author = name[0]
        author = author.strip()
        book.append(author)
        title = name[1].split('(')[0].strip()
        book.append(title)
        year = name[1].split('(')[1].rstrip(')')
        book.append(year)
        with open("catalog.csv", "a") as file:
            w = csv.writer(file, delimiter='|')
            w.writerow(book)
    print("Обработано {} файлов".format(i + 1))
except Exception as err:
    print(err)
