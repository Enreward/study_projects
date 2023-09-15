from collections import defaultdict


def solution(permissions: list, actions:list) -> None:
    commands = {
         'read': 'R',
         'write': 'W',
         'execute': 'X',
     }
    permissions_dict = defaultdict(lambda: [])
    # распарсить permissions
    for s in permissions:
        tmp = s.split(' ')
        permissions_dict[tmp[0]] = tmp[1:]
    # распарсить actions и проверить условие выполнения команды
    for a in actions:
        command, file = a.split(' ')
        if commands[command] in permissions_dict[file]:
            print('OK')
        else:
            print('Access denied')


if __name__ == '__main__':
    permissions = []
    actions = []

    for _ in range(int(input())):
        permissions.append(input())

    for _ in range(int(input())):
        actions.append(input())

    # permissions = [
    #     'python.exe X',
    #     'book.txt R W',
    #     'notebook.exe R W X'
    # ]
    # actions = [
    #     'read python.exe',
    #     'read book.txt',
    #     'write notebook.exe',
    #     'execute notebook.exe',
    #     'write book.txt'
    # ]

    solution(permissions, actions)
