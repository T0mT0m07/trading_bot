import os

# Configuration settings for Alpaca API
ALPACA_API_KEY = os.environ.get('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.environ.get('ALPACA_SECRET_KEY')
ALPACA_BASE_URL = 'https://data.alpaca.markets' #or 'https://paper-api.alpaca.markets'  