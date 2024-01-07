from functools import partial


# def mod_checker(x, mod=0):
#     return partial(lambda y: not not y % x == mod)        # не принимает решение

# mod_checker = lambda x, mod=0: partial(lambda y: not not y % x == mod)    # не принимает решение

# mod_checker = partial(lambda x, mod=0: lambda y: not not y % x == mod)  # не принимает решение

mod_checker = lambda x, mod=0: lambda y: not not y % x == mod   # принимает решение


if __name__ == '__main__':
    mod_3 = mod_checker(3)

    print(mod_3(3))  # True
    print(mod_3(4))  # False

    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4))  # True
