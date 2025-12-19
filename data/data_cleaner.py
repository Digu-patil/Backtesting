import yfinance as yf

div_data = yf.Ticker('VEDL.NS').dividends
div_data = div_data.reset_index()
div_data['Date'] = div_data['Date'].dt.date
print(div_data.head())
print(div_data.info())
