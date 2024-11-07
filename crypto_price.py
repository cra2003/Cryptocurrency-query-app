# crypto_price.py
import requests
from cachetools import TTLCache

# Initialize a cache (you may adjust the size and TTL as needed)
cache = TTLCache(maxsize=100, ttl=300)

def get_crypto_price(crypto_id):
    # Check cache first
    if crypto_id in cache:
        print("cached")
        return cache[crypto_id]
    
    # Fetch the price from the API if not in cache
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': crypto_id, 'vs_currencies': 'usd'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data[crypto_id]['usd']
        cache[crypto_id] = price
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")
        return None
    except KeyError:
        print("Error: Unexpected data format in the API response.")
        return None
