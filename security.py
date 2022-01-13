from tkinter import *
from tkinter import font 
from tkinter import messagebox
import sys
      

root = Tk()



user = StringVar()
password = StringVar()

def verify():
    userName = user.get()
    pass2 = password.get()
    if userName=="admin":
        if pass2=="root":
            messagebox.showinfo("done","You are successfully verified !")
            root.destroy()
            
        else:
            messagebox.showwarning("Alert","You can not access this !")
            
            
    else:
            messagebox.showwarning("Alert","You can not access this !")  
            
        


root.geometry("300x300")
root.configure(bg="black")
root.title("Please verify Yourself")
Label(root, text="Please Verify Yourself!", bg="black", fg="white", font="lucida 15 bold").pack()
f= Frame()
f.pack(pady=40)
Label(f, text="User Name:").grid(row=0,column=0)
Entry(f, textvariable=user).grid(row=0, column=1)
Label(f, text="Password:").grid(row=1,column=0,pady=10)
Entry(f, textvariable=password).grid(row=1, column=1, pady=10)
Button(text="Verify", command=verify).pack()

root.mainloop()