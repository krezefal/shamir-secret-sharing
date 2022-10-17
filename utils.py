import argparse
from secrets import randbelow
import numpy as np

from consts import MODULO


class CapitalisedHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = 'Usage: '
        return super(CapitalisedHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)


def parse_args() -> tuple[int, int]:
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
    return args.threshold, args.number


def check_system_appropriateness(S, k, n: int):
    # assert MODULE is PRIME number to provide system reliability.
    assert MODULO > S, "Must be > S not to lose the secret. " \
                       "Otherwise, only the remainder of the number will be preserved."
    assert MODULO > n, "Must be > n to avoid shares repetitions."
    assert n >= k, "Must be >= k to be able to reassemble the secret."


def generate_polynomial(k, S: int) -> np.poly1d:
    random_coefficients = [(randbelow(MODULO - 1) + 1) for _ in range(k - 1)]
    polynomial = np.poly1d([*random_coefficients, S])
    return polynomial
