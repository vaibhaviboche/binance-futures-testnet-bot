import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from bot.logging_config import logger


class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://demo-fapi.binance.com"
        self.api_key = api_key
        self.api_secret = api_secret

    def _sign(self, params):
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def post(self, endpoint, params):
        url = self.base_url + endpoint

        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        logger.info(f"API Request: POST {endpoint} | Params: {params}")

        try:
            response = requests.post(url, headers=headers, params=params, timeout=10)
            data = response.json()

            logger.info(f"API Response: {data}")

            if response.status_code != 200:
                raise Exception(data)

            return data

        except requests.exceptions.RequestException as error:
            logger.error(f"Network error: {error}")
            raise Exception("Network error. Please check internet or API URL.")

        except Exception as error:
            logger.error(f"API error: {error}")
            raise