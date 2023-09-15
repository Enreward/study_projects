# -*- coding: UTF-8 -*-
from collections import defaultdict

win_points = 3
dead_heat_points = 1
defeat_points = 0


def get_input():
    list_input = []
    try:
        count_rows = int(input())
        for _ in range(count_rows):
            str_input = str(input()).strip()
            if not str_input:
                raise ValueError
            list_input.append(str_input)
        # list_input = ['Спартак;9;Зенит;10',
        #               'Локомотив;12;Зенит;3',
        #               'Спартак;8;Локомотив;15']
        return list_input
    except ValueError:
        print('wrong input')


def parse_input(list_input: List[str]) -> dict[dict]:
    result = defaultdict(lambda: {'game_count': 0,
                                  'win_count': 0,
                                  'dead_heat_count': 0,
                                  'defeat_count': 0,
                                  'score': 0})
    for s in list_input:
        sep_str = list(s.split(';'))
        team_1 = sep_str[0]
        score_team_1 = int(sep_str[1])
        team_2 = sep_str[2]
        score_team_2 = int(sep_str[3])

        winner = ''
        loser = ''
        is_dead_heat = False

        if score_team_1 > score_team_2:
            winner = team_1
            loser = team_2
        elif score_team_1 < score_team_2:
            winner = team_2
            loser = team_1
        else:
            is_dead_heat = True

        if not is_dead_heat:
            result[winner]['game_count'] += 1
            result[winner]['win_count'] += 1
            result[winner]['dead_heat_count'] += 0
            result[winner]['defeat_count'] += 0
            result[winner]['score'] += win_points

            result[loser]['game_count'] += 1
            result[loser]['win_count'] += 0
            result[loser]['dead_heat_count'] += 0
            result[loser]['defeat_count'] += 1
            result[loser]['score'] += defeat_points
        else:
            result[team_1]['game_count'] += 1
            result[team_1]['win_count'] += 0
            result[team_1]['dead_heat_count'] += 1
            result[team_1]['defeat_count'] += 0
            result[team_1]['score'] += dead_heat_points

            result[team_2]['game_count'] += 1
            result[team_2]['win_count'] += 0
            result[team_2]['dead_heat_count'] += 1
            result[team_2]['defeat_count'] += 0
            result[team_2]['score'] += dead_heat_points
    return result


def get_pivot_table(data: dict[dict]) -> str:
    result = ''
    for k in data:
        result += f'{k}:{data[k]["game_count"]} {data[k]["win_count"]} ' \
                  f'{data[k]["dead_heat_count"]} {data[k]["defeat_count"]} {data[k]["score"]}\n'
    return result


def main():
    list_input = get_input()
    pivot_data = parse_input(list_input)
    pivot_table = get_pivot_table(pivot_data)
    print(pivot_table)


main()
