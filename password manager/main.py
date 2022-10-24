from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=20)


# Password Generator
def generate_password():

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	
	password_letters = [choice(letters) for char in range(randint(8, 10))]
	password_symbols = [choice(symbols) for char in range(randint(2, 4))]
	password_numbers = [choice(numbers) for char in range(randint(2, 4))]
	
	password_list = password_letters + password_numbers + password_symbols
	
	shuffle(password_list)
	
	password = "".join(password_list)
	password_input.insert(0, password)
	pyperclip.copy(password)


# Save Password
def save_details():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS !!", message="Please make sure you haven't left any field empty.")
    else:
        ask_ok =  messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okey to Save?")
        if ask_ok:
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

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=3, row=4)

add_button = Button(text="Add", command=save_details, width=35)
add_button.grid(column=2, columnspan=2, row=5)

window.mainloop()