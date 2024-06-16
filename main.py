from alpaca_connection import connect_to_alpaca
import strategy

def main():
    api = connect_to_alpaca()

    # Define the symbol for trading
    symbol = 'AAPL'

    # Execute the strategy
    order = strategy.example_strategy(api, symbol, 10)

    # Optional: print or log the trade confirmation
    print(order)

if __name__ == "__main__":
    main()
