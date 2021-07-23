import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(index = [2016,2017,2018], columns = ["Price"], data = [100, 50,95])
sim_ret = df.pct_change().dropna()
log_ret = np.log(df/df.shift(1))
print(log_ret.dropna())