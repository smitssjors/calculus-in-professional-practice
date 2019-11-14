from . import BaseFunction


class SumFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return self.firstFunction.toString() + ' + ' + self.secondFunction.toString()

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) + self.secondFunction.evaluate(num)
