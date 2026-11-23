from tkinter import *
from tkinter import messagebox

GUI = Tk()
GUI.title("Basic GUI")
GUI.geometry("400x300")

label = Label(GUI, text="Hello, Tkinter!")
label.pack()

def popup_message():
    messagebox.showinfo("Show Popup", "This is a popup message!")

button = Button(GUI, text="Show Popup", command=popup_message)
button.pack()

GUI.mainloop()