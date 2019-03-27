import tkinter as tk
from tkinter import *


class Navbar(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self)

        self.master = master

        self.master = tk.Frame(self, height=500, bg="blue")

        self.label = tk.Label(master, text="Ustawienia wykresu")


class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master.maxsize(1000, 500)
        self.master.minsize(1000, 500)

        self.master = master
        """master.title("A simple GUI")


        self.label = tk.Label(master, text="This is our first GUI!")

        self.greet_button = tk.Button(master, text="Greet", command=self.greet)

        self.close_button = tk.Button(master, text="Close", command=master.quit)

        self.label.grid(columnspan=2,row=4, sticky=E)
        self.greet_button.grid(row=6, column=2)
        self.close_button.grid(row=5, column=1)"""

        self.navbar = Navbar()

    def greet(self):
        print("Greetings!")


root = Tk()
app = MainWindow(root)
root.mainloop()
