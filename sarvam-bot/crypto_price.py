# crypto_price.py
import requests
import redis
import json
from datetime import timedelta

# Initialize Redis client (connect to Redis server on localhost:6379 by default)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

CACHE_TTL = 300

def get_crypto_price(crypto_id):
    # Check if the price is already cached in Redis
    cached_price = redis_client.get(crypto_id)
    if cached_price:
        print("cached")
        return float(cached_price)  

    
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': crypto_id, 'vs_currencies': 'usd'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data[crypto_id]['usd']

        # Cache the price in Redis with a TTL
        redis_client.setex(crypto_id, timedelta(seconds=CACHE_TTL), price)
        
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")
        return None
    except KeyError:
        print("Error: Unexpected data format in the API response.")
        return None
