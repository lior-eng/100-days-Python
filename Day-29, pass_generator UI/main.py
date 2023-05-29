from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
'''
# String constants from string

# string.ascii_letters    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits           0123456789
# string.punctuation      !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# '''
def pass_generator() -> None:
    password = ''

    for _ in range (3):
        password += (random.choice(string.ascii_letters))
    for _ in range (4):
        password += (random.choice(string.digits))
    for _ in range (3):
        password += (random.choice(string.punctuation))

    password = ''.join(random.sample(password,len(password)))
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save() -> None:
    website = website_entry.get()
    user_name = user_name_entry.get()
    password = pass_entry.get()
    
    if website == "" or user_name == "" or password == "":
        messagebox.showerror(title= "Oops", message= "Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title= website, message=
                                    f"These are the details enterd:\n"
                                    f"{website}\n"
                                    f" {user_name}\n"
                                    f" {password}\n")
        if is_ok:
            with open(file= './Day-29, pass_generator UI/data.txt', mode= 'a') as data_file:
                data_file.write(f"{website} |"
                            f" {user_name} |"
                            f" {password}\n")
            website_entry.delete(0,END)
            user_name_entry.delete(0,END)
            pass_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
windom = Tk()
windom.title("Password Manager")
windom.config(padx= 50, pady= 50)

canvas = Canvas(height= 200, width= 200)
pass_image = PhotoImage(file= "./Day-29, pass_generator UI/logo.png")
canvas.create_image(100, 100, image= pass_image)
canvas.grid(row= 0, column= 1)

# Labels
website_label = Label(text= "Website:")
website_label.grid(row= 1, column= 0)
user_name_label = Label(text= "Email/Username:")
user_name_label.grid(row= 2, column= 0)
pass_label = Label(text= "Password:")
pass_label.grid(row= 3, column= 0)

# Entries
website_entry = Entry(width= 35)
website_entry.grid(row= 1, column= 1, columnspan= 2)
website_entry.focus()
user_name_entry = Entry(width= 35)
user_name_entry.grid(row= 2, column= 1, columnspan= 2)
pass_entry = Entry(width= 21)
pass_entry.grid(row= 3, column= 1)

# Buttons
pass_button = Button(text= "Generate Password", width= 15, command= pass_generator)
pass_button.grid(row= 3, column= 2, columnspan= 2)
add_button = Button(text= "Add", width= 36, command= save)
add_button.grid(row= 4, column= 1, columnspan= 2)


windom.mainloop()