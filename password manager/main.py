from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)



canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.pack()
window.mainloop()