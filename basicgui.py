from tkinter import *

GUI = Tk()
GUI.title("Basic GUI")
GUI.geometry("400x300")

label = Label(GUI, text="Hello, Tkinter!")
label.pack()

GUI.mainloop()