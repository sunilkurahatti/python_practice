import pandas_datareader as web
import pandas as pd
from matplotlib import style
import datetime as dt
from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

style.use('ggplot')
ticker='AAPL'
start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()
data=web.DataReader(ticker,"yahoo",start, end)
data=data[['Open','High','Low','Close']]
data.reset_index(inplace=True)
data['Date']=data['Date'].map(mdates.date2num)
data = data.astype(float)
ax=plt.subplot()
ax.xaxis_date()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('#1a1f20')
ax.set_title("{} share price".format(ticker), color='white')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white',labelrotation=45,length=6,grid_alpha=.3)
ax.tick_params(axis='y', colors='white',grid_alpha=.3)
# candlestick2_ohlc(ax, data['Date'],data['Open'],data['High'],data['Low'],data['Close'])
candlestick_ohlc(ax, data.values, colorup='#15ff00',width=.5)
plt.show()