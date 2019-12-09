from cpp.functions import *
import numpy as np


class TestNaturalNumberFunction:
    def test_toStringInt(self):
        num = 5
        n = NaturalNumberFunction(num)
        assert n.to_string() == str(num)

    def test_toStringFloat(self):
        num = 5.76
        n = NaturalNumberFunction(num)
        assert n.to_string() == str(int(num))

    def test_evaluateInt(self):
        num = 4
        n = NaturalNumberFunction(num)
        assert n.evaluate(num) == num

    def test_evaluateFloat(self):
        num = 4.87
        n = NaturalNumberFunction(num)
        assert n.evaluate(num) == int(num)


class TestRealNumberFunction:
    def test_toStringFloat(self):
        num = 3.67
        n = RealNumberFunction(num)
        assert n.to_string() == str(num)

    def test_toStringInt(self):
        num = 3
        n = RealNumberFunction(num)
        assert n.to_string() == str(float(num))

    def test_evaluateFloat(self):
        num = 4.54
        n = RealNumberFunction(num)
        assert n.evaluate(num) == num

    def test_evaluateInt(self):
        num = 6
        n = RealNumberFunction(num)
        assert n.evaluate(num) == float(num)


class TestPiFunction:
    def test_toString(self):
        n = PiFunction()
        assert n.to_string() == '\u03C0'

    def test_evaluate(self):
        n = PiFunction()
        assert n.evaluate(1.) == np.pi


class TestVariableFunction:
    def test_toString(self):
        n = VariableFunction()
        assert n.to_string() == 'x'

    def test_evaluateInt(self):
        num = 4
        n = VariableFunction()
        assert n.evaluate(num) == num

    def test_evaluateFloat(self):
        num = 6.445
        n = VariableFunction()
        assert n.evaluate(num) == num


class TestSumFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = SumFunction(one, two)
        assert n.to_string() == '(1 + 2)'

    def test_evaluate(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = SumFunction(one, two)
        assert n.evaluate(5) == 1 + 2


class TestDifferenceFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = DifferenceFunction(one, two)
        assert n.to_string() == '(1 - 2)'

    def test_evaluate(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = DifferenceFunction(one, two)
        assert n.evaluate(5) == 1 - 2


class TestProductFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = ProductFunction(one, two)
        assert n.to_string() == '(1 * 2)'

    def test_evaluate(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = ProductFunction(one, two)
        assert n.evaluate(5) == 1 * 2


class TestQuotientFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = QuotientFunction(one, two)
        assert n.to_string() == '(1 / 2)'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        two = RealNumberFunction(2)
        n = QuotientFunction(one, two)
        assert n.evaluate(5) == 1 / 2


class TestPowerFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = PowerFunction(one, two)
        assert n.to_string() == '(1 ^ 2)'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = PowerFunction(one, two)
        assert n.evaluate(5) == 1 ** 2


class TestSineFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        n = SineFunction(one)
        assert n.to_string() == 'sin(1)'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        n = SineFunction(one)
        assert n.evaluate(5) == np.sin(1)


class TestCosineFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        n = CosineFunction(one)
        assert n.to_string() == 'cos(1)'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        n = CosineFunction(one)
        assert n.evaluate(5) == np.cos(1)


class TestExponentFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        n = ExponentFunction(one)
        assert n.to_string() == '(e ^ 1)'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        n = ExponentFunction(one)
        assert n.evaluate(5) == np.exp(1)


class TestNaturalLogFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        n = NaturalLogFunction(one)
        assert n.to_string() == 'ln(1)'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        n = NaturalLogFunction(one)
        assert n.evaluate(5) == np.log(1)


class TestFactorialFunction:
    def test_toString(self):
        one = NaturalNumberFunction(1)
        n = FactorialFunction(one)
        assert n.to_string() == '1!'

    def test_evaluate(self):
        one = RealNumberFunction(1)
        n = FactorialFunction(one)
        assert n.evaluate(5) == np.math.factorial(1)
