from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=20)


# Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password_new = "".join(password_list)
    password_input.insert(0, password_new)
    pyperclip.copy(password_new)


# Save Password
def save_details():
    website_to_save = website_input.get()
    email_to_save = email_input.get()
    password_to_save = password_input.get()
    data = {
        website_to_save: {
            "email": email_to_save,
            "password": password_to_save
        }
    }
    if len(website_to_save) == 0 or len(password_to_save) == 0:
        messagebox.showinfo(title="OOPS !!", message="Please make sure you haven't left any field empty.")
    else:
        ask_ok = messagebox.askokcancel(title=website_to_save,
                                        message=f"These are the details entered: \nEmail: {email_to_save} \n"
                                                f"Password: {password_to_save} \nIs it okay to Save?")
        if ask_ok:
            try:
                with open("data.json", "r") as data_file:
                    old_data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            except json.JSONDecodeError:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    old_data.update(data)
                    json.dump(old_data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


def search():
    website_searched = website_input.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        details = data[website_searched]
        messagebox.showinfo(title=website_searched,
                            message=f"Website: {website_searched}\nusername: {details['email']}\n Password: {details['password']} ")


# UI SETUP
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=2, row=1)

website = Label(text="Website: ")
website.grid(column=1, row=2)

website_input = Entry(width=20)
website_input.focus()
website_input.grid(column=2, row=2)

search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=3, row=2)

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
