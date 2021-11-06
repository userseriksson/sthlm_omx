import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io
#from utils import Symbols

start = datetime.datetime(2021,1,1)
end = datetime.datetime(2021,11,1)

Symbols = ['8TRA.ST',	'AAK.ST',	'ABB.ST']


def download_timeseries (start,end,Symbols):
    # create empty dataframe
    stock_final_v2 = pd.DataFrame()

    t0 = time.time()

    # create empty dataframe
    stock_final_v2 = pd.DataFrame()

    # iterate over each symbol
    for i in Symbols:

        # print the symbol which is being downloaded
        print( str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)

        try:
            # download the stock price
            stock = []
            stock = yf.download(i,start=start, end=end, progress=False)

            # append the individual stock prices
            if len(stock) == 0:
                None
            else:
                stock['Name']=i
                stock_final_v2 = stock_final_v2.append(stock,sort=False)
        except Exception:
            None

    t1 = time.time()

    total = t1-t0

    print(stock_final_v2.head(10))

#stock_final_v2.to_csv('/Users/joeriksson/Desktop/python_data/stock_swe_20211106.plk')

download_timeseries(start,end,Symbols) 
