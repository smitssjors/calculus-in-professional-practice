from abc import ABC, abstractmethod
import numpy as np
import graphviz as gv


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

    @abstractmethod
    def creategraph(self):
        pass

    @abstractmethod
    def tograph(self, index, dot):
        pass


class NaturalNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.int(num)

    def toString(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        dot.node(str(index), str(self.number))
        index += 1
        return index, dot


class RealNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.float(num)

    def toString(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        dot.node(str(index), str(self.number))
        index += 1
        return index, dot


class PiFunction(BaseFunction):
    def toString(self):
        return '\u03C0'

    def evaluate(self, num):
        return np.full_like(num, np.pi)

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        dot.node(str(index), '\u03C0')
        index += 1
        return index, dot


class VariableFunction(BaseFunction):
    def toString(self):
        return 'x'

    def evaluate(self, num):
        return num

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        dot.node(str(index), 'x')
        index += 1
        return index, dot


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

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), '+')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.tograph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.tograph(index, dot)
        return index, dot


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

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), '-')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.tograph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.tograph(index, dot)
        return index, dot


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

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), '*')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.tograph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.tograph(index, dot)
        return index, dot


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

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), '/')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.tograph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.tograph(index, dot)
        return index, dot


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

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), '^')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.tograph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.tograph(index, dot)
        return index, dot


class SineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'sin({self.function.toString()})'

    def evaluate(self, num):
        return np.sin(self.function.evaluate(num))

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'sin')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.tograph(index, dot)
        return index, dot


class CosineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'cos({self.function.toString()})'

    def evaluate(self, num):
        return np.cos(self.function.evaluate(num))

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'cos')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.tograph(index, dot)
        return index, dot


class ExponentFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'(e ^ {self.function.toString()})'

    def evaluate(self, num):
        return np.exp(self.function.evaluate(num))

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'e^')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.tograph(index, dot)
        return index, dot


class NaturalLogFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def toString(self):
        return f'ln({self.function.toString()})'

    def evaluate(self, num):
        return np.log(self.function.evaluate(num))

    def __str__(self):
        return self.toString()

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'ln')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.tograph(index, dot)
        return index, dot


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

    def creategraph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.tograph(1, dot)
        print(dot.source)
        dot.render('calc.dot')
        return 'graph.png'

    def tograph(self, index, dot):
        tempindex = index
        dot.node(str(index), '!')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.tograph(index, dot)
        return index, dot
