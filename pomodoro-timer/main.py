from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, ticks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    tick.config(text="")
    ticks = ""
    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Long Break", fg=RED)
        count_down(long_break)

    elif reps % 2 == 0:
        title.config(text="Short Break", fg=PINK)
        count_down(short_break)

    else:
        title.config(text="Work", fg=GREEN)
        count_down(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, ticks, timer
    minutes = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            ticks += "✓"
            tick.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), highlightthickness=0, fg=GREEN, bg=YELLOW)
title.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_btn = Button(text="Start", highlightthickness=0, bd=0, command=start_timer)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", highlightthickness=0, bd=0, command=reset_timer)
reset_btn.grid(column=3, row=3)

tick = Label(highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
tick.grid(column=2, row=4)
window.mainloop()
