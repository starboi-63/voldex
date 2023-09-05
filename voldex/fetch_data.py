import yfinance as yf

# constants
timeout = 30
index_symbols = ["^IXIC", "^SPX", "^RUT", "^DJI"]

# download index data from Yahoo Finance
indexes = yf.download(index_symbols, period="5y", timeout=timeout)

print(indexes)