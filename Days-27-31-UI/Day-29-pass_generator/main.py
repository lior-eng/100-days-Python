from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
import json
file_path = './Days-27-31-UI/Day-29-pass_generator/data.json'
# ---------------------------------- Search ------------------------------------- #
def find_password() -> None:
    website: str = website_entry.get()
    try:
        with open(file_path, mode= 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title= "Error", message= "No Data File Found")
    except json.JSONDecodeError:
        messagebox.showerror(title= "Error", message= "File empty")
    # except KeyError:
    #     messagebox.showerror(title= "Error", message= "Invalid key")
    else: 
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title= website, message= f"Email: {email}\n"
                                                        f"Password: {password}")
        else:
            messagebox.showerror(title= website, message= f"No details for {website} exists")
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
    website: str = website_entry.get()
    user_name: str = user_name_entry.get()
    password: str = pass_entry.get()
    new_data: dict  = {
        website: {
            "email": user_name,
            "password": password
        }
    }
    if website == "" or user_name == "" or password == "":
        messagebox.showerror(title= "Oops", message= "Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title= website, message=
                                    f"These are the details enterd:\n"
                                    f"{website}\n"
                                    f" {user_name}\n"
                                    f" {password}\n")
        if is_ok:
            try:
                with open(file_path, mode= 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("New json file created")
                with open(file_path, mode= 'w') as data_file:
                    json.dump(new_data, data_file, indent= 4)
            except json.JSONDecodeError:
                print("Json file was empty")             
                with open(file_path, mode= 'w') as data_file:
                    json.dump(new_data, data_file, indent= 4)
            else:
                print("Json updated")  
                data.update(new_data)                
                with open(file_path, mode= 'w') as data_file:
                    json.dump(data, data_file, indent= 4)
                
            website_entry.delete(0,END)
            user_name_entry.delete(0,END)
            pass_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
windom = Tk()
windom.title("Password Manager")
windom.config(padx= 50, pady= 50)

canvas = Canvas(height= 200, width= 200)
pass_image = PhotoImage(file= "./Days-27-31-UI/Day-29-pass_generator/logo.png")
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
website_entry.grid(row= 1, column= 1)
website_entry.focus()
user_name_entry = Entry(width= 35)
user_name_entry.grid(row= 2, column= 1)
pass_entry = Entry(width= 35)
pass_entry.grid(row= 3, column= 1)

# Buttons
pass_button = Button(text= "Generate Password", width= 15, command= pass_generator)
pass_button.grid(row= 3, column= 2, columnspan= 2)
add_button = Button(text= "Add", width= 46, command= save)
add_button.grid(row= 4, column= 1, columnspan= 2)
search_button = Button(text= "Search", width= 15, command= find_password)
search_button.grid(row= 1, column= 2)


windom.mainloop()