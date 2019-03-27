import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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

plt.show(block=True)

