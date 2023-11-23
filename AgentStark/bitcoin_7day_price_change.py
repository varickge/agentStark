import requests

# Define the API endpoint for Bitcoin's market data
api_endpoint = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily'

# Make a GET request to fetch the data
response = requests.get(api_endpoint)
response.raise_for_status()  # Raise an error for bad http status codes

# Parse the JSON response to extract the price data
price_data = response.json().get('prices', [])

# Calculate 7-day price change
if len(price_data) >= 2:
    start_price = price_data[0][1]  # First day's price
    end_price = price_data[-1][1]  # Last day's price
    price_change = end_price - start_price
    price_change_percentage = (price_change / start_price) * 100
    print(f'Bitcoin 7-day price change: ${price_change:.2f} USD ({price_change_percentage:.2f}%)')
else:
    print('Not enough data to calculate the 7-day price change.')
