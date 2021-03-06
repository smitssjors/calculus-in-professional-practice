from abc import ABC, abstractmethod

import graphviz as gv
import numpy as np


class BaseFunction(ABC):
    @abstractmethod
    def to_string(self):
        return 'Base Class'

    @abstractmethod
    def evaluate(self, num):
        pass

    @abstractmethod
    def __str__(self):
        return self.to_string()

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def create_graph(self):
        pass

    @abstractmethod
    def to_graph(self, index, dot):
        pass

    @abstractmethod
    def analytical_derivative(self):
        pass

    @abstractmethod
    def newton_derivative(self, x, h=0.001):
        pass

    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def riemann_integral(self, x1, x2, interval=0.001):
        pass


class NaturalNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.int(num)

    def to_string(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return NaturalNumberFunction(self.number)

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        dot.node(str(index), str(self.number))
        index += 1
        return index, dot

    def analytical_derivative(self):
        return NaturalNumberFunction(0)

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        return self.copy()

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class RealNumberFunction(BaseFunction):
    def __init__(self, num):
        self.number = np.float(num)

    def to_string(self):
        return f'{self.number}'

    def evaluate(self, num):
        return np.full_like(num, self.number)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return RealNumberFunction(self.number)

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        dot.node(str(index), str(self.number))
        index += 1
        return index, dot

    def analytical_derivative(self):
        return RealNumberFunction(0)

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        return self.copy()

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class PiFunction(BaseFunction):
    def to_string(self):
        return '\u03C0'

    def evaluate(self, num):
        return np.full_like(num, np.pi)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return PiFunction()

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        dot.node(str(index), '\u03C0')
        index += 1
        return index, dot

    def analytical_derivative(self):
        return RealNumberFunction(0)

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        return self.copy()

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class VariableFunction(BaseFunction):
    def to_string(self):
        return 'x'

    def evaluate(self, num):
        return num

    def __str__(self):
        return self.to_string()

    def copy(self):
        return VariableFunction()

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        dot.node(str(index), 'x')
        index += 1
        return index, dot

    def analytical_derivative(self):
        return NaturalNumberFunction(1)

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        return self.copy()

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class SumFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def to_string(self):
        return f'({self.firstFunction.to_string()} + {self.secondFunction.to_string()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) + self.secondFunction.evaluate(num)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return SumFunction(self.firstFunction.copy(), self.secondFunction.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), '+')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.to_graph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return SumFunction(self.firstFunction.analytical_derivative(), self.secondFunction.analytical_derivative())

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_first_func = self.firstFunction.simplify()
        simplified_second_func = self.secondFunction.simplify()

        if are_numbers(simplified_first_func, simplified_second_func):
            return RealNumberFunction(simplified_first_func.number + simplified_second_func.number)
        if has_num(simplified_first_func, 0):
            return simplified_second_func
        if has_num(simplified_second_func, 0):
            return simplified_first_func
        return SumFunction(simplified_first_func, simplified_second_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class DifferenceFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def to_string(self):
        return f'({self.firstFunction.to_string()} - {self.secondFunction.to_string()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) - self.secondFunction.evaluate(num)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return DifferenceFunction(self.firstFunction.copy(), self.secondFunction.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), '-')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.to_graph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return DifferenceFunction(
            self.firstFunction.analytical_derivative(),
            self.secondFunction.analytical_derivative()
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_first_func = self.firstFunction.simplify()
        simplified_second_func = self.secondFunction.simplify()

        if are_numbers(simplified_first_func, simplified_second_func):
            return RealNumberFunction(simplified_first_func.number - simplified_second_func.number)

        return DifferenceFunction(simplified_first_func, simplified_second_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class ProductFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def to_string(self):
        return f'({self.firstFunction.to_string()} * {self.secondFunction.to_string()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) * self.secondFunction.evaluate(num)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return ProductFunction(self.firstFunction.copy(), self.secondFunction.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), '*')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.to_graph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return SumFunction(
            ProductFunction(
                self.firstFunction.analytical_derivative(),
                self.secondFunction.copy()
            ),
            ProductFunction(
                self.firstFunction.copy(),
                self.secondFunction.analytical_derivative()
            )
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_first_func = self.firstFunction.simplify()
        simplified_second_func = self.secondFunction.simplify()

        if are_numbers(simplified_first_func, simplified_second_func):
            return RealNumberFunction(simplified_first_func.number * simplified_second_func.number)
        if has_num(simplified_first_func, 0) or has_num(simplified_second_func, 0):
            return RealNumberFunction(0)
        if has_num(simplified_first_func, 1):
            return simplified_second_func
        if has_num(simplified_second_func, 1):
            return simplified_first_func
        return ProductFunction(simplified_first_func, simplified_second_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class QuotientFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def to_string(self):
        return f'({self.firstFunction.to_string()} / {self.secondFunction.to_string()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) / self.secondFunction.evaluate(num)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return QuotientFunction(self.firstFunction.copy(), self.secondFunction.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), '/')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.to_graph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return QuotientFunction(
            DifferenceFunction(
                ProductFunction(
                    self.firstFunction.analytical_derivative(),
                    self.secondFunction.copy()
                ),
                ProductFunction(
                    self.firstFunction.copy(),
                    self.secondFunction.analytical_derivative()
                )
            ),
            PowerFunction(
                self.secondFunction.copy(),
                NaturalNumberFunction(2)
            )
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_first_func = self.firstFunction.simplify()
        simplified_second_func = self.secondFunction.simplify()

        if are_numbers(simplified_first_func, simplified_second_func):
            return RealNumberFunction(simplified_first_func.number / simplified_second_func.number)
        if has_num(simplified_second_func, 1):
            return simplified_first_func

        return QuotientFunction(simplified_first_func, simplified_second_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class PowerFunction(BaseFunction):
    def __init__(self, firstFun, secondFun):
        self.firstFunction = firstFun
        self.secondFunction = secondFun

    def to_string(self):
        return f'({self.firstFunction.to_string()} ^ {self.secondFunction.to_string()})'

    def evaluate(self, num):
        return self.firstFunction.evaluate(num) ** self.secondFunction.evaluate(num)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return PowerFunction(self.firstFunction.copy(), self.secondFunction.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), '^')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.firstFunction.to_graph(index, dot)
        dot.edge(str(tempindex), str(index))
        index, dot = self.secondFunction.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return ProductFunction(
            ProductFunction(
                self.secondFunction.copy(),
                PowerFunction(
                    self.firstFunction.copy(),
                    DifferenceFunction(
                        self.secondFunction.copy(),
                        NaturalNumberFunction(1)
                    )
                )
            ),
            self.firstFunction.analytical_derivative()
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_first_func = self.firstFunction.simplify()
        simplified_second_func = self.secondFunction.simplify()

        if are_numbers(simplified_first_func, simplified_second_func):
            return RealNumberFunction(simplified_first_func.number ** simplified_second_func.number)
        if has_num(simplified_second_func, 1):
            return simplified_first_func
        if has_num(simplified_second_func, 0):
            return RealNumberFunction(1)
        return PowerFunction(simplified_first_func, simplified_second_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class SineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def to_string(self):
        return f'sin({self.function.to_string()})'

    def evaluate(self, num):
        return np.sin(self.function.evaluate(num))

    def __str__(self):
        return self.to_string()

    def copy(self):
        return SineFunction(self.function.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'sin')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return ProductFunction(
            CosineFunction(
                self.function.copy()
            ),
            self.function.analytical_derivative()
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_func = self.function.simplify()

        if has_num(simplified_func, 0):
            return RealNumberFunction(0)

        return SineFunction(simplified_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class CosineFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def to_string(self):
        return f'cos({self.function.to_string()})'

    def evaluate(self, num):
        return np.cos(self.function.evaluate(num))

    def __str__(self):
        return self.to_string()

    def copy(self):
        return CosineFunction(self.function.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'cos')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return ProductFunction(
            DifferenceFunction(
                NaturalNumberFunction(0),
                SineFunction(self.function.copy())
            ),
            self.function.analytical_derivative()
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_func = self.function.simplify()

        if has_num(simplified_func, 0):
            return RealNumberFunction(1)

        return CosineFunction(simplified_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class ExponentFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def to_string(self):
        return f'(e ^ {self.function.to_string()})'

    def evaluate(self, num):
        return np.exp(self.function.evaluate(num))

    def __str__(self):
        return self.to_string()

    def copy(self):
        return ExponentFunction(self.function.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'e^')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return ProductFunction(
            self.copy(),
            self.function.analytical_derivative()
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_func = self.function.simplify()

        if has_num(simplified_func, 0):
            return RealNumberFunction(1)
        if is_log(simplified_func):
            return simplified_func.function.copy()
        return ExponentFunction(simplified_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class NaturalLogFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def to_string(self):
        return f'ln({self.function.to_string()})'

    def evaluate(self, num):
        return np.log(self.function.evaluate(num))

    def __str__(self):
        return self.to_string()

    def copy(self):
        return NaturalLogFunction(self.function.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), 'ln')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return ProductFunction(
            QuotientFunction(
                NaturalNumberFunction(1),
                self.function.copy()
            ),
            self.function.analytical_derivative()
        )

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        simplified_func = self.function.simplify()

        if has_num(simplified_func, 1):
            return RealNumberFunction(0)
        return NaturalLogFunction(simplified_func)

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


class FactorialFunction(BaseFunction):
    def __init__(self, fun):
        self.function = fun

    def to_string(self):
        return f'{self.function.to_string()}!'

    def evaluate(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return np.math.factorial(self.function.evaluate(num))

        temp = []
        for x in num:
            temp.append(np.math.factorial(self.function.evaluate(int(x))))

        return np.array(temp)

    def __str__(self):
        return self.to_string()

    def copy(self):
        return FactorialFunction(self.function.copy())

    def create_graph(self):
        dot = gv.Graph(name='calc')
        index, dot = self.to_graph(1, dot)
        dot.render('calc.dot')
        return 'graph.png'

    def to_graph(self, index, dot):
        tempindex = index
        dot.node(str(index), '!')
        index += 1
        dot.edge(str(tempindex), str(index))
        index, dot = self.function.to_graph(index, dot)
        return index, dot

    def analytical_derivative(self):
        return RealNumberFunction(0)

    def newton_derivative(self, x, h=0.001):
        return (self.evaluate(x + h) - self.evaluate(x)) / h

    def simplify(self):
        return FactorialFunction(self.function.simplify())

    def riemann_integral(self, x1, x2, interval=0.001):
        x = np.arange(x1, x2, interval)
        y = self.evaluate(x)
        ans = np.sum(y) * interval
        return x, y, ans


def are_numbers(first, second):
    return is_number(first) and is_number(second)


def is_number(func):
    func_type = type(func)
    return (func_type is NaturalNumberFunction) or (func_type is RealNumberFunction)


def is_variable(func):
    return type(func) is VariableFunction


def has_num(func, num):
    if not is_number(func):
        return False
    return func.number == num


def is_pi(func):
    return isinstance(func, PiFunction)


def is_log(func):
    return isinstance(func, NaturalLogFunction)


def taylor_analytical(function, n=8, a=0.):
    if n == 0:
        return function

    derivative = function.analytical_derivative().simplify()
    taylor_functions = [taylorify(derivative, 1, a)]
    for i in range(n - 1):
        derivative = derivative.analytical_derivative().simplify()
        taylor_functions.append(taylorify(derivative, i + 2, a))

    return SumFunction(RealNumberFunction(function.evaluate(a)), sum_all(taylor_functions)).simplify()


def taylor_newton(function, x, n=8, a=0):
    a = float(a)
    taylor_functions = [taylorify(RealNumberFunction(function.newton_derivative(a)), 1, a)]
    derivative = function.analytical_derivative().simplify()
    for i in range(2, n + 1):
        taylor_functions.append(taylorify(RealNumberFunction(derivative.newton_derivative(a)), i, a))
        derivative = derivative.analytical_derivative().simplify()

    s = SumFunction(RealNumberFunction(function.evaluate(a)), sum_all(taylor_functions)).simplify()
    print(s)
    return s.evaluate(x)


def sum_all(functions):
    if len(functions) == 1:
        return functions[0]

    return SumFunction(functions[0], sum_all(functions[1:]))


def taylorify(function, n, a):
    return ProductFunction(
        QuotientFunction(
            RealNumberFunction(function.evaluate(a)),
            FactorialFunction(
                NaturalNumberFunction(n)
            )
        ),
        PowerFunction(
            DifferenceFunction(
                VariableFunction(),
                RealNumberFunction(a)
            ),
            NaturalNumberFunction(n)
        )
    )


if __name__ == '__main__':
    sin = SineFunction(VariableFunction())
    print(taylor_analytical(sin))
    taylor_newton(sin, np.arange(-5, 5, 0.01))
