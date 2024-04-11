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

def calc_ranges(data, direction):
    # define ranges
    # 0-5 | 5-10 | 10-15 | 15-20 | 20-25 | 25-30 | 30-35 | 35-40 | 40-45 | 45-50 | 50+
    ranges = {
        '0-5': 0,
        '5-10': 0,
        '10-15': 0,
        '15-20': 0,
        '20-25': 0,
        '25-30': 0,
        '30-35': 0,
        '35-40': 0,
        '40-45': 0,
        '45-50': 0,
        '50+': 0,
    }
    for r in data[f'Open to {direction}']:
        if r > 0 and r <= 5:
            ranges['0-5'] += 1
        elif r > 5 and r <= 10:
            ranges['5-10'] += 1
        elif r > 10 and r <= 15:
            ranges['10-15'] += 1
        elif r > 15 and r <= 20:
            ranges['15-20'] += 1
        elif r > 20 and r <= 25:
            ranges['20-25'] += 1
        elif r > 25 and r <= 30:
            ranges['25-30'] += 1
        elif r > 30 and r <= 35:
            ranges['30-35'] += 1
        elif r > 35 and r <= 40:
            ranges['35-40'] += 1
        elif r > 40 and r <= 45:
            ranges['40-45'] += 1
        elif r > 45 and r <= 50:
            ranges['45-50'] += 1
        elif r > 50:
            ranges['50+'] += 1

    return ranges