from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=20)

def button_clicked():
    pass

# Save Password
def save_details():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    with open("data.txt", "a") as data:
        data.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)

# UI SETUP
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=2, row=1)

website = Label(text="Website: ")
website.grid(column=1, row=2)

website_input = Entry(width=37)
website_input.focus()
website_input.grid(column=2, columnspan=2, row=2)

email = Label(text="Email/Username: ")
email.grid(column=1, row=3)

email_input = Entry(width=37)
email_input.insert(0, "prajjwalsubedi95@gmail.com")
email_input.grid(column=2, columnspan=2, row=3)

password = Label(text="Password: ")
password.grid(column=1, row=4)

password_input = Entry(width=20)
password_input.grid(column=2, row=4)

password_button = Button(text="Generate Password", command=button_clicked)
password_button.grid(column=3, row=4)

add_button = Button(text="Add", command=save_details, width=35)
add_button.grid(column=2, columnspan=2, row=5)

window.mainloop()