import pandas_datareader as web
import pandas as pd
import datetime as dt
from mpl_finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
data=web.DataReader("AAPL","yahoo",start, end)
data=data[['Open','High','Low','Close']]
data.reset_index(inplace=True)
data['Date']=data['Date'].map(mdates.date2num)
data = data.astype(float)
ax=plt.subplot()
ax.xaxis_date()
# candlestick2_ohlc(ax, data['Date'],data['Open'],data['High'],data['Low'],data['Close'])
candlestick2_ohlc(ax, data.values)
plt.show()