import yfinance as yf
import pandas as pd
from pandas import DataFrame
import os
from typing import List

# constants
timeout = 30

def download_ohlc(symbols: List[str]) -> DataFrame:
    # download index data from Yahoo Finance
    indexes = yf.download(symbols, period="5y", timeout=timeout)

    # create .csv outfiles
    for index in symbols:
        # extract data pertaining to current index from master DataFrame
        open = indexes["Open"][index]
        high = indexes["High"][index]
        low = indexes["Low"][index]
        close = indexes["Close"][index]
        df = pd.concat([open, high, low, close], axis=1)
        df.columns = ["Open", "High", "Low", "Close"]
        # save the DataFrame in .csv format
        outfile_name = f"{index}.csv"
        outfile_path = os.path.join(os.getcwd(), "voldex", "data", "index_data", outfile_name)
        df.to_csv(outfile_path)

    return indexes
