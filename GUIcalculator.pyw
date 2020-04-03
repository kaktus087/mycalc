from tkinter import *
from tkinter import messagebox

inputFieldString = ""


def onclick(number):
    global inputFieldString
    inputFieldString = str(inputFieldString) + number
    input_Text.config(text=inputFieldString)


def __CE__():
    global inputFieldString
    inputFieldString = ''
    input_Text.config(text=inputFieldString)


def square():
    global inputFieldString
    inputFieldString = str(inputFieldString) + "**2"
    input_Text.config(text=inputFieldString)


def square_root():
    global inputFieldString
    inputFieldString = str(inputFieldString) + "**0.5"
    input_Text.config(text=inputFieldString)


def main_():
    global inputFieldString
    try:
        inputFieldString = eval(inputFieldString)
        if inputFieldString == 87:
            messagebox.showinfo("lefort87", "ЛЕФОРТ ХУЕСОС")
        input_Text.config(text=inputFieldString)
    except ZeroDivisionError:
        messagebox.showerror("DIV 0", "Нельзя делить на ноль!")


root = Tk()


# Поле ввода
input_Text = Label(font="1")
input_Text.pack()

# Кнопки выполняющие операции
button_ravno = Button(text="=", command=main_, width=4, height=2, font=0)
button_ravno.place(x=180, y=105)

button_tochka = Button(text=".", command=lambda: onclick(
    "."), width=4, height=2, font=0)
button_tochka.place(x=0, y=205)

button_minus = Button(
    text="-", command=lambda: onclick("-"), width=4, height=2, font=0)
button_minus.place(x=135, y=55)

button_plus = Button(text="+", command=lambda: onclick("+"),
                     width=4, height=2, font=0)
button_plus.place(x=135, y=105)

button_umnojenie = Button(
    text="*", command=lambda: onclick("*"), width=4, height=2, font=0)
button_umnojenie.place(x=135, y=155)

button_delenie = Button(
    text="/", command=lambda: onclick("/"), width=4, height=2, font=0)
button_delenie.place(x=135, y=205)

button_CE = Button(text="C", command=__CE__, width=4, height=2, font=0)
button_CE.place(x=90, y=205)

# Кнопки ввода цифр
button_zero = Button(text="0", command=lambda: onclick(
    "0"), width=4, height=2, font=0)
button_zero.place(x=45, y=205)

button_1 = Button(text="1", command=lambda: onclick("1"),
                  width=4, height=2, font=0)
button_1.place(x=0, y=55)

button_2 = Button(text="2", command=lambda: onclick("2"),
                  width=4, height=2, font=0)
button_2.place(x=45, y=55)

button_3 = Button(text="3", command=lambda: onclick("3"),
                  width=4, height=2, font=0)
button_3.place(x=90, y=55)

button_4 = Button(text="4", command=lambda: onclick("4"),
                  width=4, height=2, font=0)
button_4.place(x=0, y=105)

button_5 = Button(text="5", command=lambda: onclick("5"),
                  width=4, height=2, font=0)
button_5.place(x=45, y=105)

button_6 = Button(text="6", command=lambda: onclick("6"),
                  width=4, height=2, font=0)
button_6.place(x=90, y=105)

button_7 = Button(text="7", command=lambda: onclick("7"),
                  width=4, height=2, font=0)
button_7.place(x=0, y=155)

button_8 = Button(text="8", command=lambda: onclick("8"),
                  width=4, height=2, font=0)
button_8.place(x=45, y=155)

button_9 = Button(text="9", command=lambda: onclick("9"),
                  width=4, height=2, font=0)
button_9.place(x=90, y=155)

button_sqr = Button(text="x^2", command=square,
                    width=4, height=2, font=0)
button_sqr.place(x=180, y=155)

button_sqrt = Button(text="√", command=square_root,
                     width=4, height=2, font=0)
button_sqrt.place(x=180, y=205)

root.geometry("225x255")
root.title("Calculator")
root.mainloop()
