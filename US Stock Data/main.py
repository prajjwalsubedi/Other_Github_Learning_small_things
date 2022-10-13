from data import scrapper
from tkinter import *

window = Tk()
window.title("STOCK DATA Checker")
window.minsize(500, 300)
window.config(padx=20, pady=20)


def button_clicked():
    my_dict = scrapper(user_input.get().lower())
    window.title(f"{user_input.get().upper()} - Stock Details")

    row_count = 3
    for key in my_dict:
        show = Label(text=f"{key}: {my_dict[key].strip()}")
        row_count += 1
        show.grid(column=2, row=row_count)


heading = Label(text="Please Put The Stock Symbol : ", font=("Times New Roman", 20, "bold"))
heading.config(padx=5, pady=20)
heading.grid(column=2, row=0)

title = Label(text="Please Put The Stock Symbol : ")
title.grid(column=1, row=1)

user_input = Entry(width=15)
user_input.grid(column=2, row=1, padx=5, pady=0)

button = Button(text="Show Details", command=button_clicked)
button.grid(column=3, row=1)

mainloop()
