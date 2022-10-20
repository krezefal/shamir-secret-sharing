from .polynomial import generate_polynomial, calc_polynomial_value, lagrange_calc_value
from .utils import setup_mersenne_prime, check_system_appropriateness, \
    secret_to_int, int_to_secret, points_to_shares, shares_to_points


def secret_to_shares(secret: str, k, n: int) -> list[str]:
    mersenne_prime = setup_mersenne_prime(len(secret))
    module = 2 ** mersenne_prime - 1

    S = secret_to_int(secret)
    check_system_appropriateness(S, k, n, module)
    polynomial = generate_polynomial(k - 1, S, module)

    points = []
    for x_i in range(1, n + 1):
        y_i = calc_polynomial_value(polynomial, x_i, module)
        points.append((x_i, y_i))

    shares = points_to_shares(points, mersenne_prime)
    return shares


def shares_to_secret(shares: list[str]) -> str:
    points, mersenne_prime = shares_to_points(shares)
    module = 2 ** mersenne_prime - 1
    S = lagrange_calc_value(0, points, module)

    secret = int_to_secret(S)
    return secret
