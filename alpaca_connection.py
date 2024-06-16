import alpaca_trade_api as tradeapi
import config

def connect_to_alpaca():
    """
    Establishes a connection to Alpaca using the API key and secret.
    """
    api = tradeapi.REST(
        config.ALPACA_API_KEY,
        config.ALPACA_SECRET_KEY,
        config.ALPACA_BASE_URL
    )
    return api
