from tkinter import *
import math

window = Tk()
window.title("Miles to Kms Converter")
window.minsize(500, 300)
window.config(padx=20, pady=20)


# def update_label():
#     my_label.config(text="I Love You")
#
#
# def user_input_func():
#     my_label.config(text=user_input.get())


# my_label = Label(text="Hello World!", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)
#
# button = Button(text="Click Me", command=user_input_func)
# button.grid(column=4, row=0)
#
# user_input = Entry(width=10)
# user_input.grid(column=2, row=0)

def calculate():
    result_in_km = float(user_input.get()) * 1.60934
    result.config(text=math.trunc(result_in_km))


user_input = Entry(width=10)
user_input.grid(column=3, row=0)

miles = Label(text="miles")
miles.grid(column=4, row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=2, row=1)

result = Label(text=0)
result.grid(column=3, row=1)

km = Label(text="Kms")
km.grid(column=4, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=3, row=2)

mainloop()
