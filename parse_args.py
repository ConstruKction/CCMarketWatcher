import argparse
import logging
import pathlib
import re
import sys

LEGAL_CHARACTERS = re.compile('^[A-Za-z0-9,]*$')


class ParseArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not re.match(LEGAL_CHARACTERS, values):
            sys.exit(logging.critical("Only characters a-z and numbers 0-9 allowed without spaces!"))

        split_arg_values = values.split(',')

        setattr(namespace, self.dest, split_arg_values)

        if self.dest == 'cat' or self.dest == 'subcat':
            self.validate_categories(split_arg_values)

    @staticmethod
    def validate_categories(values):
        with open(pathlib.Path('item_classes.txt')) as f:
            content = f.read().splitlines()

        for value in values:
            if value not in content:
                logging.error(f"Invalid (sub)category: {value}! Please refer to item_classes.txt")
