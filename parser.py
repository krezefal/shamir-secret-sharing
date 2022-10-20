import argparse
from typing import Union


class CapitalisedHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = 'Usage: '
        return super(CapitalisedHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)


def parse_args() -> Union[tuple[int, int], int]:
    parser = argparse.ArgumentParser(add_help=False, formatter_class=CapitalisedHelpFormatter)
    parser._optionals.title = 'Options'

    if parser.prog == 'sss-split.py':
        parser.add_argument('-n', '--number',
                            help='Number of shares to be generated.',
                            required=True,
                            type=int)
    parser.add_argument('-t', '--threshold',
                        help='Minimum number of shares required to restore a secret secured by SSS.',
                        required=True,
                        type=int)
    parser.add_argument('-h', '--help',
                        help='Show this help message and exit.',
                        default=argparse.SUPPRESS,
                        action='help')

    args = parser.parse_args()

    if parser.prog == 'sss-split.py':
        return args.threshold, args.number
    else:
        return args.threshold
