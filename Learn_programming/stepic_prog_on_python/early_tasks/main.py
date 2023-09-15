# coding: utf-8

if __name__ == '__main__':
    d = {'foo': 1, 'bar': 2, 'baz': 3}
    max_res = max(d, key=lambda x: sum(map(ord, x)))
    print(d[max_res])
