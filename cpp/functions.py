from abc import ABC, abstractmethod
import numpy as np


class BaseFunction(ABC):
    @abstractmethod
    def toString(self):
        return 'Base Class'

    @abstractmethod
    def evaluate(self, num):
        pass


class NaturalNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.int(num)

    def toString(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)


class RealNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.float(num)

    def toString(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)


class PiFunction(BaseFunction):
    def toString(self):
        return '\u03C0'

    def evaluate(self, num):
        return np.full_like(num, np.pi)


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
        return f'({self.firstFunction.toString()} + {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) + self.secondFunction.evaluate(num)


class DifferenceFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} - {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) - self.secondFunction.evaluate(num)


class ProductFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} * {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) * self.secondFunction.evaluate(num)


class QuotientFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} / {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) / self.secondFunction.evaluate(num)


class PowerFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} ^ {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) ** self.secondFunction.evaluate(num)


class SineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'sin({self.function.toString()})'

    def evaluate(self, num):
        return np.sin(self.function.evaluate(num))


class CosineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'cos({self.function.toString()})'

    def evaluate(self, num):
        return np.cos(self.function.evaluate(num))


class ExponentFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'(e ^ {self.function.toString()})'

    def evaluate(self, num):
        return np.exp(self.function.evaluate(num))


class NaturalLogFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'ln({self.function.toString()})'

    def evaluate(self, num):
        return np.log(self.function.evaluate(num))


class FactorialFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'{self.function.toString()}!'

    def evaluate(self, num):
        return np.factorial(self.function.evaluate(num))
