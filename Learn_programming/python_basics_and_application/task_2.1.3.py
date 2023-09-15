class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, __object) -> None:
        if __object > 0:
            super(PositiveList, self).append(__object)
        else:
            raise NonPositiveError


if __name__ == '__main__':
    pos_list = PositiveList()
    while True:
        try:
            pos_list.append(int(input("Enter number: ")))
        except NonPositiveError:
            print('Try again.')
            continue
        except KeyboardInterrupt:
            print(pos_list)
            break
