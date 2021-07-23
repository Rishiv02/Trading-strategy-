import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as py
from pandas_datareader import data
import cufflinks as cf
ticker = ["ESCORTS.NS" ,"TATAMOTORS.NS" ,"M&M.NS" ,"MARUTI.NS"]
df = data.DataReader(name = ticker, data_source = "yahoo",start ="2016-01-01" , end = "2021-05-05")
df.to_csv("stock.csv")
close = df.Close
print(close.head())
cf.set_config_file(offline = True)

df.loc["2016-01": , ("Close", "TATAMOTORS.NS")].iplot()
