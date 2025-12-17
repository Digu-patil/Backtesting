import yfinance as yf

ticker = input("Please enter the Ticker Name : ")
exchange = input("Please enter the Stock Exchange : ")
ticker_name = f'{ticker.upper()}.{exchange.upper()}'

print(f'Fetching data for the following ticker {ticker_name}')
# Check if the stock is listed on the given stock exchange
try:
    data = yf.Ticker(ticker_name)
except Exception as e:
    raise RuntimeError(f'{ticker_name} might not exist') from e

data_history = data.history(period ="max")
print(data_history.index.min())

underlying_data = yf.download(ticker_name,period="max")
underlying_data.to_csv(f'{ticker.upper()}.csv')