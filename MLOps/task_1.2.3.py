def solution(n: int) -> int:
    # put your python code here
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    print(solution(int(input())))
