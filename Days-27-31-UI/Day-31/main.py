from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word: dict = {}
try:
    df:pd.DataFrame = pd.read_csv("./Days-27-31-UI/Day-31/data/words_to_learn.csv")
except FileNotFoundError:
    df:pd.DataFrame = pd.read_csv("./Days-27-31-UI/Day-31/data/french_words.csv")
    to_learn: list[dict] = df.to_dict(orient= "records")
else:
    to_learn: list[dict] = df.to_dict(orient= "records")
    
def new_card() -> None:
    global card_timer, current_word
    current_word = random.choice(to_learn) # ---> {'French': 'tiens', 'English': 'here'}
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_word["French"], fill= "black")
    canvas.itemconfig(card_background, image= front_card_img)
    window.after_cancel(card_timer)
    card_timer = window.after(3000, flip_card)

def flip_card() -> None:
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= current_word["English"], fill= "white")
    canvas.itemconfig(card_background, image= back_card_img)

def is_known() -> None:
    to_learn.remove(current_word)
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv("./Days-27-31-UI/Day-31/data/words_to_learn.csv", index= False)
    new_card()
    
window:object = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= "#B1DDC6")

card_timer = window.after(3000, func= new_card)

canvas = Canvas(height= 526, width= 800)
front_card_img = PhotoImage(file= "./Days-27-31-UI/Day-31/images/card_front.png")
back_card_img = PhotoImage(file= "./Days-27-31-UI/Day-31/images/card_back.png")
card_background = canvas.create_image(400, 263, image= front_card_img)
card_title = canvas.create_text(400, 150, text= "French", font= ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 260, text= "", font= ("Arial", 60, "bold"))
canvas.config(bg= "#B1DDC6", highlightthickness= 0)
canvas.grid(row= 0, column= 0, columnspan= 2)

# Buttons
v_mark_image = PhotoImage(file= "./Days-27-31-UI/Day-31/images/right.png")
v_mark_button = Button(image= v_mark_image, highlightthickness= 0, command= is_known)
v_mark_button.grid(row= 1, column= 1)

x_mark_img = PhotoImage(file= "./Days-27-31-UI/Day-31/images/wrong.png")
x_mark_button = Button(image= x_mark_img, highlightthickness= 0, command= new_card)
x_mark_button.grid(row= 1, column= 0)

new_card()   

window.mainloop()