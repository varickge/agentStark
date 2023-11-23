import requests
import datetime

# Function to fetch the price of Bitcoin
def fetch_bitcoin_price(date=None):
    # CoinGecko API URL for Bitcoin
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '7',
        'interval': 'daily'
    }
    if date:
        params['date'] = date
    response = requests.get(url, params=params).json()
    prices = response['prices']
    return prices # Returning the array of prices

# Get current and 7 days ago prices
prices = fetch_bitcoin_price()
current_price = prices[-1][1] # Last price is the current price
seven_days_ago_price = prices[0][1] # First price is from 7 days ago

# Calculate the price change
price_change = current_price - seven_days_ago_price
print(f'The 7-day price change for Bitcoin is: ${price_change:.2f}')
