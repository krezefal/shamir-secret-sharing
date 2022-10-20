from .consts import MAX_SECRET_LENGTH, X, Y, HEX, \
    MERSENNE_PRIME_64, MERSENNE_PRIME_128, MERSENNE_PRIME_256


def setup_mersenne_prime(secret_length: int) -> int:
    if 0 <= secret_length <= 64:
        return MERSENNE_PRIME_64
    elif 64 < secret_length <= 128:
        return MERSENNE_PRIME_128
    elif 128 < secret_length <= 256:
        return MERSENNE_PRIME_256
    else:
        raise ValueError('Secret is too long!')


def check_system_appropriateness(S, k, n, module: int):
    # assert MODULE is PRIME number to provide system reliability.
    assert S < module, "Must be < MODULO not to lose the secret. " \
                       "Otherwise, the secret cannot be reassembled."
    assert n < module, "Must be > n to avoid shares repetitions."
    assert k >= 2, "Must be > n to avoid shares repetitions."
    assert n >= k, "Must be >= k to be able to reassemble the secret."


def secret_to_int(secret: str) -> int:
    bytes_ = bytes(secret, 'ascii')
    int_ = int.from_bytes(bytes_, byteorder='big')
    return int_


def int_to_secret(int_: int) -> str:
    bytes_ = int_.to_bytes(MAX_SECRET_LENGTH, byteorder='big')
    secret = bytes_.decode("ascii")
    return secret


def points_to_shares(points: list[tuple[int, int]], mersenne_prime: int) -> list[str]:
    shares = []
    for point in points:
        shares.append(f'{point[X]}-{hex(mersenne_prime)[2:]}-{hex(point[Y])[2:]}')
    return shares


def shares_to_points(shares: list[str]) -> tuple[list[tuple[int, int]], int]:
    points = []
    mersenne_prime = None
    for share in shares:
        x, mersenne_prime, y = share.split('-')
        points.append((int(x), int(y, HEX)))
    return points, int(mersenne_prime, HEX)
