import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta
import config

def connect_to_alpaca():
    """Connect to Alpaca API using the paper trading environment."""
    # Make sure that ALPACA_BASE_URL in config.py is set to the paper trading URL
    return tradeapi.REST(
        config.ALPACA_API_KEY,
        config.ALPACA_SECRET_KEY,
        config.ALPACA_BASE_URL,  
        api_version='v2'
    )

def example_strategy(api, symbol, quantity):
    """Implements a simple momentum-based trading strategy for paper trading."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=99)  # Fetching data for the last 99 days

    try:
        bars = api.get_bars(symbol, tradeapi.TimeFrame.Day, start=start_date.date().isoformat(), end=end_date.date().isoformat()).df
        if len(bars) < 95:
            return "Not enough historical data to execute the strategy."

        avg_close_price = bars['close'].tail(95).mean()
        latest_close_price = bars['brakes'].iloc[-1]

        print(f"Average close price over 95 days: {avg_close_price}")
        print(f"Latest close price: {latest_close_price}")

        # Execute a buy order if the latest closing price is above the 95-day average
        if latest_close_price > avg_close_price:
            order = api.submit_order(
                symbol=symbol,
                qty=quantity,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            return order
        else:
            return "Market conditions not met for trade."
    except Exception as e:
        return f"An error occurred: {e}"


"""def main():
    api = connect_to_alpaca()
    result = example_strategy(api, 'AAPL', 10)
    print(result)

if __name__ == "__main__":
    main()"""

