import yfinance as yf
import pandas as pd

def print_info(ticker):
    for key, value in ticker.info.items():
        print(f'{key}: {value}')

def get_hist(ticker):
    hist = ticker.history(period='1mo')
    hist.drop(hist.columns[[-1,-2]], axis=1, inplace=True)
    hist['Range'] = round(hist['High'] - hist['Low'], 2)
    hist['Low'] = round(hist['Low'], 2)
    hist['Close'] = round(hist['Close'], 2)
    hist['Volume'] = hist.apply(lambda x: '{:,}'.format(round(x['Volume'])), axis=1)
    return hist

future = yf.Ticker('ES=F')

data = get_hist(future)
print(data)