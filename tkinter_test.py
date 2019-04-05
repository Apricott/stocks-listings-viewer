import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.use("TkAgg")


class Navbar(tk.Frame):
    def __init__(self, master=None):
        super(Navbar, self).__init__()

        self.master = master

        self.columnconfigure(5, weight=1)
        self.rowconfigure(5, weight=1)

        self.master = tk.Frame(master, bg="gray", width=200, height=500)
        self.master.grid(row=0, column=0, rowspan=20, sticky=W)

        self.label = tk.Label(master, width =28, text="Settings")
        self.label.grid(master, row=0, column=0, sticky=NW)

        self.button = tk.Button(master, width=10, text="Select File")
        self.button.grid(master, row=1, column=0)

        self.button = Button(master, text="Show Plot", command= lambda: show_plot())
        self.button.grid(row=19, column=0)

        var = StringVar()
        r1 = Radiobutton(master, text="close", variable=var, value="close", width=10, command=lambda: plot_customization())
        r1.grid(column=0, row=4)
        r2 = Radiobutton(master, text="open", variable=var, value="open", width=10, command=lambda: plot_customization())
        r2.grid(column=0, row=5)
        r3 = Radiobutton(master, text="high", variable=var, value="high", width=10, command=lambda: plot_customization())
        r3.grid(column=0, row=6)
        r2 = Radiobutton(master, text="low", variable=var, value="low", width=10, command=lambda: plot_customization())
        r2.grid(column=0, row=7)
        r3 = Radiobutton(master, text="volume", variable=var, value="volume", width=10, command=lambda: plot_customization())
        r3.grid(column=0, row=8)

        def plot_customization():
            arg1 = var.get()
            return arg1

        def show_plot():
            data_type = plot_customization()
            if data_type:
                c = MainPlot()
                MainPlot.plot(c, data_type)


class MainPlot(tk.Frame):
    def __init__(self, master=None):
        super(MainPlot, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="white", width=800, height=350)
        self.master.grid(row=0, rowspan=19, column=1, columnspan=9, sticky=NE)

    def plot(self, param):
            exchange_listing = pd.read_csv('tsla_us_d.csv', index_col=0, parse_dates=True)
            exchange_listing.columns = ['open', 'high', 'low', 'close', 'volume']
            exchange_listing.index.name = 'time'
            exchange_listing['wzrost'] = exchange_listing['close'] / exchange_listing['close'].shift(1)

            print(param)

            fig = Figure(figsize=(9, 3.5))
            a = fig.add_subplot(111)
            a.plot(exchange_listing[param])

            fig = Figure(figsize=(8, 3.5))
            a = fig.add_subplot(111)
            a.plot(exchange_listing[param])

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().grid(row=1, column=1)
            canvas.draw()

            toolbar_frame = Frame(master=root)
            toolbar_frame.grid(row=0, column=3, columnspan=4, sticky=NW)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()
            canvas._tkcanvas.grid(row=1, column=1)


"""class PlotCustomization():
    def __init__(self, master=None):

        exchange_listing = pd.read_csv('tsla_us_d.csv', index_col=0, parse_dates=True)
        exchange_listing.columns = ['open', 'high', 'low', 'close', 'volume']
        exchange_listing.index.name = 'time'
        exchange_listing['growth'] = exchange_listing['close'] / exchange_listing['close'].shift(1)

        def mean():
            print(exchange_listing['close']['2018'].mean())

        print(exchange_listing['close']['2018'].min())

        print(exchange_listing['close']['2018'].max())

        # prints mean of every year
        yearly_mean = exchange_listing['close'].resample('A').mean()
        print(yearly_mean)"""


class PlotSpecs(tk.Frame):
    def __init__(self, master=None):
        super(PlotSpecs, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="gray", width=800, height=150)
        self.master.grid(row=17, rowspan=3, column=1, columnspan=9, sticky=SE)

        #self.label = tk.Label(master, text="Tu ma być opis wykresu")
        #self.label.grid(master, row=1, rowspan=1, column=1, sticky=NW)

        self.text1 = tk.Label(master, height=1, width=6, text="Max")
        self.text1.grid(master, row=17, column=1)

        self.text2 = tk.Label(master, height=1, width=6,  text="Min")
        self.text2.grid(master, row=18, column=1)

        self.text3 = tk.Label(master, height=1, width=6,  text="Mean")
        self.text3.grid(master, row=19, column=1)

        self.text4 = tk.Label(master, height=1, width=6,  text="Trend")
        self.text4.grid(master, row=19, column=3)


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

        master.title("DataFrame")


        self.label = tk.Label(master, text="DataFrame")

        """self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.label.grid(columnspan=2,row=4, sticky=E)
        self.greet_button.grid(row=6, column=2)
        self.close_button.grid(row=5, column=1)"""

        self.navbar = Navbar()
        self.mainplot = MainPlot()
        self.plotspecs = PlotSpecs()



    """def greet(self):
        print("Greetings!")"""


root = Tk()
app = MainWindow(root)
root.mainloop()
