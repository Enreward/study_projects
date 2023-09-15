# -*- coding: UTF-8 -*-
import copy
from pprint import pprint
from collections import defaultdict


def get_input():
    list_input = []
    try:
        for _ in range(2):
            temp_input = []
            for _ in range(int(input())):
                str_input = str(input()).strip()
                if not str_input:
                    raise ValueError
                temp_input.append(str_input)
            list_input.append(temp_input)
        # list_input = [
        #     [
        #         'A: B C',
        #         'B: D',
        #         'C: D',
        #         'D: E',
        #         'E'
        #     ],
        #     [
        #         'E',
        #         'A',
        #         'B',
        #         'C',
        #         'D'
        #     ]
        # ]
        return list_input
    except ValueError:
        print('wrong input')


def parse_input(list_input):
    exceptions = defaultdict(lambda: list())
    for elem in list_input[0]:
        temp = list(map(str.strip, elem.split(':')))
        if len(temp) == 1:
            exceptions[temp[0]] = []
        else:
            clss, parents = temp
            parents = list(parents.split(' '))
            exceptions[clss] += parents
    check_list = list_input[-1]

    return exceptions, check_list


def create_generation_tree(classes):
    tree = defaultdict(lambda: set())
    for class_name, parents_names in classes.items():
        parents = parents_names.copy()
        for parent_name in parents:
            parents.extend(classes[parent_name])
        tree[class_name] = set(parents)
    return tree


def find_extra_ones(exceptions, check_list):
    extra_ones = []
    previous = []
    for class_name in check_list:
        if class_name in previous and class_name not in extra_ones:
            extra_ones.append(class_name)
            continue
        for parent in exceptions[class_name]:
            if parent in previous:
                if class_name not in extra_ones:
                    extra_ones.append(class_name)
        previous.append(class_name)

    return extra_ones


if __name__ == '__main__':
    list_input = get_input()
    exceptions, check_list = parse_input(list_input)
    exceptions = create_generation_tree(exceptions)
    result = find_extra_ones(exceptions, check_list)
    for r in result:
        print(r)
