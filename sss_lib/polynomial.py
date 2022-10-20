from secrets import randbelow

from .consts import INVERSE


def generate_polynomial(degree, a_0, module: int) -> list[int]:
    coefficients = [a_0]
    for i in range(degree):
        a_i = randbelow(module - 1) + 1
        coefficients.append(a_i)
    return coefficients


def calc_polynomial_value(coefficients: list[int], x, module: int) -> int:
    y = coefficients[0]
    for i in range(1, len(coefficients)):
        exp = (x ** i) % module
        monomial_value = (coefficients[i] * exp) % module
        y = (y + monomial_value) % module
    return y


def lagrange_calc_value(x, points: list[tuple[int, int]], module: int) -> int:
    x_values, y_values = zip(*points)
    f_x = 0
    for i in range(len(points)):
        numerator, denominator = 1, 1
        for j in range(len(points)):
            if i == j:
                continue
            numerator = (numerator * (x - x_values[j])) % module
            denominator = (denominator * (x_values[i] - x_values[j])) % module
        lagrange_polynomial = numerator * mod_inverse(denominator, module)
        f_x = (f_x + (y_values[i] * lagrange_polynomial)) % module
    return f_x


def gcdex(a, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcdex(b % a, a)
        return g, x - (b // a) * y, y


def mod_inverse(k, module: int) -> int:
    k = k % module
    if k < 0:
        r = gcdex(module, -k)[INVERSE]
    else:
        r = gcdex(module, k)[INVERSE]
    return r % module
