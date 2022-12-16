from tkinter import messagebox, ttk, Button
from tkinter import *

def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="anusoochak").grid(column=0, row=0)
    t = optionMenu(root, frm)

    button = Button(frm, text="Test").grid(column=0, row=1)

    root.mainloop()

class optionMenu():
    def __init__(self, root, frm) -> None:
        choices = ["First come First serve", "Round robin", "Shortest job first", "Shortest time first", "Bozo"]
        self.__option = StringVar(root)
        self.__option.set("First come First serve")
        optionMenu = OptionMenu(frm, self.__option, *choices).grid(column=1, row=0)

    def getOption(self):
        return self.__option.get()

if __name__ == "__main__":
    main()
