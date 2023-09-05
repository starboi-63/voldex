import yfinance as yf
import pandas as pd
import os

# constants
timeout = 30
index_symbols = ["^IXIC", "^SPX", "^RUT", "^DJI"]

# download index data from Yahoo Finance
indexes = yf.download(index_symbols, period="5y", timeout=timeout)

# create .csv outfiles
for index in index_symbols:
    open = indexes["Open"][index]
    high = indexes["High"][index]
    low = indexes["Low"][index]
    close = indexes["Close"][index]
    df = pd.concat([open, high, low, close], axis=1)

    outfile_name = f"{index}.csv"
    outfile_path = os.path.join(os.getcwd(), "voldex", "data", "index_data", outfile_name)
    df.to_csv(outfile_path)
