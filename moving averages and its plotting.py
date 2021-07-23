import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
tick = ["^NSEI"]
nse = yf.download(tick, start = "2017-01-01", end = "2021-05-05")
nse.to_csv("nse.csv")
NSE = pd.read_csv("nse.csv", parse_dates =["Date"], index_col = "Date")
NSE.pop("Adj Close") # pop() helps to delete the unwanted columns by specifying the column names in the round brackets
NSE.pop("Volume")
NSE = NSE.Close.to_frame() # .close.to_frame() gives the only 1 specific column.
SMA_10 = NSE.rolling(window = 10).mean()
SMA_10 = SMA_10.dropna()
SMA_50 = NSE.rolling(window = 50).mean()
SMA_50 = SMA_50.dropna()
SMA_100 = NSE.rolling(window = 100).mean()
SMA_100 = SMA_100.dropna()
SMA_10.plot(figsize = (20,10))
plt.legend( loc = "upper right", fontsize = 13)
plt.plot(NSE, color = "g")
plt.plot(SMA_10, color ="r" )
plt.plot(SMA_50, color = "b")
plt.plot(SMA_100, color = "y")
plt.show()
