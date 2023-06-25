from tkinter import *

def draw_keys():
    symbols = [["C", "/", "*"],
               ["7", "8", "9"],
               ["4", "5", "6"],
               ["1", "2", "3"]]

    for r in range(4):
        for c in range(3):
            btn = Button(app, width=4, height=2, font='Arial 20 bold', fg='black', text=symbols[r][c],
                         command=lambda r=r, c=c: toggle_keys(symbols[r][c]))
            btn.grid(row=r + 2, column=c, pady=2, padx=2)

    zero = Button(app, width=9, height=2, font='Arial 20 bold', fg='black', text="0", command=lambda: toggle_keys("0"))
    zero.grid(row=6, column=0, columnspan=2, pady=2, padx=2)
    dot = Button(app, width=4, height=2, font='Arial 20 bold', fg='black', text=".", command=lambda: toggle_keys("."))
    dot.grid(row=6, column=2, pady=2, padx=2)

    minus = Button(app, width=4, height=2, font='Arial 20 bold', fg='black', text="-", command=lambda: toggle_keys("-"))
    minus.grid(row=2, column=4, pady=2, padx=2)
    add = Button(app, width=4, height=5, font='Arial 20 bold', fg='black', text="+", command=lambda: toggle_keys("+"))
    add.grid(row=3, rowspan=2, column=4, pady=2, padx=2)

    enter = Button(app, width=4, height=5, font='Arial 20 bold', fg='black', text="=", command=lambda: toggle_keys("="))
    enter.grid(row=5, rowspan=2, column=4, pady=2, padx=2)
    clearAll = Button(app, width=19, height=2, font='Arial 20 bold', fg='black', text="Clear All", command=lambda: toggle_keys("A"))
    clearAll.grid(row=1, columnspan=5, pady=2, padx=2)


def draw_calculator():
    global display
    display = Label(app, width=19, height=2, font='Arial 20 bold', bg="lightgray", fg='black')
    display.grid(row=0, columnspan=5, padx=2, pady=2)
    draw_keys()


def toggle_keys(key):
    global display

    signs = ["+", "-", "*", "/", "."]
    result = display["text"]
    length = len(result)
    previous = result[length - 1] if length > 0 else {}

    if key in signs and length == 0:
        return
    if key == "A":
        result = ""
    elif key == "=":
        try:
            result = str(eval(result))
        except SyntaxError:
            result = result
    elif key == "C":
        result = result[0: length - 1]
    elif previous in signs and key in signs:
        result = result[0: length - 1] + key
    else:
        result += key

    display["text"] = result


# Main App

app = Tk()
app.resizable(0, 0)
app.title("Calculator")
app.config(pady=5, padx=5)

display = None
draw_calculator()

app.mainloop()