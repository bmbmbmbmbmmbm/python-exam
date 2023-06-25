import tkinter.messagebox
from tkinter import *
import tkinter.messagebox


def submit():
    global nameEntry, surnameEntry, loginEntry, passwordEntry, passwordRepeatEntry

    name = nameEntry.get().strip()
    surname = surnameEntry.get().strip()
    login = loginEntry.get().strip()
    password = passwordEntry.get().strip()
    passwordRepeat = passwordRepeatEntry.get().strip()

    if name == "" or surname == "" or login == "" or password == "" or passwordRepeat == "":
        tkinter.messagebox.showerror("Attention", "Please do not leave any field empty.")
    elif password != passwordRepeat:
        tkinter.messagebox.showwarning("Attention", "The password must be the same.")
    elif password == passwordRepeat:
        tkinter.messagebox.showinfo("Congratulations",
                                    f"The account has been added.\n\n" +
                                    f"Name:  {name}\n" +
                                    f"Surname:  {surname}\n" +
                                    f"Login:  {login}\n" +
                                    f"Password:  {password}")


app = Tk()
app.title("Registration Card")
app.resizable(0, 0)
app.config(padx=15, pady=15)

nameLabel = Label(app, text="Name: ", justify=LEFT, font="Arial 16", padx=5, pady=5)
nameLabel.grid(row=0, column=0, columnspan=1)
surnameLabel = Label(app, text="Surname: ", justify=LEFT, font="Arial 16", padx=5, pady=5)
surnameLabel.grid(row=1, column=0)
loginLabel = Label(app, text="Login: ", justify=LEFT, font="Arial 16", padx=5, pady=5)
loginLabel.grid(row=2, column=0)
passwordLabel = Label(app, text="Password: ", justify=LEFT, font="Arial 16", padx=5, pady=5)
passwordLabel.grid(row=3, column=0)
passwordRepeatLabel = Label(app, text="Repeat the Password: ", justify=LEFT, font="Arial 16", padx=5, pady=5)
passwordRepeatLabel.grid(row=4, column=0)

nameEntry = Entry(app, font="Arial 16")
nameEntry.grid(row=0, column=1)
surnameEntry = Entry(app, font="Arial 16")
surnameEntry.grid(row=1, column=1)
loginEntry = Entry(app, font="Arial 16")
loginEntry.grid(row=2, column=1)
passwordEntry = Entry(app, font="Arial 16")
passwordEntry.grid(row=3, column=1)
passwordRepeatEntry = Entry(app, font="Arial 16")
passwordRepeatEntry.grid(row=4, column=1)

submitBtn = Button(app, text="Submit", command=submit, font="Arial 18 bold", padx=5, pady=5)
submitBtn.grid(row=5, columnspan=2)

app.mainloop()