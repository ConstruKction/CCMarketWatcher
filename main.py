import argparse
import logging

from item import Item
from market_request import MarketRequest
from parser import Parser
from split_args import SplitArgs

MARKET_JSON = MarketRequest().get_json()

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

item_parser = Parser()


def create_item_object_list(items_string):
    item_object_list = []

    if items_string is None:
        return item_object_list

    for lookup_item_name in items_string:
        item_object_list.extend(filter_item_listings(get_item_group(lookup_item_name)))

    log_details(sorted(item_object_list,
                       key=lambda item: getattr(item, args.sort.replace('name', 'full_name')),
                       reverse=args.desc))


def log_details(item_list):
    for item in item_list:
        details = f"{item.quality}{item.full_name}" \
                  f"{item_parser.parse_plus(item.plus)}" \
                  f"{item_parser.abbreviate_gems(item.gem1, item.gem2)} " \
                  f"spotted on {item.region}! " \
                  f"Sold by {item.seller}({item.position}) " \
                  f"for {item.price:n} silver.".replace('None', '')

        logging.info(details)


def get_item_group(item_name):
    return [json_object for json_object in MARKET_JSON if item_name in json_object['AttributeName']]


def filter_item_listings(item_objects_list):
    item_list = []

    for item_object in item_objects_list:
        if args.region and item_object['ServerName'] not in args.region:
            continue
        elif args.quality and item_object['QualityName'] not in args.quality:
            continue
        elif args.plus and str(item_object['AdditionLevel']) not in args.plus:
            continue
        elif args.gem1 and item_object['Gem1'] not in item_parser.expand_gems(args.gem1):
            continue
        elif args.gem2 and item_object['Gem2'] not in item_parser.expand_gems(args.gem2):
            continue
        elif args.cost and item_object['Price'] > args.cost:
            continue
        else:
            return_item = Item()
            return_item.full_name = item_object['AttributeName']
            return_item.region = item_object['ServerName']
            return_item.quality = item_object['QualityName']
            return_item.gem1 = item_object['Gem1']
            return_item.gem2 = item_object['Gem2']
            return_item.plus = item_object['AdditionLevel']
            return_item.seller = item_object['SellerName']
            return_item.position = f"{item_object['PositionX']},{item_object['PositionY']}"
            return_item.price = item_object['Price']
            item_list.append(return_item)

    return item_list


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
                        help='1st socket gem(s) (e.g. sdg,srg)',
                        action=SplitArgs)
    parser.add_argument('-g2', '--gem2',
                        help='2nd socket gem(s) (e.g. nfg,rmg,spg)',
                        action=SplitArgs)
    parser.add_argument('-c', '--cost',
                        help='max price of an item',
                        type=int)
    parser.add_argument('-s', '--sort',
                        help='sort by (lowest number/alphabetically from top)',
                        choices=['region', 'name', 'quality', 'plus', 'gem1', 'gem2', 'seller', 'price'])
    parser.add_argument('-d', '--desc',
                        help='reverse sorting',
                        action='store_true')
    args = parser.parse_args()

    create_item_object_list(args.item)
