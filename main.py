# On day 28 I build a pomodoro app, using the GUI module tkinter. Use this app to up your productivity by
# working in timed intervals.

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
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_seconds = 1 * 60
    short_break_minutes = 1 * 60
    long_break_minutes = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 == 0:
        countdown(short_break_minutes)
        timer_label.config(text="Short Break", fg=PINK)

    elif reps % 8 == 0:
        countdown(long_break_minutes)
        timer_label.config(text="Long Break", fg=RED)

    else:
        countdown(work_seconds)
        timer_label.config(text="Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = "0" + str(count_seconds)

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_marks = ""
        work_reps = (math.floor(reps/2))
        for item in range(work_reps):
            check_marks += "✓"
            level_check_mark.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_background = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_background)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

reset_button = Button(text="RESET")
reset_button.grid(column=2, row=2)

start_button = Button(text="START", command=start_timer)
start_button.grid(column=0, row=2)

level_check_mark = Label(font=FONT_NAME, fg=GREEN, bg=YELLOW)
level_check_mark.grid(column=1, row=3)

timer_label = Label(text="TIMER", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

window.mainloop()
