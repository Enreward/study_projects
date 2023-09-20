class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина функций (pos >= neg)
        if pos >= neg:
            return True
        return False

    @staticmethod
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
        return False

    @staticmethod
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.result = []
        for i in iterable:
            pos = 0
            neg = 0
            for f in funcs:
                if f(i):
                    pos += 1
                else:
                    neg += 1
            if getattr(multifilter, judge.__func__.__name__)(pos, neg):
                self.result.append(i)

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return iter(self.result)
