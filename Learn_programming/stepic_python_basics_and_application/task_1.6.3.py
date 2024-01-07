import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, elem):
        self.log(elem)
        super(LoggableList, self).append(elem)


if __name__ == '__main__':
    test_list = LoggableList()
    test_list.append(123)
