import yfinance as yf
import pandas as pd
from helper import print_info, tick_round, get_hist, calc_ranges

future = yf.Ticker('ES=F')

data = get_hist(future)

print()
print(data)

# DATA EXTRACT
avg_range = data['Range'].mean()
avg_vol = data['Volume'].mean()
avg_up_move = data['Open to Hi'].mean()
avg_dwn_move = data['Open to Lo'].mean()

days = len(data)

max_up = data['Open to Hi'].max()
max_dwn = data['Open to Lo'].max()

ranges_up = calc_ranges(data, 'Hi')
ranges_dwn = calc_ranges(data, 'Lo')


print()
# open is at midnight

print(f'AVG Range: {tick_round(avg_range)}')
print(f'AVG Volume: {round(avg_vol):,}')
print(f'AVG Upper move from open: {tick_round(avg_up_move)}')
print(f'AVG Lower move from open: {tick_round(avg_dwn_move)}')
print()
print(f'Max up move from open: {max_up}')
print(f'Max down move from open: {max_dwn}')

print('\nMOVES FROM OPEN TO HIGH:')
for key, value in ranges_up.items():
    print(f'{key}: {round((value/days)*100, 2)}%')

print('\nMOVES FROM OPEN TO LOW:')
for key, value in ranges_dwn.items():
    print(f'{key}: {round((value/days)*100, 2)}%')

print()
