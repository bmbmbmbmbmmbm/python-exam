import tkinter.messagebox
from tkinter import *


def end(event):
    app.destroy()


def help(event):
    tkinter.messagebox.showinfo("About game",
                                "F1 - Info \n" +
                                "F12 - New Game \n" +
                                "Esc - Exit game \n" +
                                "Author - Arthur Mirzoyan \n" +
                                "Group number - 019 \n"
                                )


def showInfo(winner):
    if winner == '':
        tkinter.messagebox.showinfo("Results", "It's a tie.")
    elif winner == 'X':
        tkinter.messagebox.showinfo("Results", "X is the winner.")
    else:
        tkinter.messagebox.showinfo("Results", "O is the winner.")


def generateBoard(event):
    global board
    global symbol
    board = []
    symbol = 'X'
    for i in range(0, 3):
        for j in range(0, 3):
            btn = Button(app, width=10, height=5, font='Arial 20 bold', fg='white',
                         command=lambda i=i, j=j: onClick(i, j))
            btn.grid(row=i, column=j)
            board.append(btn)


def checkWin():
    global winVariants
    winner = ''
    for i in range(0, 8):
        variant = winVariants[i]
        if board[variant[0]]['text'] == board[variant[1]]['text'] == board[variant[2]]['text'] == 'O':
            winner = '0'
            break
        elif board[variant[0]]['text'] == board[variant[1]]['text'] == board[variant[2]]['text'] == 'X':
            winner = 'X'
            break
    return winner


def onClick(i, j):
    global symbol
    btn = board[i * 3 + j]
    if btn['text'] == '':
        btn['text'] = symbol
        btn['bg'] = 'red' if symbol == 'X' else 'lightblue'
        symbol = 'O' if symbol == 'X' else 'X'

        winner = checkWin()
        if (winner == '' and not freeSpaceLeft()) or winner != '':
            showInfo(winner)


def freeSpaceLeft():
    for i in range(0, 9):
        if board[i]['text'] == '':
            return True
    return False


winVariants = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
board = []
symbol = 'X'

# App
app = Tk()
app.resizable(0, 0)
app.title('Tic-Tac-Toe')

# Start
generateBoard(0)

# Functional Buttons
app.bind("<Escape>", end)
app.bind("<F1>", help)
app.bind("<F12>", generateBoard)

app.mainloop()
