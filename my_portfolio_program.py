from tabulate import tabulate
from tvDatafeed import TvDatafeed, Interval
import time
import pandas as pd
from datetime import date



tv = TvDatafeed()

#today_date = date.today()   # bydefault its today's date
today_date = '2024-05-22'  # this is custom date, uncomment this to use and comment above


data = pd.read_csv('portfolio_data.csv')
df = pd.DataFrame(data)

symbol_list = df.iloc[:, 0]
symbols = []
for i in symbol_list:
    symbols.append(i)

exchange_list = df.iloc[:, 1]
exchanges = []
for i in exchange_list:
    exchanges.append(i)

buy_prices_list = df.iloc[:, 2]
buy_prices = []
for i in buy_prices_list:
    buy_prices.append(i)

quantities_list = df.iloc[:, 3]
quantities = []
for i in quantities_list:
    quantities.append(i)

total_daily_pl = 0
overall_pl = 0
total_invested = 0

table_data = []


for i, symbol in enumerate(symbols):
    while True:
        try:
            stock_data = tv.get_hist(symbol=symbol, exchange=exchanges[i], interval=Interval.in_daily, n_bars=100)
            stock_data.index = stock_data.index.strftime('%Y-%m-%d')

            filtered_data = stock_data[stock_data.index == today_date]

            if not filtered_data.empty:
                stock_close_price = round(float(filtered_data['close'].iloc[0]), 2)

                # Fetch data for the previous trading day
                previous_trading_day_data = stock_data[stock_data.index < today_date].iloc[-1]
                yesterday_price = round(float(previous_trading_day_data['close']), 2)

                change_price = round(stock_close_price - yesterday_price, 2)
                change_percent = round(((stock_close_price - yesterday_price) / yesterday_price) * 100, 2)

                today_pl = quantities[i] * change_price
                total_daily_pl += today_pl

                total_pl = (stock_close_price - buy_prices[i]) * quantities[i]
                overall_pl += total_pl

                invested_value = buy_prices[i] * quantities[i]
                total_invested += invested_value

                stock_current_value = stock_close_price * quantities[i]

                table_data.append([symbol,  stock_close_price, change_price, f"{change_percent}%", today_pl, total_pl, invested_value, stock_current_value])
            else:
                print(f"Market is closed for {symbol} on the specified date: {today_date}")
                break

            break

        except Exception as e:
            print(f"Error occurred for {symbol}: {e}")
            print("Retrying...again...")
            time.sleep(2)

headers = ["Symbol", "Current Price", "Change Price", "Change %", "Daily P&L", "Total P&L", "Total Investment", "Current value"]


print(tabulate(table_data, headers=headers, tablefmt="grid"))
print('Total daily P&L for all symbols = ', round((total_daily_pl), 2))
print("Total Overall P&L = ", round((overall_pl), 2))
print("Total Investment = ", round((total_invested), 2))
print("Overall Current Value = ", round((total_invested + overall_pl), 2))
