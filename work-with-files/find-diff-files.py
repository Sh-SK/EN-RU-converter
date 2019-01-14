#! python3
# find-diff-files.py - находит различающиеся файлы папок A и B (элементы, входящие в A, но не входящие в B, и наоборот).

import os


def print_list(spisok):
    spisok.sort()
    for i in range(len(spisok)):
        print(spisok[i])


print("Скрипт find-diff-files.py - находит различающиеся файлы папок A и B.\n")
while True:
    try:
        folder1 = input("Введите путь к первой директории (А): ")
        os.chdir(folder1)
        break
    except FileNotFoundError:
        print("Ошибка! Введите правильный путь к директории!")
        continue
while True:
    try:
        folder2 = input("Введите путь ко второй директории (В): ")
        os.chdir(folder2)
        break
    except FileNotFoundError:
        print("Ошибка! Введите правильный путь к директории!")
        continue

files1 = []
files2 = []

for filename in os.listdir(folder2):
    files2.append(filename)

os.chdir(folder1)
for filename in os.listdir(folder1):
    files1.append(filename)

s_files1 = set(files1)
s_files2 = set(files2)
diff_ab = s_files1.difference(s_files2)
diff_ba = s_files2.difference(s_files1)
l_diff1 = list(diff_ab)
l_diff2 = list(diff_ba)

print()
print("A – B: ")
print("Кол-во элементов: " + str(len(diff_ab)))
print_list(l_diff1)
print()
print("B – A: ")
print("Кол-во элементов: " + str(len(diff_ba)))
print_list(l_diff2)

# TODO: Предложить скопировать эти файлы в новую директорию
