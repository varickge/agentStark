import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Fetch the Bitcoin price data
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {
    'vs_currency': 'usd',
    'days': '7',
    'interval': 'daily'
}
response = requests.get(url, params=params).json()
prices = response['prices']

dates = [datetime.utcfromtimestamp(price[0]/1000).date() for price in prices]
price_values = [price[1] for price in prices]

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(dates, price_values, marker='o')

# Format the plot
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.title('Bitcoin Price Distribution over the Last 7 Days')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('bitcoin_price_distribution.png')

# Show the plot
plt.show()
