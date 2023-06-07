import argparse
import logging
import pathlib


class SplitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        split_value = values.split(',')

        setattr(namespace, self.dest, split_value)

        if self.dest == 'cat' or self.dest == 'subcat':
            self.validate_categories(split_value)

    @staticmethod
    def validate_categories(values):
        with open(pathlib.Path('item_classes.txt')) as f:
            content = f.read().splitlines()

        for value in values:
            if value not in content:
                logging.error(f"Invalid (sub)category: {value}! Please refer to item_classes.txt")
