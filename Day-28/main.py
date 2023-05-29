from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 24, "bold")
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset() -> None:
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")    
    title_label.config(text= "Timer")
    check_marks.config(text= "")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer() -> None:
    global reps
    reps += 1
    
    if reps % 8 == 0:
        title_label.config(text="Break time", fg= RED)
        count_down(LONG_BREAK_MIN * 60)
        
    elif reps % 2 !=  0:
        title_label.config(text="Work  time", fg= PINK)
        count_down(WORK_MIN * 60)
        
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break time", fg= RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count: int) -> str:
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps / 2)
        for _ in range (work_sessions):
            marks += "✔"
        check_marks.config(text= marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 20, pady= 20, bg= YELLOW)



title_label = Label(text= "Timer", fg= GREEN,bg= YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0,column=1)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file= "./Day-28/tomato.png")
canvas.create_image(100, 112, image= tomato_image)
timer_text = canvas.create_text(100, 135, text= "00:00", fill= "white", font= FONT)
canvas.grid(row= 1,column= 1)

start_button = Button(text= "Start", highlightthickness=0, command= start_timer)
start_button.grid(row= 2,column= 0)

reset_button = Button(text= "Reset", highlightthickness=0, command= reset)
reset_button.grid(row= 2,column= 2)

check_marks = Label(fg= GREEN,bg= YELLOW)
check_marks.grid(row= 2, column= 1)


window.mainloop()
