#FRAME - a rectangular region on the screen
#It generates a GUI with a main window containing a frame, labels, and buttons, all with specified options like background color, border size, cursor style, and more, enhancing visual consistency and usability
import tkinter as tk

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

window = create_widget(None, tk.Tk)
window.title("GUI Example")


frame = create_widget(window, tk.Frame, bg='lightblue', bd=3, cursor='hand2', height=100,
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                      relief=tk.RAISED, width=200)
frame.pack(padx=20, pady=20)
#frame is created for the label

label = create_widget(frame, tk.Label, text='NAMES', font='50', bg='lightblue', bd=3, cursor='hand2',
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                      relief=tk.RAISED)
label.pack()
#a label is created inside the frame

button_frame = create_widget(window, tk.Frame, bg='lightblue', bd=3, cursor='hand2', height=50, 
                              highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                              relief=tk.RAISED, width=200)
button_frame.pack(pady=10)
#a frame is created for the buttons

def create_button(parent, text, fg):
    return create_widget(parent, tk.Button, text=text, fg=fg, bg='lightblue', bd=3, cursor='hand2',
                         highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                         relief=tk.RAISED)

buttons_info = [("LEWIS", "cyan"), ("MAX", "blue"), ("CHARLES", "red"), 
                ("BOTTAS", "green"), ("SAINZ", "red")]

for text, fg in buttons_info:
    button = create_button(button_frame, text=text, fg=fg)
    button.pack(side=tk.LEFT)
# the buttons are created inside the frame
# Run the Tkinter event loop
window.mainloop()