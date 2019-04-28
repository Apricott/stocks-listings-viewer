import tkinter as tk
import tkinter.scrolledtext as tkst
import datetime
import matplotlib
from tkinter import *
from tkinter import messagebox
from pandas_datareader._utils import RemoteDataError
from pandas_datareader import data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from statsmodels.tsa.seasonal import seasonal_decompose
matplotlib.use("TkAgg")


class Navbar(tk.Frame):
    def __init__(self, master=None):
        super(Navbar, self).__init__()

        self.master = master

        self.columnconfigure(5, weight=1)
        self.rowconfigure(5, weight=1)

        self.master = tk.Frame(master, bg="darkslategray", width=200, height=500)
        self.master.grid(row=0, column=0, rowspan=20, sticky=W)

        self.label = tk.Label(master, bg="oldlace", font=('Century Gothic', '11', 'bold', 'italic'), height=2, width=22, text="Menu")
        self.label.grid(master, row=0, column=0, sticky=NW)

        self.label = tk.Label(master, bg="linen", font=('Century Gothic', '9'), width=22, text="Enter ticker symbol below:")
        self.label.grid(master, column=0, row=1)

        entry_ticker_var = StringVar()
        self.entry = tk.Entry(master, width=10, bg="lightcyan", textvariable=entry_ticker_var)
        self.entry.grid(master, column=0, row=2)
        self.entry.focus_set()
        self.entry.bind('<Return>', lambda e: enter(e))

        self.label = tk.Label(master, bg="peachpuff", font=('Century Gothic', '9'), width=10, text="Date from:")
        self.label.grid(master, row=14, column=0)

        entry1_var = StringVar()
        self.entry = tk.Entry(master, bg="lightcyan", font=('Century Gothic', '9'), width=20, textvariable=entry1_var)
        self.entry.grid(master, column=0, row=15)

        self.label = tk.Label(master, bg="peachpuff1", font=('Century Gothic', '9'), width=10, text="Date to:")
        self.label.grid(row=16, column=0)

        entry2_var = StringVar()
        self.entry = tk.Entry(master, bg="lightcyan", font=('Century Gothic', '9'), width=20, textvariable=entry2_var)
        self.entry.grid(master, row=17, column=0)

        self.button = Button(master, bg="peachpuff", font=('Century Gothic', '9'), text="Show Plot", command=lambda: show_plot_button())
        self.button.grid(row=19, column=0)
        self.button.bind('<Return>', lambda e: enter(e))

        radio_var = StringVar()
        r1 = Radiobutton(master, bg="antiquewhite1", text="close", variable=radio_var, value="close",
            font=('Century Gothic', '9'), width=10, command=lambda: plot_customization())
        r1.grid(column=0, row=4)
        radio_var.set("close")

        r2 = Radiobutton(master, bg="antiquewhite2", text="open", variable=radio_var, value="open",
            font=('Century Gothic', '9'), width=10, command=lambda: plot_customization())
        r2.grid(column=0, row=5)

        r3 = Radiobutton(master, bg="papayawhip", text="high", variable=radio_var, value="high",
            font=('Century Gothic', '9'), width=10, command=lambda: plot_customization())
        r3.grid(column=0, row=6)

        r4 = Radiobutton(master, bg="blanchedalmond", text="low", variable=radio_var, value="low",
            font=('Century Gothic', '9'), width=10, command=lambda: plot_customization())
        r4.grid(column=0, row=7)

        r5 = Radiobutton(master, bg="bisque", text="volume", variable=radio_var, value="volume",
            font=('Century Gothic', '9'), width=10, command=lambda: plot_customization())
        r5.grid(column=0, row=8)

        r6 = Radiobutton(master, bg="bisque2", text="growth", variable=radio_var, value="growth",
            font=('Century Gothic', '9'), width=10, command=lambda: plot_customization())
        r6.grid(column=0, row=9)


        def enter(event):
            show_plot_button()

        def show_plot_button():
            plot_specs = plot_creation()
            a = PlotSpecs()

            a.max_plot.insert(tk.INSERT, plot_specs[0])
            a.min_plot.insert(tk.INSERT, plot_specs[1])
            a.mean_plot.insert(tk.INSERT, plot_specs[2])
            a.mean_yearly.insert(tk.INSERT, plot_specs[3])

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
                c = MainPlot()
                specs = (MainPlot.plot(c, data_type[0], data_type[1], data_type[2], data_type[3]))
                return specs


class MainPlot(tk.Frame):
    def __init__(self, master=None):
        super(MainPlot, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="aliceblue", width=800, height=350)
        self.master.grid(row=0, rowspan=19, column=1, columnspan=9, sticky=NE)

    def plot(self, *args):

            start_date = datetime.datetime.now() - datetime.timedelta(days=10 * 365)

            try:
                ticker = args[0]
                # User pandas_reader.data.DataReader to load the desired data. As simple as that.
                exchange_listing = data.DataReader(ticker, 'yahoo', start_date)
            except RemoteDataError:
                messagebox.showerror("Wrong Ticker Symbol", "Could not find a company with the given symbol! \n (check for accidental whitespaces!)")
            except:
                messagebox.showerror("Unknown Error", "Something went wrong!")

            exchange_listing.columns = ['high', 'low', 'open', 'close', 'volume', 'adj_close']
            exchange_listing.index.name = 'time'
            exchange_listing['growth'] = exchange_listing['close'] / exchange_listing['close'].shift(1)

            # placing given arguments in the list
            params = []
            for ar in args:
                params.append(ar)

            # deleting empty elements
            params = list(filter(None, params))

            plot_content = params[1]

            fig = Figure(figsize=(8, 3.5))
            a = fig.add_subplot(111)
            fig.patch.set_facecolor('lightcyan')
            if len(params) > 3:
                date_start = params[2]
                date_end = params[3]

                if plot_content != 'growth':
                    timedelta = 90
                    if len(date_start) > 6:
                        # extracting trend freq of 1/10 of the given time period

                        time1 = date_start
                        time2 = date_end

                        date_time1 = datetime.datetime.strptime(time1, '%Y-%m-%d')
                        date_time2 = datetime.datetime.strptime(time2, '%Y-%m-%d')
                        timedelta = date_time2 - date_time1
                        timedelta = timedelta.days
                        timedelta = int(round(timedelta/10))

                    trend_df = exchange_listing[plot_content][date_start:date_end]
                    trend = seasonal_decompose(trend_df, model='additive', freq=timedelta)
                    a.plot(exchange_listing[plot_content][date_start:date_end])
                    a.plot(trend.trend)

                a.plot(exchange_listing[plot_content][date_start:date_end])
                maximum = exchange_listing[plot_content][date_start:date_end].max()
                minimum = exchange_listing[plot_content][date_start:date_end].min()
                mean = exchange_listing[plot_content][date_start:date_end].mean()
                mean_yearly = exchange_listing[plot_content][date_start:date_end].resample('A').mean()

            elif len(params) > 2:
                date_start = params[2]

                if plot_content != 'growth':
                     trend_df = exchange_listing[plot_content][date_start]
                     trend = seasonal_decompose(trend_df, model='additive', freq=31)
                     a.plot(exchange_listing[plot_content][date_start])
                     a.plot(trend.trend)

                a.plot(exchange_listing[plot_content][date_start])
                maximum = exchange_listing[plot_content][date_start].max()
                minimum = exchange_listing[plot_content][date_start].min()
                mean = exchange_listing[plot_content][date_start].mean()
                mean_yearly = exchange_listing[plot_content][date_start].resample('A').mean()
            else:
                a.plot(exchange_listing[plot_content])

                if plot_content != 'growth':
                    trend_df = exchange_listing[plot_content]
                    trend = seasonal_decompose(trend_df, model='additive', freq=365)
                    a.plot(exchange_listing[plot_content])
                    a.plot(trend.trend)

                maximum = exchange_listing[plot_content].max()
                minimum = exchange_listing[plot_content].min()
                mean = exchange_listing[plot_content].mean()
                mean_yearly = exchange_listing['close'].resample('A').mean()

            if plot_content == 'volume':
                a.set_ylabel('Volume')
            else:
                a.set_ylabel('Price ($)')

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().grid(row=1, column=1)
            canvas.draw()

            toolbar_frame = Frame(master=root)
            toolbar_frame.grid(row=0, column=3, columnspan=5, sticky=NW)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            return maximum, minimum, mean, mean_yearly


class PlotSpecs(tk.Frame):
    def __init__(self, master=None):
        super(PlotSpecs, self).__init__()

        self.master = master

        self.master = tk.Frame(master, bg="darkslategray", width=800, height=150)
        self.master.grid(row=15, rowspan=6, column=1, columnspan=9, sticky=SE)

        self.label_1 = tk.Label(master, bg="antiquewhite1", font=('Century Gothic', '9', 'bold'), height=1, width=6, text="Max")
        self.label_1.grid(master, row=16, column=1)

        self.max_plot = tk.Text(master, bg="lightcyan", font=('Century Gothic', '9'), height=1, width=8)
        self.max_plot.grid(master, row=16, column=2, sticky=W)

        self.label_2 = tk.Label(master, bg="antiquewhite2", font=('Century Gothic', '9', 'bold'), height=1, width=6, text="Min")
        self.label_2.grid(master, row=17, column=1)

        self.min_plot = tk.Text(master, bg="lightcyan", font=('Century Gothic', '9'), height=1, width=8)
        self.min_plot.grid(master, row=17, column=2, sticky=W)

        self.label_3 = tk.Label(master, bg="bisque", font=('Century Gothic', '9', 'bold'), height=1, width=6, text="Mean")
        self.label_3.grid(master, row=18, column=1)

        self.mean_plot = tk.Text(master, bg="lightcyan", font=('Century Gothic', '9'), height=1, width=8)
        self.mean_plot.grid(master, row=18, column=2, sticky=W)

        self.label_5 = tk.Label(master,  bg="cornsilk2", font=('Century Gothic', '10', 'bold'), height=1, width=27, text="Mean of subsequent years")
        self.label_5.grid(master, row=15, column=3, columnspan=4, sticky=S)

        self.mean_yearly = tkst.ScrolledText(master, bg="lightcyan", font=('Century Gothic', '11'), width=25, height=6)
        self.mean_yearly.grid(master, row=16, column=3, columnspan=4, rowspan=4)

        self.note = tk.Text(master, bg="darkslategray", font=('Century Gothic', '9'), fg='white', width=17,
         height=4,relief = FLAT)
        self.note.grid(master, row=16, column=7, columnspan=3, rowspan=4, sticky=N)
        self.note.insert(END, "Note \nThe smoother line \nrepresents trend.")
        self.note.config(state=DISABLED)


class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master

        self.master.maxsize(1000, 500)
        self.master.minsize(1000, 500)

        master.title("Exchange listings")

        self.label = tk.Label(master, text="Data Frame")

        self.navbar = Navbar()
        self.mainplot = MainPlot()
        self.plotspecs = PlotSpecs()


root = Tk()
app = MainWindow(root)
root.mainloop()
