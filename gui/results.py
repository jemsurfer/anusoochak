from tkinter import messagebox, ttk, Button
from tkinter import *

def inputField(page):
    ##Tkinter frame set up with name variable
    root = Tk()

    ##Frame does something, i just copied and pasted off the docs. It has frame.
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=str(page)).grid(column=0, row=0)

    root.mainloop()


