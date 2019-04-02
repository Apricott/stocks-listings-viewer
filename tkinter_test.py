import tkinter as tk
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from untitled0 import plot


class Navbar(tk.Frame):
    def __init__(self, master=None):
        super(Navbar, self).__init__()

        self.master = master

        self.columnconfigure(5, weight=1)
        self.rowconfigure(5, weight=1)

        self.master = tk.Frame(master, bg="gray", width=200, height=500)
        self.master.grid(row=0, column=0, rowspan=10, sticky=W)

        self.label = tk.Label(master, width =28, text="Settings")
        self.label.grid(master, row=0, column=0, sticky=NW)

        self.label = tk.Label(master, width=8, text="Przeglądaj")
        self.label.grid(master, row=0, column=0, sticky=W)

        self.button = Button (master, text="Show Plot", command=MainPlot.showplot)
        self.button.grid(row= 3,column=0)



class mclass:
    def __init__(self, master=None):
        self.master = master
        self.box = Entry(master)
        self.button = Button (master, text="check", command=MainPlot.plot)
        self.box.grid()
        self.button.grid()

    def plot(self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().pack()
        canvas.draw()


class MainPlot(tk.Frame):
    def __init__(self, master=None):
        super(MainPlot, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="aquamarine", width=800, height=350)
        self.master.grid(row=0, rowspan=5, column=1, columnspan=8, sticky=NE)

    def showplot(self):

        canvas = FigureCanvasTkAgg(plot(), master=self.master)
        canvas.get_tk_widget().grid(column=1, row=1)
        canvas.draw()

    """def plot (self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,3))
        a = fig.add_subplot(111)
        a.scatter(v, x, color='red')
        a.plot(p, range(2+max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().grid()
        canvas.draw()"""

    """self.box = Entry(master)
        self.button = Button (master, text="check", command=self.plot)
        self.box.grid()
        self.button.grid()

        #self.label = tk.Label(master, text="Tu ma być wykres")
        #self.label.grid(master, row=0, rowspan=1, column=1, sticky=NW)

        def plot (self):
            x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
            p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
                19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

            fig = Figure(figsize=(6,6))
            a = fig.add_subplot(111)
            a.scatter(v,x,color='red')
            a.plot(p, range(2 +max(x)),color='blue')
            a.invert_yaxis()

            a.set_title ("Estimation Grid", fontsize=16)
            a.set_ylabel("Y", fontsize=14)
            a.set_xlabel("X", fontsize=14)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().grid()
            canvas.draw()"""


class PlotSpecs(tk.Frame):
    def __init__(self, master=None):
        super(PlotSpecs, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="white", width=800, height=150)
        self.master.grid(row=1, rowspan=10, column=1, columnspan=8, sticky=SE)

        #self.label = tk.Label(master, text="Tu ma być opis wykresu")
        #self.label.grid(master, row=1, rowspan=1, column=1, sticky=NW)

        self.text1 = tk.Label(master, height=1, width=6, text="Max")
        self.text1.grid(master, row=6, column=1)

        self.text2 = tk.Label(master, height=1, width=6,  text="Min")
        self.text2.grid(master, row=7, column=1)

        self.text3 = tk.Label(master, height=1, width=6,  text="Mean")
        self.text3.grid(master, row=8, column=1)

        self.text4 = tk.Label(master, height=1, width=6,  text="Trend")
        self.text4.grid(master, row=8, column=3)


        #self.button = Button(master, text="Ok")
        #self.button.grid(master, row=1, column=0, columnspan=2, sticky=E)

        #self.button = Button(master, text="To dziala")
        #self.button.grid(master, row=1, column=0, columnspan=2, sticky=N)


        #self.text1.grid(master, row=0, column=1, columnspan=2, sticky=N)
        #self.text1.tag_add('one', '1.0', '1.30')
        #self.text1.tag_config('one', background='green', foreground='#FFFFFF')



class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master

        self.master.maxsize(1000, 500)
        self.master.minsize(1000, 500)

        master.title("CSV Compiler")


        self.label = tk.Label(master, text="DataFrame")

        """self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.label.grid(columnspan=2,row=4, sticky=E)
        self.greet_button.grid(row=6, column=2)
        self.close_button.grid(row=5, column=1)"""

        self.navbar = Navbar()
        self.mainplot = MainPlot()
        self.plotspecs = PlotSpecs()

        #self.test = mclass()

        # def greet(self):
        # print("Greetings!")


root = Tk()
app = MainWindow(root)
root.mainloop()
