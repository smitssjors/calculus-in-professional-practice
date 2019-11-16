from abc import ABC, abstractmethod


class BaseFunction(ABC):

    @abstractmethod
    def toString(self):
        return 'Base Class'

    @abstractmethod
    def evaluate(self, num):
        pass


class NaturalNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = num

    def toString(self):
        return str(self.number)

    def evaluate(self, num):
        return self.number


class VariableFunction(BaseFunction):
    def toString(self):
        return 'x'

    def evaluate(self, num):
        return num


class SumFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return self.firstFunction.toString() + ' + ' + self.secondFunction.toString()

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) + self.secondFunction.evaluate(num)
