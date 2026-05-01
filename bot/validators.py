def validate_order(symbol, side, order_type, quantity, price=None):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Symbol should be a USDT-M futures pair, for example BTCUSDT.")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

    return symbol, side, order_type