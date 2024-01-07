class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.balance = 0
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.balance + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.balance += v
