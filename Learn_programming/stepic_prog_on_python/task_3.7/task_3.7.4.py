# -*- coding: UTF-8 -*-
from pprint import pprint


def get_input():
    list_input = []
    try:
        count_rows = int(input())
        for _ in range(count_rows):
            str_input = (str(input()).strip())
            if not str_input:
                raise ValueError
            list_input.append(str_input)

        # list_input = ['север 10',
        #               'запад 20',
        #               'юг 30',
        #               'восток 40']
        return list_input
    except ValueError as err:
        err.args = ['wrong input']
        raise err


def parse_input(list_input):
    route = [(s.split(' ')[0].lower(), int(s.split(' ')[1])) for s in list_input]
    return route


def get_finish_coordinates(route):
    x, y = 0, 0
    for direction, distance in route:
        if direction == 'север':
            y += distance
        elif direction == 'юг':
            y -= distance
        elif direction == 'восток':
            x += distance
        else:
            x -= distance
    return x, y


def main():
    list_input = get_input()
    route = parse_input(list_input)
    coordinates = get_finish_coordinates(route)
    print(f'{coordinates[0]} {coordinates[1]}')


main()
