import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
ticker = ["ESCORTS.NS" ,"TATAMOTORS.NS" ,"M&M.NS" ,"MARUTI.NS"]
tick = ["^NSEI"]
nse = yf.download(tick, start = "2018-01-01", end = "2021-05-05")
nse.to_csv("nse.csv")
NSE = pd.read_csv("nse.csv", parse_dates =["Date"], index_col = "Date", usecols = ["Date", "Close"])
stocks = yf.download(ticker, start = "2010-01-01", end = "2021-01-01")
stocks.to_csv("stocks.csv")
stocks = pd.read_csv("stocks.csv", header = [0,1], index_col = [0], parse_dates = [0]).Close
escorts = stocks.loc["2019-01-01" : "2021-01-01", "ESCORTS.NS"].to_frame()
maruti = stocks.loc["2020-01-01":"2020-12-01", "MARUTI.NS"].to_frame()
