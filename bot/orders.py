from bot.validators import validate_order


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        symbol, side, order_type = validate_order(
            symbol, side, order_type, quantity, price
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self.client.post("/fapi/v1/order", params)