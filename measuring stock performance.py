import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
ticker = ["ESCORTS.NS" ,"TATAMOTORS.NS" ,"M&M.NS" ,"MARUTI.NS"]
stock = yf.download(ticker, start ="2016-01-01" , end = "2021-05-05")
stock.to_csv("stock.csv")
stocks = pd.read_csv("stock.csv", header = [0,1], index_col = [0], parse_dates = [0])
close = stocks.loc[:,"Close"].copy()
escorts = close.loc[:,"ESCORTS.NS"].copy().to_frame()
print(escorts.head())
returns = close.pct_change().dropna() # dropna() helps to remove all variable which do not have any defined values and return the values without NaN
daily_mean = returns.mean()
print ( daily_mean)
daily_var = returns.var()
print(daily_var)
std_dev_daily = (daily_var)**0.5 # can also directly calculate using returns.std()
print(std_dev_daily)
yearly_mean_return = 238*daily_mean
print(yearly_mean_return)
avg_monthly_returns = 20*daily_mean
print(avg_monthly_returns)
print(returns.describe().T) # if we add .loc[" col1", "col2"] then we get only those 2 req columns
