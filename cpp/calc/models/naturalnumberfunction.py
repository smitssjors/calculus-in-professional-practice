from . import BaseFunction


class NaturalNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = num

    def toString(self):
        return str(self.number)

    def evaluate(self, num):
        return self.number
