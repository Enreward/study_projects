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
        #         'classA : classB classC classD classG classH',
        #         'classB : classC classE classG classH classK classL',
        #         'classC : classE classD classH classK classL',
        #         'classE : classD classF classK classL',
        #         'classD : classG classH',
        #         'classF : classK',
        #         'classG : classF', 'classH : classL',
        #         'classK : classH classL', 'classL'
        #      ],
        #     [
        #         'classK classD',
        #         'classD classA',
        #         'classG classD',
        #         'classH classA',
        #         'classE classE',
        #         'classH classG',
        #         'classE classL',
        #         'classB classD',
        #         'classD classL',
        #         'classD classG',
        #         'classD classE',
        #         'classA classF',
        #         'classA classC',
        #         'classK classA',
        #         'classA classH',
        #         'classK classD',
        #         'classH classB',
        #         'classK classB',
        #         'classD classL',
        #         'classG classG',
        #         'classA classH',
        #         'classK classL',
        #         'classG classE',
        #         'classB classA',
        #         'classC classK',
        #         'classK classL',
        #         'classC classL',
        #         'classG classC',
        #         'classD classD',
        #         'classC classG',
        #         'classE classA',
        #         'classF classK',
        #         'classB classG',
        #         'classH classL',
        #         'classL classF',
        #         'classH classG',
        #         'classD classA',
        #         'classH classL'
        #     ]
        # ]

        return list_input
    except ValueError:
        print('wrong input')


def parse_input(list_input):
    classes = defaultdict(lambda: list())
    queries = []
    for elem in list_input[0]:
        temp = list(map(str.strip, elem.split(':')))
        if len(temp) == 1:
            classes[temp[0]] = temp
        else:
            clss, parents = temp
            parents = list(parents.split(' '))
            classes[clss] += parents

    for elem in list_input[1]:
        query = tuple(elem.split(' '))
        queries.append(query)
        # if query[0] == query[1] and query[0] not in classes:
        #     classes[query[0]].append(query[0])

    return classes, queries


def create_parents_tree(classes):
    tree = classes.copy()

    for child, parents in classes.items():
        tree[child].append(child)
        for parent in parents:
            if parent in classes:
                for grand_parent in classes[parent]:
                    if grand_parent not in classes[child]:
                        classes[child].append(grand_parent)
    return tree


def query_execution(query, classes):
    try:
        if query[0] in classes[query[1]]:
            return 'Yes'
        else:
            return 'No'
    except KeyError:
        return 'No'


if __name__ == '__main__':
    list_input = get_input()
    classes, queries = parse_input(list_input)
    parents_tree = create_parents_tree(classes)
    for query in queries:
        print(query_execution(query, parents_tree))
