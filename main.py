
import pandas as pd
import yfinance as yf


tickers_doc = pd.read_excel('S&P500.xlsx')


tickers = tickers_doc['Тикер'].to_list()
tickers = [str(item) for item in tickers]



tickers_list = tickers_doc['Тикер'].to_list()
tickers_list = [str(item) for item in tickers_list]
# Import pandas

data = pd.DataFrame(columns=tickers_list)

# Fetch the data

for ticker in tickers_list:
    try:
        data[ticker] = yf.download(ticker,'2015-01-01', interval='1mo')['Adj Close']
    except (TypeError, ValueError):
        print(ticker)
# Print first 5 rows of the data
data.head()


writer = pd.ExcelWriter('S&P500.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file
data.to_excel(writer, 'Sheet1')

# Save the result
writer.save()