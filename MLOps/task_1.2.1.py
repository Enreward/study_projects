def get_input():
    list_input = list(map(int, input().split(' ')))
    # list_input = [8, 11, 2, -1, 42]
    return list_input


if __name__ == '__main__':
    list_input = get_input()
    list_input.sort()
    print(list_input[-1])
