import itertools
def primes():
    pass


if __name__ == '__main__':
    print(list(itertools.takewhile(lambda x: x <= 31, primes())))