import yfinance as yf
import pandas as pd

def print_info(ticker):
    for key, value in ticker.info.items():
        print(f'{key}: {value}')

def tick_round(x):
    return round(x*4)/4

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

future = yf.Ticker('ES=F')

data = get_hist(future)

print()
print(data)

avg_range = data['Range'].mean()
avg_vol = data['Volume'].mean()
avg_up_move = data['Open to Hi'].mean()
avg_dwn_move = data['Open to Lo'].mean()

print()
# open is at midnight

print(f'AVG Range: {tick_round(avg_range)}')
print(f'AVG Volume: {round(avg_vol):,}')
print(f'AVG Upper move from open: {tick_round(avg_up_move)}')
print(f'AVG Lower move from open: {tick_round(avg_dwn_move)}')
print()
