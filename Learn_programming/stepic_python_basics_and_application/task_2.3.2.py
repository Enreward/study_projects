import itertools
from math import sqrt


def is_prime(n):
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True


def primes():
    yield 2
    yield 3
    i = 3
    while True:
        i += 2
        if (i > 10) and (i % 10 == 5):
            continue
        elif is_prime(i):
            yield i


if __name__ == '__main__':
    print(list(itertools.takewhile(lambda x: x <= 10000, primes())))
