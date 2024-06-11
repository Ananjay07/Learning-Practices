#Tkinter - used for developing GUI (Graphical User Interface)
import tkinter

#widgets:
#Label - a text or image is displayed

tk = tkinter.Tk()
from tkinter import *
label = Label(tk, text="Hello World")
label.pack()
tk.mainloop

#Buttons, Checkboxes and Radiobuttons
from tkinter import *
root =Tk()
myButton1 = Button(root, text="Click Me") # normal button
myButton1.pack()
root.mainloop()

from tkinter import *
master = Tk()
Checkbutton(master, text='Sports').grid(row=0, sticky=W)
Checkbutton(master, text='Arts').grid(row=1, sticky=W)
mainloop()

from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()