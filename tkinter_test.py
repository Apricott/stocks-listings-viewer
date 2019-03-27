import tkinter as tk
from tkinter import *


class Navbar(tk.Frame):
    def __init__(self, master=None):
        super(Navbar, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="green", width=200, height=500)
        self.master.grid(row=0, column=0, rowspan=2, sticky=W)

        self.label = tk.Label(master, text="Settings")
        self.label.grid(master, row=0, column=0, columnspan=1, sticky=N)


class MainPlot(tk.Frame):
    def __init__(self, master=None):
        super(MainPlot, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="red", width=800, height=350)
        self.master.grid(row=0, column=1, sticky=NE)

        self.label = tk.Label(master, text="Tu ma być wykres")
        self.label.grid(master, row=0, rowspan=1, column=1, sticky=N)


class PlotSpecs(tk.Frame):
    def __init__(self, master=None):
        super(PlotSpecs, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="blue", width=800, height=150)
        self.master.grid(row=1, column=1, sticky=SE)

        self.label = tk.Label(master, text="Tu ma być opis wykresu")
        self.label.grid(master, row=1, rowspan=1, column=1, sticky=N)




class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master.maxsize(1000, 500)
        self.master.minsize(1000, 500)

        self.master = master
        master.title("A simple GUI")

        self.label = tk.Label(master, text="DataFrame")

        """self.greet_button = tk.Button(master, text="Greet", command=self.greet)

        self.close_button = tk.Button(master, text="Close", command=master.quit)

        self.label.grid(columnspan=2,row=4, sticky=E)
        self.greet_button.grid(row=6, column=2)
        self.close_button.grid(row=5, column=1)"""

        self.navbar = Navbar()
        self.mainplot = MainPlot()
        self.plotspecs = PlotSpecs()


    def greet(self):
        print("Greetings!")


root = Tk()
app = MainWindow(root)
root.mainloop()
