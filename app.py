import yfinance as yf

def print_info(ticker):
    for key, value in ticker.info.items():
        print(f'{key}: {value}')

future = yf.Ticker('ES=F')

print_info(future)