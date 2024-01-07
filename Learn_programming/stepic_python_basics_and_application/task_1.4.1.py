# -*- coding: UTF-8 -*-
from pprint import pprint
from collections import defaultdict


def get_input():
    list_input = []
    try:
        count_rows = int(input())
        for _ in range(count_rows):
            str_input = str(input()).strip()
            if not str_input:
                raise ValueError
            list_input.append(str_input)
        # list_input = ['add global a',
        #               'create foo global',
        #               'add foo b',
        #               'get foo a',
        #               'get foo c',
        #               'create bar foo',
        #               'add bar a',
        #               'get bar a',
        #               'get bar b']
        return list_input
    except ValueError:
        print('wrong input')


def command_execution(list_input):
    scopes = {
        'global': {'parent': None,
                   'vars': set()}
        }
    result_get_cmd = []

    for s in list_input:
        command, arg1, arg2 = s.split(' ')
        if command == 'create':
            scopes[arg1] = {'parent': arg2,
                            'vars': set()}
        elif command == 'add':
            scopes[arg1]['vars'].add(arg2)
            pass
        elif command == 'get':
            ns = arg1
            while True:
                if ns is None:
                    break
                if arg2 not in scopes[ns]['vars']:
                    ns = scopes[ns]['parent']
                else:
                    break
            result_get_cmd.append(ns)
    return result_get_cmd


if __name__ == '__main__':
    list_input = get_input()
    result_get_cmd = command_execution(list_input)
    for r in result_get_cmd:
        print(r)
