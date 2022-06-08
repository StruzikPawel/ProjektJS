import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from pandas import DataFrame
import statsmodels.api as sm
from pandas_datareader import data as wb
from tkinter import Tk

print("Program do porównywania spółek giełdowych")

print("Podaj skrót pierwszej spółki:")
sp1= input()

print("Podaj skrót drugiej spółki")
sp2= input()


tickers = [sp1, sp2]

dane_spolek = pd.DataFrame()
for t in tickers:
    dane_spolek[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']

print(dane_spolek)

print("Stopy zwrotu dla wybranych spółek")

log_returns = np.log(1+ dane_spolek.pct_change())
print (log_returns.tail())

print("Wykres notowań wybranych spółek")


plt.show(dane_spolek)plt.title("Notowania")
plt.plot(dane_spolek)
plt.show()

plt.title("Dzienne stopy zwrotu")
plt.plot(log_returns)
plt.show()
