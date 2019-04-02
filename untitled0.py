import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


notowania = pd.read_csv ('tsla_us_d.csv', index_col=0, parse_dates=True)
notowania.columns = ['open', 'high', 'low', 'close', 'volume']
notowania.index.name = 'time'
notowania['wzrost'] = notowania['close'] / notowania['close'].shift(1) 


print (notowania['2018'].head())

print ("średnia cena zamkniecia dla 2018:")
print (notowania['close']['2018'].mean())

print ("minimalna cena zamkniecia dla 2018:")
print (notowania['close']['2018'].min())

print ("maksymalna cena zamkniecia dla 2018:")	
print (notowania['close']['2018'].max())


szereg_czasowy = notowania['close'].resample('A').mean()
print(szereg_czasowy)
notowania['close'].plot()


def plot():

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    v = np.array([16, 16.31925, 17.6394, 16.003, 17.2861, 17.3131, 19.1259, 18.9694, 22.0003, 22.81226])
    p = np.array([16.23697, 17.31653, 17.22094, 17.68631, 17.73641, 18.6368,
                  19.32125, 19.31756, 21.20247, 22.41444, 22.11718, 22.12453])

    fig = Figure(figsize=(6, 3))
    a = fig.add_subplot(111)
    a.scatter(v, x, color='red')
    a.plot(p, range(2 + max(x)), color='blue')
    a.invert_yaxis()

    a.set_title("Estimation Grid", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)

    return fig

plt.show(block=True)

