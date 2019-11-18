from abc import ABC, abstractmethod
import numpy as np


class BaseFunction(ABC):
    @abstractmethod
    def toString(self):
        return 'Base Class'

    @abstractmethod
    def evaluate(self, num):
        pass

    @abstractmethod
    def __str__(self):
        return self.toString()


class NaturalNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.int(num)

    def toString(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)

    def __str__(self):
        return self.toString()


class RealNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.float(num)

    def toString(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)

    def __str__(self):
        return self.toString()


class PiFunction(BaseFunction):
    def toString(self):
        return '\u03C0'

    def evaluate(self, num):
        return np.full_like(num, np.pi)

    def __str__(self):
        return self.toString()


class VariableFunction(BaseFunction):
    def toString(self):
        return 'x'

    def evaluate(self, num):
        return num

    def __str__(self):
        return self.toString()


class SumFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} + {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) + self.secondFunction.evaluate(num)

    def __str__(self):
        return self.toString()


class DifferenceFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} - {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) - self.secondFunction.evaluate(num)

    def __str__(self):
        return self.toString()


class ProductFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} * {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) * self.secondFunction.evaluate(num)

    def __str__(self):
        return self.toString()


class QuotientFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} / {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) / self.secondFunction.evaluate(num)

    def __str__(self):
        return self.toString()


class PowerFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def toString(self):
        return f'({self.firstFunction.toString()} ^ {self.secondFunction.toString()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) ** self.secondFunction.evaluate(num)

    def __str__(self):
        return self.toString()


class SineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'sin({self.function.toString()})'

    def evaluate(self, num):
        return np.sin(self.function.evaluate(num))

    def __str__(self):
        return self.toString()


class CosineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'cos({self.function.toString()})'

    def evaluate(self, num):
        return np.cos(self.function.evaluate(num))

    def __str__(self):
        return self.toString()


class ExponentFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'(e ^ {self.function.toString()})'

    def evaluate(self, num):
        return np.exp(self.function.evaluate(num))

    def __str__(self):
        return self.toString()


class NaturalLogFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'ln({self.function.toString()})'

    def evaluate(self, num):
        return np.log(self.function.evaluate(num))

    def __str__(self):
        return self.toString()


class FactorialFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'{self.function.toString()}!'

    def evaluate(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return np.math.factorial(self.function.evaluate(num))

        temp = []
        for x in num:
            if x >= 0 and x.is_integer():
                temp.append(np.math.factorial(self.function.evaluate(int(x))))
            else:
                temp.append(np.nan)
        return np.array(temp)

    def __str__(self):
        return self.toString()
