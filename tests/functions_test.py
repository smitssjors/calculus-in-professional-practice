from cpp.functions import NaturalNumberFunction, RealNumberFunction, PiFunction, VariableFunction, SumFunction
import numpy as np


class TestNaturalNumberFunction:
    def test_toStringInt(self):
        num = 5
        n = NaturalNumberFunction(num)
        assert n.toString() == str(num)

    def test_toStringFloat(self):
        num = 5.76
        n = NaturalNumberFunction(num)
        assert n.toString() == str(int(num))

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
        assert n.toString() == str(num)

    def test_toStringInt(self):
        num = 3
        n = RealNumberFunction(num)
        assert n.toString() == str(float(num))

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
        assert n.toString() == '\u03C0'

    def test_evaluate(self):
        n = PiFunction()
        assert n.evaluate(1.) == np.pi


class TestVariableFunction:
    def test_toString(self):
        n = VariableFunction()
        assert n.toString() == 'x'

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
        assert n.toString() == '(1 + 2)'

    def test_evaluate(self):
        one = NaturalNumberFunction(1)
        two = NaturalNumberFunction(2)
        n = SumFunction(one, two)
        assert n.evaluate(5) == 1 + 2
