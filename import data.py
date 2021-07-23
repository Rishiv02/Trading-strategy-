import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
ticker = ["ESCORTS.NS" ,"TATAMOTORS.NS" ,"M&M.NS" ,"MARUTI.NS"]
stock = yf.download(ticker, start ="2016-01-01" , end = "2021-05-05")
stock.to_csv("stock.csv")
stocks = pd.read_csv("stock.csv", header = [0,1], index_col = [0], parse_dates = [0])
close = stocks.loc[:,"Close"].copy()
print(stocks.head())
plt.style.use("seaborn")
close.plot(figsize = (15,8), fontsize =13)
plt.legend(fontsize =13)
plt.show()




