#Entry
import tkinter as tk
root=tk.Tk()

name_var=tk.StringVar()
passw_var=tk.StringVar()
 
def submit():           #define what will happen when entries are entered and submitted
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is:", name)
    print("The password is:", password)
     
    name_var.set("")
    passw_var.set("")

name_label = tk.Label(root, text = 'Username')           #Label for username
name_entry = tk.Entry(root,textvariable = name_var)      #Entry for username
  
passw_label = tk.Label(root, text = 'Password')                     #Label for pw
passw_entry=tk.Entry(root, textvariable = passw_var, show = '*')    #Entry for pw

sub_btn=tk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()