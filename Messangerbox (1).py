from tkinter import *
from tkinter import messagebox
a=Tk()
a.geometry("500x500")
def fun():
    messagebox.showinfo("Hello","Successfully Submited")
B=Button(a,text="Login",command=fun)
B.pack(expand=True)
a.mainloop()