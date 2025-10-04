#create window
#adding widgets 
#use of layouts 

import tkinter as tk 
root = tk.Tk()
root.title("this is my first window")

def submit():
    name = entery.get()
    if name:
        print(f"hello,{name}")
    else:
        print("enter your name")
        
lable = tk.Label(root,text="enter your name")
lable.pack()
entery = tk.Entry(root)
entery.pack()
tk.Button(root,text="print",command=submit).pack()
root.geometry("300x200")
root.mainloop()