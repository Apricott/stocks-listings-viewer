import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Data_Frame():
    def __init__(self):
        exchange_listing = pd.read_csv ('tsla_us_d.csv', index_col=0, parse_dates=True)
        exchange_listing.columns = ['open', 'high', 'low', 'close', 'volume']
        exchange_listing.index.name = 'time'
        exchange_listing['growth'] = exchange_listing['close'] / exchange_listing['close'].shift(1)

        print(exchange_listing['close']['2018'].mean())

        print(exchange_listing['close']['2018'].min())

        print(exchange_listing['close']['2018'].max())

        #prints mean of every year
        yearly_mean = exchange_listing['close'].resample('A').mean()
        print(yearly_mean)


"""print (notowania['2018'].head())

print ("średnia cena zamkniecia dla 2018:")
print (notowania['close']['2018'].mean())

print ("minimalna cena zamkniecia dla 2018:")
print (notowania['close']['2018'].min())

print ("maksymalna cena zamkniecia dla 2018:")	
print (notowania['close']['2018'].max())


szereg_czasowy = notowania['close'].resample('A').mean()
print(szereg_czasowy)
notowania['close'].plot()"""


plt.show(block=True)

