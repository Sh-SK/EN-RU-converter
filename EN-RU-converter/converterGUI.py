import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from converter import convert


# Функция для исправления текста
def converter():
    output_text.delete("0.0", "end")
    if input_text.get('1.0', END).strip() != "":
        input_str = input_text.get('1.0', END)
        if convert_type.get() == "en-ru":
            output_str = convert(input_str)
            output_text.insert("end", "%s" % output_str)
            # app.clipboard_clear()
            # app.clipboard_append(output_str)
        elif convert_type.get() == "ru-en":
            mb.showwarning("Предупреждение", "Функция исправления текста, набранного в русской раскладке, пока не реализована.")


# def ctrlV(event):
    # content = str(app.clipboard_get())
    # input_text.insert("end", "%s" % content)
    # pass

# Создание приложения
app = tkinter.Tk()
app.title("EN-RU converter")
app.configure(background='#ececec')

name_label = ttk.Label(app, text="EN-RU converter – Программа для исправления текста, набранного в неверной раскладке.",
                       font='Garamond 16 bold', foreground='#333')
name_label.grid(row=0, column=0, columnspan=3)

# Создание лэйблов
input_label = ttk.Label(app, text="Введите текст, который надо исправить: ", font='Verdana 12')
input_label.grid(row=1, column=0)
output_label = ttk.Label(app, text="Исправленный текст: ", font='Verdana 12')
output_label.grid(row=1, column=2)

# Создание поля для ввода информации и установка на нем фокуса
input_text = Text(app, width=50, height=5, font='Consolas 12', wrap=WORD)
input_text.grid(row=2, column=0)
input_text.focus()

# Создание поле для вывода
output_text = Text(app, width=50, height=5, font='Consolas 12', wrap=WORD)
output_text.grid(row=2, column=2)

# Установка RadioButton
convert_type = StringVar()
convert_type.set('en-ru')

radio_enru = ttk.Radiobutton(app, text='En --> Ru', value='en-ru', variable=convert_type)
radio_enru.grid(row=2, column=1, sticky=N)
radio_ruen = ttk.Radiobutton(app, text='Ru --> En', value='ru-en', variable=convert_type)
radio_ruen.grid(row=2, column=1, sticky=S)

# Создание кнопки для запуска перевода
btn_converter = ttk.Button(app, text='Исправить', width=15, command=converter)
btn_converter.grid(row=3, column=1)

# Отслеживание события нажатия на клавиши Ctrl+V
# input_text.bind('<Control-v>', ctrlV)

# TODO: Сделать кнопку для копирования исправленного текста в буфер обмена

# Запускаем цикл обработки событий
app.mainloop()
