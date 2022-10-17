from secrets import randbelow
import numpy as np

import utils
from consts import MODULO


def main():
    k, n = utils.parse_args()
    secret = input('Enter the secret, at most 256 ASCII characters: ')
    secret_bytes = bytes(secret, 'ascii')
    S = int.from_bytes(secret_bytes, byteorder='big')

    utils.check_system_appropriateness(S, k, n)
    polynomial = utils.generate_polynomial(k, S)

    for x_i in range(1, n+1):
        y_i = hex(int(np.polyval(polynomial, x_i)) % MODULO)
        print(f'{x_i}-{y_i[2:]}')


if __name__ == "__main__":
    main()
