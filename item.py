import logging
import locale

from parser import Parser

locale.setlocale(locale.LC_ALL, '')


class Item:
    def __init__(self, lookup_name):
        self.lookup_name = lookup_name
        self.full_name = ''
        self.region = []
        self.quality = []
        self.plus = []
        self.gem1 = []
        self.gem2 = []
        self.price = 0
        self.seller = ''
        self.position = ''

    def filter_item_listings(self, item_objects_list, item_filter):
        for item_object in item_objects_list:
            if item_filter.region is not None and item_object['ServerName'] not in item_filter.region:
                continue
            elif item_filter.quality is not None and item_object['QualityName'] not in item_filter.quality:
                continue
            elif item_filter.plus is not None and str(item_object['AdditionLevel']) not in item_filter.plus:
                continue
            elif item_filter.gem1 is not None and item_object['Gem1'] not in item_filter.gem1:
                continue
            elif item_filter.gem2 is not None and item_object['Gem2'] not in item_filter.gem2:
                continue
            elif item_filter.price is not None and item_object['Price'] > item_filter.price:
                continue
            else:
                self.full_name = item_object['AttributeName']
                self.region = item_object['ServerName']
                self.quality = item_object['QualityName']
                self.gem1 = item_object['Gem1']
                self.gem2 = item_object['Gem2']
                self.plus = item_object['AdditionLevel']
                self.seller = item_object['SellerName']
                self.position = f"{item_object['PositionX']},{item_object['PositionY']}"
                self.price = item_object['Price']
                self.log_details()

    def log_details(self):
        item_parser = Parser()

        details = f"{self.quality}{self.full_name}" \
                  f"{item_parser.parse_plus(self.plus)}" \
                  f"{item_parser.parse_gems(self.gem1, self.gem2)} " \
                  f"spotted on {self.region}! " \
                  f"Sold by {self.seller}({self.position}) " \
                  f"for {self.price:n} silver.".replace('None', '')

        logging.info(details)
