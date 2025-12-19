import yfinance as yf


def fetch_price_data(ticker:str, exchange:str, start:str=None, end:str=None):
    '''
    Docstring for fetch_price_data
    
    :param ticker: Symbol of the Asset you want to fetch the data for
    :type ticker: str
    :param exchange: Stock Exchange on which the asset is traded
    :type exchange: str
    :param start: Start date of the data you want to fetch
    :type start: str
    :param end: End data of the data you want to fetch
    :type end: str
    '''
    ticker_name = f'{ticker.upper()}.{exchange.upper()}'

    print(f'Fetching data for the following ticker {ticker_name}')  
    
    # Check if the stock is listed on the given stock exchange
    try:
        data = yf.Ticker(ticker_name)
    except Exception as e:
        raise RuntimeError(f'{ticker_name} might not exist') from e

    # The data would be download as a python dataframe
    ticker_data = yf.download(ticker_name,start= start, end = end, period="max", auto_adjust=False)
    print(ticker_data.head())
    # Manipulating the dataframe
    '''
    1.Keep only top header
    2.Name first column as Date
    3.Add Ticker Column
    '''
    ticker_data.columns = ticker_data.columns.get_level_values(0)
    ticker_data.index.name = None
    ticker_data.reset_index(inplace=True)
    ticker_data.insert(0,"Ticker",ticker.upper())
    ticker_data.rename(columns={"index":"Date"},inplace=True) # Renaming column to date
    
    print('Following are the details fo the downlaoded dataframe')
    print(ticker_data.head(3))
    print(ticker_data.info())

    file_name = ticker.upper()
    ticker_data.to_csv(f'{file_name}.csv',index=False)

def fetch_dividend_data(ticker:str, exchange:str, start:str=None, end:str=None):
    '''
    Docstring for fetch_price_data
    
    :param ticker: Symbol of the Asset you want to fetch the data for
    :type ticker: str
    :param exchange: Stock Exchange on which the asset is traded
    :type exchange: str
    :param start: Start date of the data you want to fetch
    :type start: str
    :param end: End data of the data you want to fetch
    :type end: str
    '''
    ticker_name = f'{ticker.upper()}.{exchange.upper()}'
    print(f'Fetching dividend data for the following ticker {ticker_name}')  

    div_data = yf.Ticker(ticker_name).dividends
    div_data = div_data.reset_index()
    div_data['Date'] = div_data['Date'].dt.date
    print(div_data.info())

    file_name = ticker.upper()
    div_data.to_csv(f'{file_name}_DIV.csv',index=False)

def fetch_split_data(ticker:str, exchange:str, start:str=None, end:str=None):
    '''
    Docstring for fetch_price_data
    
    :param ticker: Symbol of the Asset you want to fetch the data for
    :type ticker: str
    :param exchange: Stock Exchange on which the asset is traded
    :type exchange: str
    :param start: Start date of the data you want to fetch
    :type start: str
    :param end: End data of the data you want to fetch
    :type end: str
    '''
    ticker_name = f'{ticker.upper()}.{exchange.upper()}'
    print(f'Fetching dividend data for the following ticker {ticker_name}')  

    div_data = yf.Ticker(ticker_name).splits
    div_data = div_data.reset_index()
    div_data['Date'] = div_data['Date'].dt.date
    print(div_data.info())

    file_name = ticker.upper()
    div_data.to_csv(f'{file_name}_SPL.csv',index=False)

if __name__ == "__main__":
    fetch_price_data('vedl','ns')
    # fetch_dividend_data('vedl','ns')
    # fetch_split_data('vedl','ns')               