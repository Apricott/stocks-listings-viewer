import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import matplotlib
from tkinter import *
from tkinter import messagebox
from pandas_datareader._utils import RemoteDataError
from pandas_datareader import data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.use("TkAgg")


"""class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label="Search", **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, tk.END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)"""


class Navbar(tk.Frame):
    def __init__(self, master=None):
        super(Navbar, self).__init__()

        self.master = master

        self.columnconfigure(5, weight=1)
        self.rowconfigure(5, weight=1)

        self.master = tk.Frame(master, bg="gray", width=200, height=500)
        self.master.grid(row=0, column=0, rowspan=20, sticky=W)

        self.label = tk.Label(master, width=28, text="Menu")
        self.label.grid(master, row=0, column=0, sticky=NW)

        self.label = tk.Label(master, width=22, text="Enter ticker symbol below:")
        self.label.grid(master, column=0, row=1)


        entry_ticker_var = StringVar()
        self.entry = tk.Entry(master, width=10, textvariable=entry_ticker_var)
        self.entry.grid(master, column=0, row=2)
        self.entry.focus_set()
        self.entry.bind('<Return>', lambda e: enter(e))

        self.label = tk.Label(master, width=10, text="Date from:")
        self.label.grid(master, row=14, column=0)

        entry1_var = StringVar()
        self.entry = tk.Entry(master, width=20, textvariable=entry1_var)
        self.entry.grid(master, column=0, row=15)

        self.label = tk.Label(master, width=10, text="Date to:")
        self.label.grid(row=16, column=0)

        entry2_var = StringVar()
        self.entry = tk.Entry(master, width=20, textvariable=entry2_var)
        self.entry.grid(master, row=17, column=0)


        self.button = Button(master, text="Show Plot", command=lambda: show_plot_button())
        self.button.grid(row=19, column=0)
        self.button.bind('<Return>', lambda e: enter(e))



        radio_var = StringVar()
        r1 = Radiobutton(master, text="close", variable=radio_var, value="close", width=10, command=lambda: plot_customization())
        r1.grid(column=0, row=4)
        radio_var.set("close")
        r2 = Radiobutton(master, text="open", variable=radio_var, value="open", width=10, command=lambda: plot_customization())
        r2.grid(column=0, row=5)
        r3 = Radiobutton(master, text="high", variable=radio_var, value="high", width=10, command=lambda: plot_customization())
        r3.grid(column=0, row=6)
        r4 = Radiobutton(master, text="low", variable=radio_var, value="low", width=10, command=lambda: plot_customization())
        r4.grid(column=0, row=7)
        r5 = Radiobutton(master, text="volume", variable=radio_var, value="volume", width=10, command=lambda: plot_customization())
        r5.grid(column=0, row=8)
        r6 = Radiobutton(master, text="growth", variable=radio_var, value="growth", width=10, command=lambda: plot_customization())
        r6.grid(column=0, row=9)

        def enter(event):
            show_plot_button()

        def show_plot_button():
            plot_specs = plot_creation()
            if plot_specs:
                print(plot_specs)
                d = PlotSpecs()
                d.maks.insert(tk.INSERT, plot_specs)


        def plot_customization():
            arg1 = radio_var.get()

            # default plot content if no other specified
            if arg1 == '0':
                arg1 = 'close'

            arg2 = entry1_var.get()
            arg3 = entry2_var.get()
            arg4 = entry_ticker_var.get()
            return arg4, arg1, arg2, arg3

        def plot_creation():
            data_type = plot_customization()
            if data_type[0] == '':
                messagebox.showwarning("No ticker symbol", "Enter ticker symbol!")
            else:
                print(data_type)
                c = MainPlot()
                specs = (MainPlot.plot(c, data_type[0], data_type[1], data_type[2], data_type[3]))
                return specs

class MainPlot(tk.Frame):
    def __init__(self, master=None):
        super(MainPlot, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="white", width=800, height=350)
        self.master.grid(row=0, rowspan=19, column=1, columnspan=9, sticky=NE)

    def plot(self, *args):

            start_date = datetime.datetime.now() - datetime.timedelta(days=10 * 365)

            try:
                print(args[0])
                ticker = args[0]
                # User pandas_reader.data.DataReader to load the desired data. As simple as that.
                exchange_listing = data.DataReader(ticker, 'yahoo', start_date)
            except RemoteDataError:
                messagebox.showerror("Wrong Ticker Symbol", "Could not find a company with the given symbol! \n (accidental whitespace maybe?)")
            except:
                messagebox.showerror("Unknown Error", "Something went wrong!")
               # panel_data.to_csv('panel_data.csv')

            #exchange_listing = pd.read_csv('panel_data.csv', index_col=0, parse_dates=True)
            exchange_listing.columns = ['high', 'low', 'open', 'close', 'volume', 'adj_close']
            exchange_listing.index.name = 'time'
            exchange_listing['growth'] = exchange_listing['close'] / exchange_listing['close'].shift(1)

            # placing given arguments in the list
            params = []
            for ar in args:
                params.append(ar)

            # deleting empty elements
            params = list(filter(None, params))

            print(params[1])

            plot_content = params[1]

            fig = Figure(figsize=(8, 3.5))
            a = fig.add_subplot(111)
            if len(params) > 3:
                date_start = params[2]
                date_end = params[3]
                a.plot(exchange_listing[plot_content][date_start:date_end])
                maximum = exchange_listing[plot_content][date_start:date_end].max()
            elif len(params) > 2:
                date_start = params[2]
                a.plot(exchange_listing[plot_content][date_start])
                maximum = exchange_listing[plot_content][date_start].max()
            else:
                a.plot(exchange_listing[plot_content])
                maximum = exchange_listing[plot_content].max()

            if plot_content == 'volume':
                print(plot_content)
                a.set_ylabel('Volume')
            else:
                a.set_ylabel('Price ($)')

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().grid(row=1, column=1)
            canvas.draw()

            toolbar_frame = Frame(master=root)
            toolbar_frame.grid(row=0, column=3, columnspan=4, sticky=NW)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            return maximum

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
        self.master.grid(row=15, rowspan=6, column=1, columnspan=9, sticky=SE)

        #self.label = tk.Label(master, text="Tu ma być opis wykresu")
        #self.label.grid(master, row=1, rowspan=1, column=1, sticky=NW)

        self.text1 = tk.Label(master, height=1, width=6, text="Max")
        self.text1.grid(master, row=16, column=1)

        self.text2 = tk.Label(master, height=1, width=6,  text="Min")
        self.text2.grid(master, row=17, column=1)

        self.text3 = tk.Label(master, height=1, width=6,  text="Mean")
        self.text3.grid(master, row=18, column=1)

        self.text4 = tk.Label(master, height=1, width=6,  text="Trend")
        self.text4.grid(master, row=18, column=3)

        self.maks = tk.Text(master, height=1, width=10)
        self.maks.grid(row=16, column=2)

        self.text5 = tk.Label(master, height=1, width=42, text="Mean of subsequent years")
        self.text5.grid(master, row=16, column=5, columnspan=4, sticky=S)


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

        master.title("Data Frame")


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
