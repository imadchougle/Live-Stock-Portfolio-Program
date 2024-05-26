# Live-Stock-Portfolio-Program

This Python program tracks the daily and overall performance of a stock portfolio. Using the tvDatafeed library, it fetches historical stock data from TradingView and calculates key metrics such as daily profit and loss (P&L), total P&L, and current investment value. The results are displayed in a neatly formatted table, making it easy for users to understand their portfolio's performance at a glance. This program will healp users who dont have stock broking api's to use in their programs but still are intrested in this. through the tvDatafeed we can get the full ohlcv data as well

## Personal Portfolio

Add your stock symbol with their exchange and buy prices and the quantity you bought in the csv

![image](https://github.com/imadchougle/Live-Stock-Portfolio-Program/assets/54437743/08f695f7-4aea-4a54-8193-0cad0478c37f)


## Your Personal portfolio realtime analytics

![image](https://github.com/imadchougle/Live-Stock-Portfolio-Program/assets/54437743/6a2ce189-5cff-4db2-b7b6-6405c8b6def3)


## Features

- Fetch Historical Stock Data: Retrieves daily stock prices from TradingView using the tvDatafeed library.
- Free and Easy to Use: The tvDatafeed library is free and does not require a connection to a real-time broker API.
- Customizable Date: Allows users to specify a custom date or use the current date by default.
- Calculate Daily P&L: Computes the profit or loss for each stock based on the change in closing prices.
- Calculate Total P&L: Computes the overall profit or loss for each stock from the purchase date to the specified date.
- Investment Analysis: Summarizes the total investment, daily P&L, and overall P&L.
- Tabular Output: Displays the results in a tabulated format for easy readability.

## Modules & Package installation

install all the dependencies before running the program

```
pip install tabulate
```

```
pip install --upgrade --no-cache-dir git+https://github.com/rongardF/tvdatafeed.git
```

```
pip install pandas
```
