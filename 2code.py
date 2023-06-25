import tkinter.messagebox
from tkinter import *


def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    result = ""
    while decimal != 0:
        result += str(decimal % 2)
        decimal = decimal // 2

    return result[::-1]


def convert():
    global inputBox, binaryLabel

    try:
        decimal = int(inputBox.get())
        binaryLabel["text"] = decimal_to_binary(decimal)
    except ValueError:
        tkinter.messagebox.showwarning("Attention", "Please check Your input.")


app = Tk()
app.title("Decimal To Binary")
app.config(padx=15, pady=15)
app.resizable(0, 0)

decimalLabel = Label(app, text="Decimal", font="Arial 16")
decimalLabel.grid(row=0, column=0, padx=15, pady=15)

inputBox = Entry(app, font="Arial 16 bold")
inputBox.grid(row=0, column=1, padx=15, pady=15)

runBtn = Button(app, text="Convert", command=convert, font="Arial 16")
runBtn.grid(row=1, column=0)

binaryLabel = Label(app, font="Arial 16")
binaryLabel.grid(row=1, column=1, padx=15, pady=15)

app.mainloop()
