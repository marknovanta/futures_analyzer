import yfinance as yf
import pandas as pd

def tick_round(x):
    return round(x*4)/4

def print_info(ticker):
    for key, value in ticker.info.items():
        print(f'{key}: {value}')

def get_hist(ticker):
    # get all available data
    hist = ticker.history(period='max')
    hist.drop(hist.columns[[-1,-2]], axis=1, inplace=True)
    hist['Range'] = round(hist['High'] - hist['Low'], 2)
    hist['Low'] = round(hist['Low'], 2)
    hist['Close'] = round(hist['Close'], 2)
    hist['Open to Hi'] = hist['High'] - hist['Open']
    hist['Open to Lo'] = hist['Open'] - hist['Low']
    #hist['Volume'] = hist.apply(lambda x: '{:,}'.format(round(x['Volume'])), axis=1)
    return hist