from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Pandas
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")

data_dict = data.to_dict(orient="records")
print(len(data_dict))
word = {}


def is_known():
    data_dict.remove(word)
    data_to_learn = pandas.DataFrame(data_dict)
    data_to_learn.to_csv("words_to_learn.csv")
    get_word()


def get_word():
    global word, timer
    window.after_cancel(timer)
    word = random.choice(data_dict)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    canvas.itemconfig(image, image=front_image)
    timer = window.after(3000, func=translate)


def translate():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(image, image=back_image)


timer = window.after(3000, func=translate)

# UI
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 253, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_img, highlightthickness=0, bd=0, command=get_word)
cross_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=is_known)
right_btn.grid(column=1, row=1)

get_word()

window.mainloop()
