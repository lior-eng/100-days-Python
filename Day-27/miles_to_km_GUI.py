from tkinter import *

FONT = ("Courier", 24, "bold")
WIDTH = 500
HEIGHT = 300

def miles_to_km() -> None:
    miles = float(miles_input.get())
    km = miles * 1.609
    km = round(km,2)
    km_display.config(text= f" {km}")

window = Tk()
window.title("Miles to Km converter")
window.minsize(width= WIDTH, height= HEIGHT)
window.config(padx= 20, pady= 20)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0,column=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1,column=0)

km_display = Label(text="0")
km_display.grid(row=1,column=1)

miles_input = Entry(width=5)
miles_input.grid(row=0,column=1)

calculate_button = Button(text= "Calculate", command= miles_to_km)
calculate_button.grid(row=2,column=1)


window.mainloop()