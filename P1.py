## Na początku pobieramy potrzebne biblioteki
import sys
import math
from tkinter import *
admin = Tk()
admin.title("Pierwiastki trójmianu kwadratowego")
admin.geometry ('680x220')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats
from pandas import DataFrame
import statsmodels.api as sm
from pandas_datareader import data as wb
# Tworzymy zbiór ze skrótami giełdowymi spółek technologicznych, są to kolejno: Google, Netflix, Tesla, Amazon, Lockheed Martin, Boeing, Ford

## Za Pomocą API pobieramy dane spółek ze zbioru
print ("wpisz skrót pierwszej spółki")



def trojmian (a, b):

        a=input()
        b=input()



aLabel=Label(admin, text="Pierwsza spółka ", font='Cambria 18')
aLabel.place(x=10, y=20, width=200, height=40)


aEntry=Entry(admin, bd=1)
aEntry.place(x=210, y=20, width= 90, height=40)


bLabel=Label(admin, text="Druga spółka", font='Cambria 18')
bLabel.place(x=300, y=20, width=200, height=40)

bEntry=Entry(admin, bd=1)
bEntry.place(x=500, y=20, width= 90, height=40)


#sp1 = input()
#print ("Wpisz skrót drugiej spółki")
#sp2 = input()
#tickers= [sp1, sp2]
#dane_spolek = pd.DataFrame()
#for t in tickers:
    #dane_spolek[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']
#print("W tabeli znajdują się notowania wybranych przez Ciebie spółek, spójrz na dół tabeli, zobaczysz aktualne notowania, ceny wyrażanev są w USD")

tickers= [trojmian]
def account():
  dane_spolek = pd.DataFrame()
  for t in tickers:
    dane_spolek[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']




button= Button(text= "Sprawdź", command=account, font= 'Cambria 16')
button.place (x=90, y=80, width= 240, height=40)

button1= Button(text= "Koniec",command=quit,  font= 'Cambria 16')
button1.place (x=330, y=80, width= 240, height=40)

admin.mainloop()
print(dane_spolek)