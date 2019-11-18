from functions import *


def read(formula):
    if (not isinstance(formula, str)) or len(formula) == 0 or formula.isspace():
        raise ValueError(f'{formula} is not of value string or is size 0')

    func, _ = _read(formula.replace(' ', ''))
    return func


def _read(formula):
    firstchar, formula = getfirstchar(formula)

    # No switches in Python :(
    if firstchar == 'x':
        before, formula = readuntil(formula, ',', ')')
        return VariableFunction(), formula
    elif firstchar.isnumeric():
        before, formula = readuntil(formula, ',', ')')
        num = firstchar + before
        if '.' in num:
            return RealNumberFunction(num), formula
        return NaturalNumberFunction(num), formula
    elif firstchar == 'n':
        num, formula = readuntil(formula[1:], ')', '.')
        return NaturalNumberFunction(num), formula
    elif firstchar == 'r':
        num, formula = readuntil(formula[1:], ')')
        return RealNumberFunction(num), formula
    elif firstchar == 'p':
        before, formula = readuntil(formula, ',', ')')
        return PiFunction(), formula
    elif firstchar == '+':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return SumFunction(firstFunc, secondFunc), formula
    elif firstchar == '-':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return DifferenceFunction(firstFunc, secondFunc), formula
    elif firstchar == '*':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return ProductFunction(firstFunc, secondFunc), formula
    elif firstchar == '/':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return QuotientFunction(firstFunc, secondFunc), formula
    elif firstchar == '^':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return PowerFunction(firstFunc, secondFunc), formula
    elif firstchar == 's':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return SineFunction(func), formula
    elif firstchar == 'c':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return CosineFunction(func), formula
    elif firstchar == 'e':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return ExponentFunction(func), formula
    elif firstchar == 'l':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return NaturalLogFunction(func), formula
    elif firstchar == '!':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return FactorialFunction(func), formula


def getfirstchar(f):
    first = f[:1]
    f = f[1:]
    return first, f


def readuntil(f, *until):
    for i, x in enumerate(f):
        for y in until:
            if x == y:
                return f[:i], f[i:]

    return f
