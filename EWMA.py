import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
tick = ["^NSEI"]
nse = yf.download(tick, start = "2017-01-01", end = "2021-05-05")
nse.to_csv("nse.csv")
NSE = pd.read_csv("nse.csv", parse_dates =["Date"], index_col = "Date", usecols = ["Date", "Close"])
print(NSE.head(10))
ewma_10 = NSE.Close.ewm(span = 10, min_periods =10).mean()  # using ewm itself eliminates the use of putting in the formula
SMA_10 = NSE.rolling(window = 10).mean()     # use can change the span to 50, 100, 200 and more.
SMA_10.plot(figsize = (15,8), fontsize = 15)


plt.plot(SMA_10, color = 'g')
plt.plot(ewma_10, color ='r')
plt.show()