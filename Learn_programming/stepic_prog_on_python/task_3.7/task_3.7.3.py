# -*- coding: UTF-8 -*-
from pprint import pprint


def get_input():
    list_input = []
    try:
        for _ in range(2):
            temp_list_input = []
            count_rows = int(input())
            for _ in range(count_rows):
                str_input = (str(input()).strip())
                if not str_input:
                    raise ValueError
                temp_list_input.append(str_input)
            list_input.append(temp_list_input)

        # list_input = [['champions',
        #                'we',
        #                'are',
        #                'Stepik'],
        #               ['We are the champignons',
        #                'We Are The Champions',
        #                'Stepic']]
        return list_input
    except ValueError as err:
        err.args = ['wrong input']
        raise err


def parse_input(list_input):
    vocabulary, text_list = list_input
    vocabulary = [s.lower() for s in vocabulary]
    text_list = [s.lower() for s in text_list]
    return vocabulary, text_list


def get_wrong_words(text_list, vocabulary):
    wrong_words = set()
    for s in text_list:
        for w in s.split(' '):
            w = ''.join(ch for ch in w if ch.isalnum())
            if w not in vocabulary:
                wrong_words.add(w)
    return wrong_words


def main():
    list_input = get_input()
    vocabulary, text_list = parse_input(list_input)
    print(*get_wrong_words(text_list, vocabulary), sep="\n")


main()
