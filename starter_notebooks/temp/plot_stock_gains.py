# filename: plot_stock_gains.py
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define the stock symbols and the start date
stocks = ['TSLA', 'META']
start_date = '2024-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

# Fetch the stock data
data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

# Calculate YTD gains
ytd_gains = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100

# Plotting
plt.figure(figsize=(10, 6))
ytd_gains.plot(kind='bar', color=['blue', 'orange'])
plt.title('YTD Stock Price Gains for TSLA and META')
plt.ylabel('Percentage Gain (%)')
plt.xticks(rotation=0)
plt.grid(axis='y')

# Save the plot
plt.savefig('stock_gains.png')
plt.close()