#Importing Packages
import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas_datareader.data as web

style.use('ggplot')

'''
Data Fetching
'''
#Assigning start dates and end dates to fetch stock data between these times
start = dt.datetime(2000,1,1)
end = dt.datetime.now()

# #Fetching data from yahoo
df = web.DataReader('VIAANINDUS.BO','yahoo',start,end)
print(df.tail())
# # df = df.reset_index()
df.to_csv('tsla.csv')
# print(df.tail())



'''
Handling Data and plotting

'''
df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
# print(df.tail())
# df.plot()
# plt.show()

'''
Manipulating data
'''
#Moving averages
# df['100ma'] = df['Adj Close'].rolling(window = 100,min_periods = 0).mean()
# df.dropna(inplace = True)#removes data with nan
# print(df['100ma'])

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# print(df_ohlc)
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex = ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
# ax1.plot(df.index,df['Adj Close'])
# ax1.plot(df.index,df['100ma'])
# ax2.bar(df.index,df['Volume'])
plt.show()

url = 'https://en.wikipedia.org/wiki/NIFTY_50'
data = pd.read_html(url)
data = pd.DataFrame(data[1])
data.columns = data.loc[0]
data = data[1:]
data.reset_index(inplace = True)
print(data.columns)
symbols = data['Symbol']


# def fetch_data(symbol

# def get_data_from_sp50(symbols)