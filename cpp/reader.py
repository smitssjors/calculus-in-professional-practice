import functions


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
        return functions.VariableFunction(), formula
    elif firstchar.isnumeric():
        before, formula = readuntil(formula, ',', ')')
        num = firstchar + before
        if '.' in num:
            return functions.RealNumberFunction(num), formula
        return functions.NaturalNumberFunction(num), formula
    elif firstchar == 'n':
        num, formula = readuntil(formula[1:], ')', '.')
        return functions.NaturalNumberFunction(num), formula
    elif firstchar == 'r':
        num, formula = readuntil(formula[1:], ')')
        return functions.RealNumberFunction(num), formula
    elif firstchar == 'p':
        before, formula = readuntil(formula, ',', ')')
        return functions.PiFunction(), formula
    elif firstchar == '+':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return functions.SumFunction(firstFunc, secondFunc), formula
    elif firstchar == '-':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return functions.DifferenceFunction(firstFunc, secondFunc), formula
    elif firstchar == '*':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return functions.ProductFunction(firstFunc, secondFunc), formula
    elif firstchar == '/':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return functions.QuotientFunction(firstFunc, secondFunc), formula
    elif firstchar == '^':
        _, formula = readuntil(formula, '(')
        firstFunc, formula = _read(formula[1:])
        before, formula = readuntil(formula, ',')
        secondFunc, formula = _read(formula[1:])
        return functions.PowerFunction(firstFunc, secondFunc), formula
    elif firstchar == 's':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return functions.SineFunction(func), formula
    elif firstchar == 'c':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return functions.CosineFunction(func), formula
    elif firstchar == 'e':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return functions.ExponentFunction(func), formula
    elif firstchar == 'l':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return functions.NaturalLogFunction(func), formula
    elif firstchar == '!':
        _, formula = readuntil(formula, '(')
        func, formula = _read(formula[1:])
        return functions.FactorialFunction(func), formula


def getfirstchar(f):
    first = f[:1]
    f = f[1:]
    return first, f


def readuntil(f, *until):
    for i, x in enumerate(f):
        for y in until:
            if x == y:
                return f[:i], f[i:]

    return f, f
