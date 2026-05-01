import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Simplified Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Example: BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", required=False, type=float)

    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("API key or secret is missing. Please add them in .env file.")
        return

    print("\nOrder Request Summary")
    print("---------------------")
    print(f"Symbol     : {args.symbol.upper()}")
    print(f"Side       : {args.side.upper()}")
    print(f"Order Type : {args.type.upper()}")
    print(f"Quantity   : {args.quantity}")

    if args.type.upper() == "LIMIT":
        print(f"Price      : {args.price}")

    try:
        client = BinanceFuturesClient(api_key, api_secret)
        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder Response")
        print("--------------")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

        print("\nSuccess: Order placed successfully.")

    except Exception as error:
        print("\nFailure: Order could not be placed.")
        print(f"Reason: {error}")


if __name__ == "__main__":
    main()