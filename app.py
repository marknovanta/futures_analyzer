import yfinance as yf
import pandas as pd

def print_info(ticker):
    for key, value in ticker.info.items():
        print(f'{key}: {value}')

def get_hist(ticker):
    # get last month data
    hist = ticker.history(period='1mo')
    hist.drop(hist.columns[[-1,-2]], axis=1, inplace=True)
    hist['Range'] = round(hist['High'] - hist['Low'], 2)
    hist['Low'] = round(hist['Low'], 2)
    hist['Close'] = round(hist['Close'], 2)
    #hist['Volume'] = hist.apply(lambda x: '{:,}'.format(round(x['Volume'])), axis=1)
    return hist

future = yf.Ticker('ES=F')

data = get_hist(future)

print()
print(data)

avg_range = data['Range'].mean()
avg_vol = data['Volume'].mean()

print()
print('LAST MONTH')
print(f'AVG Range: {round(avg_range, 2)}')
print(f'AVG Volume: {round(avg_vol):,}')
print()
