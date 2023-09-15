from math import ceil
from string import punctuation


def solution(a_string: str) -> bool:
    a_string = ''.join(ch for ch in a_string if ch.isalnum())
    l = len(a_string)
    if l > 1:
        half_index = ceil(l/2)
        if l % 2 == 0:
            head, tail = a_string[:half_index], a_string[half_index:]
        else:
            head, tail = a_string[:half_index], a_string[half_index - 1:]
        if head == tail[::-1]:
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    print(solution(input().strip().replace(' ', '').lower()))
