import argparse
import logging

from item import Item
from item_filter import ItemFilter
from market_request import MarketRequest
from parser import Parser
from split_args import SplitArgs

MARKET_JSON = MarketRequest().get_json()

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def create_item_object_list(items_string, itemfilter):
    item_object_list = []
    if items_string is None:
        return item_object_list

    for lookup_item_name in items_string:
        item_object = Item(lookup_item_name)
        item_object.filter_item_listings(get_item_group(lookup_item_name), itemfilter)
        item_object_list.append(item_object)

    return item_object_list
#    return sorted(item_object_list, key=lambda item: getattr(item, args.sort))


def log_details(item_list):
    item_parser = Parser()

    for item in item_list:
        details = f"{item.quality}{item.full_name}" \
                  f"{item_parser.parse_plus(item.plus)}" \
                  f"{item_parser.parse_gems(item.gem1, item.gem2)} " \
                  f"spotted on {item.region}! " \
                  f"Sold by {item.seller}({item.position}) " \
                  f"for {item.price:n} silver.".replace('None', '')

        logging.info(details)


def get_item_group(item_name):
    return [json_object for json_object in MARKET_JSON if item_name in json_object['AttributeName']]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--region',
                        help='narrow down search to eu or us server',
                        action=SplitArgs)
    parser.add_argument('-i', '--item',
                        help='comma-separated item names (e.g. KylinGem, SoftBoots)',
                        action=SplitArgs)
    parser.add_argument('-q', '--quality',
                        help='comma-separated qualities (e.g. Elite,Super)',
                        action=SplitArgs)
    parser.add_argument('-p', '--plus',
                        help='comma-separated plus (e.g. 1,2,3)',
                        action=SplitArgs)
    parser.add_argument('-g1', '--gem1',
                        help='1st socket gem (e.g. SuperDragonGem,SuperPhoenixGem)',
                        action=SplitArgs)
    parser.add_argument('-g2', '--gem2',
                        help='2nd socket gem (e.g. NormalFuryGem,RefinedMoonGem)',
                        action=SplitArgs)
    parser.add_argument('-c', '--cost',
                        help='max cost of an item',
                        type=int)
    parser.add_argument('-s',
                        '--sort',
                        help='sort by (lowest number/alphabetically from top)',
                        choices=['name', 'quality', 'plus', 'gem1', 'gem2', 'seller', 'price'])
    args = parser.parse_args()

    item_filter = ItemFilter(args.region, args.quality, args.plus, args.gem1, args.gem2, args.cost)

    log_details(create_item_object_list(args.item, item_filter))
