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

# PRINT STATS
print(f'AVG Range: {tick_round(avg_range)}')
print(f'AVG Volume: {round(avg_vol):,}')
print(f'AVG Upper move from open: {tick_round(avg_up_move)}')
print(f'AVG Lower move from open: {tick_round(avg_dwn_move)}')
print()
print(f'Max up move from open: {max_up}')
print(f'Max down move from open: {max_dwn}')

print('\nMOVES FROM OPEN TO HIGH:')
for key, value in ranges_up.items():
    # print label with value and visual
    print(f'{key:<6}: {value} | {round((value/days)*100, 2):>6}%', ('#'*(int(round((value/days)*100)))))

print('\nMOVES FROM OPEN TO LOW:')
for key, value in ranges_dwn.items():
    # print label with value and visual
    print(f'{key:<6}: {value} | {round((value/days)*100, 2):>6}%', ('#'*(int(round((value/days)*100)))))

# How many days moved up within 30pt?
print('\nHow many days moved up within 30pt?')
count = 0
for v in data['Open to Hi']:
    # 2pt of stop loss
    if v < 32:
        count +=1
print(f'{round((count/days)*100, 2)}%')

# How many days moved down within 30pt?
print('\nHow many days moved down within 30pt?')
count = 0
for v in data['Open to Lo']:
    # 2pt of stop loss
    if v < 32:
        count +=1
print(f'{round((count/days)*100, 2)}%')

print()
