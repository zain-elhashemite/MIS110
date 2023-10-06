import yfinance as yf
import datetime
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

fname = input("Enter file name: ")
file = open(fname, "r")

startdate1 = str(input("Enter the starting date of the portfolio (YYYY/MM/DD): "))
enddate1 = str(input("Enter the ending date of the portfolio (YYYY/MM/DD): "))
format = '%Y/%m/%d'
startdate2 = datetime.datetime.strptime(startdate1,format)
enddate2 = datetime.datetime.strptime(enddate1,format)

mkt1 = []
mkt2 = []
portfolio = []

for i in file:
    pricelist = []

    tick, quant = i.split()
    stockinfo = yf.download(tick, startdate2, enddate2)
    pricelist.append(stockinfo['Adj Close'])

    df = pd.DataFrame(pricelist)
    df = df.transpose()
    df.rename(columns= {"Adj Close":"AdjClose"},inplace=True)

    final = df.at[df.index[-1],'AdjClose']
    mkt2.append(round(final*int(quant),2))

    starting = df.at[df.index[0], 'AdjClose']
    mkt1.append(round(starting*int(quant),2))

    ret = (final - starting)*int(quant)
    portfolio.append(round(ret,2))

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(tick)
    plt.plot(stockinfo['Adj Close'])
    plt.show()

total = 0
for i in portfolio:
    total += i

print(mkt1)
print(mkt2)
print("The total return of the portfolio is ","$",round(total,2))


#UNUSED CODE DISREGARD
#plt.hist(mkt1)
#plt.show()

    #PLACE IN FOR LOOP ABOVE AFTER DF.RENAME
    #df['Percent Change'] = df.AdjClose.pct_change()
    #df['Log Returns'] = np.log(df.AdjClose) - np.log(df.AdjClose.shift(1))
    #print(df)
