# -*- coding: UTF-8 -*-
import os
from statistics import mean
from collections import defaultdict
from pprint import pprint


def get_input(file_path):
    try:
        with open(file_path, 'r') as file:
            list_input = file.readlines()
        return list_input
    except (FileNotFoundError,  IsADirectoryError, PermissionError)as err:
        err.args = [f'wrong input, check the file {file_path}']
        raise err


def parse_input(list_input):
    result = defaultdict(lambda: [])
    for s in list_input:
        s = s.strip().split()
        result[int(s[0])].append(int(s[-1]))
    return result


def get_avg_height(data):
    avg_height = {1: '-',
                  2: '-',
                  3: '-',
                  4: '-',
                  5: '-',
                  6: '-',
                  7: '-',
                  8: '-',
                  9: '-',
                  10: '-',
                  11: '-'
                  }
    for grade, list_height in data.items():
        avg_height[grade] = mean(list_height)
    return avg_height


def write_file(data, file_path):
    write_data = [f'{key} {value}\n' for key, value in sorted(data.items())]
    with open(file_path, 'w') as file:
        file.writelines(write_data)


def main():
    file_path = os.path.abspath(os.path.join('data_task_3.7.5', 'dataset_3380_5.txt'))
    list_input = get_input(file_path)
    data = parse_input(list_input)
    avg_height = get_avg_height(data)
    answer_path = os.path.abspath(os.path.join('data_task_3.7.5', 'answer_task.3.7.5.txt'))
    write_file(avg_height, answer_path)
    pprint(answer_path)


main()
