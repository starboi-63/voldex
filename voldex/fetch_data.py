import yfinance as yf

timeout = 30
index_symbols = ["^IXIC", "^SPX", "^RUT", "^DJI"]

indexes = yf.download(index_symbols, period="5y", timeout=timeout)

print(indexes)