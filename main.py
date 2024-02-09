from tkinter import *

from tkinter import messagebox
def click():
    if messagebox.askyesno(title="Valentine Code", message="Will you be my valentine?"):
        print("I want to be your valentine as well")
        messagebox.showwarning(title="Warning", message="You are now my valentine forever")
    else:
        print("owww :(   Me sad...")
        messagebox.showerror(title="I'm sad now", message="Why don't you want to be my valentine? :(")


window = Tk()


button = Button(window, command=click, text="Valentine ", bg="cyan")
button.pack()
window.mainloop()