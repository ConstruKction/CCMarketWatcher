import json
import logging

import requests

MARKET_API_URL = "https://conqueronline.net/Community/GetItems"


class MarketRequest:
    @staticmethod
    def get_json():
        response_json = json.loads(requests.get(MARKET_API_URL).text)
        if 'html' in response_json:
            logging.critical("No API response!")
            return

        return response_json
